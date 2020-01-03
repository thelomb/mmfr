from app.model.fund_calc import PrtflPrfrmnc


class Performance:

    def __init__(self):
        self.details = ''

    def from_dict(self, record):
        self.details = PrtflPrfrmnc(
            weighted_avg_maturity=record['weighted_avg_maturity'],
            weighted_avg_life=record['weighted_avg_life'],
            daily_maturing_asset_pct=record['daily_maturing_asset_pct'],
            weekly_maturing_asset_pct=record['weekly_maturing_asset_pct'],
            ls1d_liquid=record['ls1d_liquid'],
            d2t7_liquid=record['d2t7_liquid'],
            d829_liquid=record['d829_liquid'],
            a30d_liquid=record['a30d_liquid'],
            base_ccy_nav=record['base_ccy_nav'],
            report_ccy_nav=record['report_ccy_nav'],
            lt3m_perf=record['lt3m_perf'],
            lt1m_perf=record['lt1m_perf'],
            lt1y_perf=record['lt1y_perf'],
            lt3y_perf=record['lt3y_perf'],
            lt5y_perf=record['lt5y_perf'],
            cytd_perf=record['cytd_perf'],
            lt1y_vol=record['lt1y_vol'],
            lt2y_vol=record['lt2y_vol'],
            lt3y_vol=record['lt3y_vol'],
            lt1y_shadow_vol=record['lt1y_shadow_vol'],
            lt2y_shadow_vol=record['lt2y_shadow_vol'],
            lt3y_shadow_vol=record['lt3y_shadow_vol'],
            yms2_perf=record['yms2_perf'],
            ymn3_perf=record['ymn3_perf'],
            yms1_perf=record['yms1_perf'])
