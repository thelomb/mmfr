from app.model.fund_static import FundData, FundAttributes, FundMgtCo, FundIdentity, ReportingPeriod, FundReport
from app.config import binding_files_static_fund_data
import json
from app.model.excel import XLType


class Binding():
    def __init__(self):
        with open(binding_files_static_fund_data, 'r') as file:
            self.map = json.load(file)['attributes']

class StaticData():
    binding = Binding().map

    def __init__(self):
        self.FndData = FundData()
        rp = ReportingPeriod()
        self.RptgYr = rp.RptgYr
        self.RptgPrdFrToQrtr = rp.RptgPrdFrToQrtr
        self.RptgPrd = rp.RptgPrd


    def from_dict(self, data, header):
        static_data = {}
        for key, value in StaticData.binding.items():
            static_data[key] = XLType(value['type']).clean(data[header.index(value['field'])])

        static_data['share_classes'] = self.create_share_classes(sc_ccy=static_data['sc_ccy'],
                                  sc_isin=static_data['sc_isin'],
                                  sc_name=static_data['sc_name'])
        fi = FundIdentity(mmf_lei=static_data['mmf_lei'],
                          mmf_national_code=static_data['mmf_national_code'],
                          mmf_member_state_authority=static_data['mmf_member_state_authority'],
                          mmf_name=static_data['mmf_name'],
                          mmf_domicile=static_data['mmf_domicile'],
                          mmf_ecb_code=static_data['mmf_ecb_code'])

        fm = FundMgtCo(mgr_lei=static_data['mgr_lei'],
                       mgr_name=static_data['mgr_name'],
                       mgr_ecb_code=static_data['mgr_ecb_code'],
                       mgr_national_code_authority=static_data['mgr_national_code_authority'],
                       mgr_ctry=static_data['mgr_ctry'],
                       mmf_national_code_authority=static_data['mmf_national_code_authority'])

        fa = FundAttributes(mmf_name=static_data['mmf_name'],
                            legal_framework=static_data['legal_framework'],
                            staff_saving_plan=static_data['staff_saving_plan'],
                            mmf_marketing=static_data['mmf_marketing'],
                            base_ccy=static_data['base_ccy'],
                            inception_date=static_data['inception_date'],
                            depositary_lei=static_data['depositary_lei'],
                            depositary_national_code=static_data['depositary_national_code'],
                            depositary_name=static_data['depositary_name'],
                            highest_nav_share_class_isin=static_data['highest_nav_share_class_isin'],
                            mmf_type=static_data['mmf_type'],
                            master_feed_type=static_data['master_feed_type'],
                            share_classes=static_data['share_classes'],
                            date_merger=static_data['date_merger'],
                            date_liquidation=static_data['date_liquidation'])
        self.FndData = FundData(FndNttyId=fi, FundMgtCo=fm, FundAttributes=fa)
        rp = ReportingPeriod()
        rp.set_period(static_data['report_date'])
        self.RptgYr = rp.RptgYr
        self.RptgPrdFrToQrtr = rp.RptgPrdFrToQrtr
        self.RptgPrd = rp.RptgPrd

    def create_share_classes(self, sc_ccy, sc_isin, sc_name):
        share_classes = []
        if len(sc_ccy) == len(sc_isin) and len(sc_name) == len(sc_ccy):
            for i in range(len(sc_isin)):
                sc = {'isin': sc_isin[i],
                      'ccy': sc_ccy[i],
                      'type': sc_name[i]}
                share_classes.append(sc)
        else:
            raise Exception('problem with share class mapping, inconsistent number of information')
        return share_classes

class Fund:
    def __init__(self, fund_code):
        self.fund_code=fund_code
        self.FndRpt = FundReport()

    def static_data(self, data, header):
        static_fund_data = StaticData()
        static_fund_data.from_dict(data=data, header=header)
        self.FndRpt.Upd.RptgYr = static_fund_data.RptgYr
        self.FndRpt.Upd.RptgPrdFrToQrtr = static_fund_data.RptgPrdFrToQrtr
        self.FndRpt.Upd.RptgPrd = static_fund_data.RptgPrd
        self.FndRpt.Upd.FndData = static_fund_data.FndData



