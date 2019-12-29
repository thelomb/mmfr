from app.model import pmmfr

supranationals = []
unknowns = []
class AsstInf(pmmfr.HoldingAsset3__1):
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


class AssetIdentification3__3(pmmfr.AssetIdentification3__3):
    def __init__(self, cfi_iso, instr_name=None, instr_isin=None, lei=None):
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
        self.AsstLEI = pmmfr.LEIIdentifier(lei) if lei else None


class AssetIdentification3__4(pmmfr.AssetIdentification3__4):
    def __init__(self, instr_name):
        super().__init__()
        instr = pmmfr.InstrumentIdentification4Choice__3()
        instr.Nm = pmmfr.Max350Text(instr_name)
        self.InstrmId = instr


class PartyData(pmmfr.Party46Choice__1):
    def __init__(self, sector, lei=None, name=None):
        super().__init__()
        self.IssrData = PartyAndSector(sector_type=sector, lei=lei, name=name)


class Party46Choice__2(pmmfr.Party46Choice__2):
    def __init__(self, lei=None, name=None):
        super().__init__()
        self.SpnsrData = PartyAndSector1__2(lei=lei, name=name)


class Party46Choice__3(pmmfr.Party46Choice__3):
    def __init__(self, lei=None, name=None):
        super().__init__()
        self.CtrPtyData = PartyAndSector1__2(lei=lei, name=name)


class Party46Choice__4(pmmfr.Party46Choice__4):
    def __init__(self, sector, lei=None, name=None):
        super().__init__()
        self.CtrPtyData = PartyAndSector(sector_type=sector, lei=lei, name=name)


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
        self.RstDt = pmmfr.ISODate(reset_date) if reset_date else None
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
                 base_ccy_collat=None,
                 report_ccy_collat=None,
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
        self.CollVal = ValueInBaseCcyOrReportCcy(base_ccy_val=base_ccy_collat, report_ccy_val=report_ccy_collat)
        self.XpsrVal = ValueInBaseCcyOrReportCcy(base_ccy_val=base_ccy_exposure, report_ccy_val=report_ccy_exposure)
        self.RstDt = pmmfr.ISODate(reset_date) or None


class AssetValuation2__4(pmmfr.AssetValuation2__4):
    def __init__(self,
                 maturity,
                 notional_currency,
                 quantity,
                 base_ccy_price=None,
                 report_ccy_price=None,
                 base_ccy_mv=None,
                 report_ccy_mv=None):
        super().__init__()
        self.MtrtyDt = pmmfr.ISODate(maturity)
        self.NtnlCcyFrstLeg = pmmfr.ActiveOrHistoricCurrencyCode(notional_currency)
        self.Qty = Quantity(value=quantity)
        self.Pric = ValueInBaseCcyOrReportCcy(base_ccy_val=base_ccy_price, report_ccy_val=report_ccy_price)
        self.TtlVal = ValueInBaseCcyOrReportCcy(base_ccy_val=base_ccy_mv, report_ccy_val=report_ccy_mv)


class AssetValuation2__5(pmmfr.AssetValuation2__5):
    def __init__(self,
                 maturity,
                 notional_currency,
                 base_ccy_exposure=None,
                 report_ccy_exposure=None):
        super().__init__()
        self.MtrtyDt = pmmfr.ISODate(maturity)
        self.NtnlCcyFrstLeg = pmmfr.ActiveOrHistoricCurrencyCode(notional_currency)
        self.XpsrVal = ValueInBaseCcyOrReportCcy(base_ccy_val=base_ccy_exposure, report_ccy_val=report_ccy_exposure)


