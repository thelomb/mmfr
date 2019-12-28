from app.model import pmmfr as pmmfr
from app.model.interface import Fund
from app.model.interface_pos import Position, Performance, Liability
from app.model.fund_calc import AsstInf
from app.input.mock import MockPerf

class Report():
    def __init__(self):
        self.document = pmmfr.Document(MnyMktFndRpt=pmmfr.MoneyMarketFundReportV01())
        self.funds = []
        self.positions = []

    def static_data(self, data):
        header, content = data
        for fund in content:
            f = Fund(fund[header.index('TPA_Fund_Code')])
            print('Processing fund static data for {fund}'.format(fund=f.fund_code))
            f.static_data(data=fund, header=header)
            self.funds.append(f)
            #self.document.MnyMktFndRpt.append(f.FndRpt)

    def dynamic_data(self, data=None):
        if data is None:
            for fd in self.funds:
                print('Processing fake dynamic data for ', fd.fund_code)
                fd.FndRpt.Upd.RptData = pmmfr.ReportData3Choice__1()
                fd.FndRpt.Upd.RptData.DataSetActn = pmmfr.ReportPeriodActivity3Code__1('NOTX')
        else:
             fd.FndRpt.Upd.RptData.QttvData = pmmfr.QuantitativeData4__1()
             fd.FndRpt.Upd.RptData.QttvData.AsstInf = AssetInf()
             fd.FndRpt.Upd.RptData.QttvData.LbltyInf = LiabilityData()
             fd.FndRpt.Upd.RptData.QttvData.StrssTst = StressTest()
             fd.FndRpt.Upd.RptData.QttvData.LwVoltlyNetAsstValRptData = VolatilityData()

    def position_data(self, data):
        header, content = data
        for position in content:
            p = Position(position[header.index('Fund Code')])
            p.data(data=position, header=header)
            if p.details.details:
                self.positions.append(p)
            print(self.positions)
        self.positions.sort()

    def build(self):
        for f in self.funds:
            f.FndRpt.Upd.RptData.DataSetActn=None
            f.FndRpt.Upd.RptData.QttyData = pmmfr.QuantitativeData4__1()
            f.FndRpt.Upd.RptData.QttyData.AsstInf = pmmfr.HoldingAsset3__1()
            f.FndRpt.Upd.RptData.QttyData.PrtflPrfrmnc = Performance(fund_code=f.fund_code).from_dict(data=MockPerf.data,header=MockPerf.header)
            f.FndRpt.Upd.RptData.QttyData.LbltyInf = Liability(fund_code=f.fund_code).from_dict(data=MockPerf.data,header=MockPerf.header)
            for position in self.positions:
                f.FndRpt.Upd.RptData.QttyData.AsstInf.append(position.details.details)
            print('hello')
            self.document.MnyMktFndRpt.append(f.FndRpt)

    def to_xml(self, destination):
        self.build()
        filename = destination
        with open(filename, 'wb') as f:
            f.write(self.document.toxml('utf-8'))
        return filename
