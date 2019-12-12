from model import pmmfr as pmmfr
from model.fund_static import FundStaticData
from model.fund_calc import FundDynamicData

class Document():
    def __init__(self):
        self.Upd = pmmfr.FundReportUpdate2__1()
        self.FndRpt = pmmfr.FundReportData1__1(Upd=self.Upd)
        self.MnyMktFndRpt = pmmfr.MoneyMarketFundReportV01()
        self.MnyMktFndRpt.append(self.FndRpt)
        document = pmmfr.Document(MnyMktFndRpt=self.MnyMktFndRpt)
        self.document = document

    def static_block(self, data):
        static = FundStaticData(data)
        self.Upd.RptgYr=static.RptgYr
        self.Upd.RptgPrdFrToQrtr=static.RptgPrdFrToQrtr
        self.Upd.RptgPrd=static.RptgPrd
        self.Upd.FndData = static.FndData

    def dynamic_block(self):
        dynamic = FundDynamicData()
        self.Upd.RptData = dynamic.RptData

    def to_xml(self, destination):
        filename = destination
        with open(filename, 'wb') as f:
            f.write(self.document.toxml('utf-8'))
        return filename

    def is_valid(self):
        return self.document.validateBinding()



