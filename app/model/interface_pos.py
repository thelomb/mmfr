from app.model.fund_calc import MnyMktInstrmHldg, \
    DerivHldg, \
    ScrtstnAsstBckdComrclPprHldg, \
    MnyMktFndHldgInf, \
    DpstAncllryLqdAsstHldg, \
    RpAgrmtHldg, \
    RvsRpAgrmtCollData, \
    PrtflPrfrmnc
from app.config import (binding_files_position_fund_data,
                        binding_files_performance_fund_data,
                        binding_files_liability_fund_data)
import json
from app.model.excel import XLType
from datetime import date

default_maturity = date.today().isoformat()
invalid_type = ['', 0]


class Binding:
    def __init__(self,path):
        with open(path, 'r') as file:
            self.map = json.load(file)['attributes']


class PositionData:
    binding = Binding(binding_files_position_fund_data).map
    deposit_type = ['DPSC', 'ANLA']
    repo_type = ['RVPO', 'REPO']
    repo_collat_type = []
    security_mapping = {
        'STSA': 'securitized',
        'SCRT': 'securitized',
        'ABCP': 'securitized',
        'STSS': 'securitized',
        'MMII': 'money_market_instr',
        'OTCD': 'derivatives',
        'RMTD': 'derivatives',
        'MMFT': 'money_market_fund',
        'DPSC': 'deposit',
        'ANLA': 'deposit',
        'RVPO': 'repo',
        'REPO': 'repo'
    }

    def __init__(self):
        self.details = ''

    def from_dict(self, data, header):
        static_data = {}
        for key, value in PositionData.binding.items():
            print('key: ', key, 'mapping: ', value, 'value: ', data[header.index(value['field'])])
            if key == 'asset_type' and data[header.index(value['field'])] in invalid_type:
                print('asset type:', data[header.index(value['field'])], ' is invalid. Skipping position')
                self.details = None
                static_data = {}
                break
            static_data[key] = XLType(value['type']).clean(data[header.index(value['field'])])
        if static_data:
            asset_type = PositionData.security_mapping.get(static_data['asset_type'])
            method = getattr(self, asset_type)
            self.details = method(static_data)

    @staticmethod
    def money_market_instr(data):
        return MnyMktInstrmHldg(asset_type=data['asset_type'],
                                cfi_iso=data['cfi_iso'],
                                party_sector_type=data['party_sector_type'],
                                maturity=data['maturity'] or default_maturity,
                                notional_currency=data['notional_currency'],
                                quantity=data['quantity'],
                                val_type=data['val_type'],
                                credit_assessment=data['credit_assessment'],
                                asset_ctry_code=data['asset_ctry_code'],
                                party_lei=data['party_lei'],
                                party_name=data['party_name'],
                                instr_name=data['instr_name'],
                                instr_isin=data['instr_isin'],
                                base_ccy_price=data['base_ccy_price'],
                                report_ccy_price=data['report_ccy_price'],
                                base_ccy_ai=data['base_ccy_ai'],
                                report_ccy_ai=data['report_ccy_ai'],
                                base_ccy_mv=data['base_ccy_mv'],
                                report_ccy_mv=data['report_ccy_mv'],
                                reset_date=data['reset_date'])

    @staticmethod
    def securitized(data):
        return ScrtstnAsstBckdComrclPprHldg(asset_type=data['asset_type'],
                                            cfi_iso=data['cfi_iso'],
                                            maturity=data['maturity'],
                                            notional_currency=data['notional_currency'],
                                            quantity=data['quantity'],
                                            val_type=data['val_type'],
                                            credit_assessment=data['credit_assessment'],
                                            asset_ctry_code=data['asset_ctry_code'],
                                            party_lei=data['party_lei'],
                                            party_name=data['party_name'],
                                            instr_name=data['instr_name'],
                                            instr_isin=data['instr_isin'],
                                            base_ccy_price=data['base_ccy_price'],
                                            report_ccy_price=data['report_ccy_price'],
                                            base_ccy_ai=data['base_ccy_ai'],
                                            report_ccy_ai=data['report_ccy_ai'],
                                            base_ccy_mv=data['base_ccy_mv'],
                                            report_ccy_mv=data['report_ccy_mv'])

    @staticmethod
    def derivatives(data):
        return DerivHldg(asset_type=data['asset_type'],
                         cfi_iso=data['cfi_iso'],
                         maturity=data['maturity'],
                         notional_currency=data['notional_currency'],
                         asset_ctry_code=data['asset_ctry_code'],
                         party_lei=data['party_lei'],
                         party_name=data['party_name'],
                         instr_name=data['instr_name'],
                         instr_isin=data['instr_isin'],
                         base_ccy_collat=data['base_ccy_collat'],
                         report_ccy_collat=data['report_ccy_collat'],
                         base_ccy_exposure=data['base_ccy_exposure'],
                         report_ccy_exposure=data['report_ccy_exposure'],
                         base_ccy_mv=data['base_ccy_mv'],
                         report_ccy_mv=data['report_ccy_mv'],
                         reset_date=data['reset_date'],
                         unique_instr_id=data['unique_instr_id'],
                         second_leg_currency=data['second_leg_currency'],
                         underlying_name=data['underlying_name'],
                         underlying_isin=data['underlying_isin'],
                         contract_type=data['contract_type'],
                         underlying_type=data['underlying_type'])

    @staticmethod
    def money_market_fund(data):
        return MnyMktFndHldgInf(asset_type=data['asset_type'],
                                cfi_iso=data['cfi_iso'],
                                party_sector_type=data['party_sector_type'],
                                maturity=data['maturity'] or default_maturity,
                                notional_currency=data['notional_currency'],
                                quantity=data['quantity'],
                                asset_ctry_code=data['asset_ctry_code'],
                                party_lei=data['party_lei'],
                                party_name=data['party_name'],
                                instr_name=data['instr_name'],
                                instr_isin=data['instr_isin'],
                                base_ccy_price=data['base_ccy_price'],
                                report_ccy_price=data['report_ccy_price'],
                                base_ccy_mv=data['base_ccy_mv'],
                                report_ccy_mv=data['report_ccy_mv'],
                                asset_lei=data['asset_lei'])

    @staticmethod
    def deposit(data):
        return DpstAncllryLqdAsstHldg(asset_type=data['asset_type'],
                                      maturity=data['maturity'] or default_maturity,
                                      notional_currency=data['notional_currency'],
                                      asset_ctry_code=data['asset_ctry_code'],
                                      party_lei=data['party_lei'],
                                      party_name=data['party_name'],
                                      instr_name=data['instr_name'],
                                      base_ccy_exposure=data['base_ccy_exposure'],
                                      report_ccy_exposure=data['report_ccy_exposure'])

    @staticmethod
    def repo(data):
        return RpAgrmtHldg(asset_type=data['asset_type'],
                           cfi_iso=data['cfi_iso'],
                           party_sector_type=data['party_sector_type'],
                           maturity=data['maturity'],
                           notional_currency=data['notional_currency'],
                           credit_assessment=data['credit_assessment'],
                           asset_ctry_code=data['asset_ctry_code'],
                           party_lei=data['party_lei'],
                           party_name=data['party_name'],
                           instr_name=data['instr_name'],
                           instr_isin=data['instr_isin'],
                           base_ccy_exposure=data['base_ccy_exposure'],
                           report_ccy_exposure=data['report_ccy_exposure'],
                           base_ccy_collat=data['base_ccy_collat'],
                           report_ccy_collat=data['report_ccy_collat'])

    @staticmethod
    def repo_collat(data):
        return RvsRpAgrmtCollData(collat_instr_list=data['collat_instr_list'],
                                  derogated_asset=data['derogated_asset'],
                                  base_ccy_collat=data['base_ccy_collat'],
                                  report_ccy_collat=data['base_ccy_collat'])