class AssetValuation2__6(pmmfr.AssetValuation2__6):
    def __init__(self,
                 maturity,
                 notional_currency,
                 credit_assessment,
                 base_ccy_exposure=None,
                 report_ccy_exposure=None,
                 base_ccy_collat=None,
                 report_ccy_collat=None):
        super().__init__()
        self.MtrtyDt = pmmfr.ISODate(maturity)
        self.NtnlCcyFrstLeg = pmmfr.ActiveOrHistoricCurrencyCode(notional_currency)
        self.XpsrVal = ValueInBaseCcyOrReportCcy(base_ccy_val=base_ccy_exposure, report_ccy_val=report_ccy_exposure)
        self.CollVal = ValueInBaseCcyOrReportCcy(base_ccy_val=base_ccy_collat, report_ccy_val=report_ccy_collat)
        self.CdtAssmntRslt = pmmfr.AssessmentResultType2Code(credit_assessment)


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
            print('report ccy val', report_ccy_val)
            amt = pmmfr.ActiveCurrencyAndAmount__1(report_ccy_val)
            amt.Ccy = pmmfr.ActiveCurrencyCode_fixed('EUR')
            self.RptgCcyAmt = amt


class AmountAndCcy(pmmfr.ActiveCurrencyAndAmount__1, pmmfr.ActiveCurrencyAndAmount__1_SimpleType):
    def __init__(self):
        super().__init__()


class SecurityIdentification31Choice(pmmfr.SecurityIdentification31Choice):
    def __init__(self, name=None, isin=None):
        super().__init__()
        if isin:
            self.ISIN = pmmfr.ISINOct2015Identifier(isin)
        else:
            self.Nm = pmmfr.Max35Text(name)


class DerivativeAttributes(pmmfr.DerivativeInstrument8):
    def __init__(self, contract_type, underlying_type, name=None, isin=None):
        super().__init__()
        self.CtrctTp = pmmfr.FinancialInstrumentContractType3Code(contract_type)
        self.UndrlygTp = pmmfr.UnderlyingDerivativeType2Code(underlying_type)
        self.UndrlygId = SecurityIdentification31Choice(name=name, isin=isin)


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
                 maturity,
                 notional_currency,
                 contract_type,
                 underlying_type,
                 asset_ctry_code=None,
                 party_lei=None,
                 party_name=None,
                 instr_name=None,
                 instr_isin=None,
                 base_ccy_collat=None,
                 report_ccy_collat=None,
                 base_ccy_exposure=None,
                 report_ccy_exposure=None,
                 base_ccy_mv=None,
                 report_ccy_mv=None,
                 reset_date=None,
                 unique_instr_id=None,
                 second_leg_currency=None,
                 underlying_name=None,
                 underlying_isin=None):
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
                                            base_ccy_collat=base_ccy_collat,
                                            report_ccy_collat=report_ccy_collat,
                                            base_ccy_exposure=base_ccy_exposure,
                                            report_ccy_exposure=report_ccy_exposure,
                                            base_ccy_mv=base_ccy_mv,
                                            report_ccy_mv=report_ccy_mv,
                                            reset_date=reset_date,
                                            second_leg_currency=second_leg_currency)
        self.DerivInstrmAttrbts = DerivativeAttributes(contract_type=contract_type,
                                                       underlying_type=underlying_type,
                                                       name=underlying_name,
                                                       isin=underlying_isin)


class MnyMktFndHldgInf(pmmfr.Financialinstrument81__4):
    def __init__(self,
                 asset_type,
                 cfi_iso,
                 party_sector_type,
                 maturity,
                 notional_currency,
                 quantity,
                 asset_ctry_code=None,
                 party_lei=None,
                 party_name=None,
                 instr_name=None,
                 instr_isin=None,
                 base_ccy_price=None,
                 report_ccy_price=None,
                 base_ccy_mv=None,
                 report_ccy_mv=None,
                 asset_lei=None):
        super().__init__()
        self.AsstTp = pmmfr.FinancialAssetType2Code__4(asset_type)
        self.AsstId = AssetIdentification3__3(cfi_iso=cfi_iso,
                                              instr_name=instr_name,
                                              instr_isin=instr_isin,
                                              lei=asset_lei)
        self.PtyData = PartyData(party_sector_type, lei=party_lei, name=party_name)
        self.AsstCtry = CountryOrSupraNational(asset_ctry_code)
        self.AsstValtn = AssetValuation2__4(maturity=maturity,
                                            notional_currency=notional_currency,
                                            quantity=quantity,
                                            base_ccy_price=base_ccy_price,
                                            report_ccy_price=report_ccy_price,
                                            base_ccy_mv=base_ccy_mv,
                                            report_ccy_mv=report_ccy_mv)


