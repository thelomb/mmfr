from . import pmmfr
class FundDynamicData():

    def __init__(self, data=None):
        self.calc_data()


    def load_data(self, data):
        pass

    def transform_data(self):
        pass

    def calc_data(self):
        self.RptData = pmmfr.ReportData3Choice__1(DataSetActn=pmmfr.ReportPeriodActivity3Code__1('NOTX'))
        # return self.RptData

class QttvData(pmmfr.QuantitativeData4__1):
    def __init__(self):
        super().__init__()

class PrtflPrfrmnc(pmmfr.PerformanceFactors2__1):
    def __init__(self):
        super().__init__()

class StrssTst(pmmfr.StressTestReport1__1):
    def __init__(self):
        super().__init__()

class AsstInf(pmmfr.HoldingAsset3__1):
    def __init__(self):
        super().__init__()

class LbltyInf(pmmfr.LiabilityData3__1):
    def __init__(self):
        super().__init__()

class LwVoltlyNetAsstValRptData(pmmfr.LowVolatilityNetAssetValueReportData2__1):
    def __init__(self):
        super().__init__()