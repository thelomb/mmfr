sc_type = 'A-2;I-2;I-3;J-3;K-1;K-3;L-1;L-3;X-2;Y-2;Z-1;Z-2;Z-3'.split(";")
sc_isin = 'LU0049015760;LU0108940692;LU0966092727;LU0966092990;LU0643933087;LU0966093022;LU0779217453;LU0966093295;LU1914336968;LU2027372429;LU0643933160;LU0147471253;LU0966093378'.split(";")
sc_ccy = 'GBP;GBP;GBP;GBP;GBP;GBP;GBP;GBP;GBP;GBP;GBP;GBP;GBP'. split(";")
if len(sc_ccy) == len(sc_isin) and len(sc_type) == len(sc_ccy):
    share_classes = []
    for i in range(len(sc_isin) - 1):
        sc = {'isin': sc_isin[i],
              'ccy': sc_ccy[i],
              'type': sc_type[i]}
        share_classes.append(sc)
    print(share_classes)
dist_countries = 'AT;CL;FI;FR;DE;GI;HU;IE;IM;IT;JE;LI;LU;PE;SG;ES;SE;CH;GB'
input = {'share_classes': share_classes, 'dist_countries': dist_countries.split(sep=';')}

class Data():
    def __init__(self):
        self.data = input

    def from_itself(self):
        self.start_date = '2019-07-01'
        self.end_date = '2019-09-30' # A.1.1_Reporting_Period
        self.mmf_lei = '549300HBG59GBCBNNR42' # A.1.3_LEI_MMF
        self.mmf_national_code = '00000006' # A.1.2_National_Code_MMF
        self.mmf_member_state_authority = 'LU' # A.1.9_Member_State_Authorisation_MMF
        self.mmf_name = 'Aberdeen Standard Liquidity Fund (Lux) - Sterling Fund' #  A.1.5_Name_MMF
        self.mmf_domicile = 'LU' # A.1.8_Domicile_MMF
        self.mmf_ecb_code = 'LUO000950C00006'  # A.1.4_ECB_Code_MMF
        self.legal_framework = 'UCIT' # A.1.6_UCITS_AIF_MMF
        self.staff_saving_plan = False #A.1.7_Employee_Saving_Scheme
        self.mmf_marketing = self.data['dist_countries'] # A.1.10_Member_State_Marketing_MMF
        self.base_ccy = 'EUR' # A.1.12_Base_Currency_MMF
        self.inception_date = '1985-07-01' # A.1.11_Inception_Date_MMF
        self.mmf_national_code_authority = 'S00000822' # A.1.13_National_Code_Manager_Authority_MMF
        self.mgr_national_code_authority = 'S00000822' #A.1.14_National_Code_Manager_Authority_Manager
        self.mgr_lei = '213800K3MRPGMKRTEB15' # A.1.15_LEI_Manager
        self.mgr_ecb_code = None #A.1.16_ECB_Code_Manager
        self.mgr_name = 'Aberdeen Standard Investments Luxembourg S.A.' #A.1.17_Name_Manager
        self.mgr_ctry = 'LU'  #A.1.18_Country_Manager
        self.depositary_lei = 'RNVZOEETEJ32KW0QXS82' #A.1.19_LEI_Depositary
        self.depositary_national_code = 'B00000202' #A.1.20_National_Code_Depository
        self.depositary_name = 'State Street Bank Luxembourg S.C.A.'  # A.1.21_Legal_Name_Depository
        self.mmf_type = 'SDVN' #'A.2.1_Type_MMF',
        self.master_feed_type = 'NONE' #A.3.1_Master_Feeder_MMF
        self.master_lei = None #A.3.2_LEI_Master
        self.master_national_code = None #A.3.3_National_Code_Master
        self.master_legal_name = None #A.3.4_Legal_Name_Master
        self.share_classes = self.data['share_classes'] # A.3.6_a_Shareclass_Name_MMF, A.3.6_b_Shareclass_ISINS_MMF, A.3.7_a_Shareclass_Currencies_MMF
        self.highest_nav_share_class_isin = 'LU0643933160' # A.3.7_b_Shareclass_Highest NAV
        self.date_merger = None #A.3.8_Date_Merger
        self.date_liquidation = None # A.3.9_Date_Liquidation
        self.redemption_frequency = 'Daily' # A.7.5_Redemption_Frequency
        self.redemption_notice_period = 0 # A.7.6_Redemption_Notice_Period_in_Days
        self.nav_gates = 0 # A.7.7_a_MMF_Arrangements_NAV_gates
        self.nav_suspension = 0 # A.7.7_b_MMF_Arrangements_NAV_suspension_of_dealing
        self.nav_liquidity_fees = 0 # A.7.7_c_MMF_Arrangements_NAV_liquidity_fees
        self.other_arrangements = None # A.7.7_d_MMF_Arrangements_description_other
        self.nav_other_arrangements = None # 	A.7.7_e_MMF_Arrangements_NAV_other