class DpstAncllryLqdAsstHldg(pmmfr.Financialinstrument81__5):
    def __init__(self,
                 asset_type,
                 maturity,
                 notional_currency,
                 instr_name,
                 asset_ctry_code=None,
                 party_lei=None,
                 party_name=None,
                 base_ccy_exposure=None,
                 report_ccy_exposure=None):
        super().__init__()
        self.AsstTp = pmmfr.FinancialAssetType2Code__5(asset_type)
        self.AsstId = AssetIdentification3__4(instr_name=instr_name)
        self.PtyData = Party46Choice__3(lei=party_lei, name=party_name)
        self.AsstCtry = CountryOrSupraNational(asset_ctry_code)
        self.AsstValtn = AssetValuation2__5(maturity=maturity,
                                            notional_currency=notional_currency,
                                            base_ccy_exposure=base_ccy_exposure,
                                            report_ccy_exposure=report_ccy_exposure)


class RpAgrmtHldg(pmmfr.Financialinstrument81__6):
    def __init__(self,
                 asset_type,
                 cfi_iso,
                 party_sector_type,
                 maturity,
                 notional_currency,
                 credit_assessment,
                 asset_ctry_code=None,
                 party_lei=None,
                 party_name=None,
                 instr_name=None,
                 instr_isin=None,
                 base_ccy_exposure=None,
                 report_ccy_exposure=None,
                 base_ccy_collat=None,
                 report_ccy_collat=None):
        super().__init__()
        self.AsstTp = pmmfr.FinancialAssetType2Code__6(asset_type)
        self.AsstId = AssetId(cfi_iso=cfi_iso, instr_name=instr_name, instr_isin=instr_isin)
        self.PtyData = Party46Choice__4(party_sector_type, lei=party_lei, name=party_name)
        self.AsstCtry = CountryOrSupraNational(asset_ctry_code)
        self.AsstValtn = AssetValuation2__6(maturity=maturity,
                                            notional_currency=notional_currency,
                                            credit_assessment=credit_assessment,
                                            base_ccy_exposure=base_ccy_exposure,
                                            report_ccy_exposure=report_ccy_exposure,
                                            base_ccy_collat=base_ccy_collat,
                                            report_ccy_collat=report_ccy_collat)


class RvsRpAgrmtCollData(pmmfr.FinancialInstrument80__1):
    def __init__(self,
                 collat_instr_list,
                 derogated_asset=False,
                 base_ccy_collat=None,
                 report_ccy_collat=None):
        super().__init__()
        for instr in collat_instr_list:
            isin = pmmfr.InstrumentIdentification3Choice__1()
            isin.ISIN = instr
            self.FinInstrmId.append(isin)
        self.DrgtnRcvdAssts = pmmfr.TrueFalseIndicator(derogated_asset)
        self.TtlVal = Amount(base_ccy_val=base_ccy_collat, report_ccy_val=report_ccy_collat)


class PrfrmncVal(pmmfr.PerformanceValueType1Choice__1):
    def __init__(self, perf=None):
        super().__init__()
        if perf:
            self.Rate = pmmfr.PercentageBoundedRate(perf)
        else:
            self.NotAvlblVal = pmmfr.NotAvailable1Code('NTAV')


class PrtflLqdtyBrkdwn(pmmfr.RangeBreakdown1__1):
    def __init__(self, range_type, perf=None):
        super().__init__()
        self.RgTp = pmmfr.RangeType1Code__1(range_type)
        self.PrfrmncVal = PrfrmncVal(perf)


