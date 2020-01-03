from app.model.fund_calc import (MnyMktInstrmHldg,
                                 ScrtstnAsstBckdComrclPprHldg,
                                 MnyMktFndHldgInf,
                                 DerivHldg,
                                 RvsRpAgrmtCollData,
                                 RpAgrmtHldg,
                                 DpstAncllryLqdAsstHldg
                                 )
from datetime import date

default_maturity = date.today().isoformat()


class Position:
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
    AsstTpOrder = {'MnyMktInstrmHldg': 0,
                   'ScrtstnAsstBckdComrclPprHldg': 1,
                   'DerivHldg': 2,
                   'MnyMktFndHldgInf': 3,
                   'DpstAncllryLqdAsstHldg': 4,
                   'RpAgrmtHldg': 5,
                   'RvsRpAgrmtCollData': 6}

    def __init__(self):
        self.details = ''

    def from_dict(self, record):
        asset_type = Position.security_mapping.get(record['asset_type'])
        method = getattr(self, asset_type)
        self.details = method(record)

    @staticmethod
    def money_market_instr(data):
        mmi = MnyMktInstrmHldg(asset_type=data['asset_type'],
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
        mmi.validateBinding()
        return mmi

    @staticmethod
    def securitized(data):
        sec = ScrtstnAsstBckdComrclPprHldg(asset_type=data['asset_type'],
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
                                           report_ccy_mv=data['report_ccy_mv'],
                                           fin_underlying_type=data['fin_underlying_type'])
        sec.validateBinding()
        return sec

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

    def __repr__(self):
        return 'Position({}, {})'.format(self.details.AsstTp,
                                         self.details.__class__.__name__)

    def __lt__(self, other):
        print(self.details.__class__.__name__)

        return Position.AsstTpOrder[self.details.__class__.__name__] < Position.AsstTpOrder[
            other.details.__class__.__name__]
