from . import pmmfr
from datetime import date
from .helper import quarter_of_date, quarter_start, quarter_end, is_european_country
class FundStaticData():

    def __init__(self, static_data):
        self.static_data = static_data

        # instantiate depending objects
        self.reporting_period(self.static_data.start_date, self.static_data.end_date)
        fi = FundIdentity(mmf_lei=self.static_data.mmf_lei,
                          mmf_national_code=self.static_data.mmf_national_code,
                          mmf_member_state_authority=self.static_data.mmf_member_state_authority,
                          mmf_name=self.static_data.mmf_name,
                          mmf_domicile=self.static_data.mmf_domicile,
                          mmf_ecb_code=self.static_data.mmf_ecb_code)

        fm = FundMgtCo(mgr_lei=self.static_data.mgr_lei,
                       mgr_name=self.static_data.mgr_name,
                       mgr_ecb_code=self.static_data.mgr_ecb_code,
                       mgr_national_code_authority=self.static_data.mgr_national_code_authority,
                       mgr_ctry=self.static_data.mgr_ctry,
                       mmf_national_code_authority=self.static_data.mmf_national_code_authority)



        fa = FundAttributes(mmf_name=self.static_data.mmf_name,
                            legal_framework=self.static_data.legal_framework,
                            staff_saving_plan=self.static_data.staff_saving_plan,
                            mmf_marketing=self.static_data.mmf_marketing,
                            base_ccy=self.static_data.base_ccy,
                            inception_date=self.static_data.inception_date,
                            depositary_lei=self.static_data.depositary_lei,
                            depositary_national_code=self.static_data.depositary_national_code,
                            depositary_name=self.static_data.depositary_name,
                            highest_nav_share_class_isin=self.static_data.highest_nav_share_class_isin,
                            mmf_type=self.static_data.mmf_type,
                            master_feed_type=self.static_data.master_feed_type,
                            share_classes=self.static_data.share_classes)

        self.FndData = FundData(FndNttyId=fi, FundMgtCo=fm, FundAttributes=fa)

    def reporting_period(self, start_date, end_date):
        rp = ReportingPeriod(start_date, end_date)
        self.RptgYr = rp.RptgYr
        self.RptgPrdFrToQrtr = rp.RptgPrdFrToQrtr
        self.RptgPrd = rp.RptgPrd


from .errors import EmptyDate
class ReportingPeriod():
        def __init__(self, start_date, end_date):
            if start_date is None:
                raise EmptyDate()
            if end_date is None:
                raise EmptyDate()
            if not (pmmfr.ISODate(start_date) and pmmfr.ISODate(end_date)):
                raise
            if not date.fromisoformat(start_date).year == date.fromisoformat(end_date).year:
                raise
            if start_date >= end_date:
                raise
            if not quarter_start(start_date):
                raise
            if not quarter_end(end_date):
                raise
            quarter_start_enum = quarter_of_date(start_date)
            quarter_end_enum = quarter_of_date(end_date)
            self.RptgYr = pmmfr.ISOYear(date.fromisoformat(start_date).year)

            self.RptgPrdFrToQrtr = pmmfr.QuarterPeriod1(FrPrd=pmmfr.ReportingPeriodType1Code(quarter_start_enum),
                                                        ToPrd=pmmfr.ReportingPeriodType1Code(quarter_end_enum))
            self.RptgPrd = pmmfr.Period4Choice__1(FrDtToDt=pmmfr.Period2(FrDt=start_date, ToDt=end_date))


class FundIdentity(pmmfr.PartyIdentification212__1):
    def __init__(self, mmf_lei, mmf_national_code, mmf_member_state_authority, mmf_name, mmf_domicile, mmf_ecb_code):
        super().__init__()
        self.LEI = pmmfr.LEIIdentifier(mmf_lei)
        self.NtlRegnNb = pmmfr.GenericOrganisationIdentification1__1(Id=pmmfr.Max35Text(mmf_national_code),
                                                                               Issr=pmmfr.CountryCode(mmf_member_state_authority))
        self.AltrnId = pmmfr.GenericOrganisationIdentification1__2(Id=pmmfr.Max35Text(mmf_ecb_code),Issr=pmmfr.Max35Text_fixed('ECB'))
        self.Nm = pmmfr.Max350Text(mmf_name)
        self.CtryOfDmcl = pmmfr.Country1Choice__1(Ctry=pmmfr.CountryCode(mmf_domicile))

class FundData(pmmfr.FinancialInstrument82__1):
    def __init__(self, FndNttyId, FundMgtCo, FundAttributes):
        super().__init__()
        self.FndNttyId = FndNttyId
        self.FndMgmtCpny = FundMgtCo
        self.FndAttrbts = FundAttributes

