from app.model import pmmfr

class QttvData(pmmfr.QuantitativeData4__1):
    def __init__(self):
        super().__init__()

class PrtflPrfrmnc(pmmfr.PerformanceFactors2__1):
    def __init__(self):
        super().__init__()

class StrssTst(pmmfr.StressTestReport1__1):
    def __init__(self):
        super().__init__()

class AsstInf(pmmfr.HoldingAsset3__1):
    def __init__(self):
        super().__init__()

class LbltyInf(pmmfr.LiabilityData3__1):
    def __init__(self):
        super().__init__()

class LwVoltlyNetAsstValRptData(pmmfr.LowVolatilityNetAssetValueReportData2__1):
    def __init__(self):
        super().__init__()



class AssetId(pmmfr.AssetIdentification3__1):
    def __init__(self, cfi_iso, instr_name=None, instr_isin=None):
        super().__init__()
        self.ClssfctnTp = pmmfr.CFIOct2015Identifier(cfi_iso)
        instr = pmmfr.InstrumentIdentification4Choice__1()
        if instr_name or instr_isin:
            if instr_isin:
                instr.ISIN = pmmfr.ISINOct2015Identifier(instr_isin)
            else:
                instr.Nm = pmmfr.Max350Text(instr_name)
        else:
            raise
        self.InstrmId = instr

class Derivatives(pmmfr.AssetIdentification3__2):
    def __init__(self, cfi_iso, instr_name=None, instr_isin=None, unique_instr_id=None):
        super().__init__()
        self.ClssfctnTp = pmmfr.CFIOct2015Identifier(cfi_iso)
        instr = pmmfr.InstrumentIdentification4Choice__2()
        if instr_name or instr_isin or unique_instr_id:
            if instr_isin:
                instr.ISIN = pmmfr.ISINOct2015Identifier(instr_isin)
            elif instr_name:
                instr.Nm = pmmfr.Max350Text(instr_name)
            else:
                instr.UnqPdctIdr = pmmfr.Max52Text(unique_instr_id)
        else:
            raise
        self.InstrmId = instr


class PartyData(pmmfr.Party46Choice__1):
    def __init__(self, sector, lei=None, name=None):
        super().__init__()
        self.IssrData = PartyAndSector(sector=sector, lei=lei, name=name)


class Party46Choice__2(pmmfr.Party46Choice__2):
    def __init__(self, lei=None, name=None):
        super().__init__()
        self.SpnsrData = PartyAndSector1__2(lei=lei, name=name)

class Party46Choice__3(pmmfr.Party46Choice__3):
    def __init__(self, lei=None, name=None):
        super().__init__()
        self.CtrPtyData = PartyAndSector1__2(lei=lei, name=name)

class PartyAndSector(pmmfr.PartyAndSector1__1):
    def __init__(self, sector_type, lei=None, name=None):
        super().__init__()
        self.PtyId = PartyIdentification(lei=lei, name=name)
        self.Sctr = pmmfr.PartySectorType1Code(sector_type)


class PartyAndSector1__2(pmmfr.PartyAndSector1__2):
    def __init__(self, lei=None, name=None):
        super().__init__()
        self.PtyId = PartyIdentification(lei=lei, name=name)

class PartyIdentification(pmmfr.PartyIdentification212__4):
    def __init__(self, lei=None, name=None):
        super().__init__()
        self.Nm = pmmfr.Max350Text(name) if name else None
        self.LEI = pmmfr.LEIIdentifier(lei) if lei else None

class CountryOrSupraNational(pmmfr.Country1Choice__2):
    def __init__(self, code=None):
        super().__init__()
        if code:
            self.Ctry = pmmfr.CountryCode(code)
        else:
            self.SprntnlCtry = pmmfr.TrueFalseIndicator_fixed__1(True)


class AssetVal(pmmfr.AssetValuation2__1):
    def __init__(self,
                 maturity,
                 notional_currency,
                 quantity,
                 val_type,
                 credit_assessment,
                 base_ccy_price=None,
                 report_ccy_price=None,
                 base_ccy_ai=None,
                 report_ccy_ai=None,
                 base_ccy_mv=None,
                 report_ccy_mv=None,
                 reset_date=None):
        super().__init__()
        self.MtrtyDt = pmmfr.ISODate(maturity)
        self.NtnlCcyFrstLeg = pmmfr.ActiveOrHistoricCurrencyCode(notional_currency)
        self.Qty = Quantity(value=quantity)
        self.Pric = ValueInBaseCcyOrReportCcy(base_ccy_val=base_ccy_price, report_ccy_val=report_ccy_price)
        self.AcrdIntrst = ValueInBaseCcyOrReportCcy(base_ccy_val=base_ccy_ai, report_ccy_val=report_ccy_ai)
        self.TtlVal = ValueInBaseCcyOrReportCcy(base_ccy_val=base_ccy_mv, report_ccy_val=report_ccy_mv)
        self.ValtnTp = pmmfr.ValuationType2Code(val_type)
        self.RstDt = pmmfr.ISODate(reset_date) or None
        self.CdtAssmntRslt = pmmfr.AssessmentResultType2Code(credit_assessment)