class FndValtn(pmmfr.FundValuation1__1):
    def __init__(self, weighted_avg_maturity, weighted_avg_life, base_ccy_nav=None, report_ccy_nav=None):
        super().__init__()
        self.NetAsstValPerUnit = Amount(base_ccy_val=base_ccy_nav, report_ccy_val=report_ccy_nav)
        self.WghtdAvrgLife = pmmfr.DecimalNumber(weighted_avg_life)
        self.WghtdAvrgMtrty = pmmfr.DecimalNumber(weighted_avg_maturity)


class LqdtyInf(pmmfr.FundLiquidity1__1):
    def __init__(self, daily_maturing_asset_pct, weekly_maturing_asset_pct, ls1d_liquid=None, d2t7_liquid=None,
                 d829_liquid=None, a30d_liquid=None):
        super().__init__()
        self.DalyMtrgAsstRate = pmmfr.PercentageBoundedRate(daily_maturing_asset_pct)
        self.WklyMtrgAsstRate = pmmfr.PercentageBoundedRate(weekly_maturing_asset_pct)
        self.PrtflLqdtyBrkdwn.append(PrtflLqdtyBrkdwn(range_type='LS1D', perf=ls1d_liquid))
        self.PrtflLqdtyBrkdwn.append(PrtflLqdtyBrkdwn(range_type='D2T7', perf=d2t7_liquid))
        self.PrtflLqdtyBrkdwn.append(PrtflLqdtyBrkdwn(range_type='D829', perf=d829_liquid))
        self.PrtflLqdtyBrkdwn.append(PrtflLqdtyBrkdwn(range_type='A30D', perf=a30d_liquid))


class CmltvRtrsBrkdwn(pmmfr.RangeBreakdown1__2):
    def __init__(self, range_type, perf=None):
        super().__init__()
        self.RgTp = pmmfr.RangeType1Code__2(range_type)
        self.PrfrmncVal = PrfrmncVal(perf)


class StdPrtflVoltlyBrkdwn(pmmfr.RangeBreakdown1__3):
    def __init__(self, range_type, perf=None):
        super().__init__()
        self.RgTp = pmmfr.RangeType1Code__3(range_type)
        self.PrfrmncVal = PrfrmncVal(perf)


class CalYrPrfrmncBrkdwn(pmmfr.RangeBreakdown1__4):
    def __init__(self, range_type, perf=None):
        super().__init__()
        self.RgTp = pmmfr.RangeType1Code__4(range_type)
        self.PrfrmncVal = PrfrmncVal(perf)


class Yld(pmmfr.Yield1__1):
    def __init__(self,
                 lt3m_perf=None,
                 lt1m_perf=None,
                 lt1y_perf=None,
                 lt3y_perf=None,
                 lt5y_perf=None,
                 cytd_perf=None,
                 lt1y_vol=None,
                 lt2y_vol=None,
                 lt3y_vol=None,
                 lt1y_shadow_vol=None,
                 lt2y_shadow_vol=None,
                 lt3y_shadow_vol=None,
                 yms2_perf=None,
                 ymn3_perf=None,
                 yms1_perf=None):
        super().__init__()
        self.CmltvRtrsBrkdwn.append(CmltvRtrsBrkdwn(range_type='LT3M', perf=lt3m_perf))
        self.CmltvRtrsBrkdwn.append(CmltvRtrsBrkdwn(range_type='LT1M', perf=lt1m_perf))
        self.CmltvRtrsBrkdwn.append(CmltvRtrsBrkdwn(range_type='LT1Y', perf=lt1y_perf))
        self.CmltvRtrsBrkdwn.append(CmltvRtrsBrkdwn(range_type='LT3Y', perf=lt3y_perf))
        self.CmltvRtrsBrkdwn.append(CmltvRtrsBrkdwn(range_type='LT5Y', perf=lt5y_perf))
        self.CmltvRtrsBrkdwn.append(CmltvRtrsBrkdwn(range_type='CYTD', perf=cytd_perf))
        self.StdPrtflVoltlyBrkdwn.append(StdPrtflVoltlyBrkdwn(range_type='LT1Y', perf=lt1y_vol))
        self.StdPrtflVoltlyBrkdwn.append(StdPrtflVoltlyBrkdwn(range_type='LT2Y', perf=lt2y_vol))
        self.StdPrtflVoltlyBrkdwn.append(StdPrtflVoltlyBrkdwn(range_type='LT3Y', perf=lt3y_vol))
        if lt1y_shadow_vol:
            self.ShdwPrtflVoltlyBrkdwn.append(StdPrtflVoltlyBrkdwn(range_type='LT1Y', perf=lt1y_shadow_vol))
        if lt2y_shadow_vol:
            self.ShdwPrtflVoltlyBrkdwn.append(StdPrtflVoltlyBrkdwn(range_type='LT2Y', perf=lt2y_shadow_vol))
        if lt3y_shadow_vol:
            self.ShdwPrtflVoltlyBrkdwn.append(StdPrtflVoltlyBrkdwn(range_type='LT3Y', perf=lt3y_shadow_vol))

        self.CalYrPrfrmncBrkdwn.append(CalYrPrfrmncBrkdwn(range_type='YMS2', perf=yms2_perf))
        self.CalYrPrfrmncBrkdwn.append(CalYrPrfrmncBrkdwn(range_type='YMN3', perf=ymn3_perf))
        self.CalYrPrfrmncBrkdwn.append(CalYrPrfrmncBrkdwn(range_type='YMS1', perf=yms1_perf))



