from app.model import pmmfr as pmmfr
from app.model.interface import Fund
from app.model.interface_pos import Position
from app.model.fund_calc import AsstInf

class Report():
    def __init__(self):
        self.document = pmmfr.Document(MnyMktFndRpt=pmmfr.MoneyMarketFundReportV01())
        self.funds = []

    def static_data(self, data):
        header, content = data
        for fund in content:
            f = Fund(fund[header.index('TPA_Fund_Code')])
            print('Processing fund static data for {fund}'.format(fund=f.fund_code))
            f.static_data(data=fund, header=header)
            self.funds.append(f)

    def dynamic_data(self, data=None):
        if data is None:
            for fd in self.funds:
                print('Processing fake dynamic data for ', fd.fund_code)
                fd.FndRpt.Upd.RptData = pmmfr.ReportData3Choice__1()
                fd.FndRpt.Upd.RptData.DataSetActn = pmmfr.ReportPeriodActivity3Code__1('NOTX')
        # for fd in self.funds:
        #     fd.FndRpt.Upd.RptData.QttvData = pmmfr.QuantitativeData4__1()
        #     fd.FndRpt.Upd.RptData.QttvData.AsstInf = AssetInf()
        #     fd.FndRpt.Upd.RptData.QttvData.LbltyInf = LiabilityData()
        #     fd.FndRpt.Upd.RptData.QttvData.PrtflPrfrmnc = PerformanceData()
        #     fd.FndRpt.Upd.RptData.QttvData.StrssTst = StressTest()
        #     fd.FndRpt.Upd.RptData.QttvData.LwVoltlyNetAsstValRptData = VolatilityData()

    def position_data(self, data):
        header, content = data
        positions = []
        for position in content:
            p = Position(position[header.index('TPA_Fund_Code')])
            p.data(data=position, header=header)
            positions.append(p)
        return positions

    def build(self):
        for f in self.funds:
            self.document.MnyMktFndRpt.append(f.FndRpt)

    def to_xml(self, destination):
        self.build()
        filename = destination
        with open(filename, 'wb') as f:
            f.write(self.document.toxml('utf-8'))
        return filename