class Position:
    AsstTpOrder = {'MnyMktInstrmHldg': 0,
                   'ScrtstnAsstBckdComrclPprHldg': 1,
                   'DerivHldg': 2,
                   'MnyMktFndHldgInf': 3,
                   'DpstAncllryLqdAsstHldg': 4,
                   'RpAgrmtHldg': 5,
                   'RvsRpAgrmtCollData': 6}

    def __init__(self, fund_code):
        self.fund_code = fund_code
        self.details = PositionData()

    def data(self, data, header):
        self.details.from_dict(data=data, header=header)

    def __repr__(self):
        return 'Position({}, {}, {})'.format(self.fund_code, self.details.details.AsstTp,
                                             self.details.details.__class__.__name__)

    def __lt__(self, other):
        return Position.AsstTpOrder[self.details.details.__class__.__name__] < Position.AsstTpOrder[
            other.details.details.__class__.__name__]


class Performance:
    binding = Binding(binding_files_performance_fund_data).map
    def __init__(self, fund_code):
        self.fund_code = fund_code
        self.details = ''

    def from_dict(self, data, header):
        performance = {}
        for key, value in Performance.binding.items():
            print('key: ', key, 'mapping: ', value, 'value: ', data[header.index(value['field'])])
            performance[key] = XLType(value['type']).clean(data[header.index(value['field'])])
        self.details = PrtflPrfrmnc(
            weighted_avg_maturity=performance['weighted_avg_maturity'],
            weighted_avg_life=performance['weighted_avg_life'],
            daily_maturing_asset_pct=performance['daily_maturing_asset_pct'],
            weekly_maturing_asset_pct=performance['weekly_maturing_asset_pct'],
            ls1d_liquid=performance['ls1d_liquid'],
            d2t7_liquid=performance['d2t7_liquid'],
            d829_liquid=performance['d829_liquid'],
            a30d_liquid=performance['a30d_liquid'],
            base_ccy_nav=performance['base_ccy_nav'],
            report_ccy_nav=performance['report_ccy_nav'],
            lt3m_perf=performance['lt3m_perf'],
            lt1m_perf=performance['lt1m_perf'],
            lt1y_perf=performance['lt1y_perf'],
            lt3y_perf=performance['lt3y_perf'],
            lt5y_perf=performance['lt5y_perf'],
            cytd_perf=performance['cytd_perf'],
            lt1y_vol=performance['lt1y_vol'],
            lt2y_vol=performance['lt2y_vol'],
            lt3y_vol=performance['lt3y_vol'],
            lt1y_shadow_vol=performance['lt1y_shadow_vol'],
            lt2y_shadow_vol=performance['lt2y_shadow_vol'],
            lt3y_shadow_vol=performance['lt3y_shadow_vol'],
            yms2_perf=performance['yms2_perf'],
            ymn3_perf=performance['ymn3_perf'],
            yms1_perf=performance['yms1_perf'])


