from app.model.fund_calc import MnyMktInstrmHldg, \
    DerivHldg, \
    ScrtstnAsstBckdComrclPprHldg, \
    MnyMktFndHldgInf, \
    DpstAncllryLqdAsstHldg, \
    RpAgrmtHldg, \
    RvsRpAgrmtCollData
from app.config import binding_files_position_fund_data
import json
from app.model.excel import XLType


class Binding:
    def __init__(self):
        with open(binding_files_position_fund_data, 'r') as file:
            self.map = json.load(file)['attributes']


class PositionData:
    binding = Binding().map
    securitized_type = ['STSA', 'SCRT', 'ABCP', 'STSS']
    money_market_type = ['MMII']
    derivative_type = ['OTCD', 'RMTD']
    money_market_fund_type = ['MMFT']
    deposit_type = ['DPSC', 'ANLA']
    repo_type = ['RVPO', 'REPO']
    repo_collat_type = []

    def __init__(self):
        self.details = ''

    def from_dict(self, data, header):
        static_data = {}
        for key, value in PositionData.binding.items():
            static_data[key] = XLType(value['type']).clean(data[header.index(value['field'])])
        asset_type = data[2]
        method = getattr(self, asset_type)
        self.details = method(data, header)

    @staticmethod
    def money_market_instr(data):
        return MnyMktInstrmHldg(asset_type=data['asset_type'],
                                cfi_iso=data['cfi_iso'],
                                party_sector_type=data['party_sector_type'],
                                maturity=data['maturity'],
                                notional_currency=data['notional_currency'],
                                quantity=data['quantity'],
                                val_type=data['val_type'],
                                credit_assessment=data['credit_assement'],
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
                                            credit_assessment=data['credit_assement'],
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
                         base_ccy_colat=data['base_ccy_colat'],
                         report_ccy_colat=data['report_ccy_colat'],
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
                                maturity=data['maturity'],
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
                                      maturity=data['maturity'],
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
                           credit_assessment=data['credit_assement'],
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
        return RvsRpAgrmtCollData(asset_type=data['asset_type'],
                                  cfi_iso=data['cfi_iso'],
                                  party_sector_type=data['party_sector_type'],
                                  maturity=data['maturity'],
                                  notional_currency=data['notional_currency'],
                                  quantity=data['quantity'],
                                  val_type=data['val_type'],
                                  credit_assessment=data['credit_assement'],
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


class Position:
    def __init__(self, fund_code, fund_type):
        self.fund_code = fund_code
        self.type = fund_type
        self.details = PositionData()

    def data(self, data, header):
        self.details.from_dict(data=data, header=header)
