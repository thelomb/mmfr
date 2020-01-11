from app.lib import pmmfr

class QttvData(pmmfr.QuantitativeData4__1):
    def __init__(self):
        super().__init__()

    def quantitative_data(self, pos, perf, stress_test, liability):
        self.AsstInf = pos
        self.LbltyInf = liability
        self.StrssTst = stress_test
        self.PrtflPrfrmnc = perf

class Report(pmmfr.FundReportUpdate2__1):
    def __init__(self):
        super().__init__()

    def fund_data(self, fund_data):
        self.FndData = fund_data

    def report_dates(self, report_date):
        self.RptgPrd = report_date.RptgPrd
        self.RptgYr = report_date.RptgYr
        self.RptgPrdFrToQrtr = report_date.RptgPrdFrToQrtr

    def reporting_data(self, fund, liability_data, performance_data, stress_test_data, position_data):
        rd = RptData()
        liability = liability_data.xml(fund)
        perf = performance_data.xml(fund)
        stress_test = stress_test_data.xml(fund)
        pos = position_data.xml(fund)
        if liability is None or perf is None or stress_test is None or pos is None:
            rd.no_activity()
        else:
            q = QttvData()
            q.quantitative_data(pos=pos, perf=perf.details, stress_test=stress_test, liability=liability.details)
            rd.QttvData = q
        self.RptData = rd


class FndRpt(pmmfr.FundReportData1__1):
    def __init__(self, report=None):
        super().__init__()
        if report:
            self.create(report)

    def create(self, report):
        self.Upd = report


class MnyMktFndRpt(pmmfr.MoneyMarketFundReportV01):

    def __init__(self, FndRpt=None):
        super().__init__()


class RptData(pmmfr.ReportData3Choice__1):
    def __init__(self):
        super().__init__()

    def no_activity(self):
        self.DataSetActn = pmmfr.ReportPeriodActivity3Code__1('NOTX')


class StressTestReport(pmmfr.StressTestReport1__1):
    def __init__(self):
        super().__init__()

    def new(self, test):
        self.StrssTstRslt.append(test)


class AsstInf(pmmfr.HoldingAsset3__1):
    def __init__(self):
        super().__init__()


document = pmmfr.Document(MnyMktFndRpt=MnyMktFndRpt())