class Liability:
    binding = Binding(binding_files_liability_fund_data).map
    def __init__(self, fund_code):
        self.fund_code = fund_code
        self.details = ''

    def from_dict(self, data, header):
        performance = {}
        for key, value in Performance.binding.items():
            print('key: ', key, 'mapping: ', value, 'value: ', data[header.index(value['field'])])
            performance[key] = XLType(value['type']).clean(data[header.index(value['field'])])
        self.details = PrtflPrfrmnc(
            weighted_avg_maturity=performance['weighted_avg_maturity'],
            weighted_avg_life=performance['weighted_avg_life'],
            daily_maturing_asset_pct=performance['daily_maturing_asset_pct'],
            weekly_maturing_asset_pct=performance['weekly_maturing_asset_pct'],
            ls1d_liquid=performance['ls1d_liquid'],
            d2t7_liquid=performance['d2t7_liquid'],
            d829_liquid=performance['d829_liquid'],
            a30d_liquid=performance['a30d_liquid'],
            base_ccy_nav=performance['base_ccy_nav'],
            report_ccy_nav=performance['report_ccy_nav'],
            lt3m_perf=performance['lt3m_perf'],
            lt1m_perf=performance['lt1m_perf'],
            lt1y_perf=performance['lt1y_perf'],
            lt3y_perf=performance['lt3y_perf'],
            lt5y_perf=performance['lt5y_perf'],
            cytd_perf=performance['cytd_perf'],
            lt1y_vol=performance['lt1y_vol'],
            lt2y_vol=performance['lt2y_vol'],
            lt3y_vol=performance['lt3y_vol'],
            lt1y_shadow_vol=performance['lt1y_shadow_vol'],
            lt2y_shadow_vol=performance['lt2y_shadow_vol'],
            lt3y_shadow_vol=performance['lt3y_shadow_vol'],
            yms2_perf=performance['yms2_perf'],
            ymn3_perf=performance['ymn3_perf'],
            yms1_perf=performance['yms1_perf'])