class AssetValuation2__2(pmmfr.AssetValuation2__2):
    def __init__(self,
                 maturity,
                 notional_currency,
                 quantity,
                 val_type,
                 credit_assessment,
                 base_ccy_price=None,
                 report_ccy_price=None,
                 base_ccy_ai=None,
                 report_ccy_ai=None,
                 base_ccy_mv=None,
                 report_ccy_mv=None,
                 reset_date=None):
        super().__init__()
        self.MtrtyDt = pmmfr.ISODate(maturity)
        self.NtnlCcyFrstLeg = pmmfr.ActiveOrHistoricCurrencyCode(notional_currency)
        self.Qty = Quantity(value=quantity)
        self.Pric = ValueInBaseCcyOrReportCcy(base_ccy_val=base_ccy_price, report_ccy_val=report_ccy_price)
        self.AcrdIntrst = ValueInBaseCcyOrReportCcy(base_ccy_val=base_ccy_ai, report_ccy_val=report_ccy_ai)
        self.TtlVal = ValueInBaseCcyOrReportCcy(base_ccy_val=base_ccy_mv, report_ccy_val=report_ccy_mv)
        self.ValtnTp = pmmfr.ValuationType2Code(val_type)
        self.CdtAssmntRslt = pmmfr.AssessmentResultType2Code(credit_assessment)

class AssetValuation2__3(pmmfr.AssetValuation2__3):
    def __init__(self,
                 maturity,
                 notional_currency,
                 base_ccy_colat=None,
                 report_ccy_colat=None,
                 base_ccy_exposure=None,
                 report_ccy_exposure=None,
                 base_ccy_mv=None,
                 report_ccy_mv=None,
                 reset_date=None,
                 second_leg_currency=None):
        super().__init__()
        self.MtrtyDt = pmmfr.ISODate(maturity)
        self.NtnlCcyFrstLeg = pmmfr.ActiveOrHistoricCurrencyCode(notional_currency)
        self.NtnlCcyScndLeg = pmmfr.ActiveOrHistoricCurrencyCode(second_leg_currency) or None
        self.TtlVal = ValueInBaseCcyOrReportCcy(base_ccy_val=base_ccy_mv, report_ccy_val=report_ccy_mv)
        self.CollVal = ValueInBaseCcyOrReportCcy(base_ccy_val=base_ccy_colat, report_ccy_val=report_ccy_colat)
        self.XpsrVal = ValueInBaseCcyOrReportCcy(base_ccy_val=base_ccy_exposure, report_ccy_val=report_ccy_exposure)
        self.RstDt = pmmfr.ISODate(reset_date) or None


class Quantity(pmmfr.FinancialInstrumentQuantity1Choice__1):
    def __init__(self, value):
        super().__init__()
        self.Unit = pmmfr.NonNegativeDecimalNumber(value)


class ValueInBaseCcyOrReportCcy(pmmfr.CurrencyExchange1Choice__1):
    def __init__(self, base_ccy_val=None, report_ccy_val=None):
        super().__init__()
        if base_ccy_val:
            self.Amt = Amount(base_ccy_val=base_ccy_val, report_ccy_val=report_ccy_val)
        else:
            self.NotAvlblVal = pmmfr.NotAvailable1Code('NTAV')


class Amount(pmmfr.CurrencyExchange14__1):
    def __init__(self, base_ccy_val, report_ccy_val=None):
        super().__init__()
        self.BaseCcyAmt = pmmfr.ImpliedCurrencyAndAmount(base_ccy_val)
        if report_ccy_val:
            self.RptgCcyAmt = AmountAndCcy().from_float(report_ccy_val)

class AmountAndCcy(pmmfr.ActiveCurrencyAndAmount__1, pmmfr.ActiveCurrencyAndAmount__1_SimpleType):
    def __init__(self):
        super().__init__()
        self.Ccy = pmmfr.ActiveCurrencyCode_fixed('EUR')

