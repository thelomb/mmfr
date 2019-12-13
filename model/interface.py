from .fund_static import FundData, FundAttributes, FundMgtCo, FundIdentity, ReportingPeriod, FundReport
from datetime import date
import datetime

class StaticData():
    def __init__(self):
        self.fund_code = ''
        self.fund_name = ''
        self.report_date = date.today()
        self.mmf_lei = ''
        self.mmf_national_code = ''
        self.mmf_member_state_authority = ''
        self.mmf_name = ''
        self.mmf_domicile = ''
        self.mmf_ecb_code = ''
        self.legal_framework = '' #enum
        self.staff_saving_plan = False
        self.mmf_marketing = []
        self.base_ccy = ''
        self.inception_date = date.today()
        self.mmf_national_code_authority = ''
        self.mgr_national_code_authority = ''
        self.mgr_lei = ''
        self.mgr_ecb_code = ''
        self.mgr_name = ''
        self.mgr_ctry = ''
        self.depositary_lei = ''
        self.depositary_national_code = ''
        self.depositary_name = ''
        self.mmf_type = '' # enum
        self.master_feed_type = '' #enum, capitalize?
        self.master_lei = ''
        self.master_national_code = ''
        self.master_legal_name = ''
        self.share_classes = []
        self.highest_nav_share_class_isin = ''
        self.date_merger = date.today()
        self.date_liquidation = date.today()
        self.redemption_frequency = ''
        self.redemption_notice_period = 0
        self.nav_gates = 0
        self.nav_suspension = 0
        self.nav_liquidity_fees = 0
        self.other_arrangements = ''
        self.nav_other_arrangements = ''
        self.sc_name = ''
        self.sc_isin = ''
        self.sc_ccy = ''
        self.dist_countries = ''


    def from_dict(self, data):
        binding = Binding().map
        for key, value in vars(self).items():
            try:
                setattr(self, key, self.postprocess(key, data[binding[key]]))
            except:
                continue
        self.create_share_classes()
        self.create_dist_countries()
        fi = FundIdentity(mmf_lei=self.mmf_lei,
                          mmf_national_code=self.mmf_national_code,
                          mmf_member_state_authority=self.mmf_member_state_authority,
                          mmf_name=self.mmf_name,
                          mmf_domicile=self.mmf_domicile,
                          mmf_ecb_code=self.mmf_ecb_code)

        fm = FundMgtCo(mgr_lei=self.mgr_lei,
                       mgr_name=self.mgr_name,
                       mgr_ecb_code=self.mgr_ecb_code,
                       mgr_national_code_authority=self.mgr_national_code_authority,
                       mgr_ctry=self.mgr_ctry,
                       mmf_national_code_authority=self.mmf_national_code_authority)

        fa = FundAttributes(mmf_name=self.mmf_name,
                            legal_framework=self.legal_framework,
                            staff_saving_plan=self.staff_saving_plan,
                            mmf_marketing=self.mmf_marketing,
                            base_ccy=self.base_ccy,
                            inception_date=self.inception_date,
                            depositary_lei=self.depositary_lei,
                            depositary_national_code=self.depositary_national_code,
                            depositary_name=self.depositary_name,
                            highest_nav_share_class_isin=self.highest_nav_share_class_isin,
                            mmf_type=self.mmf_type,
                            master_feed_type=self.master_feed_type,
                            share_classes=self.share_classes)
        self.FndData = FundData(FndNttyId=fi, FundMgtCo=fm, FundAttributes=fa)
        rp = ReportingPeriod(self.report_date)
        self.RptgYr = rp.RptgYr
        self.RptgPrdFrToQrtr = rp.RptgPrdFrToQrtr
        self.RptgPrd = rp.RptgPrd

    def create_share_classes(self):
        sc_name = self.sc_name.split(';')
        sc_isin = self.sc_isin.split(';')
        sc_ccy = self.sc_ccy.split(';')
        if len(sc_ccy) == len(sc_isin) and len(sc_name) == len(sc_ccy):
            for i in range(len(sc_isin)):
                sc = {'isin': sc_isin[i],
                      'ccy': sc_ccy[i],
                      'type': sc_name[i]}
                self.share_classes.append(sc)
        else:
            raise Exception('problem with share class mapping, inconsistent number of information')


    def create_dist_countries(self):
        self.dist_countries = self.dist_countries.split(sep=';')

    @staticmethod
    def postprocess(key, data):
        if isinstance(data, str):
            data = data.strip()
            if data in ['Yes', 'YES', 'No', 'NO']:
                data = data in ['Yes', 'YES']
        if key == 'mmf_type':
            data = MMFType.to_code(data)
        if key == 'master_feed_type':
            data = MasterFeedType.to_code(data)
        if isinstance(data, datetime.datetime):
            data = data.date().isoformat()
        return data