class PrtflPrfrmnc(pmmfr.PerformanceFactors2__1):
    def __init__(self,
                 weighted_avg_maturity,
                 weighted_avg_life,
                 daily_maturing_asset_pct,
                 weekly_maturing_asset_pct,
                 ls1d_liquid=None,
                 d2t7_liquid=None,
                 d829_liquid=None,
                 a30d_liquid=None,
                 base_ccy_nav=None,
                 report_ccy_nav=None,
                 lt3m_perf=None,
                 lt1m_perf=None,
                 lt1y_perf=None,
                 lt3y_perf=None,
                 lt5y_perf=None,
                 cytd_perf=None,
                 lt1y_vol=None,
                 lt2y_vol=None,
                 lt3y_vol=None,
                 lt1y_shadow_vol=None,
                 lt2y_shadow_vol=None,
                 lt3y_shadow_vol=None,
                 yms2_perf=None,
                 ymn3_perf=None,
                 yms1_perf=None):
        super().__init__()
        self.FndValtn = FndValtn(weighted_avg_maturity, weighted_avg_life, base_ccy_nav, report_ccy_nav)
        self.LqdtyInf = LqdtyInf(daily_maturing_asset_pct, weekly_maturing_asset_pct, ls1d_liquid, d2t7_liquid,
                                 d829_liquid, a30d_liquid)
        self.Yld = Yld(lt3m_perf,
                       lt1m_perf,
                       lt1y_perf,
                       lt3y_perf,
                       lt5y_perf,
                       cytd_perf,
                       lt1y_vol,
                       lt2y_vol,
                       lt3y_vol,
                       lt1y_shadow_vol,
                       lt2y_shadow_vol,
                       lt3y_shadow_vol,
                       yms2_perf,
                       ymn3_perf,
                       yms1_perf)

# Liability

class LiabilityRate(pmmfr.Liability1__1):
    def __init__(self, estimated_rate, precise_rate):
        super().__init__()
        self.EstmtdRate = pmmfr.PercentageBoundedRate(estimated_rate)
        self.PreciseRate = pmmfr.PercentageBoundedRate(precise_rate)

class InvstrCncntrtn(pmmfr.InvestorConcentration1__1):
    def __init__(self, prof_estimated_rate, prof_precise_rate, retail_estimated_rate, retail_precise_rate):
        super().__init__()
        self.PrfssnlInvstrRate = LiabilityRate(prof_estimated_rate, prof_precise_rate)
        self.RtlInvstrRate = LiabilityRate(retail_estimated_rate, retail_precise_rate)

