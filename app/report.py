from app.model.excel import Reader, XLType
from app.config import bindings_path
from app.model.static_data import FundStaticData
from app.model.liability_data import Liability
from app.model.pmmfr_helpers import document, Report, RptData, FndRpt, MnyMktFndRpt
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
            mock = self.data_description.get('data')
            header = mock.header
            content = mock.data_new
        else:
            raise Exception('unknown data source type')
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

    @staticmethod
    def pmmfr_interface(record):
        raise Exception('sub class not implemented')

    @classmethod
    def reject_record(cls, header, row, key, value):
        return key == 'asset_type' and row[header.index(value['field'])] in cls.rejection_list


class StaticData(GenericData):
    
    @staticmethod
    def pmmfr_interface(record):
        fund_static_data = FundStaticData()
        fund_static_data.from_dict(record)
        return fund_static_data

    def xml(self, fund_code):
        print(self.data_dict)
        f = find(lst=self.data_dict, key='fund_code', value=fund_code)
        return self.data_dict[f].get('details')


class LiabilityData(GenericData):

    @staticmethod
    def pmmfr_interface(record):
        liability_data = Liability()
        liability_data.from_dict(record)
        return


class PerformanceData(GenericData):
    pass


class DataCollection(GenericData):
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
        return record_key

class StressTest(DataCollection):
    pass


class PositionData(DataCollection):
    rejection_list = ['', 0]


class ReportData:

    xsd = XMLSchema('app/data/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd')

    def __init__(self,
                 static_data,
                 position_data=None,
                 liability_data=None,
                 stress_test_data=None,
                 performance_data=None):
        self.document = document
        self.funds = []
        self.output_path = None
        self.static_data = StaticData(static_data)
        self.liability_data = None
        self.stress_test_data = None
        self.performance_data = None
        self.position_data = None
        # self.liability_data = LiabilityData(liability_data) if liability_data else None
        # self.stress_test_data = StressTest(stress_test_data) if stress_test_data else None
        # self.performance_data = PerformanceData(performance_data) if performance_data else None
        # self.position_data = PositionData(position_data) if position_data else None
        self.set_funds()

    def generate_xml(self, output_path):
        mmf = MnyMktFndRpt()
        if (self.liability_data is None
                and self.stress_test_data is None
                and self.performance_data is None
                and self.position_data is None):
            for fund in self.funds:
                sd = self.static_data.xml(fund)
                r = Report()
                print('sd :', sd.FndData.validateBinding())
                r.fund_data(sd.FndData)
                r.RptgPrdFrToQrtr = sd.RptgPrdFrToQrtr
                r.RptgPrd = sd.RptgPrd
                r.RptgYr = sd.RptgYr
                r.RptData = self.report_data()
                print('rpt', r.RptData.validateBinding())
                r.validateBinding()
                fr = FndRpt()
                fr.create(r)
                fr.validateBinding()
                mmf.new_fund(fr)
                mmf.validateBinding()
                self.document.MnyMktFndRpt=mmf
            with open(output_path, 'wb') as f:
                f.write(self.document.toxml('utf-8'))
            self.output_path = output_path
            parser = etree.XMLParser(remove_blank_text=True)
            tree = etree.parse(self.output_path, parser)
            beautiful_output = self.output_path.replace('.xml', '_beautiful.xml')
            tree.write(beautiful_output, pretty_print=True)

        else:
            print('pass')
            pass

    def set_funds(self, fund_list=None):
        if fund_list:
            self.funds = fund_list
        else:
            for fund in self.static_data.data_dict:
                self.funds.append(fund.get('fund_code'))

    def report_data(self):
        if (self.liability_data is None
                and self.stress_test_data is None
                and self.performance_data is None
                and self.position_data is None):
            rd = RptData()
            rd.no_activity()
            print(rd.DataSetActn)
            print('rd', rd.validateBinding())
            return rd
        else:
            pass

    def validate(self):
        if ReportData.xsd.is_valid(self.output_path):
            print('🥳😜')
        else:
            print('🧐🤨')
