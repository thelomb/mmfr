from model import pmmfr as pmmfr
from model.fund_calc import FundDynamicData
from model.interface import StaticData, Fund

class Report():
    def __init__(self):
        self.document = pmmfr.Document(MnyMktFndRpt=pmmfr.MoneyMarketFundReportV01())
        self.funds = []

    def static_data(self, range):
        for fund in range:
            f = Fund(fund.get('TPA_Fund_Code'))
            print('Processing fund static data for {fund}'.format(fund=f.fund_code))
            f.static_data(data=fund)

            # dynamic = FundDynamicData()
            # Upd.RptData = dynamic.RptData
            self.funds.append(f)

    def dynamic_data(self, range=None):
        if range is None:
            for fd in self.funds:
                print('Processing fake dynamic data for ', fd.fund_code)
                fd.FndRpt.Upd.RptData = pmmfr.ReportData3Choice__1(
                    DataSetActn=pmmfr.ReportPeriodActivity3Code__1('NOTX'))

    def position_data(self, range):
        pass

    def build(self):
        for f in self.funds:
            self.document.MnyMktFndRpt.append(f.FndRpt)

    def to_xml(self, destination):
        self.build()
        filename = destination
        with open(filename, 'wb') as f:
            f.write(self.document.toxml('utf-8'))
        return filename