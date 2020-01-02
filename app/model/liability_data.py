from app.model.fund_calc import LbltyInf

class Liability:

    def __init__(self, fund_code):
        self.fund_code = fund_code
        self.details = ''

    def from_dict(self, record):
        self.details = LbltyInf(
            highest_beneficial_owner_pct=record['highest_beneficial_owner_pct'],
            prof_estimated_rate=record['prof_estimated_rate'],
            prof_precise_rate=record['prof_precise_rate'],
            retail_estimated_rate=record['retail_estimated_rate'],
            retail_precise_rate=record['retail_precise_rate'],
            investor_bank_pct=record['investor_bank_pct'],
            investor_general_govt_pct=record['investor_general_govt_pct'],
            investor_household_pct=record['investor_household_pct'],
            investor_insurance_pct=record['investor_insurance_pct'],
            investor_non_fin_pct=record['investor_non_fin_pct'],
            investor_mmf_pct=record['investor_mmf_pct'],
            investor_other_fin_pct=record['investor_other_fin_pct'],
            investor_pension_fund_pct=record['investor_pension_fund_pct'],
            investor_unknown_pct=record['investor_unknown_pct'],
            country_breakdown_pct=record['country_breakdown_pct'],
            redemption_frequency=record['redemption_frequency'],
            notice_period=record['notice_period'],
            arrangement_breakdown_pct=record['arrangement_breakdown_pct'],
            other_arrangement=record['other_arrangement'],
            monthly_nav=record['monthly_nav'],
            monthly_subs=record['monthly_subs'],
            monthly_redemption=record['monthly_redemption'],
            monthly_payment=record['monthly_payment'],
            monthly_xrate=record['monthly_xrate'])