class InvestorGroupBreakdown(pmmfr.InvestorGroupBreakdownType2__1):
    def __init__(self,
                 investor_bank_pct,
                 investor_general_govt_pct,
                 investor_household_pct,
                 investor_insurance_pct,
                 investor_non_fin_pct,
                 investor_mmf_pct,
                 investor_other_fin_pct,
                 investor_pension_fund_pct,
                 investor_unknown_pct):
        super().__init__()
        self.BkRate = pmmfr.PercentageBoundedRate(investor_bank_pct)
        self.GnlGovntRate = pmmfr.PercentageBoundedRate(investor_general_govt_pct)
        self.HsHldRate = pmmfr.PercentageBoundedRate(investor_household_pct)
        self.InsrncCorptnRate = pmmfr.PercentageBoundedRate(investor_insurance_pct)
        self.NonFinCorptnRate = pmmfr.PercentageBoundedRate(investor_non_fin_pct)
        self.NonMnyMktFndInvstmtFndRate = pmmfr.PercentageBoundedRate(investor_mmf_pct)
        self.OthrFIRate = pmmfr.PercentageBoundedRate(investor_other_fin_pct)
        self.PnsnPlanOrFndRate = pmmfr.PercentageBoundedRate(investor_pension_fund_pct)
        self.UknwnRate = pmmfr.PercentageBoundedRate(investor_unknown_pct)

class Country1Choice__3(pmmfr.Country1Choice__3):
    def __init__(self, ctry):
        super().__init__()
        if ctry in supranationals:
            self.SprntnlCtry = pmmfr.TrueFalseIndicator_fixed__1(True)
        elif ctry in unknowns:
            self.UknwnCtry = pmmfr.TrueFalseIndicator_fixed__1(True)
        else:
            self.Ctry = pmmfr.CountryCode(ctry)

class CountryPct(pmmfr.BreakdownByCountry4__1):
    def __init__(self, ctry, pct):
        super().__init__()
        self.CtryOfRes = Country1Choice__3(ctry=ctry)
        self.Rate = pmmfr.PercentageBoundedRate(pct)

class BrkdwnByArrgmnt(pmmfr.BreakdownByArrangement2__1):
    def __init__(self, arrangement_type, pct):
        super().__init__()
        self.ArrgmntTp = pmmfr.ArrangementType4Code(arrangement_type)
        self.NetAsstValRate = pmmfr.PercentageBoundedRate(pct)

class MonthlyValue2Choice__1(pmmfr.MonthlyValue2Choice__1):
    def __init__(self, val):
        super().__init__()
        if val:
            self.Val = pmmfr.ImpliedCurrencyAndAmount(val)
        else:
            self.NotAvlblVal = pmmfr.NotAvailable1Code('NTAV')

class ForeignExchangeTerms36__1(pmmfr.ForeignExchangeTerms36__1):
    def __init__(self, ccy, xrate):
        super().__init__()
        self.UnitCcy = pmmfr.ActiveOrHistoricCurrencyCode_fixed('EUR')
        self.QtdCcy = pmmfr.ActiveOrHistoricCurrencyCode(ccy)
        self.XchgRate = pmmfr.BaseOneRate(xrate)

class MonthlyValue2Choice__2(pmmfr.MonthlyValue2Choice__2):
    def __init__(self, ccy, xrate):
        super().__init__()
        if ccy and xrate:
            self.FX = ForeignExchangeTerms36__1(ccy=ccy, xrate=xrate)
        else:
            self.NotAvlblVal = pmmfr.NotAvailable1Code('NTAV')


class MonthType3__1(pmmfr.MonthType3__1):
    def __init__(self, month, val):
        super().__init__()
        self.Mnth = pmmfr.ReportingPeriodType2Code__1("MM"+f"{month:02d}")
        self.Val = MonthlyValue2Choice__1(val)

class MonthType3__2(pmmfr.MonthType3__2):
    def __init__(self, month, val):
        super().__init__()
        self.Mnth = pmmfr.ReportingPeriodType2Code__2("MM"+f"{month:02d}")
        self.Val = MonthlyValue2Choice__1(val)

