from app.model.excel import Reader, XLType
from app.config import bindings_path, mmf_xsd_path
from app.model.static_data import FundStaticData
from app.model.liability_data import Liability
from app.model.perf_data import Performance
from app.model.stress_test_data import StressTest, ActionPlan
from app.model.position_data import Position
from app.model.pmmfr_helpers import (document, Report, FndRpt, StressTestReport, AsstInf)
import json
from xmlschema import XMLSchema
from lxml import etree


def find(lst, key, value):
    for i, dic in enumerate(lst):
        if dic[key] == value:
            return i
    return -1


class Binding:
    bindings_path = bindings_path

    def __init__(self, file):
        with open(bindings_path + file, 'r') as file:
            self.map = json.load(file)['attributes']


class GenericData:
    pmmfr_map = None
    rejection_list = []

    def __init__(self, data_description):
        self.row_record_count = 0
        self.data_dict = None
        self.data_description = data_description
        self.bindings = Binding(self.data_description.get('bindings')).map
        header, content = self.process_data()
        self.to_dict(header, content)

    def process_data(self):
        if self.data_description.get('type') == 'file':
            xl = Reader()
            header, content = xl.parse(path=self.data_description.get('path'),
                                       sheetname=self.data_description.get('sheet'))
        elif self.data_description.get('type') == 'mock':
            mock = self.data_description.get('schema')
            header = mock.header
            content = mock.data_new
        else:
            raise Exception('unknown schema source type')
        self.row_record_count = len(content)
        return header, content

    def to_dict(self, header, content):
        record_key = []
        for row in content:
            record = self.single_row(header, row)
            xml_record = self.pmmfr_interface(record)
            record_key.append({'fund_code': record['fund_code'], 'details': xml_record})
        self.data_dict = record_key

    def single_row(self, header, row):
        record = {}
        reject = False
        for key, value in self.bindings.items():
            reject = self.reject_record(header, row, key, value)
            if reject:
                break
            #print('key: ', key,
            #      'mapping: ', value,
            #      'index :', header.index(value['field']),
            #      'value: ', row[header.index(value['field'])])
            record[key] = XLType(value['type']).clean(row[header.index(value['field'])])
        return record if not reject else None

    @classmethod
    def pmmfr_interface(cls, record):
        data = cls.pmmfr_map()
        data.from_dict(record)
        return data
        # raise Exception('sub class not implemented')

    @classmethod
    def reject_record(cls, header, row, key, value):
        return key == 'asset_type' and row[header.index(value['field'])] in cls.rejection_list

    def xml(self, fund_code):
        f = find(lst=self.data_dict, key='fund_code', value=fund_code)
        if f == -1:
            return None
        return self.data_dict[f].get('details')


class StaticData(GenericData):
    pmmfr_map = FundStaticData


class LiabilityData(GenericData):
    pmmfr_map = Liability


class PerformanceData(GenericData):
    pmmfr_map = Performance


class DataCollection(GenericData):

    def __init__(self, data_description):
        super().__init__(data_description)
        self.collection = []

    def to_dict(self, header, content):
        record_key = []
        row_id = 0
        for row in content:
            record = self.single_row(header, row)
            if record:
                record_key.append({'fund_code': (record['fund_code'], row_id), 'details': record})
                row_id += 1
            else:
                print('row skipped')
        self.data_dict = record_key



class StressTestData(DataCollection):

    pmmfr_map = StressTest
    pmmfr_col = StressTestReport

    def xml(self, fund_code):
        test_report = StressTestReport()
        for tst in self.data_dict:
            if tst.get('fund_code')[0] == fund_code:
                st = StressTest()
                st.from_dict(tst.get('details'))
                test_report.new(st.details)
        test_report.ActnPlan = ActionPlan()
        return test_report


class PositionData(DataCollection):
    rejection_list = ['', 0]
    pmmfr_map = Position
    pmmfr_col = AsstInf

    def xml(self, fund_code):
        ai = AsstInf()
        positions = []
        for pos in self.data_dict:
            if pos.get('fund_code')[0] == fund_code:
                p = Position()
                p.from_dict(pos.get('details'))
                positions.append(p)
        _ = [ai.append(d.details) for d in sorted(positions)]
        return ai

class ReportData:

    xsd = XMLSchema(mmf_xsd_path)

    def __init__(self,
                 static_data,
                 position_data=None,
                 liability_data=None,
                 stress_test_data=None,
                 performance_data=None):
        self.document = document
        self.funds = []
        self.static_data = StaticData(static_data)
        self.liability_data = LiabilityData(liability_data) if liability_data else None
        self.stress_test_data = StressTestData(stress_test_data) if stress_test_data else None
        self.performance_data = PerformanceData(performance_data) if performance_data else None
        self.position_data = PositionData(position_data) if position_data else None
        self.set_funds()

    def generate_xml(self, output_path):
        for fund in self.funds:
            sd = self.static_data.xml(fund)
            r = Report()
            r.fund_data(sd.FndData)
            r.report_dates(sd)
            r.reporting_data(fund=fund,
                             liability_data=self.liability_data,
                             performance_data=self.performance_data,
                             stress_test_data=self.stress_test_data,
                             position_data=self.position_data)
            fr = FndRpt(r)
            self.document.MnyMktFndRpt.append(fr)
        self.save_xml(output_path)

    def save_xml(self, output_path):
            with open(output_path, 'wb') as f:
                f.write(self.document.toxml('utf-8'))
            self.output_path = output_path
            parser = etree.XMLParser(remove_blank_text=True)
            tree = etree.parse(self.output_path, parser)
            beautiful_output = self.output_path.replace('.xml', '_beautiful.xml')
            tree.write(beautiful_output, pretty_print=True)

    def set_funds(self, fund_list=None):
        if fund_list:
            self.funds = fund_list
        else:
            for fund in self.static_data.data_dict:
                self.funds.append(fund.get('fund_code'))

    def validate(self):
        if ReportData.xsd.is_valid(self.output_path):
            print('🥳😜')
        else:
            print('🧐🤨')