class Binding():
    def __init__(self):
        self.map = {
            'report_date': 'A.1.1_Reporting_Period',
            'mmf_lei': 'A.1.3_LEI_MMF',
            'mmf_national_code': 'A.1.2_National_Code_MMF',
            'mmf_member_state_authority': 'A.1.9_Member_State_Authorisation_MMF',
            'mmf_name': 'A.1.5_Name_MMF',
            'mmf_domicile': 'A.1.8_Domicile_MMF',
            'mmf_ecb_code':  'A.1.4_ECB_Code_MMF',
            'legal_framework': 'A.1.6_UCITS_AIF_MMF',
            'staff_saving_plan': 'A.1.7_Employee_Saving_Scheme',
            'mmf_marketing':  'A.1.10_Member_State_Marketing_MMF',
            'base_ccy': 'A.1.12_Base_Currency_MMF',
            'inception_date': 'A.1.11_Inception_Date_MMF',
            'mmf_national_code_authority': 'A.1.13_National_Code_Manager_Authority_MMF',
            'mgr_national_code_authority': 'A.1.14_National_Code_Manager_Authority_Manager',
            'mgr_lei': 'A.1.15_LEI_Manager',
            'mgr_ecb_code': 'A.1.16_ECB_Code_Manager',
            'mgr_name': 'A.1.17_Name_Manager',
            'mgr_ctry': 'A.1.18_Country_Manager',
            'depositary_lei': 'A.1.19_LEI_Depositary',
            'depositary_national_code': 'A.1.20_National_Code_Depository',
            'depositary_name': 'A.1.21_Legal_Name_Depository',
            'mmf_type': 'A.2.1_Type_MMF',
            'master_feed_type': 'A.3.1_Master_Feeder_MMF',
            'master_lei': 'A.3.2_LEI_Master',
            'master_national_code': 'A.3.3_National_Code_Master',
            'master_legal_name': 'A.3.4_Legal_Name_Master',
            'share_classes': 'share_classes',
            'highest_nav_share_class_isin': 'A.3.7_b_Shareclass_Highest NAV',
            'date_merger': 'A.3.8_Date_Merger',
            'date_liquidation': 'A.3.9_Date_Liquidation',
            'redemption_frequency': 'A.7.5_Redemption_Frequency',
            'redemption_notice_period': 'A.7.6_Redemption_Notice_Period_in_Days',
            'nav_gates': 'A.7.7_a_MMF_Arrangements_NAV_gates',
            'nav_suspension': 'A.7.7_b_MMF_Arrangements_NAV_suspension_of_dealing',
            'nav_liquidity_fees': 'A.7.7_c_MMF_Arrangements_NAV_liquidity_fees',
            'other_arrangements': 'A.7.7_d_MMF_Arrangements_description_other',
            'nav_other_arrangements': 'A.7.7_e_MMF_Arrangements_NAV_other',
            'fund_code': 'TPA_Fund_Code',
            'sc_name' : 'A.3.6_a_Shareclass_Name_MMF',
            'sc_isin': 'A.3.6_b_Shareclass_ISINS_MMF',
            'sc_ccy': 'A.3.7_a_Shareclass_Currencies_MMF',
            'dist_countries': 'A.1.10_Member_State_Marketing_MMF',
            'fund_name': 'Fund_Name'

        }

class MMFType():
    mapping = { 'shorttermlvnavmoneymarketfund': 'STLV',
                'shorttermpublicdebtcnavmoneymarketfund': 'STCN',
                'shorttermvnavmoneymarketfund': 'STVN',
                'standardvnavmoneymarketfund': 'SDVN',
                'ShortTermLVNAVMoneyMarketFund': 'STLV',
                'ShortTermPublicDebtCNAVMoneyMarketFund': 'STCN',
                'ShortTermVNAVMoneyMarketFund': 'STVN',
                'StandardVNAVMoneyMarketFund': 'SDVN',
                'shorttermlvnavmmf': 'STLV',
                'shorttermpublicdebtcnavmmf': 'STCN',
                'shorttermvnavmmf': 'STVN',
                'standardvnavmmf': 'SDVN'
    }

    @classmethod
    def to_code(cls, value):
        if isinstance(value, str):
            space = str.maketrans(dict.fromkeys(' '))
            value = value.translate(space)
            return cls.mapping[value.lower()]
        return value