class MonthType3__3(pmmfr.MonthType3__3):
    def __init__(self, month, val):
        super().__init__()
        self.Mnth = pmmfr.ReportingPeriodType2Code__3("MM"+f"{month:02d}")
        self.Val = MonthlyValue2Choice__1(val)

class MonthType3__4(pmmfr.MonthType3__4):
    def __init__(self, month, val):
        super().__init__()
        self.Mnth = pmmfr.ReportingPeriodType2Code__4("MM"+f"{month:02d}")
        self.Val = MonthlyValue2Choice__1(val)

class MonthType3__5(pmmfr.MonthType3__5):
    def __init__(self, month, ccy, xrate):
        super().__init__()
        self.Val = MonthlyValue2Choice__2(ccy=ccy, xrate=xrate)
        self.Mnth = pmmfr.ReportingPeriodType2Code__1("MM"+f"{month:02d}")

class MonthType3__6(pmmfr.MonthType3__6):
    def __init__(self, month, ccy, xrate):
        super().__init__()
        self.Val = MonthlyValue2Choice__2(ccy=ccy, xrate=xrate)
        self.Mnth = pmmfr.ReportingPeriodType2Code__2("MM"+f"{month:02d}")

class MonthType3__7(pmmfr.MonthType3__7):
    def __init__(self, month, ccy, xrate):
        super().__init__()
        self.Val = MonthlyValue2Choice__2(ccy=ccy, xrate=xrate)
        self.Mnth = pmmfr.ReportingPeriodType2Code__3("MM"+f"{month:02d}")

class MonthType3__8(pmmfr.MonthType3__8):
    def __init__(self, month, ccy, xrate):
        super().__init__()
        self.Val = MonthlyValue2Choice__2(ccy=ccy, xrate=xrate)
        self.Mnth = pmmfr.ReportingPeriodType2Code__4("MM"+f"{month:02d}")


class Quarter3__1(pmmfr.Quarter3__1):
    def __init__(self, val):
        super().__init__()
        for m in range(3):
            self.MnthInf.append(MonthType3__1(month=m+1, val=val[m]))

class Quarter3__2(pmmfr.Quarter3__2):
    def __init__(self, val):
        super().__init__()
        for m in range(3):
            self.MnthInf.append(MonthType3__2(month=m+4, val=val[m]))

class Quarter3__3(pmmfr.Quarter3__3):
    def __init__(self, val):
        super().__init__()
        for m in range(3):
            self.MnthInf.append(MonthType3__3(month=m+7, val=val[m]))


class Quarter3__4(pmmfr.Quarter3__4):
    def __init__(self, val):
        super().__init__()
        for m in range(3):
            self.MnthInf.append(MonthType3__4(month=m+10, val=val[m]))

class Quarter3__5(pmmfr.Quarter3__5):
    def __init__(self, val):
        super().__init__()
        for m in range(3):
            self.MnthInf.append(MonthType3__5(month=m + 1, ccy=val[m].get('ccy'), xrate=val[m].get('xrate')))

class Quarter3__6(pmmfr.Quarter3__6):
    def __init__(self, val):
        super().__init__()
        for m in range(3):
            self.MnthInf.append(MonthType3__6(month=m + 4, ccy=val[m].get('ccy'), xrate=val[m].get('xrate')))

class Quarter3__7(pmmfr.Quarter3__7):
    def __init__(self, val):
        super().__init__()
        for m in range(3):
            self.MnthInf.append(MonthType3__7(month=m + 7, ccy=val[m].get('ccy'), xrate=val[m].get('xrate')))

class Quarter3__8(pmmfr.Quarter3__8):
    def __init__(self, val):
        super().__init__()
        for m in range(3):
            self.MnthInf.append(MonthType3__8(month=m + 10, ccy=val[m].get('ccy'), xrate=val[m].get('xrate')))


