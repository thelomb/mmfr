from app.model.fund_static import FundData, FundAttributes, FundMgtCo, FundIdentity, ReportingPeriod, FundReport
from app.model.fund_calc import MnyMktInstrmHldg
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
    derivative_type = ['OTCD','RMTD']

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
                                report_ccy_mv=data['report_ccy_mv'])

class Position:
    def __init__(self, fund_code, fund_type):
        self.fund_code=fund_code
        self.type = fund_type
        self.details = PositionData()

    def data(self, data, header):
        self.details.from_dict(data=data, header=header)