class MasterFeedType():
    mapping = { 'fder': 'FDER',
                'mstr': 'MSTR',
                'none': 'NONE',
                'feeder': 'FDER',
                'master': 'MSTR'
    }

    @classmethod
    def to_code(cls, value):
        if isinstance(value, str):
            space = str.maketrans(dict.fromkeys(' '))
            value = value.translate(space)
            return cls.mapping[value.lower()]
        if value is None:
            return 'NONE'
        return value


# report_date = data['A.1.1_Reporting_Period'].date().isoformat()  # '2019-09-30' # A.1.1_Reporting_Period
# mmf_lei = '549300HBG59GBCBNNR42'  # A.1.3_LEI_MMF
# mmf_national_code = '00000006'  # A.1.2_National_Code_MMF
# mmf_member_state_authority = 'LU'  # A.1.9_Member_State_Authorisation_MMF
# mmf_name = 'Aberdeen Standard Liquidity Fund (Lux) - Sterling Fund'  # A.1.5_Name_MMF
# mmf_domicile = 'LU'  # A.1.8_Domicile_MMF
# mmf_ecb_code = 'LUO000950C00006'  # A.1.4_ECB_Code_MMF
# legal_framework = 'UCIT'  # A.1.6_UCITS_AIF_MMF
# staff_saving_plan = False  # A.1.7_Employee_Saving_Scheme
# mmf_marketing = data['dist_countries']  # A.1.10_Member_State_Marketing_MMF
# base_ccy = 'EUR'  # A.1.12_Base_Currency_MMF
# inception_date = '1985-07-01'  # A.1.11_Inception_Date_MMF
# mmf_national_code_authority = 'S00000822'  # A.1.13_National_Code_Manager_Authority_MMF
# mgr_national_code_authority = 'S00000822'  # A.1.14_National_Code_Manager_Authority_Manager
# mgr_lei = '213800K3MRPGMKRTEB15'  # A.1.15_LEI_Manager
# mgr_ecb_code = None  # A.1.16_ECB_Code_Manager
# mgr_name = 'Aberdeen Standard Investments Luxembourg S.A.'  # A.1.17_Name_Manager
# mgr_ctry = 'LU'  # A.1.18_Country_Manager
# depositary_lei = 'RNVZOEETEJ32KW0QXS82'  # A.1.19_LEI_Depositary
# depositary_national_code = 'B00000202'  # A.1.20_National_Code_Depository
# depositary_name = 'State Street Bank Luxembourg S.C.A.'  # A.1.21_Legal_Name_Depository
# mmf_type = 'SDVN'  # 'A.2.1_Type_MMF',
# master_feed_type = 'NONE'  # A.3.1_Master_Feeder_MMF
# master_lei = None  # A.3.2_LEI_Master
# master_national_code = None  # A.3.3_National_Code_Master
# master_legal_name = None  # A.3.4_Legal_Name_Master
# share_classes = data[
#     'share_classes']  # A.3.6_a_Shareclass_Name_MMF, A.3.6_b_Shareclass_ISINS_MMF, A.3.7_a_Shareclass_Currencies_MMF
# highest_nav_share_class_isin = 'LU0643933160'  # A.3.7_b_Shareclass_Highest NAV
# date_merger = None  # A.3.8_Date_Merger
# date_liquidation = None  # A.3.9_Date_Liquidation
# redemption_frequency = 'Daily'  # A.7.5_Redemption_Frequency
# redemption_notice_period = 0  # A.7.6_Redemption_Notice_Period_in_Days
# nav_gates = 0  # A.7.7_a_MMF_Arrangements_NAV_gates
# nav_suspension = 0  # A.7.7_b_MMF_Arrangements_NAV_suspension_of_dealing
# nav_liquidity_fees = 0  # A.7.7_c_MMF_Arrangements_NAV_liquidity_fees
# other_arrangements = None  # A.7.7_d_MMF_Arrangements_description_other
# nav_other_arrangements = None  # A.7.7_e_MMF_Arrangements_NAV_other


class PositionData():
    pass

class Fund():
    def __init__(self, fund_code):
        self.fund_code=fund_code
        self.FndRpt = FundReport()

    def static_data(self, data):
        static_fund_data = StaticData()
        static_fund_data.from_dict(data=data)
        self.FndRpt.Upd.RptgYr = static_fund_data.RptgYr
        self.FndRpt.Upd.RptgPrdFrToQrtr = static_fund_data.RptgPrdFrToQrtr
        self.FndRpt.Upd.RptgPrd = static_fund_data.RptgPrd
        self.FndRpt.Upd.FndData = static_fund_data.FndData