class MnthlyValue(pmmfr.MonthValue2__1):
    def __init__(self, monthly_val):
        super().__init__()
        self.FrstQrtr = Quarter3__1(val=monthly_val[:3])
        self.ScndQrtr = Quarter3__2(val=monthly_val[3:6])
        self.ThrdQrtr = Quarter3__3(val=monthly_val[6:9])
        self.FrthQrtr = Quarter3__4(val=monthly_val[9:12])


class MonthValue2__2(pmmfr.MonthValue2__2):
    def __init__(self, monthly_val):
        super().__init__()
        self.FrstQrtr = Quarter3__5(val=monthly_val[:3])
        self.ScndQrtr = Quarter3__6(val=monthly_val[3:6])
        self.ThrdQrtr = Quarter3__7(val=monthly_val[6:9])
        self.FrthQrtr = Quarter3__8(val=monthly_val[9:12])


class LbltyInf(pmmfr.LiabilityData3__1):
    def __init__(self,
                 highest_beneficial_owner_pct,
                 prof_estimated_rate,
                 prof_precise_rate,
                 retail_estimated_rate,
                 retail_precise_rate,
                 investor_bank_pct,
                 investor_general_govt_pct,
                 investor_household_pct,
                 investor_insurance_pct,
                 investor_non_fin_pct,
                 investor_mmf_pct,
                 investor_other_fin_pct,
                 investor_pension_fund_pct,
                 investor_unknown_pct,
                 country_breakdown_pct, #list
                 redemption_frequency, #enum -> in static data...
                 notice_period,
                 arrangement_breakdown_pct, #list
                 other_arrangement,
                 monthly_nav, #list,
                 monthly_subs, #list
                 monthly_redemption, #list
                 monthly_payment, #list
                 monthly_xrate #list of dict ccy/xrate
                 ):
        super().__init__()
        self.HghstBnfclOwnrRate = pmmfr.PercentageBoundedRate(highest_beneficial_owner_pct)
        self.InvstrCncntrtn = InvstrCncntrtn(prof_estimated_rate, prof_precise_rate, retail_estimated_rate, retail_precise_rate)
        for _ in range(9):
            self.InvstrGrpBrkdwn.append(InvestorGroupBreakdown(investor_bank_pct=investor_bank_pct,
                                                               investor_general_govt_pct=investor_general_govt_pct,
                                                               investor_household_pct=investor_household_pct,
                                                               investor_insurance_pct=investor_insurance_pct,
                                                               investor_non_fin_pct=investor_non_fin_pct,
                                                               investor_mmf_pct=investor_mmf_pct,
                                                               investor_other_fin_pct=investor_other_fin_pct,
                                                               investor_pension_fund_pct=investor_pension_fund_pct,
                                                               investor_unknown_pct=investor_unknown_pct))
        for country in country_breakdown_pct:
            for ctry, pct in country.items():
                self.BrkdwnByCtry.append(CountryPct(ctry, pct))
        self.RedDealgFrqcy = pmmfr.EventFrequency9Code__1(redemption_frequency)
        self.NtceDays = pmmfr.Max3Number(notice_period)
        for arrangement in arrangement_breakdown_pct:
            for arrangement_type, pct in arrangement.items():
                self.BrkdwnByArrgmnt.append(BrkdwnByArrgmnt(arrangement_type=arrangement_type, pct=pct))
        self.OthrArrgmntAddtlInf = pmmfr.Max350Text(other_arrangement) if other_arrangement else None
        self.MnthlyNetAsstValPerUnitInf = MnthlyValue(monthly_val=monthly_nav)
        self.MnthlySbcptInf = MnthlyValue(monthly_val=monthly_subs)
        self.MnthlyRedInf = MnthlyValue(monthly_val=monthly_redemption)
        self.MnthlyPmtToInvstrInf = MnthlyValue(monthly_val=monthly_payment)
        self.MnthlyXchgRateInf = MonthValue2__2(monthly_val=monthly_xrate)

# Stress Test
class StrssTst():
    pass