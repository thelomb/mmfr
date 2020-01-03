from app.model import pmmfr

class Report(pmmfr.FundReportUpdate2__1):
    def __init__(self):
        super().__init__()

    def fund_data(self, fund_data):
        self.FndData = fund_data

    def report_dates(self, report_date):
        self.RptgPrd = report_date.RptgPrd
        self.RptgYr = report_date.RptgYr
        self.RptgPrdFrToQrtr = report_date.RptgPrdFrToQrtr

    def reporting_data(self, report_data):
        self.RptData = report_data

class FndRpt(pmmfr.FundReportData1__1):
    def __init__(self):
        super().__init__()

    def create(self, report):
        self.Upd = report

class MnyMktFndRpt(pmmfr.MoneyMarketFundReportV01):

    def __init__(self):
        super().__init__()

    def new_fund(self, FndRpt):
        self.FndRpt.append(FndRpt)

#
# class Document(pmmfr.Document):
#     def __init__(self):
#         print('hello')
#         super().__init__()
#         self.MnyMktFndRpt = MnyMktFndRpt()


document = pmmfr.Document(MnyMktFndRpt=MnyMktFndRpt())

class RptData(pmmfr.ReportData3Choice__1):
    def __init__(self):
        super().__init__()

    def no_activity(self):
        self.DataSetActn = pmmfr.ReportPeriodActivity3Code__1('NOTX')

class QttvData(pmmfr.QuantitativeData4__1):
    def __init__(self):
        super().__init__()


class StressTestReport(pmmfr.StressTestReport1__1):
    def __init__(self):
        super().__init__()

    def new(self, test):
        self.StrssTstRslt.append(test)

class AsstInf(pmmfr.HoldingAsset3__1):
    def __init__(self):
        super().__init__()