class FundMgtCo(pmmfr.PartyIdentification195__1):
    def __init__(self, mgr_lei, mgr_name, mgr_ecb_code, mgr_national_code_authority, mgr_ctry, mmf_national_code_authority):
        super().__init__()
        if mgr_lei:
            self.LEI = pmmfr.LEIIdentifier(mgr_lei)
        self.FndAuthrtyRegnNb = pmmfr.GenericOrganisationIdentification1__3(Id=pmmfr.Max35Text(mmf_national_code_authority))

        self.FndMgmtCpnyAuthrtyRegnNb.append(
                pmmfr.GenericOrganisationIdentification1__1(Id=pmmfr.Max35Text(mgr_national_code_authority), Issr=pmmfr.CountryCode(mgr_ctry)))
        self.AltrnId = pmmfr.GenericIdentification3__1(Id=pmmfr.Max35Text(mgr_ecb_code), Issr=pmmfr.Max35Text_fixed('ECB'))
        self.Nm = pmmfr.Max350Text(mgr_name)

class FundAttributes(pmmfr.FinancialInstrumentAttributes101__1):
    def __init__(self,
                 mmf_name,
                 legal_framework,
                 staff_saving_plan,
                 mmf_marketing,
                 base_ccy,
                 inception_date,
                 depositary_lei,
                 depositary_national_code,
                 depositary_name,
                 highest_nav_share_class_isin,
                 mmf_type,
                 master_feed_type,
                 share_classes):
        super().__init__()
        self.Nm = pmmfr.Max350Text(mmf_name)
        self.LglFrmwk = pmmfr.LegalFramework5Choice__1(Cd=pmmfr.LegalFramework2Code(legal_framework))
        self.StffWthSvgsPlan = pmmfr.TrueFalseIndicator(staff_saving_plan)
        no_eu = False
        countries = []
        for ctry in mmf_marketing:
            if is_european_country(ctry):
                countries = pmmfr.RegisteredDistributionCountry2Choice__1(pmmfr.CountryCode(ctry))
                self.RegdDstrbtnCtry.append(countries)
            else:
                no_eu=True
        if no_eu:
            self.RegdDstrbtnCtry.append(
                pmmfr.RegisteredDistributionCountry2Choice__1(NonEurpnCtry=pmmfr.TrueFalseIndicator_fixed('true')))
        self.BaseCcy= pmmfr.ActiveOrHistoricCurrencyCode(base_ccy)
        self.DpstryId = pmmfr.PartyIdentification212__2(LEI=pmmfr.LEIIdentifier(depositary_lei),
                                                                   NtlRegnNb=pmmfr.GenericOrganisationIdentification1__3(
                                                                  Id=pmmfr.Max35Text(depositary_national_code)),
                                                                   Nm=pmmfr.Max350Text(depositary_name))
        self.MnyMktFndTp = pmmfr.MoneyMarketFundType1Choice__1(Cd=pmmfr.MoneyMarketFundType1Code(mmf_type))
        self.MstrFnd = pmmfr.MasterFundType1Code(master_feed_type)
        # to do
        # master_lei
        # master_national_code  # A.3.3_National_Code_Master
        # master_legal_name   # A.3.4_Legal_Name_Master

        self.ShrClss = pmmfr.FinancialInstrument60Choice__1()
        if share_classes:
            self.ShrClssInd = pmmfr.TrueFalseIndicator(True)
            for share_class in share_classes:
                highest = share_class.get('isin') == highest_nav_share_class_isin
                sc = ShareClass(isin=share_class.get('isin'),
                                ccy=share_class.get('ccy'),
                                is_highest_nav=highest)
                self.ShrClss.append(sc)
        else:
            self.ShrClssInd = pmmfr.TrueFalseIndicator(False)
            self.ShrClss.append(pmmfr.ShareClassList1__1(Id=pmmfr.SecurityIdentification31Choice(Nm=pmmfr.Max35Text(name))))
        self.FndRltdEvt = pmmfr.RelatedEvent2(IncptnDt=pmmfr.ISODate(inception_date),
                                                         LastRptSnt=pmmfr.TrueFalseIndicator(True))
        # to do related event
        # date_merger = None  # A.3.8_Date_Merger
        #date_liquidation = None  # A.3.9_Date_Liquidation
        #redemption_frequency = 'Daily'  # A.7.5_Redemption_Frequency
        #redemption_notice_period = 0  # A.7.6_Redemption_Notice_Period_in_Days
        #nav_gates = 0  # A.7.7_a_MMF_Arrangements_NAV_gates
        #nav_suspension = 0  # A.7.7_b_MMF_Arrangements_NAV_suspension_of_dealing
        #nav_liquidity_fees = 0  # A.7.7_c_MMF_Arrangements_NAV_liquidity_fees
        #other_arrangements = None  # A.7.7_d_MMF_Arrangements_description_other
        #nav_other_arrangements = None  # A.7.7_e_MMF_Arrangements_NAV_other


class ShareClass(pmmfr.ShareClassList1__2):
    def __init__(self, isin, ccy, is_highest_nav):
        super().__init__()
        self.Id = pmmfr.SecurityIdentification31Choice(ISIN=pmmfr.ISINOct2015Identifier(isin))
        self.Ccy = pmmfr.ActiveOrHistoricCurrencyCode(ccy)
        self.HghstNetAsstVal = pmmfr.TrueFalseIndicator(is_highest_nav)


