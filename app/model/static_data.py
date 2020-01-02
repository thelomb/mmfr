from app.model.fund_static import (FundData,
                                   ReportingPeriod,
                                   FundIdentity,
                                   FundMgtCo,
                                   FundAttributes)


class FundStaticData:

    def __init__(self):
        self.FndData = FundData()
        rp = ReportingPeriod()
        self.RptgYr = rp.RptgYr
        self.RptgPrdFrToQrtr = rp.RptgPrdFrToQrtr
        self.RptgPrd = rp.RptgPrd

    def from_dict(self, record):
        record['share_classes'] = self.create_share_classes(sc_ccy=record['sc_ccy'],
                                  sc_isin=record['sc_isin'],
                                  sc_name=record['sc_name'])
        fi = FundIdentity(mmf_lei=record['mmf_lei'],
                          mmf_national_code=record['mmf_national_code'],
                          mmf_member_state_authority=record['mmf_member_state_authority'],
                          mmf_name=record['mmf_name'],
                          mmf_domicile=record['mmf_domicile'],
                          mmf_ecb_code=record['mmf_ecb_code'])

        fm = FundMgtCo(mgr_lei=record['mgr_lei'],
                       mgr_name=record['mgr_name'],
                       mgr_ecb_code=record['mgr_ecb_code'],
                       mgr_national_code_authority=record['mgr_national_code_authority'],
                       mgr_ctry=record['mgr_ctry'],
                       mmf_national_code_authority=record['mmf_national_code_authority'])

        fa = FundAttributes(mmf_name=record['mmf_name'],
                            legal_framework=record['legal_framework'],
                            staff_saving_plan=record['staff_saving_plan'],
                            mmf_marketing=record['mmf_marketing'],
                            base_ccy=record['base_ccy'],
                            inception_date=record['inception_date'],
                            depositary_lei=record['depositary_lei'],
                            depositary_national_code=record['depositary_national_code'],
                            depositary_name=record['depositary_name'],
                            highest_nav_share_class_isin=record['highest_nav_share_class_isin'],
                            mmf_type=record['mmf_type'],
                            master_feed_type=record['master_feed_type'],
                            share_classes=record['share_classes'],
                            date_merger=record['date_merger'],
                            date_liquidation=record['date_liquidation'])
        self.FndData = FundData(FndNttyId=fi, FundMgtCo=fm, FundAttributes=fa)
        rp = ReportingPeriod()
        rp.set_period(record['report_date'])
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