class MnyMktInstrmHldg(pmmfr.Financialinstrument81__1):
    def __init__(self,
                 asset_type,
                 cfi_iso,
                 party_sector_type,
                 maturity,
                 notional_currency,
                 quantity,
                 val_type,
                 credit_assessment,
                 asset_ctry_code=None,
                 party_lei=None,
                 party_name=None,
                 instr_name=None,
                 instr_isin=None,
                 base_ccy_price=None,
                 report_ccy_price=None,
                 base_ccy_ai=None,
                 report_ccy_ai=None,
                 base_ccy_mv=None,
                 report_ccy_mv=None,
                 reset_date=None):
        super().__init__()
        self.AsstTp = pmmfr.FinancialAssetType2Code__1(asset_type)
        self.AsstId = AssetId(cfi_iso=cfi_iso, instr_name=instr_name, instr_isin=instr_isin)
        self.PtyData = PartyData(party_sector_type, lei=party_lei, name=party_name)
        self.AsstCtry = CountryOrSupraNational(asset_ctry_code)
        self.AsstValtn = AssetVal(maturity=maturity,
                                  notional_currency=notional_currency,
                                  quantity=quantity,
                                  val_type=val_type,
                                  credit_assessment=credit_assessment,
                                  base_ccy_price=base_ccy_price,
                                  report_ccy_price=report_ccy_price,
                                  base_ccy_ai=base_ccy_ai,
                                  report_ccy_ai=report_ccy_ai,
                                  base_ccy_mv=base_ccy_mv,
                                  report_ccy_mv=report_ccy_mv,
                                  reset_date=reset_date)


class ScrtstnAsstBckdComrclPprHldg(pmmfr.Financialinstrument81__2):
    def __init__(self,
                 asset_type,
                 cfi_iso,
                 maturity,
                 notional_currency,
                 quantity,
                 val_type,
                 credit_assessment,
                 asset_ctry_code=None,
                 party_lei=None,
                 party_name=None,
                 instr_name=None,
                 instr_isin=None,
                 base_ccy_price=None,
                 report_ccy_price=None,
                 base_ccy_ai=None,
                 report_ccy_ai=None,
                 base_ccy_mv=None,
                 report_ccy_mv=None):
        super().__init__()
        self.AsstTp = pmmfr.FinancialAssetType2Code__2(asset_type)
        self.AsstId = AssetId(cfi_iso=cfi_iso, instr_name=instr_name, instr_isin=instr_isin)
        self.PtyData = Party46Choice__2(lei=party_lei, name=party_name)
        self.AsstCtry = CountryOrSupraNational(asset_ctry_code)
        self.AsstValtn = AssetValuation2__2(maturity=maturity,
                                  notional_currency=notional_currency,
                                  quantity=quantity,
                                  val_type=val_type,
                                  credit_assessment=credit_assessment,
                                  base_ccy_price=base_ccy_price,
                                  report_ccy_price=report_ccy_price,
                                  base_ccy_ai=base_ccy_ai,
                                  report_ccy_ai=report_ccy_ai,
                                  base_ccy_mv=base_ccy_mv,
                                  report_ccy_mv=report_ccy_mv)


class DerivHldg(pmmfr.Financialinstrument81__3):
    def __init__(self,
                 asset_type,
                 cfi_iso,
                 party_sector_type,
                 maturity,
                 notional_currency,
                 quantity,
                 val_type,
                 credit_assessment,
                 asset_ctry_code=None,
                 party_lei=None,
                 party_name=None,
                 instr_name=None,
                 instr_isin=None,
                 base_ccy_price=None,
                 report_ccy_price=None,
                 base_ccy_ai=None,
                 report_ccy_ai=None,
                 base_ccy_mv=None,
                 report_ccy_mv=None,
                 reset_date=None,
                 unique_instr_id=None,
                 second_leg_currency=None):
        super().__init__()
        self.AsstTp = pmmfr.FinancialAssetType2Code__3(asset_type)
        self.AsstId = Derivatives(cfi_iso=cfi_iso,
                                  instr_name=instr_name,
                                  instr_isin=instr_isin,
                                  unique_instr_id=unique_instr_id)
        self.PtyData = Party46Choice__3(lei=party_lei, name=party_name)
        self.AsstCtry = CountryOrSupraNational(asset_ctry_code)
        self.AsstValtn = AssetValuation2__3(maturity=maturity,
                                  notional_currency=notional_currency,
                                  quantity=quantity,
                                  val_type=val_type,
                                  credit_assessment=credit_assessment,
                                  base_ccy_price=base_ccy_price,
                                  report_ccy_price=report_ccy_price,
                                  base_ccy_ai=base_ccy_ai,
                                  report_ccy_ai=report_ccy_ai,
                                  base_ccy_mv=base_ccy_mv,
                                  report_ccy_mv=report_ccy_mv,
                                  reset_date=reset_date,
                                  second_leg_currency=second_leg_currency)

class MnyMktFndHldgInf(pmmfr.Financialinstrument81__4):
    pass


class DpstAncllryLqdAsstHldg(pmmfr.Financialinstrument81__5):
    pass


class RpAgrmtHldg(pmmfr.Financialinstrument81__6):
    pass


class RvsRpAgrmtCollData(pmmfr.FinancialInstrument80__1):
    pass
