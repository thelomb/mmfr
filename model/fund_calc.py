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