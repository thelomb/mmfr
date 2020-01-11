# ./mmfr_small.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:2f7fa5f5afdd2d587bab2d949cd2ee356861f34d
# Generated 2019-12-10 10:33:50.575289 by PyXB version 1.2.6 using Python 3.7.5.final.0
# Namespace urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01

from __future__ import unicode_literals
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys
import pyxb.utils.six as _six
# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:2c22852c-1b30-11ea-b726-88e9fe84fcb4')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.6'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# A holder for module-level binding classes so we can access them from
# inside class definitions where property names may conflict.
_module_typeBindings = pyxb.utils.utility.Object()

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be schema (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement, default_namespace=default_namespace)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, _six.text_type):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Atomic simple type: {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}ActiveCurrencyAndAmount__1_SimpleType
class ActiveCurrencyAndAmount__1_SimpleType (pyxb.binding.datatypes.decimal):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ActiveCurrencyAndAmount__1_SimpleType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 63, 4)
    _Documentation = None
ActiveCurrencyAndAmount__1_SimpleType._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=ActiveCurrencyAndAmount__1_SimpleType, value=pyxb.binding.datatypes.decimal('0.0'))
ActiveCurrencyAndAmount__1_SimpleType._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(18))
ActiveCurrencyAndAmount__1_SimpleType._CF_fractionDigits = pyxb.binding.facets.CF_fractionDigits(value=pyxb.binding.datatypes.nonNegativeInteger(5))
ActiveCurrencyAndAmount__1_SimpleType._InitializeFacetMap(ActiveCurrencyAndAmount__1_SimpleType._CF_minInclusive,
   ActiveCurrencyAndAmount__1_SimpleType._CF_totalDigits,
   ActiveCurrencyAndAmount__1_SimpleType._CF_fractionDigits)
Namespace.addCategoryObject('typeBinding', 'ActiveCurrencyAndAmount__1_SimpleType', ActiveCurrencyAndAmount__1_SimpleType)
_module_typeBindings.ActiveCurrencyAndAmount__1_SimpleType = ActiveCurrencyAndAmount__1_SimpleType

# Atomic simple type: {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}ActiveCurrencyCode_fixed
class ActiveCurrencyCode_fixed (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """ActiveCurrencyCode_fixed"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ActiveCurrencyCode_fixed')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 86, 4)
    _Documentation = 'ActiveCurrencyCode_fixed'
ActiveCurrencyCode_fixed._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ActiveCurrencyCode_fixed, enum_prefix=None)
ActiveCurrencyCode_fixed.EUR = ActiveCurrencyCode_fixed._CF_enumeration.addEnumeration(unicode_value='EUR', tag='EUR')
ActiveCurrencyCode_fixed._InitializeFacetMap(ActiveCurrencyCode_fixed._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ActiveCurrencyCode_fixed', ActiveCurrencyCode_fixed)
_module_typeBindings.ActiveCurrencyCode_fixed = ActiveCurrencyCode_fixed

# Atomic simple type: {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}ActiveOrHistoricCurrencyCode
class ActiveOrHistoricCurrencyCode (pyxb.binding.datatypes.string):

    """ActiveOrHistoricCurrencyCodeA code allocated to a currency by a Maintenance Agency under an international identification scheme, as described in the latest edition of the international standard ISO 4217 "Codes for the representation of currencies and funds"."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ActiveOrHistoricCurrencyCode')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 98, 4)
    _Documentation = 'ActiveOrHistoricCurrencyCodeA code allocated to a currency by a Maintenance Agency under an international identification scheme, as described in the latest edition of the international standard ISO 4217 "Codes for the representation of currencies and funds".'
ActiveOrHistoricCurrencyCode._CF_pattern = pyxb.binding.facets.CF_pattern()
ActiveOrHistoricCurrencyCode._CF_pattern.addPattern(pattern='[A-Z]{3,3}')
ActiveOrHistoricCurrencyCode._InitializeFacetMap(ActiveOrHistoricCurrencyCode._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'ActiveOrHistoricCurrencyCode', ActiveOrHistoricCurrencyCode)
_module_typeBindings.ActiveOrHistoricCurrencyCode = ActiveOrHistoricCurrencyCode

# Atomic simple type: {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}ActiveOrHistoricCurrencyCode_fixed
class ActiveOrHistoricCurrencyCode_fixed (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """ActiveOrHistoricCurrencyCode_fixed"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ActiveOrHistoricCurrencyCode_fixed')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 107, 4)
    _Documentation = 'ActiveOrHistoricCurrencyCode_fixed'
ActiveOrHistoricCurrencyCode_fixed._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ActiveOrHistoricCurrencyCode_fixed, enum_prefix=None)
ActiveOrHistoricCurrencyCode_fixed.EUR = ActiveOrHistoricCurrencyCode_fixed._CF_enumeration.addEnumeration(unicode_value='EUR', tag='EUR')
ActiveOrHistoricCurrencyCode_fixed._InitializeFacetMap(ActiveOrHistoricCurrencyCode_fixed._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ActiveOrHistoricCurrencyCode_fixed', ActiveOrHistoricCurrencyCode_fixed)
_module_typeBindings.ActiveOrHistoricCurrencyCode_fixed = ActiveOrHistoricCurrencyCode_fixed

# Atomic simple type: {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}ArrangementType4Code
class ArrangementType4Code (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """ArrangementType4CodeSpecifies the type of arrangement to which the fund is subject on."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ArrangementType4Code')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 178, 4)
    _Documentation = 'ArrangementType4CodeSpecifies the type of arrangement to which the fund is subject on.'
ArrangementType4Code._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ArrangementType4Code, enum_prefix=None)
ArrangementType4Code.SPRN = ArrangementType4Code._CF_enumeration.addEnumeration(unicode_value='SPRN', tag='SPRN')
ArrangementType4Code.GATE = ArrangementType4Code._CF_enumeration.addEnumeration(unicode_value='GATE', tag='GATE')
ArrangementType4Code.RDLF = ArrangementType4Code._CF_enumeration.addEnumeration(unicode_value='RDLF', tag='RDLF')
ArrangementType4Code.OTHR = ArrangementType4Code._CF_enumeration.addEnumeration(unicode_value='OTHR', tag='OTHR')
ArrangementType4Code._InitializeFacetMap(ArrangementType4Code._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ArrangementType4Code', ArrangementType4Code)
_module_typeBindings.ArrangementType4Code = ArrangementType4Code

# Atomic simple type: {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}ArrangementType5Code
class ArrangementType5Code (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """ArrangementType5CodeSpecifies the type of measure to which the fund is subject on."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ArrangementType5Code')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 210, 4)
    _Documentation = 'ArrangementType5CodeSpecifies the type of measure to which the fund is subject on.'
ArrangementType5Code._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ArrangementType5Code, enum_prefix=None)
ArrangementType5Code.RDLF = ArrangementType5Code._CF_enumeration.addEnumeration(unicode_value='RDLF', tag='RDLF')
ArrangementType5Code.NOAC = ArrangementType5Code._CF_enumeration.addEnumeration(unicode_value='NOAC', tag='NOAC')
ArrangementType5Code.GATE = ArrangementType5Code._CF_enumeration.addEnumeration(unicode_value='GATE', tag='GATE')
ArrangementType5Code.SPDL = ArrangementType5Code._CF_enumeration.addEnumeration(unicode_value='SPDL', tag='SPDL')
ArrangementType5Code._InitializeFacetMap(ArrangementType5Code._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ArrangementType5Code', ArrangementType5Code)
_module_typeBindings.ArrangementType5Code = ArrangementType5Code

# Atomic simple type: {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}ArrangementType6Code
class ArrangementType6Code (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """ArrangementType6CodeSpecifies the type of measure to which the fund is subject on."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ArrangementType6Code')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 242, 4)
    _Documentation = 'ArrangementType6CodeSpecifies the type of measure to which the fund is subject on.'
ArrangementType6Code._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ArrangementType6Code, enum_prefix=None)
ArrangementType6Code.SPDL = ArrangementType6Code._CF_enumeration.addEnumeration(unicode_value='SPDL', tag='SPDL')
ArrangementType6Code.RDLF = ArrangementType6Code._CF_enumeration.addEnumeration(unicode_value='RDLF', tag='RDLF')
ArrangementType6Code._InitializeFacetMap(ArrangementType6Code._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ArrangementType6Code', ArrangementType6Code)
_module_typeBindings.ArrangementType6Code = ArrangementType6Code

# Atomic simple type: {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}AssessmentResultType2Code
class AssessmentResultType2Code (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """AssessmentResultType2CodeSpecifies whether the result of the assessment is favorable or unfavorable."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AssessmentResultType2Code')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 262, 4)
    _Documentation = 'AssessmentResultType2CodeSpecifies whether the result of the assessment is favorable or unfavorable.'
AssessmentResultType2Code._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=AssessmentResultType2Code, enum_prefix=None)
AssessmentResultType2Code.FVRB = AssessmentResultType2Code._CF_enumeration.addEnumeration(unicode_value='FVRB', tag='FVRB')
AssessmentResultType2Code.NOAP = AssessmentResultType2Code._CF_enumeration.addEnumeration(unicode_value='NOAP', tag='NOAP')
AssessmentResultType2Code.UFVB = AssessmentResultType2Code._CF_enumeration.addEnumeration(unicode_value='UFVB', tag='UFVB')
AssessmentResultType2Code.NOVF = AssessmentResultType2Code._CF_enumeration.addEnumeration(unicode_value='NOVF', tag='NOVF')
AssessmentResultType2Code._InitializeFacetMap(AssessmentResultType2Code._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'AssessmentResultType2Code', AssessmentResultType2Code)
_module_typeBindings.AssessmentResultType2Code = AssessmentResultType2Code

# Atomic simple type: {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}BaseOneRate
class BaseOneRate (pyxb.binding.datatypes.decimal):

    """BaseOneRateRate expressed as a decimal, for example, 0.7 is 7/10 and 70%."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BaseOneRate')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 693, 4)
    _Documentation = 'BaseOneRateRate expressed as a decimal, for example, 0.7 is 7/10 and 70%.'
BaseOneRate._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(11))
BaseOneRate._CF_fractionDigits = pyxb.binding.facets.CF_fractionDigits(value=pyxb.binding.datatypes.nonNegativeInteger(10))
BaseOneRate._InitializeFacetMap(BaseOneRate._CF_totalDigits,
   BaseOneRate._CF_fractionDigits)
Namespace.addCategoryObject('typeBinding', 'BaseOneRate', BaseOneRate)
_module_typeBindings.BaseOneRate = BaseOneRate

# Atomic simple type: {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}CFIOct2015Identifier
class CFIOct2015Identifier (pyxb.binding.datatypes.string):

    """CFIOct2015IdentifierClassification type of the financial instrument, as per the ISO 10962 Classification of Financial Instrument (CFI) codification, for example, common share with voting rights, fully paid, or registered."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CFIOct2015Identifier')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 743, 4)
    _Documentation = 'CFIOct2015IdentifierClassification type of the financial instrument, as per the ISO 10962 Classification of Financial Instrument (CFI) codification, for example, common share with voting rights, fully paid, or registered.'
CFIOct2015Identifier._CF_pattern = pyxb.binding.facets.CF_pattern()
CFIOct2015Identifier._CF_pattern.addPattern(pattern='[A-Z]{6,6}')
CFIOct2015Identifier._InitializeFacetMap(CFIOct2015Identifier._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'CFIOct2015Identifier', CFIOct2015Identifier)
_module_typeBindings.CFIOct2015Identifier = CFIOct2015Identifier

# Atomic simple type: {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}CountryCode
class CountryCode (pyxb.binding.datatypes.string):

    """CountryCodeCode to identify a country, a dependency, or another area of particular geopolitical interest, on the basis of country names obtained from the United Nations (ISO 3166, Alpha-2 code)."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CountryCode')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 871, 4)
    _Documentation = 'CountryCodeCode to identify a country, a dependency, or another area of particular geopolitical interest, on the basis of country names obtained from the United Nations (ISO 3166, Alpha-2 code).'
CountryCode._CF_pattern = pyxb.binding.facets.CF_pattern()
CountryCode._CF_pattern.addPattern(pattern='[A-Z]{2,2}')
CountryCode._InitializeFacetMap(CountryCode._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'CountryCode', CountryCode)
_module_typeBindings.CountryCode = CountryCode

# Atomic simple type: {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}DecimalNumber
class DecimalNumber (pyxb.binding.datatypes.decimal):

    """DecimalNumberNumber of objects represented as a decimal number, for example 0.75 or 45.6."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DecimalNumber')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 920, 4)
    _Documentation = 'DecimalNumberNumber of objects represented as a decimal number, for example 0.75 or 45.6.'
DecimalNumber._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(18))
DecimalNumber._CF_fractionDigits = pyxb.binding.facets.CF_fractionDigits(value=pyxb.binding.datatypes.nonNegativeInteger(17))
DecimalNumber._InitializeFacetMap(DecimalNumber._CF_totalDigits,
   DecimalNumber._CF_fractionDigits)
Namespace.addCategoryObject('typeBinding', 'DecimalNumber', DecimalNumber)
_module_typeBindings.DecimalNumber = DecimalNumber

# Atomic simple type: {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}EventFrequency9Code__1
class EventFrequency9Code__1 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """EventFrequency9Code__1Specifies the regularity of an event."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'EventFrequency9Code__1')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 961, 4)
    _Documentation = 'EventFrequency9Code__1Specifies the regularity of an event.'
EventFrequency9Code__1._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=EventFrequency9Code__1, enum_prefix=None)
EventFrequency9Code__1.MNTH = EventFrequency9Code__1._CF_enumeration.addEnumeration(unicode_value='MNTH', tag='MNTH')
EventFrequency9Code__1.TWMN = EventFrequency9Code__1._CF_enumeration.addEnumeration(unicode_value='TWMN', tag='TWMN')
EventFrequency9Code__1.WEEK = EventFrequency9Code__1._CF_enumeration.addEnumeration(unicode_value='WEEK', tag='WEEK')
EventFrequency9Code__1.DAIL = EventFrequency9Code__1._CF_enumeration.addEnumeration(unicode_value='DAIL', tag='DAIL')
EventFrequency9Code__1.ADHO = EventFrequency9Code__1._CF_enumeration.addEnumeration(unicode_value='ADHO', tag='ADHO')
EventFrequency9Code__1.NONE = EventFrequency9Code__1._CF_enumeration.addEnumeration(unicode_value='NONE', tag='NONE')
EventFrequency9Code__1._InitializeFacetMap(EventFrequency9Code__1._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'EventFrequency9Code__1', EventFrequency9Code__1)
_module_typeBindings.EventFrequency9Code__1 = EventFrequency9Code__1

# Atomic simple type: {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}FinancialAssetType2Code__1
class FinancialAssetType2Code__1 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """FinancialAssetType2Code__1Categorisation of financial asset type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'FinancialAssetType2Code__1')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1005, 4)
    _Documentation = 'FinancialAssetType2Code__1Categorisation of financial asset type.'
FinancialAssetType2Code__1._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=FinancialAssetType2Code__1, enum_prefix=None)
FinancialAssetType2Code__1.MMII = FinancialAssetType2Code__1._CF_enumeration.addEnumeration(unicode_value='MMII', tag='MMII')
FinancialAssetType2Code__1._InitializeFacetMap(FinancialAssetType2Code__1._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'FinancialAssetType2Code__1', FinancialAssetType2Code__1)
_module_typeBindings.FinancialAssetType2Code__1 = FinancialAssetType2Code__1

# Atomic simple type: {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}FinancialAssetType2Code__2
class FinancialAssetType2Code__2 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """FinancialAssetType2Code__2Categorisation of financial asset type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'FinancialAssetType2Code__2')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1019, 4)
    _Documentation = 'FinancialAssetType2Code__2Categorisation of financial asset type.'
FinancialAssetType2Code__2._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=FinancialAssetType2Code__2, enum_prefix=None)
FinancialAssetType2Code__2.STSA = FinancialAssetType2Code__2._CF_enumeration.addEnumeration(unicode_value='STSA', tag='STSA')
FinancialAssetType2Code__2.SCRT = FinancialAssetType2Code__2._CF_enumeration.addEnumeration(unicode_value='SCRT', tag='SCRT')
FinancialAssetType2Code__2.ABCP = FinancialAssetType2Code__2._CF_enumeration.addEnumeration(unicode_value='ABCP', tag='ABCP')
FinancialAssetType2Code__2.STSS = FinancialAssetType2Code__2._CF_enumeration.addEnumeration(unicode_value='STSS', tag='STSS')
FinancialAssetType2Code__2._InitializeFacetMap(FinancialAssetType2Code__2._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'FinancialAssetType2Code__2', FinancialAssetType2Code__2)
_module_typeBindings.FinancialAssetType2Code__2 = FinancialAssetType2Code__2

# Atomic simple type: {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}FinancialAssetType2Code__3
class FinancialAssetType2Code__3 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """FinancialAssetType2Code__3Categorisation of financial asset type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'FinancialAssetType2Code__3')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1051, 4)
    _Documentation = 'FinancialAssetType2Code__3Categorisation of financial asset type.'
FinancialAssetType2Code__3._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=FinancialAssetType2Code__3, enum_prefix=None)
FinancialAssetType2Code__3.OTCD = FinancialAssetType2Code__3._CF_enumeration.addEnumeration(unicode_value='OTCD', tag='OTCD')
FinancialAssetType2Code__3.RMTD = FinancialAssetType2Code__3._CF_enumeration.addEnumeration(unicode_value='RMTD', tag='RMTD')
FinancialAssetType2Code__3._InitializeFacetMap(FinancialAssetType2Code__3._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'FinancialAssetType2Code__3', FinancialAssetType2Code__3)
_module_typeBindings.FinancialAssetType2Code__3 = FinancialAssetType2Code__3

# Atomic simple type: {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}FinancialAssetType2Code__4
class FinancialAssetType2Code__4 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """FinancialAssetType2Code__4Categorisation of financial asset type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'FinancialAssetType2Code__4')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1071, 4)
    _Documentation = 'FinancialAssetType2Code__4Categorisation of financial asset type.'
FinancialAssetType2Code__4._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=FinancialAssetType2Code__4, enum_prefix=None)
FinancialAssetType2Code__4.MMFT = FinancialAssetType2Code__4._CF_enumeration.addEnumeration(unicode_value='MMFT', tag='MMFT')
FinancialAssetType2Code__4._InitializeFacetMap(FinancialAssetType2Code__4._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'FinancialAssetType2Code__4', FinancialAssetType2Code__4)
_module_typeBindings.FinancialAssetType2Code__4 = FinancialAssetType2Code__4

# Atomic simple type: {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}FinancialAssetType2Code__5
class FinancialAssetType2Code__5 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """FinancialAssetType2Code__5Categorisation of financial asset type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'FinancialAssetType2Code__5')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1085, 4)
    _Documentation = 'FinancialAssetType2Code__5Categorisation of financial asset type.'
FinancialAssetType2Code__5._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=FinancialAssetType2Code__5, enum_prefix=None)
FinancialAssetType2Code__5.DPSC = FinancialAssetType2Code__5._CF_enumeration.addEnumeration(unicode_value='DPSC', tag='DPSC')
FinancialAssetType2Code__5.ANLA = FinancialAssetType2Code__5._CF_enumeration.addEnumeration(unicode_value='ANLA', tag='ANLA')
FinancialAssetType2Code__5._InitializeFacetMap(FinancialAssetType2Code__5._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'FinancialAssetType2Code__5', FinancialAssetType2Code__5)
_module_typeBindings.FinancialAssetType2Code__5 = FinancialAssetType2Code__5

# Atomic simple type: {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}FinancialAssetType2Code__6
class FinancialAssetType2Code__6 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """FinancialAssetType2Code__6Categorisation of financial asset type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'FinancialAssetType2Code__6')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1105, 4)
    _Documentation = 'FinancialAssetType2Code__6Categorisation of financial asset type.'
FinancialAssetType2Code__6._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=FinancialAssetType2Code__6, enum_prefix=None)
FinancialAssetType2Code__6.RVPO = FinancialAssetType2Code__6._CF_enumeration.addEnumeration(unicode_value='RVPO', tag='RVPO')
FinancialAssetType2Code__6.REPO = FinancialAssetType2Code__6._CF_enumeration.addEnumeration(unicode_value='REPO', tag='REPO')
FinancialAssetType2Code__6._InitializeFacetMap(FinancialAssetType2Code__6._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'FinancialAssetType2Code__6', FinancialAssetType2Code__6)
_module_typeBindings.FinancialAssetType2Code__6 = FinancialAssetType2Code__6

# Atomic simple type: {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}FinancialInstrumentContractType3Code
class FinancialInstrumentContractType3Code (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """FinancialInstrumentContractType3CodeSpecifies the contract type of a derivative financial instrument."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'FinancialInstrumentContractType3Code')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1283, 4)
    _Documentation = 'FinancialInstrumentContractType3CodeSpecifies the contract type of a derivative financial instrument.'
FinancialInstrumentContractType3Code._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=FinancialInstrumentContractType3Code, enum_prefix=None)
FinancialInstrumentContractType3Code.CFDS = FinancialInstrumentContractType3Code._CF_enumeration.addEnumeration(unicode_value='CFDS', tag='CFDS')
FinancialInstrumentContractType3Code.FRAS = FinancialInstrumentContractType3Code._CF_enumeration.addEnumeration(unicode_value='FRAS', tag='FRAS')
FinancialInstrumentContractType3Code.FUTR = FinancialInstrumentContractType3Code._CF_enumeration.addEnumeration(unicode_value='FUTR', tag='FUTR')
FinancialInstrumentContractType3Code.FORW = FinancialInstrumentContractType3Code._CF_enumeration.addEnumeration(unicode_value='FORW', tag='FORW')
FinancialInstrumentContractType3Code.OPTN = FinancialInstrumentContractType3Code._CF_enumeration.addEnumeration(unicode_value='OPTN', tag='OPTN')
FinancialInstrumentContractType3Code.SWAP = FinancialInstrumentContractType3Code._CF_enumeration.addEnumeration(unicode_value='SWAP', tag='SWAP')
FinancialInstrumentContractType3Code.SWPT = FinancialInstrumentContractType3Code._CF_enumeration.addEnumeration(unicode_value='SWPT', tag='SWPT')
FinancialInstrumentContractType3Code.OTHR = FinancialInstrumentContractType3Code._CF_enumeration.addEnumeration(unicode_value='OTHR', tag='OTHR')
FinancialInstrumentContractType3Code.FWOS = FinancialInstrumentContractType3Code._CF_enumeration.addEnumeration(unicode_value='FWOS', tag='FWOS')
FinancialInstrumentContractType3Code.FONS = FinancialInstrumentContractType3Code._CF_enumeration.addEnumeration(unicode_value='FONS', tag='FONS')
FinancialInstrumentContractType3Code._InitializeFacetMap(FinancialInstrumentContractType3Code._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'FinancialInstrumentContractType3Code', FinancialInstrumentContractType3Code)
_module_typeBindings.FinancialInstrumentContractType3Code = FinancialInstrumentContractType3Code

# Atomic simple type: {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}FinancingUnderlyingType1Code
class FinancingUnderlyingType1Code (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """FinancingUnderlyingType1CodeCategorisation of financial asset type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'FinancingUnderlyingType1Code')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1609, 4)
    _Documentation = 'FinancingUnderlyingType1CodeCategorisation of financial asset type.'
FinancingUnderlyingType1Code._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=FinancingUnderlyingType1Code, enum_prefix=None)
FinancingUnderlyingType1Code.CMBS = FinancingUnderlyingType1Code._CF_enumeration.addEnumeration(unicode_value='CMBS', tag='CMBS')
FinancingUnderlyingType1Code.CSML = FinancingUnderlyingType1Code._CF_enumeration.addEnumeration(unicode_value='CSML', tag='CSML')
FinancingUnderlyingType1Code.CCRB = FinancingUnderlyingType1Code._CF_enumeration.addEnumeration(unicode_value='CCRB', tag='CCRB')
FinancingUnderlyingType1Code.LESG = FinancingUnderlyingType1Code._CF_enumeration.addEnumeration(unicode_value='LESG', tag='LESG')
FinancingUnderlyingType1Code.LTCS = FinancingUnderlyingType1Code._CF_enumeration.addEnumeration(unicode_value='LTCS', tag='LTCS')
FinancingUnderlyingType1Code.OTHR = FinancingUnderlyingType1Code._CF_enumeration.addEnumeration(unicode_value='OTHR', tag='OTHR')
FinancingUnderlyingType1Code.RMBS = FinancingUnderlyingType1Code._CF_enumeration.addEnumeration(unicode_value='RMBS', tag='RMBS')
FinancingUnderlyingType1Code.TDRB = FinancingUnderlyingType1Code._CF_enumeration.addEnumeration(unicode_value='TDRB', tag='TDRB')
FinancingUnderlyingType1Code._InitializeFacetMap(FinancingUnderlyingType1Code._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'FinancingUnderlyingType1Code', FinancingUnderlyingType1Code)
_module_typeBindings.FinancingUnderlyingType1Code = FinancingUnderlyingType1Code

# Atomic simple type: {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}ISINOct2015Identifier
class ISINOct2015Identifier (pyxb.binding.datatypes.string):

    """ISINOct2015IdentifierInternational Securities Identification Number (ISIN). A numbering system designed by the United Nation's International Organisation for Standardisation (ISO). The ISIN is composed of a 2-character prefix representing the country of issue, followed by the national security number (if one exists), and a check digit. Each country has a national numbering agency that assigns ISIN numbers for securities in that country."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ISINOct2015Identifier')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1960, 4)
    _Documentation = "ISINOct2015IdentifierInternational Securities Identification Number (ISIN). A numbering system designed by the United Nation's International Organisation for Standardisation (ISO). The ISIN is composed of a 2-character prefix representing the country of issue, followed by the national security number (if one exists), and a check digit. Each country has a national numbering agency that assigns ISIN numbers for securities in that country."
ISINOct2015Identifier._CF_pattern = pyxb.binding.facets.CF_pattern()
ISINOct2015Identifier._CF_pattern.addPattern(pattern='[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}')
ISINOct2015Identifier._InitializeFacetMap(ISINOct2015Identifier._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'ISINOct2015Identifier', ISINOct2015Identifier)
_module_typeBindings.ISINOct2015Identifier = ISINOct2015Identifier

# Atomic simple type: {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}ISODate
class ISODate (pyxb.binding.datatypes.date):

    """ISODateA particular point in the progression of time in a calendar year expressed in the YYYY-MM-DD format. This representation is defined in "XML Schema Part 2: Datatypes Second Edition - W3C Recommendation 28 October 2004" which is aligned with ISO 8601."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ISODate')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1969, 4)
    _Documentation = 'ISODateA particular point in the progression of time in a calendar year expressed in the YYYY-MM-DD format. This representation is defined in "XML Schema Part 2: Datatypes Second Edition - W3C Recommendation 28 October 2004" which is aligned with ISO 8601.'
ISODate._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'ISODate', ISODate)
_module_typeBindings.ISODate = ISODate

# Atomic simple type: {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}ISOYear
class ISOYear (pyxb.binding.datatypes.gYear):

    """ISOYearYear represented by YYYY (ISO 8601)."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ISOYear')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1976, 4)
    _Documentation = 'ISOYearYear represented by YYYY (ISO 8601).'
ISOYear._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'ISOYear', ISOYear)
_module_typeBindings.ISOYear = ISOYear

# Atomic simple type: {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}ImpliedCurrencyAndAmount
class ImpliedCurrencyAndAmount (pyxb.binding.datatypes.decimal):

    """ImpliedCurrencyAndAmountNumber of monetary units specified in a currency where the unit of currency is implied by the context and compliant with ISO 4217. The decimal separator is a dot.
Note: a zero amount is considered a positive amount."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ImpliedCurrencyAndAmount')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1983, 4)
    _Documentation = 'ImpliedCurrencyAndAmountNumber of monetary units specified in a currency where the unit of currency is implied by the context and compliant with ISO 4217. The decimal separator is a dot.\nNote: a zero amount is considered a positive amount.'
ImpliedCurrencyAndAmount._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=ImpliedCurrencyAndAmount, value=pyxb.binding.datatypes.decimal('0.0'))
ImpliedCurrencyAndAmount._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(18))
ImpliedCurrencyAndAmount._CF_fractionDigits = pyxb.binding.facets.CF_fractionDigits(value=pyxb.binding.datatypes.nonNegativeInteger(5))
ImpliedCurrencyAndAmount._InitializeFacetMap(ImpliedCurrencyAndAmount._CF_minInclusive,
   ImpliedCurrencyAndAmount._CF_totalDigits,
   ImpliedCurrencyAndAmount._CF_fractionDigits)
Namespace.addCategoryObject('typeBinding', 'ImpliedCurrencyAndAmount', ImpliedCurrencyAndAmount)
_module_typeBindings.ImpliedCurrencyAndAmount = ImpliedCurrencyAndAmount

# Atomic simple type: {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}LEIIdentifier
class LEIIdentifier (pyxb.binding.datatypes.string):

    """LEIIdentifierLegal Entity Identifier is a code allocated to a party as described in ISO 17442 "Financial Services - Legal Entity Identifier (LEI)"."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LEIIdentifier')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2158, 4)
    _Documentation = 'LEIIdentifierLegal Entity Identifier is a code allocated to a party as described in ISO 17442 "Financial Services - Legal Entity Identifier (LEI)".'
LEIIdentifier._CF_pattern = pyxb.binding.facets.CF_pattern()
LEIIdentifier._CF_pattern.addPattern(pattern='[A-Z0-9]{18,18}[0-9]{2,2}')
LEIIdentifier._InitializeFacetMap(LEIIdentifier._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'LEIIdentifier', LEIIdentifier)
_module_typeBindings.LEIIdentifier = LEIIdentifier

# Atomic simple type: {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}LegalFramework2Code
class LegalFramework2Code (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """LegalFramework2CodeIdentifies the legal framework of the fund."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LegalFramework2Code')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2167, 4)
    _Documentation = 'LegalFramework2CodeIdentifies the legal framework of the fund.'
LegalFramework2Code._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=LegalFramework2Code, enum_prefix=None)
LegalFramework2Code.UCIT = LegalFramework2Code._CF_enumeration.addEnumeration(unicode_value='UCIT', tag='UCIT')
LegalFramework2Code.AIFD = LegalFramework2Code._CF_enumeration.addEnumeration(unicode_value='AIFD', tag='AIFD')
LegalFramework2Code._InitializeFacetMap(LegalFramework2Code._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'LegalFramework2Code', LegalFramework2Code)
_module_typeBindings.LegalFramework2Code = LegalFramework2Code

# Atomic simple type: {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}MasterFundType1Code
class MasterFundType1Code (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """MasterFundType1CodeIndicates whether the fund is a master or a feeder fund."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MasterFundType1Code')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2367, 4)
    _Documentation = 'MasterFundType1CodeIndicates whether the fund is a master or a feeder fund.'
MasterFundType1Code._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=MasterFundType1Code, enum_prefix=None)
MasterFundType1Code.FDER = MasterFundType1Code._CF_enumeration.addEnumeration(unicode_value='FDER', tag='FDER')
MasterFundType1Code.MSTR = MasterFundType1Code._CF_enumeration.addEnumeration(unicode_value='MSTR', tag='MSTR')
MasterFundType1Code.NONE = MasterFundType1Code._CF_enumeration.addEnumeration(unicode_value='NONE', tag='NONE')
MasterFundType1Code._InitializeFacetMap(MasterFundType1Code._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'MasterFundType1Code', MasterFundType1Code)
_module_typeBindings.MasterFundType1Code = MasterFundType1Code

# Atomic simple type: {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}Max2000Text
class Max2000Text (pyxb.binding.datatypes.string):

    """Max2000TextSpecifies a character string with a maximum length of 2000 characters."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Max2000Text')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2419, 4)
    _Documentation = 'Max2000TextSpecifies a character string with a maximum length of 2000 characters.'
Max2000Text._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
Max2000Text._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(2000))
Max2000Text._InitializeFacetMap(Max2000Text._CF_minLength,
   Max2000Text._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'Max2000Text', Max2000Text)
_module_typeBindings.Max2000Text = Max2000Text

# Atomic simple type: {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}Max350Text
class Max350Text (pyxb.binding.datatypes.string):

    """Max350TextSpecifies a character string with a maximum length of 350 characters."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Max350Text')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2429, 4)
    _Documentation = 'Max350TextSpecifies a character string with a maximum length of 350 characters.'
Max350Text._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
Max350Text._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(350))
Max350Text._InitializeFacetMap(Max350Text._CF_minLength,
   Max350Text._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'Max350Text', Max350Text)
_module_typeBindings.Max350Text = Max350Text

# Atomic simple type: {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}Max35Text
class Max35Text (pyxb.binding.datatypes.string):

    """Max35TextSpecifies a character string with a maximum length of 35 characters."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Max35Text')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2439, 4)
    _Documentation = 'Max35TextSpecifies a character string with a maximum length of 35 characters.'
Max35Text._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
Max35Text._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(35))
Max35Text._InitializeFacetMap(Max35Text._CF_minLength,
   Max35Text._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'Max35Text', Max35Text)
_module_typeBindings.Max35Text = Max35Text

# Atomic simple type: {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}Max35Text_fixed
class Max35Text_fixed (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Max35Text_fixed"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Max35Text_fixed')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2449, 4)
    _Documentation = 'Max35Text_fixed'
Max35Text_fixed._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=Max35Text_fixed, enum_prefix=None)
Max35Text_fixed.ECB = Max35Text_fixed._CF_enumeration.addEnumeration(unicode_value='ECB', tag='ECB')
Max35Text_fixed._InitializeFacetMap(Max35Text_fixed._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'Max35Text_fixed', Max35Text_fixed)
_module_typeBindings.Max35Text_fixed = Max35Text_fixed

# Atomic simple type: {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}Max3Number
class Max3Number (pyxb.binding.datatypes.decimal):

    """Max3NumberNumber (max 999) of objects represented as an integer."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Max3Number')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2461, 4)
    _Documentation = 'Max3NumberNumber (max 999) of objects represented as an integer.'
Max3Number._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(3))
Max3Number._CF_fractionDigits = pyxb.binding.facets.CF_fractionDigits(value=pyxb.binding.datatypes.nonNegativeInteger(0))
Max3Number._InitializeFacetMap(Max3Number._CF_totalDigits,
   Max3Number._CF_fractionDigits)
Namespace.addCategoryObject('typeBinding', 'Max3Number', Max3Number)
_module_typeBindings.Max3Number = Max3Number

# Atomic simple type: {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}Max52Text
class Max52Text (pyxb.binding.datatypes.string):

    """Max52TextSpecifies a character string with a maximum length of 52 characters."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Max52Text')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2471, 4)
    _Documentation = 'Max52TextSpecifies a character string with a maximum length of 52 characters.'
Max52Text._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
Max52Text._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(52))
Max52Text._InitializeFacetMap(Max52Text._CF_minLength,
   Max52Text._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'Max52Text', Max52Text)
_module_typeBindings.Max52Text = Max52Text

# Atomic simple type: {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}Max5Number
class Max5Number (pyxb.binding.datatypes.decimal):

    """Max5NumberNumber (max 99999) of objects represented as an integer."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Max5Number')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2481, 4)
    _Documentation = 'Max5NumberNumber (max 99999) of objects represented as an integer.'
Max5Number._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(5))
Max5Number._CF_fractionDigits = pyxb.binding.facets.CF_fractionDigits(value=pyxb.binding.datatypes.nonNegativeInteger(0))
Max5Number._InitializeFacetMap(Max5Number._CF_totalDigits,
   Max5Number._CF_fractionDigits)
Namespace.addCategoryObject('typeBinding', 'Max5Number', Max5Number)
_module_typeBindings.Max5Number = Max5Number

# Atomic simple type: {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}MoneyMarketFundType1Code
class MoneyMarketFundType1Code (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """MoneyMarketFundType1CodeSpecifies the type of the money market fund."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MoneyMarketFundType1Code')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2542, 4)
    _Documentation = 'MoneyMarketFundType1CodeSpecifies the type of the money market fund.'
MoneyMarketFundType1Code._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=MoneyMarketFundType1Code, enum_prefix=None)
MoneyMarketFundType1Code.STLV = MoneyMarketFundType1Code._CF_enumeration.addEnumeration(unicode_value='STLV', tag='STLV')
MoneyMarketFundType1Code.STCN = MoneyMarketFundType1Code._CF_enumeration.addEnumeration(unicode_value='STCN', tag='STCN')
MoneyMarketFundType1Code.STVN = MoneyMarketFundType1Code._CF_enumeration.addEnumeration(unicode_value='STVN', tag='STVN')
MoneyMarketFundType1Code.SDVN = MoneyMarketFundType1Code._CF_enumeration.addEnumeration(unicode_value='SDVN', tag='SDVN')
MoneyMarketFundType1Code._InitializeFacetMap(MoneyMarketFundType1Code._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'MoneyMarketFundType1Code', MoneyMarketFundType1Code)
_module_typeBindings.MoneyMarketFundType1Code = MoneyMarketFundType1Code

# Atomic simple type: {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}NetAssetValueBasis1Code
class NetAssetValueBasis1Code (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """NetAssetValueBasis1CodeIdentifies whether the net asset value used as a basis for the stress test scenario is the constant net asset value."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'NetAssetValueBasis1Code')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2864, 4)
    _Documentation = 'NetAssetValueBasis1CodeIdentifies whether the net asset value used as a basis for the stress test scenario is the constant net asset value.'
NetAssetValueBasis1Code._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=NetAssetValueBasis1Code, enum_prefix=None)
NetAssetValueBasis1Code.CNAV = NetAssetValueBasis1Code._CF_enumeration.addEnumeration(unicode_value='CNAV', tag='CNAV')
NetAssetValueBasis1Code.NAVL = NetAssetValueBasis1Code._CF_enumeration.addEnumeration(unicode_value='NAVL', tag='NAVL')
NetAssetValueBasis1Code._InitializeFacetMap(NetAssetValueBasis1Code._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'NetAssetValueBasis1Code', NetAssetValueBasis1Code)
_module_typeBindings.NetAssetValueBasis1Code = NetAssetValueBasis1Code

# Atomic simple type: {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}NoVulnerability1Code_fixed
class NoVulnerability1Code_fixed (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """NoVulnerability1Code_fixed"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'NoVulnerability1Code_fixed')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2884, 4)
    _Documentation = 'NoVulnerability1Code_fixed'
NoVulnerability1Code_fixed._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=NoVulnerability1Code_fixed, enum_prefix=None)
NoVulnerability1Code_fixed.NOVN = NoVulnerability1Code_fixed._CF_enumeration.addEnumeration(unicode_value='NOVN', tag='NOVN')
NoVulnerability1Code_fixed._InitializeFacetMap(NoVulnerability1Code_fixed._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'NoVulnerability1Code_fixed', NoVulnerability1Code_fixed)
_module_typeBindings.NoVulnerability1Code_fixed = NoVulnerability1Code_fixed

# Atomic simple type: {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}NonNegativeDecimalNumber
class NonNegativeDecimalNumber (pyxb.binding.datatypes.decimal):

    """NonNegativeDecimalNumberNumber of objects represented as a non negative decimal number, for example, 0.75 or 45.6."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'NonNegativeDecimalNumber')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2896, 4)
    _Documentation = 'NonNegativeDecimalNumberNumber of objects represented as a non negative decimal number, for example, 0.75 or 45.6.'
NonNegativeDecimalNumber._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=NonNegativeDecimalNumber, value=pyxb.binding.datatypes.decimal('0.0'))
NonNegativeDecimalNumber._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(18))
NonNegativeDecimalNumber._CF_fractionDigits = pyxb.binding.facets.CF_fractionDigits(value=pyxb.binding.datatypes.nonNegativeInteger(17))
NonNegativeDecimalNumber._InitializeFacetMap(NonNegativeDecimalNumber._CF_minInclusive,
   NonNegativeDecimalNumber._CF_totalDigits,
   NonNegativeDecimalNumber._CF_fractionDigits)
Namespace.addCategoryObject('typeBinding', 'NonNegativeDecimalNumber', NonNegativeDecimalNumber)
_module_typeBindings.NonNegativeDecimalNumber = NonNegativeDecimalNumber

# Atomic simple type: {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}NotAvailable1Code
class NotAvailable1Code (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """NotAvailable1CodeSpecifies a not available value code."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'NotAvailable1Code')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2907, 4)
    _Documentation = 'NotAvailable1CodeSpecifies a not available value code.'
NotAvailable1Code._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=NotAvailable1Code, enum_prefix=None)
NotAvailable1Code.NTAV = NotAvailable1Code._CF_enumeration.addEnumeration(unicode_value='NTAV', tag='NTAV')
NotAvailable1Code._InitializeFacetMap(NotAvailable1Code._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'NotAvailable1Code', NotAvailable1Code)
_module_typeBindings.NotAvailable1Code = NotAvailable1Code

# Atomic simple type: {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}PartySectorType1Code
class PartySectorType1Code (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """PartySectorType1CodeSpecifies the sector of a financial party."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PartySectorType1Code')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3184, 4)
    _Documentation = 'PartySectorType1CodeSpecifies the sector of a financial party.'
PartySectorType1Code._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=PartySectorType1Code, enum_prefix=None)
PartySectorType1Code.SRSN = PartySectorType1Code._CF_enumeration.addEnumeration(unicode_value='SRSN', tag='SRSN')
PartySectorType1Code.SRSB = PartySectorType1Code._CF_enumeration.addEnumeration(unicode_value='SRSB', tag='SRSB')
PartySectorType1Code.SRPB = PartySectorType1Code._CF_enumeration.addEnumeration(unicode_value='SRPB', tag='SRPB')
PartySectorType1Code.SRCB = PartySectorType1Code._CF_enumeration.addEnumeration(unicode_value='SRCB', tag='SRCB')
PartySectorType1Code.RGNL = PartySectorType1Code._CF_enumeration.addEnumeration(unicode_value='RGNL', tag='RGNL')
PartySectorType1Code.OFCP = PartySectorType1Code._CF_enumeration.addEnumeration(unicode_value='OFCP', tag='OFCP')
PartySectorType1Code.NRSN = PartySectorType1Code._CF_enumeration.addEnumeration(unicode_value='NRSN', tag='NRSN')
PartySectorType1Code.NRSB = PartySectorType1Code._CF_enumeration.addEnumeration(unicode_value='NRSB', tag='NRSB')
PartySectorType1Code.NRPB = PartySectorType1Code._CF_enumeration.addEnumeration(unicode_value='NRPB', tag='NRPB')
PartySectorType1Code.NRCB = PartySectorType1Code._CF_enumeration.addEnumeration(unicode_value='NRCB', tag='NRCB')
PartySectorType1Code.NFIN = PartySectorType1Code._CF_enumeration.addEnumeration(unicode_value='NFIN', tag='NFIN')
PartySectorType1Code.NTPB = PartySectorType1Code._CF_enumeration.addEnumeration(unicode_value='NTPB', tag='NTPB')
PartySectorType1Code.LOCA = PartySectorType1Code._CF_enumeration.addEnumeration(unicode_value='LOCA', tag='LOCA')
PartySectorType1Code.CDTI = PartySectorType1Code._CF_enumeration.addEnumeration(unicode_value='CDTI', tag='CDTI')
PartySectorType1Code._InitializeFacetMap(PartySectorType1Code._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'PartySectorType1Code', PartySectorType1Code)
_module_typeBindings.PartySectorType1Code = PartySectorType1Code

# Atomic simple type: {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}PercentageBoundedRate
class PercentageBoundedRate (pyxb.binding.datatypes.decimal):

    """PercentageBoundedRateRate expressed as a percentage, ie, in hundredths, eg, 0.7 is 7/10 of a percent, and 7.0 is 7%."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PercentageBoundedRate')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3277, 4)
    _Documentation = 'PercentageBoundedRateRate expressed as a percentage, ie, in hundredths, eg, 0.7 is 7/10 of a percent, and 7.0 is 7%.'
PercentageBoundedRate._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=PercentageBoundedRate, value=pyxb.binding.datatypes.decimal('0.0'))
PercentageBoundedRate._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=PercentageBoundedRate, value=pyxb.binding.datatypes.decimal('100.0'))
PercentageBoundedRate._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(11))
PercentageBoundedRate._CF_fractionDigits = pyxb.binding.facets.CF_fractionDigits(value=pyxb.binding.datatypes.nonNegativeInteger(10))
PercentageBoundedRate._InitializeFacetMap(PercentageBoundedRate._CF_minInclusive,
   PercentageBoundedRate._CF_maxInclusive,
   PercentageBoundedRate._CF_totalDigits,
   PercentageBoundedRate._CF_fractionDigits)
Namespace.addCategoryObject('typeBinding', 'PercentageBoundedRate', PercentageBoundedRate)
_module_typeBindings.PercentageBoundedRate = PercentageBoundedRate

# Atomic simple type: {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}PercentageRate
class PercentageRate (pyxb.binding.datatypes.decimal):

    """PercentageRateRate expressed as a percentage, that is, in hundredths, for example, 0.7 is 7/10 of a percent, and 7.0 is 7%."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PercentageRate')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3289, 4)
    _Documentation = 'PercentageRateRate expressed as a percentage, that is, in hundredths, for example, 0.7 is 7/10 of a percent, and 7.0 is 7%.'
PercentageRate._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(11))
PercentageRate._CF_fractionDigits = pyxb.binding.facets.CF_fractionDigits(value=pyxb.binding.datatypes.nonNegativeInteger(10))
PercentageRate._InitializeFacetMap(PercentageRate._CF_totalDigits,
   PercentageRate._CF_fractionDigits)
Namespace.addCategoryObject('typeBinding', 'PercentageRate', PercentageRate)
_module_typeBindings.PercentageRate = PercentageRate

# Atomic simple type: {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}RangeType1Code__1
class RangeType1Code__1 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """RangeType1Code__1Specifies the type of range."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RangeType1Code__1')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3633, 4)
    _Documentation = 'RangeType1Code__1Specifies the type of range.'
RangeType1Code__1._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=RangeType1Code__1, enum_prefix=None)
RangeType1Code__1.D2T7 = RangeType1Code__1._CF_enumeration.addEnumeration(unicode_value='D2T7', tag='D2T7')
RangeType1Code__1.D829 = RangeType1Code__1._CF_enumeration.addEnumeration(unicode_value='D829', tag='D829')
RangeType1Code__1.LS1D = RangeType1Code__1._CF_enumeration.addEnumeration(unicode_value='LS1D', tag='LS1D')
RangeType1Code__1.A30D = RangeType1Code__1._CF_enumeration.addEnumeration(unicode_value='A30D', tag='A30D')
RangeType1Code__1._InitializeFacetMap(RangeType1Code__1._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'RangeType1Code__1', RangeType1Code__1)
_module_typeBindings.RangeType1Code__1 = RangeType1Code__1

# Atomic simple type: {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}RangeType1Code__2
class RangeType1Code__2 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """RangeType1Code__2Specifies the type of range."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RangeType1Code__2')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3665, 4)
    _Documentation = 'RangeType1Code__2Specifies the type of range.'
RangeType1Code__2._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=RangeType1Code__2, enum_prefix=None)
RangeType1Code__2.LT3M = RangeType1Code__2._CF_enumeration.addEnumeration(unicode_value='LT3M', tag='LT3M')
RangeType1Code__2.LT1M = RangeType1Code__2._CF_enumeration.addEnumeration(unicode_value='LT1M', tag='LT1M')
RangeType1Code__2.LT1Y = RangeType1Code__2._CF_enumeration.addEnumeration(unicode_value='LT1Y', tag='LT1Y')
RangeType1Code__2.LT3Y = RangeType1Code__2._CF_enumeration.addEnumeration(unicode_value='LT3Y', tag='LT3Y')
RangeType1Code__2.LT5Y = RangeType1Code__2._CF_enumeration.addEnumeration(unicode_value='LT5Y', tag='LT5Y')
RangeType1Code__2.CYTD = RangeType1Code__2._CF_enumeration.addEnumeration(unicode_value='CYTD', tag='CYTD')
RangeType1Code__2._InitializeFacetMap(RangeType1Code__2._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'RangeType1Code__2', RangeType1Code__2)
_module_typeBindings.RangeType1Code__2 = RangeType1Code__2

# Atomic simple type: {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}RangeType1Code__3
class RangeType1Code__3 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """RangeType1Code__3Specifies the type of range."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RangeType1Code__3')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3709, 4)
    _Documentation = 'RangeType1Code__3Specifies the type of range.'
RangeType1Code__3._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=RangeType1Code__3, enum_prefix=None)
RangeType1Code__3.LT1Y = RangeType1Code__3._CF_enumeration.addEnumeration(unicode_value='LT1Y', tag='LT1Y')
RangeType1Code__3.LT2Y = RangeType1Code__3._CF_enumeration.addEnumeration(unicode_value='LT2Y', tag='LT2Y')
RangeType1Code__3.LT3Y = RangeType1Code__3._CF_enumeration.addEnumeration(unicode_value='LT3Y', tag='LT3Y')
RangeType1Code__3._InitializeFacetMap(RangeType1Code__3._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'RangeType1Code__3', RangeType1Code__3)
_module_typeBindings.RangeType1Code__3 = RangeType1Code__3

# Atomic simple type: {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}RangeType1Code__4
class RangeType1Code__4 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """RangeType1Code__4Specifies the type of range."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RangeType1Code__4')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3735, 4)
    _Documentation = 'RangeType1Code__4Specifies the type of range.'
RangeType1Code__4._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=RangeType1Code__4, enum_prefix=None)
RangeType1Code__4.YMS2 = RangeType1Code__4._CF_enumeration.addEnumeration(unicode_value='YMS2', tag='YMS2')
RangeType1Code__4.YMN3 = RangeType1Code__4._CF_enumeration.addEnumeration(unicode_value='YMN3', tag='YMN3')
RangeType1Code__4.YMS1 = RangeType1Code__4._CF_enumeration.addEnumeration(unicode_value='YMS1', tag='YMS1')
RangeType1Code__4._InitializeFacetMap(RangeType1Code__4._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'RangeType1Code__4', RangeType1Code__4)
_module_typeBindings.RangeType1Code__4 = RangeType1Code__4

# Atomic simple type: {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}ReportPeriodActivity3Code__1
class ReportPeriodActivity3Code__1 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """ReportPeriodActivity3Code__1Specifies the type of report activity for a specific reporting period."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ReportPeriodActivity3Code__1')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3855, 4)
    _Documentation = 'ReportPeriodActivity3Code__1Specifies the type of report activity for a specific reporting period.'
ReportPeriodActivity3Code__1._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ReportPeriodActivity3Code__1, enum_prefix=None)
ReportPeriodActivity3Code__1.NOTX = ReportPeriodActivity3Code__1._CF_enumeration.addEnumeration(unicode_value='NOTX', tag='NOTX')
ReportPeriodActivity3Code__1._InitializeFacetMap(ReportPeriodActivity3Code__1._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ReportPeriodActivity3Code__1', ReportPeriodActivity3Code__1)
_module_typeBindings.ReportPeriodActivity3Code__1 = ReportPeriodActivity3Code__1

# Atomic simple type: {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}ReportingPeriodType1Code
class ReportingPeriodType1Code (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """ReportingPeriodType1CodeSpecifies the period related to the reporting schema."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ReportingPeriodType1Code')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3869, 4)
    _Documentation = 'ReportingPeriodType1CodeSpecifies the period related to the reporting schema.'
ReportingPeriodType1Code._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ReportingPeriodType1Code, enum_prefix=None)
ReportingPeriodType1Code.QTR1 = ReportingPeriodType1Code._CF_enumeration.addEnumeration(unicode_value='QTR1', tag='QTR1')
ReportingPeriodType1Code.QTR4 = ReportingPeriodType1Code._CF_enumeration.addEnumeration(unicode_value='QTR4', tag='QTR4')
ReportingPeriodType1Code.QTR2 = ReportingPeriodType1Code._CF_enumeration.addEnumeration(unicode_value='QTR2', tag='QTR2')
ReportingPeriodType1Code.QTR3 = ReportingPeriodType1Code._CF_enumeration.addEnumeration(unicode_value='QTR3', tag='QTR3')
ReportingPeriodType1Code._InitializeFacetMap(ReportingPeriodType1Code._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ReportingPeriodType1Code', ReportingPeriodType1Code)
_module_typeBindings.ReportingPeriodType1Code = ReportingPeriodType1Code

# Atomic simple type: {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}ReportingPeriodType2Code__1
class ReportingPeriodType2Code__1 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """ReportingPeriodType2Code__1Specifies the month for which value is reported."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ReportingPeriodType2Code__1')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3901, 4)
    _Documentation = 'ReportingPeriodType2Code__1Specifies the month for which value is reported.'
ReportingPeriodType2Code__1._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ReportingPeriodType2Code__1, enum_prefix=None)
ReportingPeriodType2Code__1.MM01 = ReportingPeriodType2Code__1._CF_enumeration.addEnumeration(unicode_value='MM01', tag='MM01')
ReportingPeriodType2Code__1.MM02 = ReportingPeriodType2Code__1._CF_enumeration.addEnumeration(unicode_value='MM02', tag='MM02')
ReportingPeriodType2Code__1.MM03 = ReportingPeriodType2Code__1._CF_enumeration.addEnumeration(unicode_value='MM03', tag='MM03')
ReportingPeriodType2Code__1._InitializeFacetMap(ReportingPeriodType2Code__1._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ReportingPeriodType2Code__1', ReportingPeriodType2Code__1)
_module_typeBindings.ReportingPeriodType2Code__1 = ReportingPeriodType2Code__1

# Atomic simple type: {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}ReportingPeriodType2Code__2
class ReportingPeriodType2Code__2 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """ReportingPeriodType2Code__2Specifies the month for which value is reported."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ReportingPeriodType2Code__2')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3927, 4)
    _Documentation = 'ReportingPeriodType2Code__2Specifies the month for which value is reported.'
ReportingPeriodType2Code__2._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ReportingPeriodType2Code__2, enum_prefix=None)
ReportingPeriodType2Code__2.MM05 = ReportingPeriodType2Code__2._CF_enumeration.addEnumeration(unicode_value='MM05', tag='MM05')
ReportingPeriodType2Code__2.MM04 = ReportingPeriodType2Code__2._CF_enumeration.addEnumeration(unicode_value='MM04', tag='MM04')
ReportingPeriodType2Code__2.MM06 = ReportingPeriodType2Code__2._CF_enumeration.addEnumeration(unicode_value='MM06', tag='MM06')
ReportingPeriodType2Code__2._InitializeFacetMap(ReportingPeriodType2Code__2._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ReportingPeriodType2Code__2', ReportingPeriodType2Code__2)
_module_typeBindings.ReportingPeriodType2Code__2 = ReportingPeriodType2Code__2

# Atomic simple type: {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}ReportingPeriodType2Code__3
class ReportingPeriodType2Code__3 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """ReportingPeriodType2Code__3Specifies the month for which value is reported."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ReportingPeriodType2Code__3')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3953, 4)
    _Documentation = 'ReportingPeriodType2Code__3Specifies the month for which value is reported.'
ReportingPeriodType2Code__3._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ReportingPeriodType2Code__3, enum_prefix=None)
ReportingPeriodType2Code__3.MM08 = ReportingPeriodType2Code__3._CF_enumeration.addEnumeration(unicode_value='MM08', tag='MM08')
ReportingPeriodType2Code__3.MM09 = ReportingPeriodType2Code__3._CF_enumeration.addEnumeration(unicode_value='MM09', tag='MM09')
ReportingPeriodType2Code__3.MM07 = ReportingPeriodType2Code__3._CF_enumeration.addEnumeration(unicode_value='MM07', tag='MM07')
ReportingPeriodType2Code__3._InitializeFacetMap(ReportingPeriodType2Code__3._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ReportingPeriodType2Code__3', ReportingPeriodType2Code__3)
_module_typeBindings.ReportingPeriodType2Code__3 = ReportingPeriodType2Code__3

# Atomic simple type: {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}ReportingPeriodType2Code__4
class ReportingPeriodType2Code__4 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """ReportingPeriodType2Code__4Specifies the month for which value is reported."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ReportingPeriodType2Code__4')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3979, 4)
    _Documentation = 'ReportingPeriodType2Code__4Specifies the month for which value is reported.'
ReportingPeriodType2Code__4._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ReportingPeriodType2Code__4, enum_prefix=None)
ReportingPeriodType2Code__4.MM11 = ReportingPeriodType2Code__4._CF_enumeration.addEnumeration(unicode_value='MM11', tag='MM11')
ReportingPeriodType2Code__4.MM10 = ReportingPeriodType2Code__4._CF_enumeration.addEnumeration(unicode_value='MM10', tag='MM10')
ReportingPeriodType2Code__4.MM12 = ReportingPeriodType2Code__4._CF_enumeration.addEnumeration(unicode_value='MM12', tag='MM12')
ReportingPeriodType2Code__4._InitializeFacetMap(ReportingPeriodType2Code__4._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ReportingPeriodType2Code__4', ReportingPeriodType2Code__4)
_module_typeBindings.ReportingPeriodType2Code__4 = ReportingPeriodType2Code__4

# Atomic simple type: {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}TrueFalseIndicator
class TrueFalseIndicator (pyxb.binding.datatypes.boolean):

    """TrueFalseIndicatorA flag indicating a True or False value."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TrueFalseIndicator')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 4179, 4)
    _Documentation = 'TrueFalseIndicatorA flag indicating a True or False value.'
TrueFalseIndicator._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'TrueFalseIndicator', TrueFalseIndicator)
_module_typeBindings.TrueFalseIndicator = TrueFalseIndicator

# Atomic simple type: {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}TrueFalseIndicator_fixed
class TrueFalseIndicator_fixed (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """TrueFalseIndicator_fixed"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TrueFalseIndicator_fixed')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 4186, 4)
    _Documentation = 'TrueFalseIndicator_fixed'
TrueFalseIndicator_fixed._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=TrueFalseIndicator_fixed, enum_prefix=None)
TrueFalseIndicator_fixed.true = TrueFalseIndicator_fixed._CF_enumeration.addEnumeration(unicode_value='true', tag='true')
TrueFalseIndicator_fixed._InitializeFacetMap(TrueFalseIndicator_fixed._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'TrueFalseIndicator_fixed', TrueFalseIndicator_fixed)
_module_typeBindings.TrueFalseIndicator_fixed = TrueFalseIndicator_fixed

# Atomic simple type: {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}TrueFalseIndicator_fixed__1
class TrueFalseIndicator_fixed__1 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """TrueFalseIndicator_fixed__1"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TrueFalseIndicator_fixed__1')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 4198, 4)
    _Documentation = 'TrueFalseIndicator_fixed__1'
TrueFalseIndicator_fixed__1._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=TrueFalseIndicator_fixed__1, enum_prefix=None)
TrueFalseIndicator_fixed__1.True_ = TrueFalseIndicator_fixed__1._CF_enumeration.addEnumeration(unicode_value='True', tag='True_')
TrueFalseIndicator_fixed__1._InitializeFacetMap(TrueFalseIndicator_fixed__1._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'TrueFalseIndicator_fixed__1', TrueFalseIndicator_fixed__1)
_module_typeBindings.TrueFalseIndicator_fixed__1 = TrueFalseIndicator_fixed__1

# Atomic simple type: {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}UnderlyingDerivativeType2Code
class UnderlyingDerivativeType2Code (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """UnderlyingDerivativeType2CodeCategorisation of financial asset type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'UnderlyingDerivativeType2Code')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 4210, 4)
    _Documentation = 'UnderlyingDerivativeType2CodeCategorisation of financial asset type.'
UnderlyingDerivativeType2Code._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=UnderlyingDerivativeType2Code, enum_prefix=None)
UnderlyingDerivativeType2Code.CURR = UnderlyingDerivativeType2Code._CF_enumeration.addEnumeration(unicode_value='CURR', tag='CURR')
UnderlyingDerivativeType2Code.CIDX = UnderlyingDerivativeType2Code._CF_enumeration.addEnumeration(unicode_value='CIDX', tag='CIDX')
UnderlyingDerivativeType2Code.IIDX = UnderlyingDerivativeType2Code._CF_enumeration.addEnumeration(unicode_value='IIDX', tag='IIDX')
UnderlyingDerivativeType2Code.INTR = UnderlyingDerivativeType2Code._CF_enumeration.addEnumeration(unicode_value='INTR', tag='INTR')
UnderlyingDerivativeType2Code.INCU = UnderlyingDerivativeType2Code._CF_enumeration.addEnumeration(unicode_value='INCU', tag='INCU')
UnderlyingDerivativeType2Code._InitializeFacetMap(UnderlyingDerivativeType2Code._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'UnderlyingDerivativeType2Code', UnderlyingDerivativeType2Code)
_module_typeBindings.UnderlyingDerivativeType2Code = UnderlyingDerivativeType2Code

# Atomic simple type: {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}ValuationType2Code
class ValuationType2Code (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """ValuationType2CodeSpecifies the type used for the calculation of the valuation."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ValuationType2Code')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 4250, 4)
    _Documentation = 'ValuationType2CodeSpecifies the type used for the calculation of the valuation.'
ValuationType2Code._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ValuationType2Code, enum_prefix=None)
ValuationType2Code.MTMO = ValuationType2Code._CF_enumeration.addEnumeration(unicode_value='MTMO', tag='MTMO')
ValuationType2Code.MTMA = ValuationType2Code._CF_enumeration.addEnumeration(unicode_value='MTMA', tag='MTMA')
ValuationType2Code.AMCS = ValuationType2Code._CF_enumeration.addEnumeration(unicode_value='AMCS', tag='AMCS')
ValuationType2Code._InitializeFacetMap(ValuationType2Code._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ValuationType2Code', ValuationType2Code)
_module_typeBindings.ValuationType2Code = ValuationType2Code

# Complex type {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}ActionPlan1Choice__1 with content type ELEMENT_ONLY
class ActionPlan1Choice__1 (pyxb.binding.basis.complexTypeDefinition):
    """ActionPlan1Choice__1Choice between no action plan (because no vulnerability was revealed) or the description of the action plan proposed by the manager of the fund.
"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ActionPlan1Choice__1')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 42, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}NoVlnrblty uses Python identifier NoVlnrblty
    __NoVlnrblty = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NoVlnrblty'), 'NoVlnrblty', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_ActionPlan1Choice__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01NoVlnrblty', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 49, 12), )

    
    NoVlnrblty = property(__NoVlnrblty.value, __NoVlnrblty.set, None, 'NoVulnerabilityIndicates that no vulnerability was revealed by the stress tests.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}PropsdActnPlan uses Python identifier PropsdActnPlan
    __PropsdActnPlan = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PropsdActnPlan'), 'PropsdActnPlan', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_ActionPlan1Choice__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01PropsdActnPlan', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 55, 12), )

    
    PropsdActnPlan = property(__PropsdActnPlan.value, __PropsdActnPlan.set, None, 'ProposedActionPlanSpecifies the action plan as proposed by the board of directors.')

    _ElementMap.update({
        __NoVlnrblty.name() : __NoVlnrblty,
        __PropsdActnPlan.name() : __PropsdActnPlan
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ActionPlan1Choice__1 = ActionPlan1Choice__1
Namespace.addCategoryObject('typeBinding', 'ActionPlan1Choice__1', ActionPlan1Choice__1)


# Complex type {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}AmortisedCostMethodPriceDeviationEvent1__1 with content type ELEMENT_ONLY
class AmortisedCostMethodPriceDeviationEvent1__1 (pyxb.binding.basis.complexTypeDefinition):
    """AmortisedCostMethodPriceDeviationEvent1__1Details of the events where the price of an asset valued by using the amortised cost method deviates from the price of that asset by more than 10 basis points."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AmortisedCostMethodPriceDeviationEvent1__1')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 119, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}ValtnDt uses Python identifier ValtnDt
    __ValtnDt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ValtnDt'), 'ValtnDt', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_AmortisedCostMethodPriceDeviationEvent1__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01ValtnDt', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 125, 12), )

    
    ValtnDt = property(__ValtnDt.value, __ValtnDt.set, None, 'ValuationDateValuation date from which the price of an asset calculated in accordance with the mark-to-market or mark-to-model method deviates from the asset price calculated in accordance with the amortised cost method by more than 10 basis points.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}AsstId uses Python identifier AsstId
    __AsstId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AsstId'), 'AsstId', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_AmortisedCostMethodPriceDeviationEvent1__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01AsstId', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 131, 12), )

    
    AsstId = property(__AsstId.value, __AsstId.set, None, 'AssetIdentificationIdentification of the instrument\r\n')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}RptgCcyMktPric uses Python identifier RptgCcyMktPric
    __RptgCcyMktPric = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RptgCcyMktPric'), 'RptgCcyMktPric', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_AmortisedCostMethodPriceDeviationEvent1__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01RptgCcyMktPric', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 138, 12), )

    
    RptgCcyMktPric = property(__RptgCcyMktPric.value, __RptgCcyMktPric.set, None, 'ReportingCurrencyMarketPriceSpecifies the market price expressed in the reporting currency of the asset valued by using the mark-to-market or mark-to-model method.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}RptgCcyAmtsdCostPric uses Python identifier RptgCcyAmtsdCostPric
    __RptgCcyAmtsdCostPric = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RptgCcyAmtsdCostPric'), 'RptgCcyAmtsdCostPric', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_AmortisedCostMethodPriceDeviationEvent1__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01RptgCcyAmtsdCostPric', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 144, 12), )

    
    RptgCcyAmtsdCostPric = property(__RptgCcyAmtsdCostPric.value, __RptgCcyAmtsdCostPric.set, None, 'ReportingCurrencyAmortisedCostPriceSpecifies the price expressed in the reporting currency of the asset valued by using the amortised cost method.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}NbOfDaysDvtn uses Python identifier NbOfDaysDvtn
    __NbOfDaysDvtn = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NbOfDaysDvtn'), 'NbOfDaysDvtn', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_AmortisedCostMethodPriceDeviationEvent1__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01NbOfDaysDvtn', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 150, 12), )

    
    NbOfDaysDvtn = property(__NbOfDaysDvtn.value, __NbOfDaysDvtn.set, None, 'NumberOfDaysDeviationSpecifies the number of days the price of an asset calculated in accordance with the mark-to-market or mark-to-model method deviates from the asset price calculated in accordance with the amortised cost method by more than 10 basis points.\r\n')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}AvrgBsisPtSprd uses Python identifier AvrgBsisPtSprd
    __AvrgBsisPtSprd = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AvrgBsisPtSprd'), 'AvrgBsisPtSprd', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_AmortisedCostMethodPriceDeviationEvent1__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01AvrgBsisPtSprd', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 157, 12), )

    
    AvrgBsisPtSprd = property(__AvrgBsisPtSprd.value, __AvrgBsisPtSprd.set, None, 'AverageBasisPointSpreadProvides the average number of basis points added to (if positive) or deducted from (if negative) the price of an asset calculated in accordance with the mark-to-market or mark-to-model method to calculate the asset price calculated in accordance with the amortised cost method when the two asset prices deviates by more than 10 basis points.\r\nUsed to express differences in interest rates, for example, a difference of 0.10 % is equivalent to a change of 10 basis points.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}LwstPricDvtn uses Python identifier LwstPricDvtn
    __LwstPricDvtn = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'LwstPricDvtn'), 'LwstPricDvtn', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_AmortisedCostMethodPriceDeviationEvent1__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01LwstPricDvtn', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 164, 12), )

    
    LwstPricDvtn = property(__LwstPricDvtn.value, __LwstPricDvtn.set, None, 'LowestPriceDeviationMinimum price deviation between the price of an asset calculated in accordance with the mark-to-market or mark-to-model method and the asset price calculated in accordance with the amortised cost method.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}HghstPricDvtn uses Python identifier HghstPricDvtn
    __HghstPricDvtn = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'HghstPricDvtn'), 'HghstPricDvtn', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_AmortisedCostMethodPriceDeviationEvent1__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01HghstPricDvtn', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 170, 12), )

    
    HghstPricDvtn = property(__HghstPricDvtn.value, __HghstPricDvtn.set, None, 'HighestPriceDeviationMaximum price deviation between the price of an asset calculated in accordance with the mark-to-market or mark-to-model method and the asset price calculated in accordance with the amortised cost method.')

    _ElementMap.update({
        __ValtnDt.name() : __ValtnDt,
        __AsstId.name() : __AsstId,
        __RptgCcyMktPric.name() : __RptgCcyMktPric,
        __RptgCcyAmtsdCostPric.name() : __RptgCcyAmtsdCostPric,
        __NbOfDaysDvtn.name() : __NbOfDaysDvtn,
        __AvrgBsisPtSprd.name() : __AvrgBsisPtSprd,
        __LwstPricDvtn.name() : __LwstPricDvtn,
        __HghstPricDvtn.name() : __HghstPricDvtn
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.AmortisedCostMethodPriceDeviationEvent1__1 = AmortisedCostMethodPriceDeviationEvent1__1
Namespace.addCategoryObject('typeBinding', 'AmortisedCostMethodPriceDeviationEvent1__1', AmortisedCostMethodPriceDeviationEvent1__1)


# Complex type {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}AssetIdentification3__1 with content type ELEMENT_ONLY
class AssetIdentification3__1 (pyxb.binding.basis.complexTypeDefinition):
    """AssetIdentification3__1Identification of the asset held by the fund."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AssetIdentification3__1')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 295, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}ClssfctnTp uses Python identifier ClssfctnTp
    __ClssfctnTp = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ClssfctnTp'), 'ClssfctnTp', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_AssetIdentification3__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01ClssfctnTp', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 301, 12), )

    
    ClssfctnTp = property(__ClssfctnTp.value, __ClssfctnTp.set, None, 'ClassificationTypeClassification type of the financial instrument, as per the ISO classification of financial instrument (CFI) codification, that is common share with voting rights, fully paid, or registered.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}InstrmId uses Python identifier InstrmId
    __InstrmId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'InstrmId'), 'InstrmId', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_AssetIdentification3__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01InstrmId', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 307, 12), )

    
    InstrmId = property(__InstrmId.value, __InstrmId.set, None, 'InstrumentIdentificationIdentification of the instrument held by the money market fund.')

    _ElementMap.update({
        __ClssfctnTp.name() : __ClssfctnTp,
        __InstrmId.name() : __InstrmId
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.AssetIdentification3__1 = AssetIdentification3__1
Namespace.addCategoryObject('typeBinding', 'AssetIdentification3__1', AssetIdentification3__1)


# Complex type {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}AssetIdentification3__2 with content type ELEMENT_ONLY
class AssetIdentification3__2 (pyxb.binding.basis.complexTypeDefinition):
    """AssetIdentification3__2Identification of the asset held by the fund."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AssetIdentification3__2')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 315, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}ClssfctnTp uses Python identifier ClssfctnTp
    __ClssfctnTp = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ClssfctnTp'), 'ClssfctnTp', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_AssetIdentification3__2_urnisostdiso20022techxsdDRAFT3auth_093_001_01ClssfctnTp', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 321, 12), )

    
    ClssfctnTp = property(__ClssfctnTp.value, __ClssfctnTp.set, None, 'ClassificationTypeClassification type of the financial instrument, as per the ISO classification of financial instrument (CFI) codification, that is common share with voting rights, fully paid, or registered.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}InstrmId uses Python identifier InstrmId
    __InstrmId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'InstrmId'), 'InstrmId', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_AssetIdentification3__2_urnisostdiso20022techxsdDRAFT3auth_093_001_01InstrmId', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 327, 12), )

    
    InstrmId = property(__InstrmId.value, __InstrmId.set, None, 'InstrumentIdentificationIdentification of the instrument held by the money market fund.')

    _ElementMap.update({
        __ClssfctnTp.name() : __ClssfctnTp,
        __InstrmId.name() : __InstrmId
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.AssetIdentification3__2 = AssetIdentification3__2
Namespace.addCategoryObject('typeBinding', 'AssetIdentification3__2', AssetIdentification3__2)


# Complex type {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}AssetIdentification3__3 with content type ELEMENT_ONLY
class AssetIdentification3__3 (pyxb.binding.basis.complexTypeDefinition):
    """AssetIdentification3__3Identification of the asset held by the fund."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AssetIdentification3__3')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 335, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}ClssfctnTp uses Python identifier ClssfctnTp
    __ClssfctnTp = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ClssfctnTp'), 'ClssfctnTp', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_AssetIdentification3__3_urnisostdiso20022techxsdDRAFT3auth_093_001_01ClssfctnTp', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 341, 12), )

    
    ClssfctnTp = property(__ClssfctnTp.value, __ClssfctnTp.set, None, 'ClassificationTypeClassification type of the financial instrument, as per the ISO classification of financial instrument (CFI) codification, that is common share with voting rights, fully paid, or registered.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}InstrmId uses Python identifier InstrmId
    __InstrmId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'InstrmId'), 'InstrmId', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_AssetIdentification3__3_urnisostdiso20022techxsdDRAFT3auth_093_001_01InstrmId', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 347, 12), )

    
    InstrmId = property(__InstrmId.value, __InstrmId.set, None, 'InstrumentIdentificationIdentification of the instrument held by the money market fund.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}AsstLEI uses Python identifier AsstLEI
    __AsstLEI = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AsstLEI'), 'AsstLEI', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_AssetIdentification3__3_urnisostdiso20022techxsdDRAFT3auth_093_001_01AsstLEI', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 353, 12), )

    
    AsstLEI = property(__AsstLEI.value, __AsstLEI.set, None, 'AssetLEILegal entity identification of the fund as an alternate identification for a party.')

    _ElementMap.update({
        __ClssfctnTp.name() : __ClssfctnTp,
        __InstrmId.name() : __InstrmId,
        __AsstLEI.name() : __AsstLEI
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.AssetIdentification3__3 = AssetIdentification3__3
Namespace.addCategoryObject('typeBinding', 'AssetIdentification3__3', AssetIdentification3__3)


# Complex type {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}AssetIdentification3__4 with content type ELEMENT_ONLY
class AssetIdentification3__4 (pyxb.binding.basis.complexTypeDefinition):
    """AssetIdentification3__4Identification of the asset held by the fund."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AssetIdentification3__4')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 361, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}InstrmId uses Python identifier InstrmId
    __InstrmId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'InstrmId'), 'InstrmId', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_AssetIdentification3__4_urnisostdiso20022techxsdDRAFT3auth_093_001_01InstrmId', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 367, 12), )

    
    InstrmId = property(__InstrmId.value, __InstrmId.set, None, 'InstrumentIdentificationIdentification of the instrument held by the money market fund.')

    _ElementMap.update({
        __InstrmId.name() : __InstrmId
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.AssetIdentification3__4 = AssetIdentification3__4
Namespace.addCategoryObject('typeBinding', 'AssetIdentification3__4', AssetIdentification3__4)


# Complex type {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}AssetValuation2__1 with content type ELEMENT_ONLY
class AssetValuation2__1 (pyxb.binding.basis.complexTypeDefinition):
    """AssetValuation2__1Provides details about the valuation of the assets held by the fund."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AssetValuation2__1')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 375, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}MtrtyDt uses Python identifier MtrtyDt
    __MtrtyDt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'MtrtyDt'), 'MtrtyDt', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_AssetValuation2__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01MtrtyDt', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 381, 12), )

    
    MtrtyDt = property(__MtrtyDt.value, __MtrtyDt.set, None, 'MaturityDatePlanned final repayment date at the time of issuance.\r\nThe maturity date has to be reported for the money market instruments, the securitisations, asset backed commercial papers and financial derivatives.\r\n')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}NtnlCcyFrstLeg uses Python identifier NtnlCcyFrstLeg
    __NtnlCcyFrstLeg = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NtnlCcyFrstLeg'), 'NtnlCcyFrstLeg', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_AssetValuation2__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01NtnlCcyFrstLeg', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 389, 12), )

    
    NtnlCcyFrstLeg = property(__NtnlCcyFrstLeg.value, __NtnlCcyFrstLeg.set, None, 'NotionalCurrencyFirstLegCurrency of the financial instrument.\r\nThe currency first leg has to be reported for the money market instruments, the securitisations, asset backed commercial papers, deposits or ancillary services, repurchase agreements, reverse repurchase agreements, financial derivatives and shares or units of other funds.\r\nUsage: In the case of an interest rate or currency derivative contract, this will be the notional currency of first leg.\r\n')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}Qty uses Python identifier Qty
    __Qty = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Qty'), 'Qty', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_AssetValuation2__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01Qty', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 398, 12), )

    
    Qty = property(__Qty.value, __Qty.set, None, 'QuantityQuantity of the financial instrument held by the fund.\r\nThe quantity has to be reported for the money market instruments, the securitisations, asset backed commercial papers and shares or units of other funds.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}Pric uses Python identifier Pric
    __Pric = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Pric'), 'Pric', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_AssetValuation2__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01Pric', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 405, 12), )

    
    Pric = property(__Pric.value, __Pric.set, None, 'PricePrice of the asset expressed as a clean price for the money market instruments, the securitisations or asset backed commercial papers. and as a net asset value per unit or share for other money market funds.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}AcrdIntrst uses Python identifier AcrdIntrst
    __AcrdIntrst = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AcrdIntrst'), 'AcrdIntrst', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_AssetValuation2__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01AcrdIntrst', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 411, 12), )

    
    AcrdIntrst = property(__AcrdIntrst.value, __AcrdIntrst.set, None, 'AccruedInterestInterest amount that has accrued in between coupon payment periods.\r\n')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}TtlVal uses Python identifier TtlVal
    __TtlVal = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TtlVal'), 'TtlVal', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_AssetValuation2__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01TtlVal', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 418, 12), )

    
    TtlVal = property(__TtlVal.value, __TtlVal.set, None, 'TotalValueThe end-of period total market value in base currency of the financial instrument in which the money market fund has invested.\r\nthe total value has to be reported for the money market instruments, the securitisations, asset backed commercial papers, the financial derivatives, the shares or units of other funds, the repurchase agreements and reverse repurchase agreements.\r\n')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}ValtnTp uses Python identifier ValtnTp
    __ValtnTp = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ValtnTp'), 'ValtnTp', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_AssetValuation2__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01ValtnTp', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 426, 12), )

    
    ValtnTp = property(__ValtnTp.value, __ValtnTp.set, None, 'ValuationTypeIndicate whether valuation was performed mark to market, mark to model or in accordance with the cost amortised method.\r\nThe valuation type has to be reported for the money market instruments, securitisations and asset backed commercial papers.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}CdtAssmntRslt uses Python identifier CdtAssmntRslt
    __CdtAssmntRslt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CdtAssmntRslt'), 'CdtAssmntRslt', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_AssetValuation2__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01CdtAssmntRslt', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 433, 12), )

    
    CdtAssmntRslt = property(__CdtAssmntRslt.value, __CdtAssmntRslt.set, None, 'CreditAssessmentResultSpecifies whether the credit assessment is favourable or unfavourable.\r\nThe credit assessment result has to be provided for the money market instruments, the securitisations and asset backed commercial papers and the repurchase agreements.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}RstDt uses Python identifier RstDt
    __RstDt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RstDt'), 'RstDt', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_AssetValuation2__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01RstDt', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 440, 12), )

    
    RstDt = property(__RstDt.value, __RstDt.set, None, 'ResetDateDate at which the interest rate of an interest bearing instrument will be reset, according to the terms of the issue.\r\nThe reset date has to be reported for money market instruments and financial derivatives.\r\n')

    _ElementMap.update({
        __MtrtyDt.name() : __MtrtyDt,
        __NtnlCcyFrstLeg.name() : __NtnlCcyFrstLeg,
        __Qty.name() : __Qty,
        __Pric.name() : __Pric,
        __AcrdIntrst.name() : __AcrdIntrst,
        __TtlVal.name() : __TtlVal,
        __ValtnTp.name() : __ValtnTp,
        __CdtAssmntRslt.name() : __CdtAssmntRslt,
        __RstDt.name() : __RstDt
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.AssetValuation2__1 = AssetValuation2__1
Namespace.addCategoryObject('typeBinding', 'AssetValuation2__1', AssetValuation2__1)


# Complex type {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}AssetValuation2__2 with content type ELEMENT_ONLY
class AssetValuation2__2 (pyxb.binding.basis.complexTypeDefinition):
    """AssetValuation2__2Provides details about the valuation of the assets held by the fund."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AssetValuation2__2')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 450, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}MtrtyDt uses Python identifier MtrtyDt
    __MtrtyDt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'MtrtyDt'), 'MtrtyDt', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_AssetValuation2__2_urnisostdiso20022techxsdDRAFT3auth_093_001_01MtrtyDt', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 456, 12), )

    
    MtrtyDt = property(__MtrtyDt.value, __MtrtyDt.set, None, 'MaturityDatePlanned final repayment date at the time of issuance.\r\nThe maturity date has to be reported for the money market instruments, the securitisations, asset backed commercial papers and financial derivatives.\r\n')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}NtnlCcyFrstLeg uses Python identifier NtnlCcyFrstLeg
    __NtnlCcyFrstLeg = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NtnlCcyFrstLeg'), 'NtnlCcyFrstLeg', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_AssetValuation2__2_urnisostdiso20022techxsdDRAFT3auth_093_001_01NtnlCcyFrstLeg', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 464, 12), )

    
    NtnlCcyFrstLeg = property(__NtnlCcyFrstLeg.value, __NtnlCcyFrstLeg.set, None, 'NotionalCurrencyFirstLegCurrency of the financial instrument.\r\nThe currency first leg has to be reported for the money market instruments, the securitisations, asset backed commercial papers, deposits or ancillary services, repurchase agreements, reverse repurchase agreements, financial derivatives and shares or units of other funds.\r\nUsage: In the case of an interest rate or currency derivative contract, this will be the notional currency of first leg.\r\n')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}Qty uses Python identifier Qty
    __Qty = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Qty'), 'Qty', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_AssetValuation2__2_urnisostdiso20022techxsdDRAFT3auth_093_001_01Qty', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 473, 12), )

    
    Qty = property(__Qty.value, __Qty.set, None, 'QuantityQuantity of the financial instrument held by the fund.\r\nThe quantity has to be reported for the money market instruments, the securitisations, asset backed commercial papers and shares or units of other funds.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}Pric uses Python identifier Pric
    __Pric = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Pric'), 'Pric', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_AssetValuation2__2_urnisostdiso20022techxsdDRAFT3auth_093_001_01Pric', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 480, 12), )

    
    Pric = property(__Pric.value, __Pric.set, None, 'PricePrice of the asset expressed as a clean price for the money market instruments, the securitisations or asset backed commercial papers. and as a net asset value per unit or share for other money market funds.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}AcrdIntrst uses Python identifier AcrdIntrst
    __AcrdIntrst = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AcrdIntrst'), 'AcrdIntrst', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_AssetValuation2__2_urnisostdiso20022techxsdDRAFT3auth_093_001_01AcrdIntrst', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 486, 12), )

    
    AcrdIntrst = property(__AcrdIntrst.value, __AcrdIntrst.set, None, 'AccruedInterestInterest amount that has accrued in between coupon payment periods.\r\n')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}TtlVal uses Python identifier TtlVal
    __TtlVal = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TtlVal'), 'TtlVal', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_AssetValuation2__2_urnisostdiso20022techxsdDRAFT3auth_093_001_01TtlVal', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 493, 12), )

    
    TtlVal = property(__TtlVal.value, __TtlVal.set, None, 'TotalValueThe end-of period total market value in base currency of the financial instrument in which the money market fund has invested.\r\nthe total value has to be reported for the money market instruments, the securitisations, asset backed commercial papers, the financial derivatives, the shares or units of other funds, the repurchase agreements and reverse repurchase agreements.\r\n')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}ValtnTp uses Python identifier ValtnTp
    __ValtnTp = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ValtnTp'), 'ValtnTp', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_AssetValuation2__2_urnisostdiso20022techxsdDRAFT3auth_093_001_01ValtnTp', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 501, 12), )

    
    ValtnTp = property(__ValtnTp.value, __ValtnTp.set, None, 'ValuationTypeIndicate whether valuation was performed mark to market, mark to model or in accordance with the cost amortised method.\r\nThe valuation type has to be reported for the money market instruments, securitisations and asset backed commercial papers.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}CdtAssmntRslt uses Python identifier CdtAssmntRslt
    __CdtAssmntRslt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CdtAssmntRslt'), 'CdtAssmntRslt', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_AssetValuation2__2_urnisostdiso20022techxsdDRAFT3auth_093_001_01CdtAssmntRslt', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 508, 12), )

    
    CdtAssmntRslt = property(__CdtAssmntRslt.value, __CdtAssmntRslt.set, None, 'CreditAssessmentResultSpecifies whether the credit assessment is favourable or unfavourable.\r\nThe credit assessment result has to be provided for the money market instruments, the securitisations and asset backed commercial papers and the repurchase agreements.')

    _ElementMap.update({
        __MtrtyDt.name() : __MtrtyDt,
        __NtnlCcyFrstLeg.name() : __NtnlCcyFrstLeg,
        __Qty.name() : __Qty,
        __Pric.name() : __Pric,
        __AcrdIntrst.name() : __AcrdIntrst,
        __TtlVal.name() : __TtlVal,
        __ValtnTp.name() : __ValtnTp,
        __CdtAssmntRslt.name() : __CdtAssmntRslt
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.AssetValuation2__2 = AssetValuation2__2
Namespace.addCategoryObject('typeBinding', 'AssetValuation2__2', AssetValuation2__2)


# Complex type {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}AssetValuation2__3 with content type ELEMENT_ONLY
class AssetValuation2__3 (pyxb.binding.basis.complexTypeDefinition):
    """AssetValuation2__3Provides details about the valuation of the assets held by the fund."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AssetValuation2__3')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 517, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}MtrtyDt uses Python identifier MtrtyDt
    __MtrtyDt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'MtrtyDt'), 'MtrtyDt', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_AssetValuation2__3_urnisostdiso20022techxsdDRAFT3auth_093_001_01MtrtyDt', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 523, 12), )

    
    MtrtyDt = property(__MtrtyDt.value, __MtrtyDt.set, None, 'MaturityDatePlanned final repayment date at the time of issuance.\r\nThe maturity date has to be reported for the money market instruments, the securitisations, asset backed commercial papers and financial derivatives.\r\n')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}NtnlCcyFrstLeg uses Python identifier NtnlCcyFrstLeg
    __NtnlCcyFrstLeg = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NtnlCcyFrstLeg'), 'NtnlCcyFrstLeg', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_AssetValuation2__3_urnisostdiso20022techxsdDRAFT3auth_093_001_01NtnlCcyFrstLeg', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 531, 12), )

    
    NtnlCcyFrstLeg = property(__NtnlCcyFrstLeg.value, __NtnlCcyFrstLeg.set, None, 'NotionalCurrencyFirstLegCurrency of the financial instrument.\r\nThe currency first leg has to be reported for the money market instruments, the securitisations, asset backed commercial papers, deposits or ancillary services, repurchase agreements, reverse repurchase agreements, financial derivatives and shares or units of other funds.\r\nUsage: In the case of an interest rate or currency derivative contract, this will be the notional currency of first leg.\r\n')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}NtnlCcyScndLeg uses Python identifier NtnlCcyScndLeg
    __NtnlCcyScndLeg = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NtnlCcyScndLeg'), 'NtnlCcyScndLeg', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_AssetValuation2__3_urnisostdiso20022techxsdDRAFT3auth_093_001_01NtnlCcyScndLeg', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 540, 12), )

    
    NtnlCcyScndLeg = property(__NtnlCcyScndLeg.value, __NtnlCcyScndLeg.set, None, 'NotionalCurrencySecondLegOther currency of the notional amount. \r\nThe currency second leg has to be reported for the financial derivatives with two currencies.\r\nUsage: In the case of an interest rate or currency derivative contract, this will be the notional currency of the second leg.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}TtlVal uses Python identifier TtlVal
    __TtlVal = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TtlVal'), 'TtlVal', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_AssetValuation2__3_urnisostdiso20022techxsdDRAFT3auth_093_001_01TtlVal', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 548, 12), )

    
    TtlVal = property(__TtlVal.value, __TtlVal.set, None, 'TotalValueThe end-of period total market value in base currency of the financial instrument in which the money market fund has invested.\r\nthe total value has to be reported for the money market instruments, the securitisations, asset backed commercial papers, the financial derivatives, the shares or units of other funds, the repurchase agreements and reverse repurchase agreements.\r\n')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}XpsrVal uses Python identifier XpsrVal
    __XpsrVal = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'XpsrVal'), 'XpsrVal', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_AssetValuation2__3_urnisostdiso20022techxsdDRAFT3auth_093_001_01XpsrVal', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 556, 12), )

    
    XpsrVal = property(__XpsrVal.value, __XpsrVal.set, None, 'ExposureValueExposure of the financial derivative instrument, the repurchase agreement, reverse repurchase agreement and the deposit or ancillary liquid assets. in the case of the reverse repurchase agreements, this is the amount of cash provided to the counterparty.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}CollVal uses Python identifier CollVal
    __CollVal = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CollVal'), 'CollVal', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_AssetValuation2__3_urnisostdiso20022techxsdDRAFT3auth_093_001_01CollVal', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 562, 12), )

    
    CollVal = property(__CollVal.value, __CollVal.set, None, 'CollateralValueValue of the collateral at the end-of-period after taking into account the haircut.\r\nThe collateral value has to be reported for financial derivatives, repurchase agreements and reverse repurchase agreements. This is the amount of cash received by the fund as part of the repurchase agreements.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}RstDt uses Python identifier RstDt
    __RstDt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RstDt'), 'RstDt', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_AssetValuation2__3_urnisostdiso20022techxsdDRAFT3auth_093_001_01RstDt', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 569, 12), )

    
    RstDt = property(__RstDt.value, __RstDt.set, None, 'ResetDateDate at which the interest rate of an interest bearing instrument will be reset, according to the terms of the issue.\r\nThe reset date has to be reported for money market instruments and financial derivatives.\r\n')

    _ElementMap.update({
        __MtrtyDt.name() : __MtrtyDt,
        __NtnlCcyFrstLeg.name() : __NtnlCcyFrstLeg,
        __NtnlCcyScndLeg.name() : __NtnlCcyScndLeg,
        __TtlVal.name() : __TtlVal,
        __XpsrVal.name() : __XpsrVal,
        __CollVal.name() : __CollVal,
        __RstDt.name() : __RstDt
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.AssetValuation2__3 = AssetValuation2__3
Namespace.addCategoryObject('typeBinding', 'AssetValuation2__3', AssetValuation2__3)


# Complex type {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}AssetValuation2__4 with content type ELEMENT_ONLY
class AssetValuation2__4 (pyxb.binding.basis.complexTypeDefinition):
    """AssetValuation2__4Provides details about the valuation of the assets held by the fund."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AssetValuation2__4')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 579, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}NtnlCcyFrstLeg uses Python identifier NtnlCcyFrstLeg
    __NtnlCcyFrstLeg = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NtnlCcyFrstLeg'), 'NtnlCcyFrstLeg', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_AssetValuation2__4_urnisostdiso20022techxsdDRAFT3auth_093_001_01NtnlCcyFrstLeg', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 585, 12), )

    
    NtnlCcyFrstLeg = property(__NtnlCcyFrstLeg.value, __NtnlCcyFrstLeg.set, None, 'NotionalCurrencyFirstLegCurrency of the financial instrument.\r\nThe currency first leg has to be reported for the money market instruments, the securitisations, asset backed commercial papers, deposits or ancillary services, repurchase agreements, reverse repurchase agreements, financial derivatives and shares or units of other funds.\r\nUsage: In the case of an interest rate or currency derivative contract, this will be the notional currency of first leg.\r\n')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}Qty uses Python identifier Qty
    __Qty = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Qty'), 'Qty', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_AssetValuation2__4_urnisostdiso20022techxsdDRAFT3auth_093_001_01Qty', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 594, 12), )

    
    Qty = property(__Qty.value, __Qty.set, None, 'QuantityQuantity of the financial instrument held by the fund.\r\nThe quantity has to be reported for the money market instruments, the securitisations, asset backed commercial papers and shares or units of other funds.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}Pric uses Python identifier Pric
    __Pric = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Pric'), 'Pric', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_AssetValuation2__4_urnisostdiso20022techxsdDRAFT3auth_093_001_01Pric', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 601, 12), )

    
    Pric = property(__Pric.value, __Pric.set, None, 'PricePrice of the asset expressed as a clean price for the money market instruments, the securitisations or asset backed commercial papers. and as a net asset value per unit or share for other money market funds.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}TtlVal uses Python identifier TtlVal
    __TtlVal = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TtlVal'), 'TtlVal', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_AssetValuation2__4_urnisostdiso20022techxsdDRAFT3auth_093_001_01TtlVal', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 607, 12), )

    
    TtlVal = property(__TtlVal.value, __TtlVal.set, None, 'TotalValueThe end-of period total market value in base currency of the financial instrument in which the money market fund has invested.\r\nthe total value has to be reported for the money market instruments, the securitisations, asset backed commercial papers, the financial derivatives, the shares or units of other funds, the repurchase agreements and reverse repurchase agreements.\r\n')

    _ElementMap.update({
        __NtnlCcyFrstLeg.name() : __NtnlCcyFrstLeg,
        __Qty.name() : __Qty,
        __Pric.name() : __Pric,
        __TtlVal.name() : __TtlVal
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.AssetValuation2__4 = AssetValuation2__4
Namespace.addCategoryObject('typeBinding', 'AssetValuation2__4', AssetValuation2__4)


# Complex type {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}AssetValuation2__5 with content type ELEMENT_ONLY
class AssetValuation2__5 (pyxb.binding.basis.complexTypeDefinition):
    """AssetValuation2__5Provides details about the valuation of the assets held by the fund."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AssetValuation2__5')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 617, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}MtrtyDt uses Python identifier MtrtyDt
    __MtrtyDt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'MtrtyDt'), 'MtrtyDt', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_AssetValuation2__5_urnisostdiso20022techxsdDRAFT3auth_093_001_01MtrtyDt', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 623, 12), )

    
    MtrtyDt = property(__MtrtyDt.value, __MtrtyDt.set, None, 'MaturityDatePlanned final repayment date at the time of issuance.\r\nThe maturity date has to be reported for the money market instruments, the securitisations, asset backed commercial papers and financial derivatives.\r\n')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}NtnlCcyFrstLeg uses Python identifier NtnlCcyFrstLeg
    __NtnlCcyFrstLeg = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NtnlCcyFrstLeg'), 'NtnlCcyFrstLeg', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_AssetValuation2__5_urnisostdiso20022techxsdDRAFT3auth_093_001_01NtnlCcyFrstLeg', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 631, 12), )

    
    NtnlCcyFrstLeg = property(__NtnlCcyFrstLeg.value, __NtnlCcyFrstLeg.set, None, 'NotionalCurrencyFirstLegCurrency of the financial instrument.\r\nThe currency first leg has to be reported for the money market instruments, the securitisations, asset backed commercial papers, deposits or ancillary services, repurchase agreements, reverse repurchase agreements, financial derivatives and shares or units of other funds.\r\nUsage: In the case of an interest rate or currency derivative contract, this will be the notional currency of first leg.\r\n')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}XpsrVal uses Python identifier XpsrVal
    __XpsrVal = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'XpsrVal'), 'XpsrVal', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_AssetValuation2__5_urnisostdiso20022techxsdDRAFT3auth_093_001_01XpsrVal', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 640, 12), )

    
    XpsrVal = property(__XpsrVal.value, __XpsrVal.set, None, 'ExposureValueExposure of the financial derivative instrument, the repurchase agreement, reverse repurchase agreement and the deposit or ancillary liquid assets. in the case of the reverse repurchase agreements, this is the amount of cash provided to the counterparty.')

    _ElementMap.update({
        __MtrtyDt.name() : __MtrtyDt,
        __NtnlCcyFrstLeg.name() : __NtnlCcyFrstLeg,
        __XpsrVal.name() : __XpsrVal
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.AssetValuation2__5 = AssetValuation2__5
Namespace.addCategoryObject('typeBinding', 'AssetValuation2__5', AssetValuation2__5)


# Complex type {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}AssetValuation2__6 with content type ELEMENT_ONLY
class AssetValuation2__6 (pyxb.binding.basis.complexTypeDefinition):
    """AssetValuation2__6Provides details about the valuation of the assets held by the fund."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AssetValuation2__6')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 648, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}MtrtyDt uses Python identifier MtrtyDt
    __MtrtyDt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'MtrtyDt'), 'MtrtyDt', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_AssetValuation2__6_urnisostdiso20022techxsdDRAFT3auth_093_001_01MtrtyDt', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 654, 12), )

    
    MtrtyDt = property(__MtrtyDt.value, __MtrtyDt.set, None, 'MaturityDatePlanned final repayment date at the time of issuance.\r\nThe maturity date has to be reported for the money market instruments, the securitisations, asset backed commercial papers and financial derivatives.\r\n')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}NtnlCcyFrstLeg uses Python identifier NtnlCcyFrstLeg
    __NtnlCcyFrstLeg = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NtnlCcyFrstLeg'), 'NtnlCcyFrstLeg', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_AssetValuation2__6_urnisostdiso20022techxsdDRAFT3auth_093_001_01NtnlCcyFrstLeg', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 662, 12), )

    
    NtnlCcyFrstLeg = property(__NtnlCcyFrstLeg.value, __NtnlCcyFrstLeg.set, None, 'NotionalCurrencyFirstLegCurrency of the financial instrument.\r\nThe currency first leg has to be reported for the money market instruments, the securitisations, asset backed commercial papers, deposits or ancillary services, repurchase agreements, reverse repurchase agreements, financial derivatives and shares or units of other funds.\r\nUsage: In the case of an interest rate or currency derivative contract, this will be the notional currency of first leg.\r\n')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}XpsrVal uses Python identifier XpsrVal
    __XpsrVal = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'XpsrVal'), 'XpsrVal', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_AssetValuation2__6_urnisostdiso20022techxsdDRAFT3auth_093_001_01XpsrVal', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 671, 12), )

    
    XpsrVal = property(__XpsrVal.value, __XpsrVal.set, None, 'ExposureValueExposure of the financial derivative instrument, the repurchase agreement, reverse repurchase agreement and the deposit or ancillary liquid assets. in the case of the reverse repurchase agreements, this is the amount of cash provided to the counterparty.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}CollVal uses Python identifier CollVal
    __CollVal = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CollVal'), 'CollVal', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_AssetValuation2__6_urnisostdiso20022techxsdDRAFT3auth_093_001_01CollVal', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 677, 12), )

    
    CollVal = property(__CollVal.value, __CollVal.set, None, 'CollateralValueValue of the collateral at the end-of-period after taking into account the haircut.\r\nThe collateral value has to be reported for financial derivatives, repurchase agreements and reverse repurchase agreements. This is the amount of cash received by the fund as part of the repurchase agreements.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}CdtAssmntRslt uses Python identifier CdtAssmntRslt
    __CdtAssmntRslt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CdtAssmntRslt'), 'CdtAssmntRslt', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_AssetValuation2__6_urnisostdiso20022techxsdDRAFT3auth_093_001_01CdtAssmntRslt', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 684, 12), )

    
    CdtAssmntRslt = property(__CdtAssmntRslt.value, __CdtAssmntRslt.set, None, 'CreditAssessmentResultSpecifies whether the credit assessment is favourable or unfavourable.\r\nThe credit assessment result has to be provided for the money market instruments, the securitisations and asset backed commercial papers and the repurchase agreements.')

    _ElementMap.update({
        __MtrtyDt.name() : __MtrtyDt,
        __NtnlCcyFrstLeg.name() : __NtnlCcyFrstLeg,
        __XpsrVal.name() : __XpsrVal,
        __CollVal.name() : __CollVal,
        __CdtAssmntRslt.name() : __CdtAssmntRslt
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.AssetValuation2__6 = AssetValuation2__6
Namespace.addCategoryObject('typeBinding', 'AssetValuation2__6', AssetValuation2__6)


# Complex type {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}BreakdownByArrangement2__1 with content type ELEMENT_ONLY
class BreakdownByArrangement2__1 (pyxb.binding.basis.complexTypeDefinition):
    """BreakdownByArrangement2__1Specifies the net asset value by type of arrangement."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BreakdownByArrangement2__1')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 703, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}ArrgmntTp uses Python identifier ArrgmntTp
    __ArrgmntTp = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ArrgmntTp'), 'ArrgmntTp', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_BreakdownByArrangement2__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01ArrgmntTp', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 709, 12), )

    
    ArrgmntTp = property(__ArrgmntTp.value, __ArrgmntTp.set, None, 'ArrangementTypeIndicates the types of arrangement to which the fund is subject on.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}NetAsstValRate uses Python identifier NetAsstValRate
    __NetAsstValRate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NetAsstValRate'), 'NetAsstValRate', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_BreakdownByArrangement2__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01NetAsstValRate', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 715, 12), )

    
    NetAsstValRate = property(__NetAsstValRate.value, __NetAsstValRate.set, None, 'NetAssetValueRatePortion of the net asset value subject to the arrangement type.')

    _ElementMap.update({
        __ArrgmntTp.name() : __ArrgmntTp,
        __NetAsstValRate.name() : __NetAsstValRate
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.BreakdownByArrangement2__1 = BreakdownByArrangement2__1
Namespace.addCategoryObject('typeBinding', 'BreakdownByArrangement2__1', BreakdownByArrangement2__1)


# Complex type {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}BreakdownByCountry4__1 with content type ELEMENT_ONLY
class BreakdownByCountry4__1 (pyxb.binding.basis.complexTypeDefinition):
    """BreakdownByCountry4__1Specifies the percentage of net asset value by country."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BreakdownByCountry4__1')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 723, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}CtryOfRes uses Python identifier CtryOfRes
    __CtryOfRes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CtryOfRes'), 'CtryOfRes', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_BreakdownByCountry4__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01CtryOfRes', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 729, 12), )

    
    CtryOfRes = property(__CtryOfRes.value, __CtryOfRes.set, None, "CountryOfResidenceCountry in which a person resides (the place of a person's home). In the case of a company, it is the country from which the affairs of that company are directed.")

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}Rate uses Python identifier Rate
    __Rate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Rate'), 'Rate', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_BreakdownByCountry4__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01Rate', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 735, 12), )

    
    Rate = property(__Rate.value, __Rate.set, None, 'RateSpecifies the percentage of the net asset value by country of domicile of investors.')

    _ElementMap.update({
        __CtryOfRes.name() : __CtryOfRes,
        __Rate.name() : __Rate
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.BreakdownByCountry4__1 = BreakdownByCountry4__1
Namespace.addCategoryObject('typeBinding', 'BreakdownByCountry4__1', BreakdownByCountry4__1)


# Complex type {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}ConstantNetAssetValueDeviationEvent1__1 with content type ELEMENT_ONLY
class ConstantNetAssetValueDeviationEvent1__1 (pyxb.binding.basis.complexTypeDefinition):
    """ConstantNetAssetValueDeviationEvent1__1Details of the events where the constant net asset value per unit or share calculated in accordance with the amortised cost method deviates from the net asset value per unit or share calculated in accordance with the mark-to-market or mark-to-model method by more than 20 basis points."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ConstantNetAssetValueDeviationEvent1__1')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 752, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}ValtnDt uses Python identifier ValtnDt
    __ValtnDt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ValtnDt'), 'ValtnDt', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_ConstantNetAssetValueDeviationEvent1__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01ValtnDt', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 758, 12), )

    
    ValtnDt = property(__ValtnDt.value, __ValtnDt.set, None, 'ValuationDateDate from which the price of an asset calculated in accordance with the mark-to-market or mark-to-model method deviates from the asset price calculated in accordance with the amortised cost method by more than 10 basis points.\r\n')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}CstNetAsstValPerUnit uses Python identifier CstNetAsstValPerUnit
    __CstNetAsstValPerUnit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CstNetAsstValPerUnit'), 'CstNetAsstValPerUnit', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_ConstantNetAssetValueDeviationEvent1__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01CstNetAsstValPerUnit', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 765, 12), )

    
    CstNetAsstValPerUnit = property(__CstNetAsstValPerUnit.value, __CstNetAsstValPerUnit.set, None, 'ConstantNetAssetValuePerUnitConstant net asset value at the valuation date of a specific investment fund class calculated in accordance with the amortised cost method divided by the number of outstanding units or shares of the fund.\r\n')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}NetAsstValPerUnit uses Python identifier NetAsstValPerUnit
    __NetAsstValPerUnit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NetAsstValPerUnit'), 'NetAsstValPerUnit', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_ConstantNetAssetValueDeviationEvent1__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01NetAsstValPerUnit', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 772, 12), )

    
    NetAsstValPerUnit = property(__NetAsstValPerUnit.value, __NetAsstValPerUnit.set, None, "NetAssetValuePerUnitNet asset value at the valuation date of all the holdings, less the fund's liabilities, attributable to a specific investment fund class calculated in accordance with mark-to-market or mark-to-model divided by the number of outstanding units or shares of the fund.\r\n")

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}NbOfDaysDvtn uses Python identifier NbOfDaysDvtn
    __NbOfDaysDvtn = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NbOfDaysDvtn'), 'NbOfDaysDvtn', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_ConstantNetAssetValueDeviationEvent1__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01NbOfDaysDvtn', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 779, 12), )

    
    NbOfDaysDvtn = property(__NbOfDaysDvtn.value, __NbOfDaysDvtn.set, None, 'NumberOfDaysDeviationNumber of days the net asset value deviates from the constant net asset value per unit or share by more than 20 basis points.\r\n')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}AvrgBsisPtSprd uses Python identifier AvrgBsisPtSprd
    __AvrgBsisPtSprd = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AvrgBsisPtSprd'), 'AvrgBsisPtSprd', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_ConstantNetAssetValueDeviationEvent1__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01AvrgBsisPtSprd', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 786, 12), )

    
    AvrgBsisPtSprd = property(__AvrgBsisPtSprd.value, __AvrgBsisPtSprd.set, None, 'AverageBasisPointSpreadAverage number of basis points added to (if positive) or deducted from (if negative) the net asset value to calculate the constant net asset value per unit or share when the net asset value deviates from the constant net asset value per unit or share by more than 20 basis points.\r\nUsed to express differences in interest rates, for example, a difference of 0.10 % is equivalent to a change of 10 basis points.\r\r\n\r\r\r\n')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}LwstPricDvtn uses Python identifier LwstPricDvtn
    __LwstPricDvtn = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'LwstPricDvtn'), 'LwstPricDvtn', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_ConstantNetAssetValueDeviationEvent1__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01LwstPricDvtn', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 795, 12), )

    
    LwstPricDvtn = property(__LwstPricDvtn.value, __LwstPricDvtn.set, None, 'LowestPriceDeviationMinimum price deviation between the net asset value and the constant net asset value per unit or share.\r\n')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}HghstPricDvtn uses Python identifier HghstPricDvtn
    __HghstPricDvtn = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'HghstPricDvtn'), 'HghstPricDvtn', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_ConstantNetAssetValueDeviationEvent1__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01HghstPricDvtn', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 802, 12), )

    
    HghstPricDvtn = property(__HghstPricDvtn.value, __HghstPricDvtn.set, None, 'HighestPriceDeviationMaximum price deviation between the net asset value and the constant net asset value per unit or share.\r\n')

    _ElementMap.update({
        __ValtnDt.name() : __ValtnDt,
        __CstNetAsstValPerUnit.name() : __CstNetAsstValPerUnit,
        __NetAsstValPerUnit.name() : __NetAsstValPerUnit,
        __NbOfDaysDvtn.name() : __NbOfDaysDvtn,
        __AvrgBsisPtSprd.name() : __AvrgBsisPtSprd,
        __LwstPricDvtn.name() : __LwstPricDvtn,
        __HghstPricDvtn.name() : __HghstPricDvtn
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ConstantNetAssetValueDeviationEvent1__1 = ConstantNetAssetValueDeviationEvent1__1
Namespace.addCategoryObject('typeBinding', 'ConstantNetAssetValueDeviationEvent1__1', ConstantNetAssetValueDeviationEvent1__1)


# Complex type {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}Country1Choice__1 with content type ELEMENT_ONLY
class Country1Choice__1 (pyxb.binding.basis.complexTypeDefinition):
    """Country1Choice__1Choice between ISO Country code and supranational country."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Country1Choice__1')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 811, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}Ctry uses Python identifier Ctry
    __Ctry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Ctry'), 'Ctry', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_Country1Choice__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01Ctry', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 817, 12), )

    
    Ctry = property(__Ctry.value, __Ctry.set, None, 'CountryCode to identify a country, a dependency, or another area of particular geopolitical interest, on the basis of country names obtained from the United Nations (ISO 3166, Alpha-2 code).')

    _ElementMap.update({
        __Ctry.name() : __Ctry
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Country1Choice__1 = Country1Choice__1
Namespace.addCategoryObject('typeBinding', 'Country1Choice__1', Country1Choice__1)


# Complex type {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}Country1Choice__2 with content type ELEMENT_ONLY
class Country1Choice__2 (pyxb.binding.basis.complexTypeDefinition):
    """Country1Choice__2Choice between ISO Country code and supranational country."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Country1Choice__2')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 825, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}Ctry uses Python identifier Ctry
    __Ctry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Ctry'), 'Ctry', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_Country1Choice__2_urnisostdiso20022techxsdDRAFT3auth_093_001_01Ctry', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 831, 12), )

    
    Ctry = property(__Ctry.value, __Ctry.set, None, 'CountryCode to identify a country, a dependency, or another area of particular geopolitical interest, on the basis of country names obtained from the United Nations (ISO 3166, Alpha-2 code).')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}SprntnlCtry uses Python identifier SprntnlCtry
    __SprntnlCtry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SprntnlCtry'), 'SprntnlCtry', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_Country1Choice__2_urnisostdiso20022techxsdDRAFT3auth_093_001_01SprntnlCtry', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 837, 12), )

    
    SprntnlCtry = property(__SprntnlCtry.value, __SprntnlCtry.set, None, 'SupranationalCountrySpecifies that no predominant geographical focus is possible.')

    _ElementMap.update({
        __Ctry.name() : __Ctry,
        __SprntnlCtry.name() : __SprntnlCtry
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Country1Choice__2 = Country1Choice__2
Namespace.addCategoryObject('typeBinding', 'Country1Choice__2', Country1Choice__2)


# Complex type {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}Country1Choice__3 with content type ELEMENT_ONLY
class Country1Choice__3 (pyxb.binding.basis.complexTypeDefinition):
    """Country1Choice__3Choice between ISO Country code and supranational country."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Country1Choice__3')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 845, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}Ctry uses Python identifier Ctry
    __Ctry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Ctry'), 'Ctry', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_Country1Choice__3_urnisostdiso20022techxsdDRAFT3auth_093_001_01Ctry', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 851, 12), )

    
    Ctry = property(__Ctry.value, __Ctry.set, None, 'CountryCode to identify a country, a dependency, or another area of particular geopolitical interest, on the basis of country names obtained from the United Nations (ISO 3166, Alpha-2 code).')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}SprntnlCtry uses Python identifier SprntnlCtry
    __SprntnlCtry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SprntnlCtry'), 'SprntnlCtry', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_Country1Choice__3_urnisostdiso20022techxsdDRAFT3auth_093_001_01SprntnlCtry', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 857, 12), )

    
    SprntnlCtry = property(__SprntnlCtry.value, __SprntnlCtry.set, None, 'SupranationalCountrySpecifies that no predominant geographical focus is possible.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}UknwnCtry uses Python identifier UknwnCtry
    __UknwnCtry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'UknwnCtry'), 'UknwnCtry', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_Country1Choice__3_urnisostdiso20022techxsdDRAFT3auth_093_001_01UknwnCtry', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 863, 12), )

    
    UknwnCtry = property(__UknwnCtry.value, __UknwnCtry.set, None, 'UnknownCountrySpecifies that the country is not known.')

    _ElementMap.update({
        __Ctry.name() : __Ctry,
        __SprntnlCtry.name() : __SprntnlCtry,
        __UknwnCtry.name() : __UknwnCtry
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Country1Choice__3 = Country1Choice__3
Namespace.addCategoryObject('typeBinding', 'Country1Choice__3', Country1Choice__3)


# Complex type {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}CurrencyExchange14__1 with content type ELEMENT_ONLY
class CurrencyExchange14__1 (pyxb.binding.basis.complexTypeDefinition):
    """CurrencyExchange14__1Specifies details of the fund currency exchange."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CurrencyExchange14__1')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 880, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}BaseCcyAmt uses Python identifier BaseCcyAmt
    __BaseCcyAmt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'BaseCcyAmt'), 'BaseCcyAmt', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_CurrencyExchange14__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01BaseCcyAmt', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 886, 12), )

    
    BaseCcyAmt = property(__BaseCcyAmt.value, __BaseCcyAmt.set, None, 'BaseCurrencyAmountAmount in the base currency of the fund.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}RptgCcyAmt uses Python identifier RptgCcyAmt
    __RptgCcyAmt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RptgCcyAmt'), 'RptgCcyAmt', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_CurrencyExchange14__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01RptgCcyAmt', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 892, 12), )

    
    RptgCcyAmt = property(__RptgCcyAmt.value, __RptgCcyAmt.set, None, 'ReportingCurrencyAmountAmount expressed in the reporting currency.')

    _ElementMap.update({
        __BaseCcyAmt.name() : __BaseCcyAmt,
        __RptgCcyAmt.name() : __RptgCcyAmt
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CurrencyExchange14__1 = CurrencyExchange14__1
Namespace.addCategoryObject('typeBinding', 'CurrencyExchange14__1', CurrencyExchange14__1)


# Complex type {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}CurrencyExchange1Choice__1 with content type ELEMENT_ONLY
class CurrencyExchange1Choice__1 (pyxb.binding.basis.complexTypeDefinition):
    """CurrencyExchange1Choice__1Specifies the amount value."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CurrencyExchange1Choice__1')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 900, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}Amt uses Python identifier Amt
    __Amt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Amt'), 'Amt', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_CurrencyExchange1Choice__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01Amt', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 906, 12), )

    
    Amt = property(__Amt.value, __Amt.set, None, 'AmountAmount value.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}NotAvlblVal uses Python identifier NotAvlblVal
    __NotAvlblVal = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NotAvlblVal'), 'NotAvlblVal', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_CurrencyExchange1Choice__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01NotAvlblVal', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 912, 12), )

    
    NotAvlblVal = property(__NotAvlblVal.value, __NotAvlblVal.set, None, 'NotAvailableValueThe value is not available.')

    _ElementMap.update({
        __Amt.name() : __Amt,
        __NotAvlblVal.name() : __NotAvlblVal
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CurrencyExchange1Choice__1 = CurrencyExchange1Choice__1
Namespace.addCategoryObject('typeBinding', 'CurrencyExchange1Choice__1', CurrencyExchange1Choice__1)


# Complex type {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}DerivativeInstrument8 with content type ELEMENT_ONLY
class DerivativeInstrument8 (pyxb.binding.basis.complexTypeDefinition):
    """DerivativeInstrument8Attributes of derivatives."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DerivativeInstrument8')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 930, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}CtrctTp uses Python identifier CtrctTp
    __CtrctTp = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CtrctTp'), 'CtrctTp', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_DerivativeInstrument8_urnisostdiso20022techxsdDRAFT3auth_093_001_01CtrctTp', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 936, 12), )

    
    CtrctTp = property(__CtrctTp.value, __CtrctTp.set, None, 'ContractTypeClassification of information according to contract type.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}UndrlygTp uses Python identifier UndrlygTp
    __UndrlygTp = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'UndrlygTp'), 'UndrlygTp', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_DerivativeInstrument8_urnisostdiso20022techxsdDRAFT3auth_093_001_01UndrlygTp', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 942, 12), )

    
    UndrlygTp = property(__UndrlygTp.value, __UndrlygTp.set, None, 'UnderlyingTypeSpecifies the information related to the underlying instrument of the derivatives.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}UndrlygId uses Python identifier UndrlygId
    __UndrlygId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'UndrlygId'), 'UndrlygId', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_DerivativeInstrument8_urnisostdiso20022techxsdDRAFT3auth_093_001_01UndrlygId', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 948, 12), )

    
    UndrlygId = property(__UndrlygId.value, __UndrlygId.set, None, 'UnderlyingIdentificationUnique identification to identify the direct underlying instrument.')

    _ElementMap.update({
        __CtrctTp.name() : __CtrctTp,
        __UndrlygTp.name() : __UndrlygTp,
        __UndrlygId.name() : __UndrlygId
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.DerivativeInstrument8 = DerivativeInstrument8
Namespace.addCategoryObject('typeBinding', 'DerivativeInstrument8', DerivativeInstrument8)


# Complex type {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}Document with content type ELEMENT_ONLY
class Document_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}Document with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Document')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 956, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}MnyMktFndRpt uses Python identifier MnyMktFndRpt
    __MnyMktFndRpt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'MnyMktFndRpt'), 'MnyMktFndRpt', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_Document__urnisostdiso20022techxsdDRAFT3auth_093_001_01MnyMktFndRpt', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 958, 12), )

    
    MnyMktFndRpt = property(__MnyMktFndRpt.value, __MnyMktFndRpt.set, None, None)

    _ElementMap.update({
        __MnyMktFndRpt.name() : __MnyMktFndRpt
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Document_ = Document_
Namespace.addCategoryObject('typeBinding', 'Document', Document_)


# Complex type {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}FinancialInstrument60Choice__1 with content type ELEMENT_ONLY
class FinancialInstrument60Choice__1 (pyxb.binding.basis.complexTypeDefinition):
    """FinancialInstrument60Choice__1Choice to specify the information on  share class."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'FinancialInstrument60Choice__1')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1125, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}NoShrClssInf uses Python identifier NoShrClssInf
    __NoShrClssInf = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NoShrClssInf'), 'NoShrClssInf', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_FinancialInstrument60Choice__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01NoShrClssInf', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1131, 12), )

    
    NoShrClssInf = property(__NoShrClssInf.value, __NoShrClssInf.set, None, 'NoShareClassInformationInformation on the identification of the fund when the fund is not divided into several share classes.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}ShrClssList uses Python identifier ShrClssList
    __ShrClssList = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ShrClssList'), 'ShrClssList', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_FinancialInstrument60Choice__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01ShrClssList', True, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1137, 12), )

    
    ShrClssList = property(__ShrClssList.value, __ShrClssList.set, None, 'ShareClassListInformation on the share classes of the fund when the fund has several share classes.')

    _ElementMap.update({
        __NoShrClssInf.name() : __NoShrClssInf,
        __ShrClssList.name() : __ShrClssList
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.FinancialInstrument60Choice__1 = FinancialInstrument60Choice__1
Namespace.addCategoryObject('typeBinding', 'FinancialInstrument60Choice__1', FinancialInstrument60Choice__1)


# Complex type {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}FinancialInstrument80__1 with content type ELEMENT_ONLY
class FinancialInstrument80__1 (pyxb.binding.basis.complexTypeDefinition):
    """FinancialInstrument80__1Provides details about the collateral received in the context of the reverse repurchase agreement.
"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'FinancialInstrument80__1')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1145, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}FinInstrmId uses Python identifier FinInstrmId
    __FinInstrmId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'FinInstrmId'), 'FinInstrmId', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_FinancialInstrument80__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01FinInstrmId', True, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1152, 12), )

    
    FinInstrmId = property(__FinInstrmId.value, __FinInstrmId.set, None, 'FinancialInstrumentIdentificationIdentification of the fund.\r\n')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}DrgtnRcvdAssts uses Python identifier DrgtnRcvdAssts
    __DrgtnRcvdAssts = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DrgtnRcvdAssts'), 'DrgtnRcvdAssts', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_FinancialInstrument80__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01DrgtnRcvdAssts', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1159, 12), )

    
    DrgtnRcvdAssts = property(__DrgtnRcvdAssts.value, __DrgtnRcvdAssts.set, None, 'DerogationReceivedAssetsIn the context of the reverse repurchase agreements, indicates whether there are any non-authorised assets that were received by the fund by derogation with the local regulation.\r\n')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}TtlVal uses Python identifier TtlVal
    __TtlVal = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TtlVal'), 'TtlVal', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_FinancialInstrument80__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01TtlVal', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1166, 12), )

    
    TtlVal = property(__TtlVal.value, __TtlVal.set, None, 'TotalValueTotal market value of the assets received by the money market fund in the context of a reverse repurchase agreement.')

    _ElementMap.update({
        __FinInstrmId.name() : __FinInstrmId,
        __DrgtnRcvdAssts.name() : __DrgtnRcvdAssts,
        __TtlVal.name() : __TtlVal
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.FinancialInstrument80__1 = FinancialInstrument80__1
Namespace.addCategoryObject('typeBinding', 'FinancialInstrument80__1', FinancialInstrument80__1)


# Complex type {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}FinancialInstrument82__1 with content type ELEMENT_ONLY
class FinancialInstrument82__1 (pyxb.binding.basis.complexTypeDefinition):
    """FinancialInstrument82__1Specifies further details of the financial instrument."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'FinancialInstrument82__1')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1174, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}FndNttyId uses Python identifier FndNttyId
    __FndNttyId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'FndNttyId'), 'FndNttyId', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_FinancialInstrument82__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01FndNttyId', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1180, 12), )

    
    FndNttyId = property(__FndNttyId.value, __FndNttyId.set, None, 'FundEntityIdentificationIdentification of the money market fund.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}FndMgmtCpny uses Python identifier FndMgmtCpny
    __FndMgmtCpny = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'FndMgmtCpny'), 'FndMgmtCpny', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_FinancialInstrument82__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01FndMgmtCpny', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1186, 12), )

    
    FndMgmtCpny = property(__FndMgmtCpny.value, __FndMgmtCpny.set, None, 'FundManagementCompanyCompany that is responsible for the management and operation of the fund, eg, determines the investment strategy, appoints the service providers, and makes major decisions for the fund. It is usually responsible for the distribution and marketing of the fund. For self-managed funds, this will often be a separate promoter or sponsor of the fund.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}FndAttrbts uses Python identifier FndAttrbts
    __FndAttrbts = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'FndAttrbts'), 'FndAttrbts', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_FinancialInstrument82__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01FndAttrbts', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1192, 12), )

    
    FndAttrbts = property(__FndAttrbts.value, __FndAttrbts.set, None, 'FundAttributesAttributes defining further details on the fund financial instrument.')

    _ElementMap.update({
        __FndNttyId.name() : __FndNttyId,
        __FndMgmtCpny.name() : __FndMgmtCpny,
        __FndAttrbts.name() : __FndAttrbts
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.FinancialInstrument82__1 = FinancialInstrument82__1
Namespace.addCategoryObject('typeBinding', 'FinancialInstrument82__1', FinancialInstrument82__1)


# Complex type {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}FinancialInstrumentAttributes101__1 with content type ELEMENT_ONLY
class FinancialInstrumentAttributes101__1 (pyxb.binding.basis.complexTypeDefinition):
    """FinancialInstrumentAttributes101__1Elements characterising a financial instrument.
"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'FinancialInstrumentAttributes101__1')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1200, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}Nm uses Python identifier Nm
    __Nm = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Nm'), 'Nm', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_FinancialInstrumentAttributes101__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01Nm', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1207, 12), )

    
    Nm = property(__Nm.value, __Nm.set, None, 'NameName of the financial instrument in free format text.\r\n')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}LglFrmwk uses Python identifier LglFrmwk
    __LglFrmwk = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'LglFrmwk'), 'LglFrmwk', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_FinancialInstrumentAttributes101__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01LglFrmwk', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1214, 12), )

    
    LglFrmwk = property(__LglFrmwk.value, __LglFrmwk.set, None, 'LegalFrameworkLegal framework of the fund.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}StffWthSvgsPlan uses Python identifier StffWthSvgsPlan
    __StffWthSvgsPlan = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'StffWthSvgsPlan'), 'StffWthSvgsPlan', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_FinancialInstrumentAttributes101__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01StffWthSvgsPlan', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1220, 12), )

    
    StffWthSvgsPlan = property(__StffWthSvgsPlan.value, __StffWthSvgsPlan.set, None, 'StaffWithSavingsPlanIndicates whether the fund is attributed to a staff member with a savings plan.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}RegdDstrbtnCtry uses Python identifier RegdDstrbtnCtry
    __RegdDstrbtnCtry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RegdDstrbtnCtry'), 'RegdDstrbtnCtry', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_FinancialInstrumentAttributes101__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01RegdDstrbtnCtry', True, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1226, 12), )

    
    RegdDstrbtnCtry = property(__RegdDstrbtnCtry.value, __RegdDstrbtnCtry.set, None, 'RegisteredDistributionCountryCountries where the fund is registered for distribution.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}BaseCcy uses Python identifier BaseCcy
    __BaseCcy = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'BaseCcy'), 'BaseCcy', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_FinancialInstrumentAttributes101__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01BaseCcy', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1232, 12), )

    
    BaseCcy = property(__BaseCcy.value, __BaseCcy.set, None, 'BaseCurrencyCurrency of the investment fund class.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}DpstryId uses Python identifier DpstryId
    __DpstryId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DpstryId'), 'DpstryId', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_FinancialInstrumentAttributes101__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01DpstryId', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1238, 12), )

    
    DpstryId = property(__DpstryId.value, __DpstryId.set, None, 'DepositoryIdentificationProvides information about identification of the depository.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}MnyMktFndTp uses Python identifier MnyMktFndTp
    __MnyMktFndTp = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'MnyMktFndTp'), 'MnyMktFndTp', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_FinancialInstrumentAttributes101__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01MnyMktFndTp', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1244, 12), )

    
    MnyMktFndTp = property(__MnyMktFndTp.value, __MnyMktFndTp.set, None, 'MoneyMarketFundTypeSpecifies the type of the money market fund.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}MstrFnd uses Python identifier MstrFnd
    __MstrFnd = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'MstrFnd'), 'MstrFnd', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_FinancialInstrumentAttributes101__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01MstrFnd', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1250, 12), )

    
    MstrFnd = property(__MstrFnd.value, __MstrFnd.set, None, 'MasterFundIndicates whether the fund is a master or a feeder fund.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}MstrFndList uses Python identifier MstrFndList
    __MstrFndList = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'MstrFndList'), 'MstrFndList', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_FinancialInstrumentAttributes101__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01MstrFndList', True, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1256, 12), )

    
    MstrFndList = property(__MstrFndList.value, __MstrFndList.set, None, 'MasterFundListProvides information about identification of the master fund(s).\r\n')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}ShrClssInd uses Python identifier ShrClssInd
    __ShrClssInd = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ShrClssInd'), 'ShrClssInd', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_FinancialInstrumentAttributes101__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01ShrClssInd', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1263, 12), )

    
    ShrClssInd = property(__ShrClssInd.value, __ShrClssInd.set, None, 'ShareClassIndicatorIndicates whether the fund has share classes.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}ShrClss uses Python identifier ShrClss
    __ShrClss = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ShrClss'), 'ShrClss', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_FinancialInstrumentAttributes101__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01ShrClss', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1269, 12), )

    
    ShrClss = property(__ShrClss.value, __ShrClss.set, None, 'ShareClassInformation on the sub-fund or share classes of the fund.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}FndRltdEvt uses Python identifier FndRltdEvt
    __FndRltdEvt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'FndRltdEvt'), 'FndRltdEvt', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_FinancialInstrumentAttributes101__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01FndRltdEvt', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1275, 12), )

    
    FndRltdEvt = property(__FndRltdEvt.value, __FndRltdEvt.set, None, 'FundRelatedEventSpecifies the dates in relation with the money market fund life cycle.')

    _ElementMap.update({
        __Nm.name() : __Nm,
        __LglFrmwk.name() : __LglFrmwk,
        __StffWthSvgsPlan.name() : __StffWthSvgsPlan,
        __RegdDstrbtnCtry.name() : __RegdDstrbtnCtry,
        __BaseCcy.name() : __BaseCcy,
        __DpstryId.name() : __DpstryId,
        __MnyMktFndTp.name() : __MnyMktFndTp,
        __MstrFnd.name() : __MstrFnd,
        __MstrFndList.name() : __MstrFndList,
        __ShrClssInd.name() : __ShrClssInd,
        __ShrClss.name() : __ShrClss,
        __FndRltdEvt.name() : __FndRltdEvt
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.FinancialInstrumentAttributes101__1 = FinancialInstrumentAttributes101__1
Namespace.addCategoryObject('typeBinding', 'FinancialInstrumentAttributes101__1', FinancialInstrumentAttributes101__1)


# Complex type {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}FinancialInstrumentQuantity1Choice__1 with content type ELEMENT_ONLY
class FinancialInstrumentQuantity1Choice__1 (pyxb.binding.basis.complexTypeDefinition):
    """FinancialInstrumentQuantity1Choice__1Choice between formats for the quantity of security."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'FinancialInstrumentQuantity1Choice__1')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1356, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}Unit uses Python identifier Unit
    __Unit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Unit'), 'Unit', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_FinancialInstrumentQuantity1Choice__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01Unit', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1362, 12), )

    
    Unit = property(__Unit.value, __Unit.set, None, 'UnitQuantity expressed as a number, for example, a number of shares.')

    _ElementMap.update({
        __Unit.name() : __Unit
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.FinancialInstrumentQuantity1Choice__1 = FinancialInstrumentQuantity1Choice__1
Namespace.addCategoryObject('typeBinding', 'FinancialInstrumentQuantity1Choice__1', FinancialInstrumentQuantity1Choice__1)


# Complex type {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}Financialinstrument81__1 with content type ELEMENT_ONLY
class Financialinstrument81__1 (pyxb.binding.basis.complexTypeDefinition):
    """Financialinstrument81__1Specifies the characteristics of the assets held by the fund."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Financialinstrument81__1')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1370, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}AsstTp uses Python identifier AsstTp
    __AsstTp = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AsstTp'), 'AsstTp', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_Financialinstrument81__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01AsstTp', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1376, 12), )

    
    AsstTp = property(__AsstTp.value, __AsstTp.set, None, 'AssetTypeSpecifies the type of financial assets.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}AsstId uses Python identifier AsstId
    __AsstId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AsstId'), 'AsstId', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_Financialinstrument81__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01AsstId', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1382, 12), )

    
    AsstId = property(__AsstId.value, __AsstId.set, None, 'AssetIdentificationIdentification of the asset.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}PtyData uses Python identifier PtyData
    __PtyData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PtyData'), 'PtyData', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_Financialinstrument81__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01PtyData', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1388, 12), )

    
    PtyData = property(__PtyData.value, __PtyData.set, None, 'PartyDataSpecifies further details of the party.\r\n')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}AsstCtry uses Python identifier AsstCtry
    __AsstCtry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AsstCtry'), 'AsstCtry', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_Financialinstrument81__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01AsstCtry', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1395, 12), )

    
    AsstCtry = property(__AsstCtry.value, __AsstCtry.set, None, 'AssetCountryCountry of the asset as considered relevant under the Regulation.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}AsstValtn uses Python identifier AsstValtn
    __AsstValtn = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AsstValtn'), 'AsstValtn', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_Financialinstrument81__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01AsstValtn', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1401, 12), )

    
    AsstValtn = property(__AsstValtn.value, __AsstValtn.set, None, 'AssetValuationInformation on the valuation of the assets.')

    _ElementMap.update({
        __AsstTp.name() : __AsstTp,
        __AsstId.name() : __AsstId,
        __PtyData.name() : __PtyData,
        __AsstCtry.name() : __AsstCtry,
        __AsstValtn.name() : __AsstValtn
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Financialinstrument81__1 = Financialinstrument81__1
Namespace.addCategoryObject('typeBinding', 'Financialinstrument81__1', Financialinstrument81__1)


# Complex type {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}Financialinstrument81__2 with content type ELEMENT_ONLY
class Financialinstrument81__2 (pyxb.binding.basis.complexTypeDefinition):
    """Financialinstrument81__2Specifies the characteristics of the assets held by the fund."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Financialinstrument81__2')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1409, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}AsstTp uses Python identifier AsstTp
    __AsstTp = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AsstTp'), 'AsstTp', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_Financialinstrument81__2_urnisostdiso20022techxsdDRAFT3auth_093_001_01AsstTp', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1415, 12), )

    
    AsstTp = property(__AsstTp.value, __AsstTp.set, None, 'AssetTypeSpecifies the type of financial assets.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}AsstId uses Python identifier AsstId
    __AsstId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AsstId'), 'AsstId', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_Financialinstrument81__2_urnisostdiso20022techxsdDRAFT3auth_093_001_01AsstId', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1421, 12), )

    
    AsstId = property(__AsstId.value, __AsstId.set, None, 'AssetIdentificationIdentification of the asset.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}PtyData uses Python identifier PtyData
    __PtyData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PtyData'), 'PtyData', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_Financialinstrument81__2_urnisostdiso20022techxsdDRAFT3auth_093_001_01PtyData', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1427, 12), )

    
    PtyData = property(__PtyData.value, __PtyData.set, None, 'PartyDataSpecifies further details of the party.\r\n')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}AsstCtry uses Python identifier AsstCtry
    __AsstCtry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AsstCtry'), 'AsstCtry', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_Financialinstrument81__2_urnisostdiso20022techxsdDRAFT3auth_093_001_01AsstCtry', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1434, 12), )

    
    AsstCtry = property(__AsstCtry.value, __AsstCtry.set, None, 'AssetCountryCountry of the asset as considered relevant under the Regulation.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}AsstValtn uses Python identifier AsstValtn
    __AsstValtn = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AsstValtn'), 'AsstValtn', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_Financialinstrument81__2_urnisostdiso20022techxsdDRAFT3auth_093_001_01AsstValtn', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1440, 12), )

    
    AsstValtn = property(__AsstValtn.value, __AsstValtn.set, None, 'AssetValuationInformation on the valuation of the assets.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}FincgUndrlygTp uses Python identifier FincgUndrlygTp
    __FincgUndrlygTp = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'FincgUndrlygTp'), 'FincgUndrlygTp', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_Financialinstrument81__2_urnisostdiso20022techxsdDRAFT3auth_093_001_01FincgUndrlygTp', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1446, 12), )

    
    FincgUndrlygTp = property(__FincgUndrlygTp.value, __FincgUndrlygTp.set, None, 'FinancingUnderlyingTypeUnderlying type of the financing instrument such as the asset backed commercial paper or securitisation.')

    _ElementMap.update({
        __AsstTp.name() : __AsstTp,
        __AsstId.name() : __AsstId,
        __PtyData.name() : __PtyData,
        __AsstCtry.name() : __AsstCtry,
        __AsstValtn.name() : __AsstValtn,
        __FincgUndrlygTp.name() : __FincgUndrlygTp
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Financialinstrument81__2 = Financialinstrument81__2
Namespace.addCategoryObject('typeBinding', 'Financialinstrument81__2', Financialinstrument81__2)


# Complex type {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}Financialinstrument81__3 with content type ELEMENT_ONLY
class Financialinstrument81__3 (pyxb.binding.basis.complexTypeDefinition):
    """Financialinstrument81__3Specifies the characteristics of the assets held by the fund."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Financialinstrument81__3')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1454, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}AsstTp uses Python identifier AsstTp
    __AsstTp = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AsstTp'), 'AsstTp', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_Financialinstrument81__3_urnisostdiso20022techxsdDRAFT3auth_093_001_01AsstTp', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1460, 12), )

    
    AsstTp = property(__AsstTp.value, __AsstTp.set, None, 'AssetTypeSpecifies the type of financial assets.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}AsstId uses Python identifier AsstId
    __AsstId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AsstId'), 'AsstId', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_Financialinstrument81__3_urnisostdiso20022techxsdDRAFT3auth_093_001_01AsstId', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1466, 12), )

    
    AsstId = property(__AsstId.value, __AsstId.set, None, 'AssetIdentificationIdentification of the asset.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}PtyData uses Python identifier PtyData
    __PtyData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PtyData'), 'PtyData', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_Financialinstrument81__3_urnisostdiso20022techxsdDRAFT3auth_093_001_01PtyData', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1472, 12), )

    
    PtyData = property(__PtyData.value, __PtyData.set, None, 'PartyDataSpecifies further details of the party.\r\n')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}AsstCtry uses Python identifier AsstCtry
    __AsstCtry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AsstCtry'), 'AsstCtry', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_Financialinstrument81__3_urnisostdiso20022techxsdDRAFT3auth_093_001_01AsstCtry', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1479, 12), )

    
    AsstCtry = property(__AsstCtry.value, __AsstCtry.set, None, 'AssetCountryCountry of the asset as considered relevant under the Regulation.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}AsstValtn uses Python identifier AsstValtn
    __AsstValtn = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AsstValtn'), 'AsstValtn', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_Financialinstrument81__3_urnisostdiso20022techxsdDRAFT3auth_093_001_01AsstValtn', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1485, 12), )

    
    AsstValtn = property(__AsstValtn.value, __AsstValtn.set, None, 'AssetValuationInformation on the valuation of the assets.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}DerivInstrmAttrbts uses Python identifier DerivInstrmAttrbts
    __DerivInstrmAttrbts = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DerivInstrmAttrbts'), 'DerivInstrmAttrbts', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_Financialinstrument81__3_urnisostdiso20022techxsdDRAFT3auth_093_001_01DerivInstrmAttrbts', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1491, 12), )

    
    DerivInstrmAttrbts = property(__DerivInstrmAttrbts.value, __DerivInstrmAttrbts.set, None, 'DerivativeInstrumentAttributesSpecifies the attributes specific for derivatives.')

    _ElementMap.update({
        __AsstTp.name() : __AsstTp,
        __AsstId.name() : __AsstId,
        __PtyData.name() : __PtyData,
        __AsstCtry.name() : __AsstCtry,
        __AsstValtn.name() : __AsstValtn,
        __DerivInstrmAttrbts.name() : __DerivInstrmAttrbts
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Financialinstrument81__3 = Financialinstrument81__3
Namespace.addCategoryObject('typeBinding', 'Financialinstrument81__3', Financialinstrument81__3)


# Complex type {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}Financialinstrument81__4 with content type ELEMENT_ONLY
class Financialinstrument81__4 (pyxb.binding.basis.complexTypeDefinition):
    """Financialinstrument81__4Specifies the characteristics of the assets held by the fund."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Financialinstrument81__4')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1499, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}AsstTp uses Python identifier AsstTp
    __AsstTp = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AsstTp'), 'AsstTp', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_Financialinstrument81__4_urnisostdiso20022techxsdDRAFT3auth_093_001_01AsstTp', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1505, 12), )

    
    AsstTp = property(__AsstTp.value, __AsstTp.set, None, 'AssetTypeSpecifies the type of financial assets.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}AsstId uses Python identifier AsstId
    __AsstId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AsstId'), 'AsstId', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_Financialinstrument81__4_urnisostdiso20022techxsdDRAFT3auth_093_001_01AsstId', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1511, 12), )

    
    AsstId = property(__AsstId.value, __AsstId.set, None, 'AssetIdentificationIdentification of the asset.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}AsstCtry uses Python identifier AsstCtry
    __AsstCtry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AsstCtry'), 'AsstCtry', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_Financialinstrument81__4_urnisostdiso20022techxsdDRAFT3auth_093_001_01AsstCtry', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1517, 12), )

    
    AsstCtry = property(__AsstCtry.value, __AsstCtry.set, None, 'AssetCountryCountry of the asset as considered relevant under the Regulation.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}AsstValtn uses Python identifier AsstValtn
    __AsstValtn = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AsstValtn'), 'AsstValtn', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_Financialinstrument81__4_urnisostdiso20022techxsdDRAFT3auth_093_001_01AsstValtn', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1523, 12), )

    
    AsstValtn = property(__AsstValtn.value, __AsstValtn.set, None, 'AssetValuationInformation on the valuation of the assets.')

    _ElementMap.update({
        __AsstTp.name() : __AsstTp,
        __AsstId.name() : __AsstId,
        __AsstCtry.name() : __AsstCtry,
        __AsstValtn.name() : __AsstValtn
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Financialinstrument81__4 = Financialinstrument81__4
Namespace.addCategoryObject('typeBinding', 'Financialinstrument81__4', Financialinstrument81__4)


# Complex type {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}Financialinstrument81__5 with content type ELEMENT_ONLY
class Financialinstrument81__5 (pyxb.binding.basis.complexTypeDefinition):
    """Financialinstrument81__5Specifies the characteristics of the assets held by the fund."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Financialinstrument81__5')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1531, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}AsstTp uses Python identifier AsstTp
    __AsstTp = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AsstTp'), 'AsstTp', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_Financialinstrument81__5_urnisostdiso20022techxsdDRAFT3auth_093_001_01AsstTp', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1537, 12), )

    
    AsstTp = property(__AsstTp.value, __AsstTp.set, None, 'AssetTypeSpecifies the type of financial assets.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}AsstId uses Python identifier AsstId
    __AsstId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AsstId'), 'AsstId', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_Financialinstrument81__5_urnisostdiso20022techxsdDRAFT3auth_093_001_01AsstId', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1543, 12), )

    
    AsstId = property(__AsstId.value, __AsstId.set, None, 'AssetIdentificationIdentification of the asset.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}PtyData uses Python identifier PtyData
    __PtyData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PtyData'), 'PtyData', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_Financialinstrument81__5_urnisostdiso20022techxsdDRAFT3auth_093_001_01PtyData', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1549, 12), )

    
    PtyData = property(__PtyData.value, __PtyData.set, None, 'PartyDataSpecifies further details of the party.\r\n')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}AsstCtry uses Python identifier AsstCtry
    __AsstCtry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AsstCtry'), 'AsstCtry', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_Financialinstrument81__5_urnisostdiso20022techxsdDRAFT3auth_093_001_01AsstCtry', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1556, 12), )

    
    AsstCtry = property(__AsstCtry.value, __AsstCtry.set, None, 'AssetCountryCountry of the asset as considered relevant under the Regulation.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}AsstValtn uses Python identifier AsstValtn
    __AsstValtn = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AsstValtn'), 'AsstValtn', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_Financialinstrument81__5_urnisostdiso20022techxsdDRAFT3auth_093_001_01AsstValtn', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1562, 12), )

    
    AsstValtn = property(__AsstValtn.value, __AsstValtn.set, None, 'AssetValuationInformation on the valuation of the assets.')

    _ElementMap.update({
        __AsstTp.name() : __AsstTp,
        __AsstId.name() : __AsstId,
        __PtyData.name() : __PtyData,
        __AsstCtry.name() : __AsstCtry,
        __AsstValtn.name() : __AsstValtn
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Financialinstrument81__5 = Financialinstrument81__5
Namespace.addCategoryObject('typeBinding', 'Financialinstrument81__5', Financialinstrument81__5)


# Complex type {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}Financialinstrument81__6 with content type ELEMENT_ONLY
class Financialinstrument81__6 (pyxb.binding.basis.complexTypeDefinition):
    """Financialinstrument81__6Specifies the characteristics of the assets held by the fund."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Financialinstrument81__6')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1570, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}AsstTp uses Python identifier AsstTp
    __AsstTp = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AsstTp'), 'AsstTp', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_Financialinstrument81__6_urnisostdiso20022techxsdDRAFT3auth_093_001_01AsstTp', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1576, 12), )

    
    AsstTp = property(__AsstTp.value, __AsstTp.set, None, 'AssetTypeSpecifies the type of financial assets.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}AsstId uses Python identifier AsstId
    __AsstId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AsstId'), 'AsstId', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_Financialinstrument81__6_urnisostdiso20022techxsdDRAFT3auth_093_001_01AsstId', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1582, 12), )

    
    AsstId = property(__AsstId.value, __AsstId.set, None, 'AssetIdentificationIdentification of the asset.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}PtyData uses Python identifier PtyData
    __PtyData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PtyData'), 'PtyData', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_Financialinstrument81__6_urnisostdiso20022techxsdDRAFT3auth_093_001_01PtyData', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1588, 12), )

    
    PtyData = property(__PtyData.value, __PtyData.set, None, 'PartyDataSpecifies further details of the party.\r\n')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}AsstCtry uses Python identifier AsstCtry
    __AsstCtry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AsstCtry'), 'AsstCtry', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_Financialinstrument81__6_urnisostdiso20022techxsdDRAFT3auth_093_001_01AsstCtry', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1595, 12), )

    
    AsstCtry = property(__AsstCtry.value, __AsstCtry.set, None, 'AssetCountryCountry of the asset as considered relevant under the Regulation.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}AsstValtn uses Python identifier AsstValtn
    __AsstValtn = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AsstValtn'), 'AsstValtn', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_Financialinstrument81__6_urnisostdiso20022techxsdDRAFT3auth_093_001_01AsstValtn', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1601, 12), )

    
    AsstValtn = property(__AsstValtn.value, __AsstValtn.set, None, 'AssetValuationInformation on the valuation of the assets.')

    _ElementMap.update({
        __AsstTp.name() : __AsstTp,
        __AsstId.name() : __AsstId,
        __PtyData.name() : __PtyData,
        __AsstCtry.name() : __AsstCtry,
        __AsstValtn.name() : __AsstValtn
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Financialinstrument81__6 = Financialinstrument81__6
Namespace.addCategoryObject('typeBinding', 'Financialinstrument81__6', Financialinstrument81__6)


# Complex type {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}ForeignExchangeTerms36__1 with content type ELEMENT_ONLY
class ForeignExchangeTerms36__1 (pyxb.binding.basis.complexTypeDefinition):
    """ForeignExchangeTerms36__1Information needed to process a currency exchange or conversion."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ForeignExchangeTerms36__1')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1665, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}UnitCcy uses Python identifier UnitCcy
    __UnitCcy = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'UnitCcy'), 'UnitCcy', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_ForeignExchangeTerms36__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01UnitCcy', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1671, 12), )

    
    UnitCcy = property(__UnitCcy.value, __UnitCcy.set, None, 'UnitCurrencyCurrency in which the rate of exchange is expressed in a currency exchange. In the example 1GBP = xxxCUR, the unit currency is GBP.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}QtdCcy uses Python identifier QtdCcy
    __QtdCcy = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'QtdCcy'), 'QtdCcy', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_ForeignExchangeTerms36__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01QtdCcy', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1677, 12), )

    
    QtdCcy = property(__QtdCcy.value, __QtdCcy.set, None, 'QuotedCurrencyCurrency into which the base currency is converted, in a currency exchange.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}XchgRate uses Python identifier XchgRate
    __XchgRate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'XchgRate'), 'XchgRate', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_ForeignExchangeTerms36__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01XchgRate', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1683, 12), )

    
    XchgRate = property(__XchgRate.value, __XchgRate.set, None, 'ExchangeRateThe value of one currency expressed in relation to another currency. ExchangeRate expresses the ratio between UnitCurrency and QuotedCurrency (ExchangeRate = UnitCurrency/QuotedCurrency).')

    _ElementMap.update({
        __UnitCcy.name() : __UnitCcy,
        __QtdCcy.name() : __QtdCcy,
        __XchgRate.name() : __XchgRate
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ForeignExchangeTerms36__1 = ForeignExchangeTerms36__1
Namespace.addCategoryObject('typeBinding', 'ForeignExchangeTerms36__1', ForeignExchangeTerms36__1)


# Complex type {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}FundLiquidity1__1 with content type ELEMENT_ONLY
class FundLiquidity1__1 (pyxb.binding.basis.complexTypeDefinition):
    """FundLiquidity1__1Specifies details of the liquidity indicators calculated for the money market fund."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'FundLiquidity1__1')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1691, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}DalyMtrgAsstRate uses Python identifier DalyMtrgAsstRate
    __DalyMtrgAsstRate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DalyMtrgAsstRate'), 'DalyMtrgAsstRate', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_FundLiquidity1__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01DalyMtrgAsstRate', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1697, 12), )

    
    DalyMtrgAsstRate = property(__DalyMtrgAsstRate.value, __DalyMtrgAsstRate.set, None, 'DailyMaturingAssetRateContains the percentage of assets held by the money market fund that are considered as daily maturing assets at the end of the reporting period.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}WklyMtrgAsstRate uses Python identifier WklyMtrgAsstRate
    __WklyMtrgAsstRate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'WklyMtrgAsstRate'), 'WklyMtrgAsstRate', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_FundLiquidity1__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01WklyMtrgAsstRate', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1703, 12), )

    
    WklyMtrgAsstRate = property(__WklyMtrgAsstRate.value, __WklyMtrgAsstRate.set, None, 'WeeklyMaturingAssetRateContains the percentage of assets held by the money market fund that are considered as weekly maturing assets at the end of the reporting period.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}PrtflLqdtyBrkdwn uses Python identifier PrtflLqdtyBrkdwn
    __PrtflLqdtyBrkdwn = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PrtflLqdtyBrkdwn'), 'PrtflLqdtyBrkdwn', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_FundLiquidity1__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01PrtflLqdtyBrkdwn', True, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1709, 12), )

    
    PrtflLqdtyBrkdwn = property(__PrtflLqdtyBrkdwn.value, __PrtflLqdtyBrkdwn.set, None, 'PortfolioLiquidityBreakdownSpecifies the percentage of total holdings capable of being liquidated within each time period.')

    _ElementMap.update({
        __DalyMtrgAsstRate.name() : __DalyMtrgAsstRate,
        __WklyMtrgAsstRate.name() : __WklyMtrgAsstRate,
        __PrtflLqdtyBrkdwn.name() : __PrtflLqdtyBrkdwn
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.FundLiquidity1__1 = FundLiquidity1__1
Namespace.addCategoryObject('typeBinding', 'FundLiquidity1__1', FundLiquidity1__1)


# Complex type {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}FundReportCancellation2__1 with content type ELEMENT_ONLY
class FundReportCancellation2__1 (pyxb.binding.basis.complexTypeDefinition):
    """FundReportCancellation2__1Specifies the attributes of the money market fund in case of a cancellation request."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'FundReportCancellation2__1')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1717, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}RptgYr uses Python identifier RptgYr
    __RptgYr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RptgYr'), 'RptgYr', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_FundReportCancellation2__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01RptgYr', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1723, 12), )

    
    RptgYr = property(__RptgYr.value, __RptgYr.set, None, 'ReportingYearYear the report relates to.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}RptgPrdFrToQrtr uses Python identifier RptgPrdFrToQrtr
    __RptgPrdFrToQrtr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RptgPrdFrToQrtr'), 'RptgPrdFrToQrtr', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_FundReportCancellation2__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01RptgPrdFrToQrtr', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1729, 12), )

    
    RptgPrdFrToQrtr = property(__RptgPrdFrToQrtr.value, __RptgPrdFrToQrtr.set, None, 'ReportingPeriodFromToQuarterQuarterly period range the report relates to.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}NtlRegnNb uses Python identifier NtlRegnNb
    __NtlRegnNb = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NtlRegnNb'), 'NtlRegnNb', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_FundReportCancellation2__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01NtlRegnNb', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1735, 12), )

    
    NtlRegnNb = property(__NtlRegnNb.value, __NtlRegnNb.set, None, 'NationalRegistrationNumberNumber assigned by a national registration authority to an entity.')

    _ElementMap.update({
        __RptgYr.name() : __RptgYr,
        __RptgPrdFrToQrtr.name() : __RptgPrdFrToQrtr,
        __NtlRegnNb.name() : __NtlRegnNb
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.FundReportCancellation2__1 = FundReportCancellation2__1
Namespace.addCategoryObject('typeBinding', 'FundReportCancellation2__1', FundReportCancellation2__1)


# Complex type {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}FundReportData1__1 with content type ELEMENT_ONLY
class FundReportData1__1 (pyxb.binding.basis.complexTypeDefinition):
    """FundReportData1__1Attributes defining money market fund report schema that are either new or have been corrected or have been invalidated."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'FundReportData1__1')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1743, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}Cxl uses Python identifier Cxl
    __Cxl = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Cxl'), 'Cxl', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_FundReportData1__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01Cxl', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1749, 12), )

    
    Cxl = property(__Cxl.value, __Cxl.set, None, 'CancellationSpecifies the attributes for the cancellation of the money market fund report.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}Upd uses Python identifier Upd
    __Upd = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Upd'), 'Upd', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_FundReportData1__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01Upd', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1755, 12), )

    
    Upd = property(__Upd.value, __Upd.set, None, 'UpdateSpecifies the attributes for the creation or correction of the money market fund report.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}ElmtJustfn uses Python identifier ElmtJustfn
    __ElmtJustfn = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ElmtJustfn'), 'ElmtJustfn', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_FundReportData1__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01ElmtJustfn', True, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1761, 12), )

    
    ElmtJustfn = property(__ElmtJustfn.value, __ElmtJustfn.set, None, 'ElementJustificationProvides additional information or justification such as the assumptions taken by the submitted entity for each reported item where the reporting entity considered it necessary or the justification for reporting not available value [NOTA].\r\n')

    _ElementMap.update({
        __Cxl.name() : __Cxl,
        __Upd.name() : __Upd,
        __ElmtJustfn.name() : __ElmtJustfn
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.FundReportData1__1 = FundReportData1__1
Namespace.addCategoryObject('typeBinding', 'FundReportData1__1', FundReportData1__1)


# Complex type {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}FundReportUpdate2__1 with content type ELEMENT_ONLY
class FundReportUpdate2__1 (pyxb.binding.basis.complexTypeDefinition):
    """FundReportUpdate2__1Specifies the attributes for the creation or correction of the money market fund report."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'FundReportUpdate2__1')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1770, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}RptgYr uses Python identifier RptgYr
    __RptgYr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RptgYr'), 'RptgYr', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_FundReportUpdate2__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01RptgYr', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1776, 12), )

    
    RptgYr = property(__RptgYr.value, __RptgYr.set, None, 'ReportingYearYear the report relates to.')

    _ElementMap.update({
        __RptgYr.name() : __RptgYr
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.FundReportUpdate2__1 = FundReportUpdate2__1
Namespace.addCategoryObject('typeBinding', 'FundReportUpdate2__1', FundReportUpdate2__1)


# Complex type {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}FundValuation1__1 with content type ELEMENT_ONLY
class FundValuation1__1 (pyxb.binding.basis.complexTypeDefinition):
    """FundValuation1__1Specifies details of the valuation calculated for the money market fund."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'FundValuation1__1')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1808, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}NetAsstValPerUnit uses Python identifier NetAsstValPerUnit
    __NetAsstValPerUnit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NetAsstValPerUnit'), 'NetAsstValPerUnit', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_FundValuation1__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01NetAsstValPerUnit', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1814, 12), )

    
    NetAsstValPerUnit = property(__NetAsstValPerUnit.value, __NetAsstValPerUnit.set, None, "NetAssetValuePerUnitValue at the end-of-period of all the holdings, less the fund's liabilities, attributable to a specific investment fund class calculated in accordance with mark-to-market or mark-to-model divided by the number of outstanding units or shares of the fund.")

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}WghtdAvrgMtrty uses Python identifier WghtdAvrgMtrty
    __WghtdAvrgMtrty = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'WghtdAvrgMtrty'), 'WghtdAvrgMtrty', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_FundValuation1__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01WghtdAvrgMtrty', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1820, 12), )

    
    WghtdAvrgMtrty = property(__WghtdAvrgMtrty.value, __WghtdAvrgMtrty.set, None, 'WeightedAverageMaturityContains the weighted average maturity of the fund (expressed in days).')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}WghtdAvrgLife uses Python identifier WghtdAvrgLife
    __WghtdAvrgLife = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'WghtdAvrgLife'), 'WghtdAvrgLife', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_FundValuation1__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01WghtdAvrgLife', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1826, 12), )

    
    WghtdAvrgLife = property(__WghtdAvrgLife.value, __WghtdAvrgLife.set, None, 'WeightedAverageLifeContains the weighted average life of the fund (expressed in days).')

    _ElementMap.update({
        __NetAsstValPerUnit.name() : __NetAsstValPerUnit,
        __WghtdAvrgMtrty.name() : __WghtdAvrgMtrty,
        __WghtdAvrgLife.name() : __WghtdAvrgLife
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.FundValuation1__1 = FundValuation1__1
Namespace.addCategoryObject('typeBinding', 'FundValuation1__1', FundValuation1__1)


# Complex type {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}GenericIdentification3__1 with content type ELEMENT_ONLY
class GenericIdentification3__1 (pyxb.binding.basis.complexTypeDefinition):
    """GenericIdentification3__1Information related to an identification, for example, party identification or account identification."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'GenericIdentification3__1')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1834, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}Id uses Python identifier Id
    __Id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Id'), 'Id', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_GenericIdentification3__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01Id', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1840, 12), )

    
    Id = property(__Id.value, __Id.set, None, 'IdentificationName or number assigned by an entity to enable recognition of that entity, for example, account identifier.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}Issr uses Python identifier Issr
    __Issr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Issr'), 'Issr', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_GenericIdentification3__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01Issr', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1846, 12), )

    
    Issr = property(__Issr.value, __Issr.set, None, 'IssuerEntity that assigns the identification.')

    _ElementMap.update({
        __Id.name() : __Id,
        __Issr.name() : __Issr
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.GenericIdentification3__1 = GenericIdentification3__1
Namespace.addCategoryObject('typeBinding', 'GenericIdentification3__1', GenericIdentification3__1)


# Complex type {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}GenericOrganisationIdentification1__1 with content type ELEMENT_ONLY
class GenericOrganisationIdentification1__1 (pyxb.binding.basis.complexTypeDefinition):
    """GenericOrganisationIdentification1__1Information related to an identification of an organisation."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'GenericOrganisationIdentification1__1')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1854, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}Id uses Python identifier Id
    __Id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Id'), 'Id', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_GenericOrganisationIdentification1__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01Id', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1860, 12), )

    
    Id = property(__Id.value, __Id.set, None, 'IdentificationIdentification assigned by an institution.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}Issr uses Python identifier Issr
    __Issr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Issr'), 'Issr', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_GenericOrganisationIdentification1__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01Issr', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1866, 12), )

    
    Issr = property(__Issr.value, __Issr.set, None, 'IssuerEntity that assigns the identification.')

    _ElementMap.update({
        __Id.name() : __Id,
        __Issr.name() : __Issr
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.GenericOrganisationIdentification1__1 = GenericOrganisationIdentification1__1
Namespace.addCategoryObject('typeBinding', 'GenericOrganisationIdentification1__1', GenericOrganisationIdentification1__1)


# Complex type {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}GenericOrganisationIdentification1__2 with content type ELEMENT_ONLY
class GenericOrganisationIdentification1__2 (pyxb.binding.basis.complexTypeDefinition):
    """GenericOrganisationIdentification1__2Information related to an identification of an organisation."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'GenericOrganisationIdentification1__2')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1874, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}Id uses Python identifier Id
    __Id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Id'), 'Id', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_GenericOrganisationIdentification1__2_urnisostdiso20022techxsdDRAFT3auth_093_001_01Id', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1880, 12), )

    
    Id = property(__Id.value, __Id.set, None, 'IdentificationIdentification assigned by an institution.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}Issr uses Python identifier Issr
    __Issr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Issr'), 'Issr', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_GenericOrganisationIdentification1__2_urnisostdiso20022techxsdDRAFT3auth_093_001_01Issr', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1886, 12), )

    
    Issr = property(__Issr.value, __Issr.set, None, 'IssuerEntity that assigns the identification.')

    _ElementMap.update({
        __Id.name() : __Id,
        __Issr.name() : __Issr
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.GenericOrganisationIdentification1__2 = GenericOrganisationIdentification1__2
Namespace.addCategoryObject('typeBinding', 'GenericOrganisationIdentification1__2', GenericOrganisationIdentification1__2)


# Complex type {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}GenericOrganisationIdentification1__3 with content type ELEMENT_ONLY
class GenericOrganisationIdentification1__3 (pyxb.binding.basis.complexTypeDefinition):
    """GenericOrganisationIdentification1__3Information related to an identification of an organisation."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'GenericOrganisationIdentification1__3')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1894, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}Id uses Python identifier Id
    __Id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Id'), 'Id', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_GenericOrganisationIdentification1__3_urnisostdiso20022techxsdDRAFT3auth_093_001_01Id', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1900, 12), )

    
    Id = property(__Id.value, __Id.set, None, 'IdentificationIdentification assigned by an institution.')

    _ElementMap.update({
        __Id.name() : __Id
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.GenericOrganisationIdentification1__3 = GenericOrganisationIdentification1__3
Namespace.addCategoryObject('typeBinding', 'GenericOrganisationIdentification1__3', GenericOrganisationIdentification1__3)


# Complex type {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}HoldingAsset3__1 with content type ELEMENT_ONLY
class HoldingAsset3__1 (pyxb.binding.basis.complexTypeDefinition):
    """HoldingAsset3__1Information on the assets held by the money market fund."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'HoldingAsset3__1')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1908, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}MnyMktInstrmHldg uses Python identifier MnyMktInstrmHldg
    __MnyMktInstrmHldg = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'MnyMktInstrmHldg'), 'MnyMktInstrmHldg', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_HoldingAsset3__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01MnyMktInstrmHldg', True, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1914, 12), )

    
    MnyMktInstrmHldg = property(__MnyMktInstrmHldg.value, __MnyMktInstrmHldg.set, None, 'MoneyMarketInstrumentHoldingProvides details on the money market instruments held by the fund.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}ScrtstnAsstBckdComrclPprHldg uses Python identifier ScrtstnAsstBckdComrclPprHldg
    __ScrtstnAsstBckdComrclPprHldg = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ScrtstnAsstBckdComrclPprHldg'), 'ScrtstnAsstBckdComrclPprHldg', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_HoldingAsset3__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01ScrtstnAsstBckdComrclPprHldg', True, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1920, 12), )

    
    ScrtstnAsstBckdComrclPprHldg = property(__ScrtstnAsstBckdComrclPprHldg.value, __ScrtstnAsstBckdComrclPprHldg.set, None, 'SecuritisationAssetBackedCommercialPaperHoldingProvides details on the securitisations and asset backed commercial papers held by the fund.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}DerivHldg uses Python identifier DerivHldg
    __DerivHldg = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DerivHldg'), 'DerivHldg', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_HoldingAsset3__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01DerivHldg', True, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1926, 12), )

    
    DerivHldg = property(__DerivHldg.value, __DerivHldg.set, None, 'DerivativeHoldingProvides details on the financial derivatives held by the fund.\r\n')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}MnyMktFndHldgInf uses Python identifier MnyMktFndHldgInf
    __MnyMktFndHldgInf = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'MnyMktFndHldgInf'), 'MnyMktFndHldgInf', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_HoldingAsset3__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01MnyMktFndHldgInf', True, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1933, 12), )

    
    MnyMktFndHldgInf = property(__MnyMktFndHldgInf.value, __MnyMktFndHldgInf.set, None, 'MoneyMarketFundHoldingInformationProvides details on the money market funds held by the fund.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}DpstAncllryLqdAsstHldg uses Python identifier DpstAncllryLqdAsstHldg
    __DpstAncllryLqdAsstHldg = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DpstAncllryLqdAsstHldg'), 'DpstAncllryLqdAsstHldg', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_HoldingAsset3__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01DpstAncllryLqdAsstHldg', True, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1939, 12), )

    
    DpstAncllryLqdAsstHldg = property(__DpstAncllryLqdAsstHldg.value, __DpstAncllryLqdAsstHldg.set, None, 'DepositAncillaryLiquidAssetHoldingProvides details on the deposits and ancillary liquid assets held by the fund.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}RpAgrmtHldg uses Python identifier RpAgrmtHldg
    __RpAgrmtHldg = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RpAgrmtHldg'), 'RpAgrmtHldg', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_HoldingAsset3__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01RpAgrmtHldg', True, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1945, 12), )

    
    RpAgrmtHldg = property(__RpAgrmtHldg.value, __RpAgrmtHldg.set, None, 'RepurchaseAgreementHoldingProvides details on the Repurchase agreements and reverse repurchase agreements held by the fund.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}RvsRpAgrmtCollData uses Python identifier RvsRpAgrmtCollData
    __RvsRpAgrmtCollData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RvsRpAgrmtCollData'), 'RvsRpAgrmtCollData', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_HoldingAsset3__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01RvsRpAgrmtCollData', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1951, 12), )

    
    RvsRpAgrmtCollData = property(__RvsRpAgrmtCollData.value, __RvsRpAgrmtCollData.set, None, 'ReverseRepurchaseAgreementCollateralDataInformation on the Collateral related to the reverse repurchase agreements.\r\n')

    _ElementMap.update({
        __MnyMktInstrmHldg.name() : __MnyMktInstrmHldg,
        __ScrtstnAsstBckdComrclPprHldg.name() : __ScrtstnAsstBckdComrclPprHldg,
        __DerivHldg.name() : __DerivHldg,
        __MnyMktFndHldgInf.name() : __MnyMktFndHldgInf,
        __DpstAncllryLqdAsstHldg.name() : __DpstAncllryLqdAsstHldg,
        __RpAgrmtHldg.name() : __RpAgrmtHldg,
        __RvsRpAgrmtCollData.name() : __RvsRpAgrmtCollData
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.HoldingAsset3__1 = HoldingAsset3__1
Namespace.addCategoryObject('typeBinding', 'HoldingAsset3__1', HoldingAsset3__1)


# Complex type {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}InstrumentIdentification3Choice__1 with content type ELEMENT_ONLY
class InstrumentIdentification3Choice__1 (pyxb.binding.basis.complexTypeDefinition):
    """InstrumentIdentification3Choice__1Choice between the ISIN, LEI, Unique Product Identifier and the name. ISIN is the preferred format."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'InstrumentIdentification3Choice__1')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1995, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}ISIN uses Python identifier ISIN
    __ISIN = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ISIN'), 'ISIN', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_InstrumentIdentification3Choice__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01ISIN', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2001, 12), )

    
    ISIN = property(__ISIN.value, __ISIN.set, None, "ISINInternational Securities Identification Number (ISIN).  A numbering system designed by the United Nation's International Organisation for Standardisation (ISO). The ISIN is composed of a 2-character prefix representing the country of issue, followed by the national security number (if one exists), and a check digit. Each country has a national numbering agency that assigns ISIN numbers for securities in that country.")

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}FullNm uses Python identifier FullNm
    __FullNm = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'FullNm'), 'FullNm', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_InstrumentIdentification3Choice__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01FullNm', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2007, 12), )

    
    FullNm = property(__FullNm.value, __FullNm.set, None, 'FullNameFull name or description of the financial instrument.')

    _ElementMap.update({
        __ISIN.name() : __ISIN,
        __FullNm.name() : __FullNm
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.InstrumentIdentification3Choice__1 = InstrumentIdentification3Choice__1
Namespace.addCategoryObject('typeBinding', 'InstrumentIdentification3Choice__1', InstrumentIdentification3Choice__1)


# Complex type {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}InstrumentIdentification4Choice__1 with content type ELEMENT_ONLY
class InstrumentIdentification4Choice__1 (pyxb.binding.basis.complexTypeDefinition):
    """InstrumentIdentification4Choice__1Choice between the ISIN, LEI, Unique Product Identifier and the name. ISIN is the preferred format."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'InstrumentIdentification4Choice__1')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2015, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}ISIN uses Python identifier ISIN
    __ISIN = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ISIN'), 'ISIN', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_InstrumentIdentification4Choice__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01ISIN', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2021, 12), )

    
    ISIN = property(__ISIN.value, __ISIN.set, None, "ISINInternational Securities Identification Number (ISIN).  A numbering system designed by the United Nation's International Organisation for Standardisation (ISO). The ISIN is composed of a 2-character prefix representing the country of issue, followed by the national security number (if one exists), and a check digit. Each country has a national numbering agency that assigns ISIN numbers for securities in that country.")

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}Nm uses Python identifier Nm
    __Nm = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Nm'), 'Nm', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_InstrumentIdentification4Choice__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01Nm', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2027, 12), )

    
    Nm = property(__Nm.value, __Nm.set, None, 'NameName or description of the financial instrument.')

    _ElementMap.update({
        __ISIN.name() : __ISIN,
        __Nm.name() : __Nm
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.InstrumentIdentification4Choice__1 = InstrumentIdentification4Choice__1
Namespace.addCategoryObject('typeBinding', 'InstrumentIdentification4Choice__1', InstrumentIdentification4Choice__1)


# Complex type {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}InstrumentIdentification4Choice__2 with content type ELEMENT_ONLY
class InstrumentIdentification4Choice__2 (pyxb.binding.basis.complexTypeDefinition):
    """InstrumentIdentification4Choice__2Choice between the ISIN, LEI, Unique Product Identifier and the name. ISIN is the preferred format."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'InstrumentIdentification4Choice__2')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2035, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}ISIN uses Python identifier ISIN
    __ISIN = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ISIN'), 'ISIN', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_InstrumentIdentification4Choice__2_urnisostdiso20022techxsdDRAFT3auth_093_001_01ISIN', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2041, 12), )

    
    ISIN = property(__ISIN.value, __ISIN.set, None, "ISINInternational Securities Identification Number (ISIN).  A numbering system designed by the United Nation's International Organisation for Standardisation (ISO). The ISIN is composed of a 2-character prefix representing the country of issue, followed by the national security number (if one exists), and a check digit. Each country has a national numbering agency that assigns ISIN numbers for securities in that country.")

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}UnqPdctIdr uses Python identifier UnqPdctIdr
    __UnqPdctIdr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'UnqPdctIdr'), 'UnqPdctIdr', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_InstrumentIdentification4Choice__2_urnisostdiso20022techxsdDRAFT3auth_093_001_01UnqPdctIdr', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2047, 12), )

    
    UnqPdctIdr = property(__UnqPdctIdr.value, __UnqPdctIdr.set, None, 'UniqueProductIdentifierIdentification through a unique product identifier.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}Nm uses Python identifier Nm
    __Nm = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Nm'), 'Nm', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_InstrumentIdentification4Choice__2_urnisostdiso20022techxsdDRAFT3auth_093_001_01Nm', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2053, 12), )

    
    Nm = property(__Nm.value, __Nm.set, None, 'NameName or description of the financial instrument.')

    _ElementMap.update({
        __ISIN.name() : __ISIN,
        __UnqPdctIdr.name() : __UnqPdctIdr,
        __Nm.name() : __Nm
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.InstrumentIdentification4Choice__2 = InstrumentIdentification4Choice__2
Namespace.addCategoryObject('typeBinding', 'InstrumentIdentification4Choice__2', InstrumentIdentification4Choice__2)


# Complex type {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}InstrumentIdentification4Choice__3 with content type ELEMENT_ONLY
class InstrumentIdentification4Choice__3 (pyxb.binding.basis.complexTypeDefinition):
    """InstrumentIdentification4Choice__3Choice between the ISIN, LEI, Unique Product Identifier and the name. ISIN is the preferred format."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'InstrumentIdentification4Choice__3')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2061, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}Nm uses Python identifier Nm
    __Nm = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Nm'), 'Nm', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_InstrumentIdentification4Choice__3_urnisostdiso20022techxsdDRAFT3auth_093_001_01Nm', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2067, 12), )

    
    Nm = property(__Nm.value, __Nm.set, None, 'NameName or description of the financial instrument.')

    _ElementMap.update({
        __Nm.name() : __Nm
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.InstrumentIdentification4Choice__3 = InstrumentIdentification4Choice__3
Namespace.addCategoryObject('typeBinding', 'InstrumentIdentification4Choice__3', InstrumentIdentification4Choice__3)


# Complex type {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}InvestorConcentration1__1 with content type ELEMENT_ONLY
class InvestorConcentration1__1 (pyxb.binding.basis.complexTypeDefinition):
    """InvestorConcentration1__1Information related to the investor concentration."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'InvestorConcentration1__1')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2075, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}RtlInvstrRate uses Python identifier RtlInvstrRate
    __RtlInvstrRate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RtlInvstrRate'), 'RtlInvstrRate', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_InvestorConcentration1__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01RtlInvstrRate', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2081, 12), )

    
    RtlInvstrRate = property(__RtlInvstrRate.value, __RtlInvstrRate.set, None, 'RetailInvestorRatePercentage of the net asset value held by professional investors when precise information is available.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}PrfssnlInvstrRate uses Python identifier PrfssnlInvstrRate
    __PrfssnlInvstrRate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PrfssnlInvstrRate'), 'PrfssnlInvstrRate', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_InvestorConcentration1__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01PrfssnlInvstrRate', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2087, 12), )

    
    PrfssnlInvstrRate = property(__PrfssnlInvstrRate.value, __PrfssnlInvstrRate.set, None, 'ProfessionalInvestorRatePercentage of the net asset value held by professional investors when precise information is available.')

    _ElementMap.update({
        __RtlInvstrRate.name() : __RtlInvstrRate,
        __PrfssnlInvstrRate.name() : __PrfssnlInvstrRate
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.InvestorConcentration1__1 = InvestorConcentration1__1
Namespace.addCategoryObject('typeBinding', 'InvestorConcentration1__1', InvestorConcentration1__1)


# Complex type {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}InvestorGroupBreakdownType2__1 with content type ELEMENT_ONLY
class InvestorGroupBreakdownType2__1 (pyxb.binding.basis.complexTypeDefinition):
    """InvestorGroupBreakdownType2__1Specifies the percentage of net asset value by investor group.
"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'InvestorGroupBreakdownType2__1')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2095, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}BkRate uses Python identifier BkRate
    __BkRate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'BkRate'), 'BkRate', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_InvestorGroupBreakdownType2__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01BkRate', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2102, 12), )

    
    BkRate = property(__BkRate.value, __BkRate.set, None, 'BankRateSpecifies the percentage of the net asset value by banks investor group.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}GnlGovntRate uses Python identifier GnlGovntRate
    __GnlGovntRate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'GnlGovntRate'), 'GnlGovntRate', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_InvestorGroupBreakdownType2__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01GnlGovntRate', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2108, 12), )

    
    GnlGovntRate = property(__GnlGovntRate.value, __GnlGovntRate.set, None, 'GeneralGovernmentRateSpecifies the percentage of the net asset value by general government investor group.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}HsHldRate uses Python identifier HsHldRate
    __HsHldRate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'HsHldRate'), 'HsHldRate', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_InvestorGroupBreakdownType2__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01HsHldRate', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2114, 12), )

    
    HsHldRate = property(__HsHldRate.value, __HsHldRate.set, None, 'HouseholdRateSpecifies the percentage of the net asset value by households investor group.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}InsrncCorptnRate uses Python identifier InsrncCorptnRate
    __InsrncCorptnRate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'InsrncCorptnRate'), 'InsrncCorptnRate', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_InvestorGroupBreakdownType2__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01InsrncCorptnRate', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2120, 12), )

    
    InsrncCorptnRate = property(__InsrncCorptnRate.value, __InsrncCorptnRate.set, None, 'InsuranceCorporationRateSpecifies the percentage of the net asset value by insurance corporation investor group.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}NonFinCorptnRate uses Python identifier NonFinCorptnRate
    __NonFinCorptnRate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NonFinCorptnRate'), 'NonFinCorptnRate', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_InvestorGroupBreakdownType2__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01NonFinCorptnRate', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2126, 12), )

    
    NonFinCorptnRate = property(__NonFinCorptnRate.value, __NonFinCorptnRate.set, None, 'NonFinancialCorporationRateSpecifies the percentage of the net asset value by non-financial corporations investor group.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}NonMnyMktFndInvstmtFndRate uses Python identifier NonMnyMktFndInvstmtFndRate
    __NonMnyMktFndInvstmtFndRate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NonMnyMktFndInvstmtFndRate'), 'NonMnyMktFndInvstmtFndRate', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_InvestorGroupBreakdownType2__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01NonMnyMktFndInvstmtFndRate', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2132, 12), )

    
    NonMnyMktFndInvstmtFndRate = property(__NonMnyMktFndInvstmtFndRate.value, __NonMnyMktFndInvstmtFndRate.set, None, 'NonMoneyMarketFundInvestmentFundRateSpecifies the percentage of the net asset value by other collective investment undertakings investor group.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}OthrFIRate uses Python identifier OthrFIRate
    __OthrFIRate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'OthrFIRate'), 'OthrFIRate', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_InvestorGroupBreakdownType2__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01OthrFIRate', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2138, 12), )

    
    OthrFIRate = property(__OthrFIRate.value, __OthrFIRate.set, None, 'OtherFinancialInstitutionRateSpecifies the percentage of the net asset value by other financial institution investor group.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}PnsnPlanOrFndRate uses Python identifier PnsnPlanOrFndRate
    __PnsnPlanOrFndRate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PnsnPlanOrFndRate'), 'PnsnPlanOrFndRate', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_InvestorGroupBreakdownType2__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01PnsnPlanOrFndRate', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2144, 12), )

    
    PnsnPlanOrFndRate = property(__PnsnPlanOrFndRate.value, __PnsnPlanOrFndRate.set, None, 'PensionPlanOrFundRateSpecifies the percentage of the net asset value by pension fund or funds investor group.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}UknwnRate uses Python identifier UknwnRate
    __UknwnRate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'UknwnRate'), 'UknwnRate', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_InvestorGroupBreakdownType2__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01UknwnRate', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2150, 12), )

    
    UknwnRate = property(__UknwnRate.value, __UknwnRate.set, None, 'UnknownRateSpecifies the percentage of the net asset value for unknown investor group.')

    _ElementMap.update({
        __BkRate.name() : __BkRate,
        __GnlGovntRate.name() : __GnlGovntRate,
        __HsHldRate.name() : __HsHldRate,
        __InsrncCorptnRate.name() : __InsrncCorptnRate,
        __NonFinCorptnRate.name() : __NonFinCorptnRate,
        __NonMnyMktFndInvstmtFndRate.name() : __NonMnyMktFndInvstmtFndRate,
        __OthrFIRate.name() : __OthrFIRate,
        __PnsnPlanOrFndRate.name() : __PnsnPlanOrFndRate,
        __UknwnRate.name() : __UknwnRate
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.InvestorGroupBreakdownType2__1 = InvestorGroupBreakdownType2__1
Namespace.addCategoryObject('typeBinding', 'InvestorGroupBreakdownType2__1', InvestorGroupBreakdownType2__1)


# Complex type {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}LegalFramework5Choice__1 with content type ELEMENT_ONLY
class LegalFramework5Choice__1 (pyxb.binding.basis.complexTypeDefinition):
    """LegalFramework5Choice__1Choice of format for the legal framework."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LegalFramework5Choice__1')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2187, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}Cd uses Python identifier Cd
    __Cd = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Cd'), 'Cd', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_LegalFramework5Choice__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01Cd', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2193, 12), )

    
    Cd = property(__Cd.value, __Cd.set, None, 'CodeSpecifies the legal framework, in a coded form.')

    _ElementMap.update({
        __Cd.name() : __Cd
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.LegalFramework5Choice__1 = LegalFramework5Choice__1
Namespace.addCategoryObject('typeBinding', 'LegalFramework5Choice__1', LegalFramework5Choice__1)


# Complex type {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}Liability1__1 with content type ELEMENT_ONLY
class Liability1__1 (pyxb.binding.basis.complexTypeDefinition):
    """Liability1__1Percentage of the net asset value held by retail investors."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Liability1__1')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2201, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}EstmtdRate uses Python identifier EstmtdRate
    __EstmtdRate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EstmtdRate'), 'EstmtdRate', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_Liability1__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01EstmtdRate', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2207, 12), )

    
    EstmtdRate = property(__EstmtdRate.value, __EstmtdRate.set, None, 'EstimatedRateEstimated percentage of the net asset value held by professional investors when no precise information is available.\r\n')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}PreciseRate uses Python identifier PreciseRate
    __PreciseRate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PreciseRate'), 'PreciseRate', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_Liability1__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01PreciseRate', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2214, 12), )

    
    PreciseRate = property(__PreciseRate.value, __PreciseRate.set, None, 'PreciseRatePercentage of the net asset value held by retail investors when precise information is available.\r\n')

    _ElementMap.update({
        __EstmtdRate.name() : __EstmtdRate,
        __PreciseRate.name() : __PreciseRate
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Liability1__1 = Liability1__1
Namespace.addCategoryObject('typeBinding', 'Liability1__1', Liability1__1)


# Complex type {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}LiabilityData3__1 with content type ELEMENT_ONLY
class LiabilityData3__1 (pyxb.binding.basis.complexTypeDefinition):
    """LiabilityData3__1Information related to the liabilities of the fund."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LiabilityData3__1')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2223, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}HghstBnfclOwnrRate uses Python identifier HghstBnfclOwnrRate
    __HghstBnfclOwnrRate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'HghstBnfclOwnrRate'), 'HghstBnfclOwnrRate', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_LiabilityData3__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01HghstBnfclOwnrRate', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2229, 12), )

    
    HghstBnfclOwnrRate = property(__HghstBnfclOwnrRate.value, __HghstBnfclOwnrRate.set, None, 'HighestBeneficialOwnerRatePercentage of the net asset value that is beneficially owned by the five highest beneficial owners.\r\n')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}InvstrCncntrtn uses Python identifier InvstrCncntrtn
    __InvstrCncntrtn = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'InvstrCncntrtn'), 'InvstrCncntrtn', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_LiabilityData3__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01InvstrCncntrtn', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2236, 12), )

    
    InvstrCncntrtn = property(__InvstrCncntrtn.value, __InvstrCncntrtn.set, None, 'InvestorConcentrationInformation related to the investor concentration.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}InvstrGrpBrkdwn uses Python identifier InvstrGrpBrkdwn
    __InvstrGrpBrkdwn = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'InvstrGrpBrkdwn'), 'InvstrGrpBrkdwn', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_LiabilityData3__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01InvstrGrpBrkdwn', True, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2242, 12), )

    
    InvstrGrpBrkdwn = property(__InvstrGrpBrkdwn.value, __InvstrGrpBrkdwn.set, None, 'InvestorGroupBreakdownSpecifies the rate of net asset value by type of investor group.\r\n')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}BrkdwnByCtry uses Python identifier BrkdwnByCtry
    __BrkdwnByCtry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'BrkdwnByCtry'), 'BrkdwnByCtry', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_LiabilityData3__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01BrkdwnByCtry', True, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2249, 12), )

    
    BrkdwnByCtry = property(__BrkdwnByCtry.value, __BrkdwnByCtry.set, None, 'BreakdownByCountrySpecifies the rate of net asset value by country of residence of investors.\r\n')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}RedDealgFrqcy uses Python identifier RedDealgFrqcy
    __RedDealgFrqcy = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RedDealgFrqcy'), 'RedDealgFrqcy', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_LiabilityData3__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01RedDealgFrqcy', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2256, 12), )

    
    RedDealgFrqcy = property(__RedDealgFrqcy.value, __RedDealgFrqcy.set, None, 'RedemptionDealingFrequencyFrequency at which the redemptions are done.\r\n')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}NtceDays uses Python identifier NtceDays
    __NtceDays = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NtceDays'), 'NtceDays', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_LiabilityData3__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01NtceDays', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2263, 12), )

    
    NtceDays = property(__NtceDays.value, __NtceDays.set, None, 'NoticeDaysNumber of notice in days that must be given by either the issuer or the holder before redemption can take place.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}BrkdwnByArrgmnt uses Python identifier BrkdwnByArrgmnt
    __BrkdwnByArrgmnt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'BrkdwnByArrgmnt'), 'BrkdwnByArrgmnt', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_LiabilityData3__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01BrkdwnByArrgmnt', True, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2269, 12), )

    
    BrkdwnByArrgmnt = property(__BrkdwnByArrgmnt.value, __BrkdwnByArrgmnt.set, None, 'BreakdownByArrangementSpecifies the net asset value by type of arrangement.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}OthrArrgmntAddtlInf uses Python identifier OthrArrgmntAddtlInf
    __OthrArrgmntAddtlInf = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'OthrArrgmntAddtlInf'), 'OthrArrgmntAddtlInf', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_LiabilityData3__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01OthrArrgmntAddtlInf', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2275, 12), )

    
    OthrArrgmntAddtlInf = property(__OthrArrgmntAddtlInf.value, __OthrArrgmntAddtlInf.set, None, 'OtherArrangementAdditionalInformationAdditional information about the other arrangement type.\r\n')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}MnthlyNetAsstValPerUnitInf uses Python identifier MnthlyNetAsstValPerUnitInf
    __MnthlyNetAsstValPerUnitInf = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'MnthlyNetAsstValPerUnitInf'), 'MnthlyNetAsstValPerUnitInf', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_LiabilityData3__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01MnthlyNetAsstValPerUnitInf', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2282, 12), )

    
    MnthlyNetAsstValPerUnitInf = property(__MnthlyNetAsstValPerUnitInf.value, __MnthlyNetAsstValPerUnitInf.set, None, 'MonthlyNetAssetValuePerUnitInformationInformation in relation with the net asset value per unit or share at the end of each month.\r\n')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}MnthlySbcptInf uses Python identifier MnthlySbcptInf
    __MnthlySbcptInf = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'MnthlySbcptInf'), 'MnthlySbcptInf', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_LiabilityData3__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01MnthlySbcptInf', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2289, 12), )

    
    MnthlySbcptInf = property(__MnthlySbcptInf.value, __MnthlySbcptInf.set, None, 'MonthlySubscriptionInformationInformation in relation with the subscription amounts at the end of each month.\r\n')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}MnthlyRedInf uses Python identifier MnthlyRedInf
    __MnthlyRedInf = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'MnthlyRedInf'), 'MnthlyRedInf', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_LiabilityData3__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01MnthlyRedInf', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2296, 12), )

    
    MnthlyRedInf = property(__MnthlyRedInf.value, __MnthlyRedInf.set, None, 'MonthlyRedemptionInformationInformation in relation with the redemption amounts at the end of each month.\r\n')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}MnthlyPmtToInvstrInf uses Python identifier MnthlyPmtToInvstrInf
    __MnthlyPmtToInvstrInf = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'MnthlyPmtToInvstrInf'), 'MnthlyPmtToInvstrInf', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_LiabilityData3__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01MnthlyPmtToInvstrInf', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2303, 12), )

    
    MnthlyPmtToInvstrInf = property(__MnthlyPmtToInvstrInf.value, __MnthlyPmtToInvstrInf.set, None, 'MonthlyPaymentToInvestorInformationInformation in relation with the payment-to-investors amounts at the end of each month.\r\n')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}MnthlyXchgRateInf uses Python identifier MnthlyXchgRateInf
    __MnthlyXchgRateInf = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'MnthlyXchgRateInf'), 'MnthlyXchgRateInf', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_LiabilityData3__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01MnthlyXchgRateInf', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2310, 12), )

    
    MnthlyXchgRateInf = property(__MnthlyXchgRateInf.value, __MnthlyXchgRateInf.set, None, 'MonthlyExchangeRateInformationInformation in relation with the foreign exchange rate of the last of each month.')

    _ElementMap.update({
        __HghstBnfclOwnrRate.name() : __HghstBnfclOwnrRate,
        __InvstrCncntrtn.name() : __InvstrCncntrtn,
        __InvstrGrpBrkdwn.name() : __InvstrGrpBrkdwn,
        __BrkdwnByCtry.name() : __BrkdwnByCtry,
        __RedDealgFrqcy.name() : __RedDealgFrqcy,
        __NtceDays.name() : __NtceDays,
        __BrkdwnByArrgmnt.name() : __BrkdwnByArrgmnt,
        __OthrArrgmntAddtlInf.name() : __OthrArrgmntAddtlInf,
        __MnthlyNetAsstValPerUnitInf.name() : __MnthlyNetAsstValPerUnitInf,
        __MnthlySbcptInf.name() : __MnthlySbcptInf,
        __MnthlyRedInf.name() : __MnthlyRedInf,
        __MnthlyPmtToInvstrInf.name() : __MnthlyPmtToInvstrInf,
        __MnthlyXchgRateInf.name() : __MnthlyXchgRateInf
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.LiabilityData3__1 = LiabilityData3__1
Namespace.addCategoryObject('typeBinding', 'LiabilityData3__1', LiabilityData3__1)


# Complex type {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}LowVolatilityNetAssetValueReportData2__1 with content type ELEMENT_ONLY
class LowVolatilityNetAssetValueReportData2__1 (pyxb.binding.basis.complexTypeDefinition):
    """LowVolatilityNetAssetValueReportData2__1Report schema for the low volatility net asset value money market fund."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LowVolatilityNetAssetValueReportData2__1')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2318, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}AmtsdCostMtdPricDvtnEvt uses Python identifier AmtsdCostMtdPricDvtnEvt
    __AmtsdCostMtdPricDvtnEvt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AmtsdCostMtdPricDvtnEvt'), 'AmtsdCostMtdPricDvtnEvt', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_LowVolatilityNetAssetValueReportData2__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01AmtsdCostMtdPricDvtnEvt', True, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2324, 12), )

    
    AmtsdCostMtdPricDvtnEvt = property(__AmtsdCostMtdPricDvtnEvt.value, __AmtsdCostMtdPricDvtnEvt.set, None, 'AmortisedCostMethodPriceDeviationEventDetails of the events where the price of an asset calculated in accordance with the mark-to-market or mark-to-model method deviates from the asset price calculated in accordance with the amortised cost method by more than 10 basis points.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}CstNetAsstValDvtnEvt uses Python identifier CstNetAsstValDvtnEvt
    __CstNetAsstValDvtnEvt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CstNetAsstValDvtnEvt'), 'CstNetAsstValDvtnEvt', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_LowVolatilityNetAssetValueReportData2__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01CstNetAsstValDvtnEvt', True, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2330, 12), )

    
    CstNetAsstValDvtnEvt = property(__CstNetAsstValDvtnEvt.value, __CstNetAsstValDvtnEvt.set, None, 'ConstantNetAssetValueDeviationEventDetails of the events where the constant net asset value per unit or share calculated in accordance with the amortised cost method deviates from the net asset value per unit or share calculated in accordance with the mark-to-market or mark-to-model method by more than 20 basis points.\r\n\r\n')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}MtrgAsstThrshldEvt uses Python identifier MtrgAsstThrshldEvt
    __MtrgAsstThrshldEvt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'MtrgAsstThrshldEvt'), 'MtrgAsstThrshldEvt', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_LowVolatilityNetAssetValueReportData2__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01MtrgAsstThrshldEvt', True, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2338, 12), )

    
    MtrgAsstThrshldEvt = property(__MtrgAsstThrshldEvt.value, __MtrgAsstThrshldEvt.set, None, 'MaturingAssetThresholdEventDetails of the events where the fund is not compliant with the weekly liquidity thresholds applicable to public debt constant net asset value money market funds or the low volatility net asset value money market funds.\r\n')

    _ElementMap.update({
        __AmtsdCostMtdPricDvtnEvt.name() : __AmtsdCostMtdPricDvtnEvt,
        __CstNetAsstValDvtnEvt.name() : __CstNetAsstValDvtnEvt,
        __MtrgAsstThrshldEvt.name() : __MtrgAsstThrshldEvt
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.LowVolatilityNetAssetValueReportData2__1 = LowVolatilityNetAssetValueReportData2__1
Namespace.addCategoryObject('typeBinding', 'LowVolatilityNetAssetValueReportData2__1', LowVolatilityNetAssetValueReportData2__1)


# Complex type {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}MarketSpecificAttribute1 with content type ELEMENT_ONLY
class MarketSpecificAttribute1 (pyxb.binding.basis.complexTypeDefinition):
    """MarketSpecificAttribute1Defines additional attributes for party reference schema."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MarketSpecificAttribute1')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2347, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}Nm uses Python identifier Nm
    __Nm = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Nm'), 'Nm', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_MarketSpecificAttribute1_urnisostdiso20022techxsdDRAFT3auth_093_001_01Nm', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2353, 12), )

    
    Nm = property(__Nm.value, __Nm.set, None, 'NameSpecifies the name of the market-specific attribute.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}Val uses Python identifier Val
    __Val = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Val'), 'Val', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_MarketSpecificAttribute1_urnisostdiso20022techxsdDRAFT3auth_093_001_01Val', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2359, 12), )

    
    Val = property(__Val.value, __Val.set, None, 'ValueSpecifies the value of the market-specific attribute.')

    _ElementMap.update({
        __Nm.name() : __Nm,
        __Val.name() : __Val
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.MarketSpecificAttribute1 = MarketSpecificAttribute1
Namespace.addCategoryObject('typeBinding', 'MarketSpecificAttribute1', MarketSpecificAttribute1)


# Complex type {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}MaturingAssetThresholdEvent2 with content type ELEMENT_ONLY
class MaturingAssetThresholdEvent2 (pyxb.binding.basis.complexTypeDefinition):
    """MaturingAssetThresholdEvent2Details of the events where the fund is not compliant with the weekly liquidity thresholds applicable to public debt constant net asset value money market funds or the low volatility net asset value money market funds."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MaturingAssetThresholdEvent2')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2393, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}EvtDt uses Python identifier EvtDt
    __EvtDt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EvtDt'), 'EvtDt', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_MaturingAssetThresholdEvent2_urnisostdiso20022techxsdDRAFT3auth_093_001_01EvtDt', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2399, 12), )

    
    EvtDt = property(__EvtDt.value, __EvtDt.set, None, 'EventDateDate on which the reportable event took place.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}MeasrDt uses Python identifier MeasrDt
    __MeasrDt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'MeasrDt'), 'MeasrDt', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_MaturingAssetThresholdEvent2_urnisostdiso20022techxsdDRAFT3auth_093_001_01MeasrDt', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2405, 12), )

    
    MeasrDt = property(__MeasrDt.value, __MeasrDt.set, None, 'MeasureDateDate on which the decided measure was taken.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}MeasrInf uses Python identifier MeasrInf
    __MeasrInf = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'MeasrInf'), 'MeasrInf', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_MaturingAssetThresholdEvent2_urnisostdiso20022techxsdDRAFT3auth_093_001_01MeasrInf', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2411, 12), )

    
    MeasrInf = property(__MeasrInf.value, __MeasrInf.set, None, 'MeasureInformationDetails on the measures decided by the board in case of non-compliance with the weekly liquidity thresholds applicable to public debt constant net asset value money market funds and low volatility net asset value money market funds.')

    _ElementMap.update({
        __EvtDt.name() : __EvtDt,
        __MeasrDt.name() : __MeasrDt,
        __MeasrInf.name() : __MeasrInf
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.MaturingAssetThresholdEvent2 = MaturingAssetThresholdEvent2
Namespace.addCategoryObject('typeBinding', 'MaturingAssetThresholdEvent2', MaturingAssetThresholdEvent2)


# Complex type {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}Measure2Choice with content type ELEMENT_ONLY
class Measure2Choice (pyxb.binding.basis.complexTypeDefinition):
    """Measure2ChoiceDetails on the measures decided by the board in case of non compliance with the weekly liquidity thresholds applicable to public debt constant net asset value money market funds and low volatility net asset value money market funds."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Measure2Choice')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2491, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}FrstMeasrTp uses Python identifier FrstMeasrTp
    __FrstMeasrTp = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'FrstMeasrTp'), 'FrstMeasrTp', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_Measure2Choice_urnisostdiso20022techxsdDRAFT3auth_093_001_01FrstMeasrTp', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2497, 12), )

    
    FrstMeasrTp = property(__FrstMeasrTp.value, __FrstMeasrTp.set, None, 'FirstMeasureTypeDefines the type of decision applied by the board in relation with the proportion of weekly maturing assets that is falling down below 30 % of its total assets whereas the net daily redemptions on a single working day exceed 10 % of total assets.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}ScndMeasrTp uses Python identifier ScndMeasrTp
    __ScndMeasrTp = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ScndMeasrTp'), 'ScndMeasrTp', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_Measure2Choice_urnisostdiso20022techxsdDRAFT3auth_093_001_01ScndMeasrTp', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2503, 12), )

    
    ScndMeasrTp = property(__ScndMeasrTp.value, __ScndMeasrTp.set, None, 'SecondMeasureTypeDefines the type of decision applied by the board in relation with the proportion of weekly maturing assets that is falling down below 10 % of its total assets.\r\n')

    _ElementMap.update({
        __FrstMeasrTp.name() : __FrstMeasrTp,
        __ScndMeasrTp.name() : __ScndMeasrTp
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Measure2Choice = Measure2Choice
Namespace.addCategoryObject('typeBinding', 'Measure2Choice', Measure2Choice)


# Complex type {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}MoneyMarketFundReportV01 with content type ELEMENT_ONLY
class MoneyMarketFundReportV01 (pyxb.binding.basis.complexTypeDefinition):
    """MoneyMarketFundReportV01The MoneyMarketFundReport message is sent by the reporting agent to the relevant competent authority of the money market fund, to report quarterly or yearly activity details of the money market fund.

"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MoneyMarketFundReportV01')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2512, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}FndRpt uses Python identifier FndRpt
    __FndRpt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'FndRpt'), 'FndRpt', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_MoneyMarketFundReportV01_urnisostdiso20022techxsdDRAFT3auth_093_001_01FndRpt', True, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2520, 12), )

    
    FndRpt = property(__FndRpt.value, __FndRpt.set, None, 'FundReportSpecifies the attributes for the creation, correction or cancellation of the money market fund report.')

    _ElementMap.update({
        __FndRpt.name() : __FndRpt
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.MoneyMarketFundReportV01 = MoneyMarketFundReportV01
Namespace.addCategoryObject('typeBinding', 'MoneyMarketFundReportV01', MoneyMarketFundReportV01)


# Complex type {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}MoneyMarketFundType1Choice__1 with content type ELEMENT_ONLY
class MoneyMarketFundType1Choice__1 (pyxb.binding.basis.complexTypeDefinition):
    """MoneyMarketFundType1Choice__1Choice of format between a code and a proprietary code."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MoneyMarketFundType1Choice__1')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2528, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}Cd uses Python identifier Cd
    __Cd = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Cd'), 'Cd', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_MoneyMarketFundType1Choice__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01Cd', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2534, 12), )

    
    Cd = property(__Cd.value, __Cd.set, None, 'CodeSpecifies the type of the money market fund.')

    _ElementMap.update({
        __Cd.name() : __Cd
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.MoneyMarketFundType1Choice__1 = MoneyMarketFundType1Choice__1
Namespace.addCategoryObject('typeBinding', 'MoneyMarketFundType1Choice__1', MoneyMarketFundType1Choice__1)


# Complex type {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}MonthType3__1 with content type ELEMENT_ONLY
class MonthType3__1 (pyxb.binding.basis.complexTypeDefinition):
    """MonthType3__1Information related with the months of the reporting period.
"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MonthType3__1')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2575, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}Mnth uses Python identifier Mnth
    __Mnth = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Mnth'), 'Mnth', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_MonthType3__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01Mnth', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2582, 12), )

    
    Mnth = property(__Mnth.value, __Mnth.set, None, 'MonthInformation is related to one of the three months of the reporting quarter.\r\n')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}Val uses Python identifier Val
    __Val = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Val'), 'Val', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_MonthType3__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01Val', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2589, 12), )

    
    Val = property(__Val.value, __Val.set, None, 'ValueValue expressed in the reporting currency for each month of the reporting period.\r\n')

    _ElementMap.update({
        __Mnth.name() : __Mnth,
        __Val.name() : __Val
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.MonthType3__1 = MonthType3__1
Namespace.addCategoryObject('typeBinding', 'MonthType3__1', MonthType3__1)


# Complex type {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}MonthType3__2 with content type ELEMENT_ONLY
class MonthType3__2 (pyxb.binding.basis.complexTypeDefinition):
    """MonthType3__2Information related with the months of the reporting period.
"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MonthType3__2')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2598, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}Mnth uses Python identifier Mnth
    __Mnth = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Mnth'), 'Mnth', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_MonthType3__2_urnisostdiso20022techxsdDRAFT3auth_093_001_01Mnth', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2605, 12), )

    
    Mnth = property(__Mnth.value, __Mnth.set, None, 'MonthInformation is related to one of the three months of the reporting quarter.\r\n')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}Val uses Python identifier Val
    __Val = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Val'), 'Val', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_MonthType3__2_urnisostdiso20022techxsdDRAFT3auth_093_001_01Val', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2612, 12), )

    
    Val = property(__Val.value, __Val.set, None, 'ValueValue expressed in the reporting currency for each month of the reporting period.\r\n')

    _ElementMap.update({
        __Mnth.name() : __Mnth,
        __Val.name() : __Val
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.MonthType3__2 = MonthType3__2
Namespace.addCategoryObject('typeBinding', 'MonthType3__2', MonthType3__2)


# Complex type {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}MonthType3__3 with content type ELEMENT_ONLY
class MonthType3__3 (pyxb.binding.basis.complexTypeDefinition):
    """MonthType3__3Information related with the months of the reporting period.
"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MonthType3__3')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2621, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}Mnth uses Python identifier Mnth
    __Mnth = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Mnth'), 'Mnth', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_MonthType3__3_urnisostdiso20022techxsdDRAFT3auth_093_001_01Mnth', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2628, 12), )

    
    Mnth = property(__Mnth.value, __Mnth.set, None, 'MonthInformation is related to one of the three months of the reporting quarter.\r\n')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}Val uses Python identifier Val
    __Val = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Val'), 'Val', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_MonthType3__3_urnisostdiso20022techxsdDRAFT3auth_093_001_01Val', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2635, 12), )

    
    Val = property(__Val.value, __Val.set, None, 'ValueValue expressed in the reporting currency for each month of the reporting period.\r\n')

    _ElementMap.update({
        __Mnth.name() : __Mnth,
        __Val.name() : __Val
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.MonthType3__3 = MonthType3__3
Namespace.addCategoryObject('typeBinding', 'MonthType3__3', MonthType3__3)


# Complex type {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}MonthType3__4 with content type ELEMENT_ONLY
class MonthType3__4 (pyxb.binding.basis.complexTypeDefinition):
    """MonthType3__4Information related with the months of the reporting period.
"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MonthType3__4')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2644, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}Mnth uses Python identifier Mnth
    __Mnth = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Mnth'), 'Mnth', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_MonthType3__4_urnisostdiso20022techxsdDRAFT3auth_093_001_01Mnth', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2651, 12), )

    
    Mnth = property(__Mnth.value, __Mnth.set, None, 'MonthInformation is related to one of the three months of the reporting quarter.\r\n')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}Val uses Python identifier Val
    __Val = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Val'), 'Val', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_MonthType3__4_urnisostdiso20022techxsdDRAFT3auth_093_001_01Val', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2658, 12), )

    
    Val = property(__Val.value, __Val.set, None, 'ValueValue expressed in the reporting currency for each month of the reporting period.\r\n')

    _ElementMap.update({
        __Mnth.name() : __Mnth,
        __Val.name() : __Val
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.MonthType3__4 = MonthType3__4
Namespace.addCategoryObject('typeBinding', 'MonthType3__4', MonthType3__4)


# Complex type {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}MonthType3__5 with content type ELEMENT_ONLY
class MonthType3__5 (pyxb.binding.basis.complexTypeDefinition):
    """MonthType3__5Information related with the months of the reporting period.
"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MonthType3__5')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2667, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}Mnth uses Python identifier Mnth
    __Mnth = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Mnth'), 'Mnth', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_MonthType3__5_urnisostdiso20022techxsdDRAFT3auth_093_001_01Mnth', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2674, 12), )

    
    Mnth = property(__Mnth.value, __Mnth.set, None, 'MonthInformation is related to one of the three months of the reporting quarter.\r\n')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}Val uses Python identifier Val
    __Val = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Val'), 'Val', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_MonthType3__5_urnisostdiso20022techxsdDRAFT3auth_093_001_01Val', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2681, 12), )

    
    Val = property(__Val.value, __Val.set, None, 'ValueValue expressed in the reporting currency for each month of the reporting period.\r\n')

    _ElementMap.update({
        __Mnth.name() : __Mnth,
        __Val.name() : __Val
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.MonthType3__5 = MonthType3__5
Namespace.addCategoryObject('typeBinding', 'MonthType3__5', MonthType3__5)


# Complex type {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}MonthType3__6 with content type ELEMENT_ONLY
class MonthType3__6 (pyxb.binding.basis.complexTypeDefinition):
    """MonthType3__6Information related with the months of the reporting period.
"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MonthType3__6')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2690, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}Mnth uses Python identifier Mnth
    __Mnth = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Mnth'), 'Mnth', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_MonthType3__6_urnisostdiso20022techxsdDRAFT3auth_093_001_01Mnth', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2697, 12), )

    
    Mnth = property(__Mnth.value, __Mnth.set, None, 'MonthInformation is related to one of the three months of the reporting quarter.\r\n')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}Val uses Python identifier Val
    __Val = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Val'), 'Val', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_MonthType3__6_urnisostdiso20022techxsdDRAFT3auth_093_001_01Val', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2704, 12), )

    
    Val = property(__Val.value, __Val.set, None, 'ValueValue expressed in the reporting currency for each month of the reporting period.\r\n')

    _ElementMap.update({
        __Mnth.name() : __Mnth,
        __Val.name() : __Val
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.MonthType3__6 = MonthType3__6
Namespace.addCategoryObject('typeBinding', 'MonthType3__6', MonthType3__6)


# Complex type {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}MonthType3__7 with content type ELEMENT_ONLY
class MonthType3__7 (pyxb.binding.basis.complexTypeDefinition):
    """MonthType3__7Information related with the months of the reporting period.
"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MonthType3__7')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2713, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}Mnth uses Python identifier Mnth
    __Mnth = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Mnth'), 'Mnth', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_MonthType3__7_urnisostdiso20022techxsdDRAFT3auth_093_001_01Mnth', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2720, 12), )

    
    Mnth = property(__Mnth.value, __Mnth.set, None, 'MonthInformation is related to one of the three months of the reporting quarter.\r\n')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}Val uses Python identifier Val
    __Val = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Val'), 'Val', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_MonthType3__7_urnisostdiso20022techxsdDRAFT3auth_093_001_01Val', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2727, 12), )

    
    Val = property(__Val.value, __Val.set, None, 'ValueValue expressed in the reporting currency for each month of the reporting period.\r\n')

    _ElementMap.update({
        __Mnth.name() : __Mnth,
        __Val.name() : __Val
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.MonthType3__7 = MonthType3__7
Namespace.addCategoryObject('typeBinding', 'MonthType3__7', MonthType3__7)


# Complex type {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}MonthType3__8 with content type ELEMENT_ONLY
class MonthType3__8 (pyxb.binding.basis.complexTypeDefinition):
    """MonthType3__8Information related with the months of the reporting period.
"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MonthType3__8')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2736, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}Mnth uses Python identifier Mnth
    __Mnth = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Mnth'), 'Mnth', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_MonthType3__8_urnisostdiso20022techxsdDRAFT3auth_093_001_01Mnth', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2743, 12), )

    
    Mnth = property(__Mnth.value, __Mnth.set, None, 'MonthInformation is related to one of the three months of the reporting quarter.\r\n')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}Val uses Python identifier Val
    __Val = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Val'), 'Val', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_MonthType3__8_urnisostdiso20022techxsdDRAFT3auth_093_001_01Val', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2750, 12), )

    
    Val = property(__Val.value, __Val.set, None, 'ValueValue expressed in the reporting currency for each month of the reporting period.\r\n')

    _ElementMap.update({
        __Mnth.name() : __Mnth,
        __Val.name() : __Val
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.MonthType3__8 = MonthType3__8
Namespace.addCategoryObject('typeBinding', 'MonthType3__8', MonthType3__8)


# Complex type {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}MonthValue2__1 with content type ELEMENT_ONLY
class MonthValue2__1 (pyxb.binding.basis.complexTypeDefinition):
    """MonthValue2__1Information in relation with a value or an exchange rate at the end of each month for one or several quarters."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MonthValue2__1')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2759, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}FrstQrtr uses Python identifier FrstQrtr
    __FrstQrtr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'FrstQrtr'), 'FrstQrtr', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_MonthValue2__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01FrstQrtr', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2765, 12), )

    
    FrstQrtr = property(__FrstQrtr.value, __FrstQrtr.set, None, 'FirstQuarterInformation is related with the full year period.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}ScndQrtr uses Python identifier ScndQrtr
    __ScndQrtr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ScndQrtr'), 'ScndQrtr', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_MonthValue2__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01ScndQrtr', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2771, 12), )

    
    ScndQrtr = property(__ScndQrtr.value, __ScndQrtr.set, None, 'SecondQuarterInformation is related with one quarter of the year.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}ThrdQrtr uses Python identifier ThrdQrtr
    __ThrdQrtr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ThrdQrtr'), 'ThrdQrtr', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_MonthValue2__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01ThrdQrtr', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2777, 12), )

    
    ThrdQrtr = property(__ThrdQrtr.value, __ThrdQrtr.set, None, 'ThirdQuarterInformation is related with the first half-year period.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}FrthQrtr uses Python identifier FrthQrtr
    __FrthQrtr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'FrthQrtr'), 'FrthQrtr', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_MonthValue2__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01FrthQrtr', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2783, 12), )

    
    FrthQrtr = property(__FrthQrtr.value, __FrthQrtr.set, None, 'FourthQuarterInformation is related with the second half-year period.')

    _ElementMap.update({
        __FrstQrtr.name() : __FrstQrtr,
        __ScndQrtr.name() : __ScndQrtr,
        __ThrdQrtr.name() : __ThrdQrtr,
        __FrthQrtr.name() : __FrthQrtr
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.MonthValue2__1 = MonthValue2__1
Namespace.addCategoryObject('typeBinding', 'MonthValue2__1', MonthValue2__1)


# Complex type {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}MonthValue2__2 with content type ELEMENT_ONLY
class MonthValue2__2 (pyxb.binding.basis.complexTypeDefinition):
    """MonthValue2__2Information in relation with a value or an exchange rate at the end of each month for one or several quarters."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MonthValue2__2')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2791, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}FrstQrtr uses Python identifier FrstQrtr
    __FrstQrtr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'FrstQrtr'), 'FrstQrtr', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_MonthValue2__2_urnisostdiso20022techxsdDRAFT3auth_093_001_01FrstQrtr', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2797, 12), )

    
    FrstQrtr = property(__FrstQrtr.value, __FrstQrtr.set, None, 'FirstQuarterInformation is related with the full year period.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}ScndQrtr uses Python identifier ScndQrtr
    __ScndQrtr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ScndQrtr'), 'ScndQrtr', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_MonthValue2__2_urnisostdiso20022techxsdDRAFT3auth_093_001_01ScndQrtr', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2803, 12), )

    
    ScndQrtr = property(__ScndQrtr.value, __ScndQrtr.set, None, 'SecondQuarterInformation is related with one quarter of the year.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}ThrdQrtr uses Python identifier ThrdQrtr
    __ThrdQrtr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ThrdQrtr'), 'ThrdQrtr', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_MonthValue2__2_urnisostdiso20022techxsdDRAFT3auth_093_001_01ThrdQrtr', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2809, 12), )

    
    ThrdQrtr = property(__ThrdQrtr.value, __ThrdQrtr.set, None, 'ThirdQuarterInformation is related with the first half-year period.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}FrthQrtr uses Python identifier FrthQrtr
    __FrthQrtr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'FrthQrtr'), 'FrthQrtr', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_MonthValue2__2_urnisostdiso20022techxsdDRAFT3auth_093_001_01FrthQrtr', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2815, 12), )

    
    FrthQrtr = property(__FrthQrtr.value, __FrthQrtr.set, None, 'FourthQuarterInformation is related with the second half-year period.')

    _ElementMap.update({
        __FrstQrtr.name() : __FrstQrtr,
        __ScndQrtr.name() : __ScndQrtr,
        __ThrdQrtr.name() : __ThrdQrtr,
        __FrthQrtr.name() : __FrthQrtr
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.MonthValue2__2 = MonthValue2__2
Namespace.addCategoryObject('typeBinding', 'MonthValue2__2', MonthValue2__2)


# Complex type {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}MonthlyValue2Choice__1 with content type ELEMENT_ONLY
class MonthlyValue2Choice__1 (pyxb.binding.basis.complexTypeDefinition):
    """MonthlyValue2Choice__1Value for the end-of-month. Choice between a value or the foreign exchange details used to compute other values."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MonthlyValue2Choice__1')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2823, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}Val uses Python identifier Val
    __Val = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Val'), 'Val', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_MonthlyValue2Choice__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01Val', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2829, 12), )

    
    Val = property(__Val.value, __Val.set, None, 'ValueValue expressed in the reporting currency at the end-of-month for the net asset value, the redemptions, the subscriptions, the payment to investors.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}NotAvlblVal uses Python identifier NotAvlblVal
    __NotAvlblVal = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NotAvlblVal'), 'NotAvlblVal', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_MonthlyValue2Choice__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01NotAvlblVal', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2835, 12), )

    
    NotAvlblVal = property(__NotAvlblVal.value, __NotAvlblVal.set, None, 'NotAvailableValueThe value is not available.')

    _ElementMap.update({
        __Val.name() : __Val,
        __NotAvlblVal.name() : __NotAvlblVal
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.MonthlyValue2Choice__1 = MonthlyValue2Choice__1
Namespace.addCategoryObject('typeBinding', 'MonthlyValue2Choice__1', MonthlyValue2Choice__1)


# Complex type {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}MonthlyValue2Choice__2 with content type ELEMENT_ONLY
class MonthlyValue2Choice__2 (pyxb.binding.basis.complexTypeDefinition):
    """MonthlyValue2Choice__2Value for the end-of-month. Choice between a value or the foreign exchange details used to compute other values."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MonthlyValue2Choice__2')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2843, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}FX uses Python identifier FX
    __FX = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'FX'), 'FX', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_MonthlyValue2Choice__2_urnisostdiso20022techxsdDRAFT3auth_093_001_01FX', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2849, 12), )

    
    FX = property(__FX.value, __FX.set, None, 'ForeignExchangeInformation needed to process a currency exchange or conversion.\r\n')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}NotAvlblVal uses Python identifier NotAvlblVal
    __NotAvlblVal = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NotAvlblVal'), 'NotAvlblVal', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_MonthlyValue2Choice__2_urnisostdiso20022techxsdDRAFT3auth_093_001_01NotAvlblVal', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2856, 12), )

    
    NotAvlblVal = property(__NotAvlblVal.value, __NotAvlblVal.set, None, 'NotAvailableValueThe value is not available.')

    _ElementMap.update({
        __FX.name() : __FX,
        __NotAvlblVal.name() : __NotAvlblVal
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.MonthlyValue2Choice__2 = MonthlyValue2Choice__2
Namespace.addCategoryObject('typeBinding', 'MonthlyValue2Choice__2', MonthlyValue2Choice__2)


# Complex type {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}OutflowImpact1 with content type ELEMENT_ONLY
class OutflowImpact1 (pyxb.binding.basis.complexTypeDefinition):
    """OutflowImpact1Weekly outflows derived from the monthly outflows compared with available weekly liquid assets, considered as the sum of highly liquid assets and weekly maturing assets. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'OutflowImpact1')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2921, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}FrstBcktOutflwRate uses Python identifier FrstBcktOutflwRate
    __FrstBcktOutflwRate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'FrstBcktOutflwRate'), 'FrstBcktOutflwRate', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_OutflowImpact1_urnisostdiso20022techxsdDRAFT3auth_093_001_01FrstBcktOutflwRate', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2927, 12), )

    
    FrstBcktOutflwRate = property(__FrstBcktOutflwRate.value, __FrstBcktOutflwRate.set, None, 'FirstBucketOutflowRateWeekly outflows derived from the monthly outflows compared with available weekly liquid assets, considered as the sum of highly liquid assets and weekly maturing assets. Rate computed for assets considered in the first bucket according to the Regulation.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}ScndBcktOutflwRate uses Python identifier ScndBcktOutflwRate
    __ScndBcktOutflwRate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ScndBcktOutflwRate'), 'ScndBcktOutflwRate', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_OutflowImpact1_urnisostdiso20022techxsdDRAFT3auth_093_001_01ScndBcktOutflwRate', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2933, 12), )

    
    ScndBcktOutflwRate = property(__ScndBcktOutflwRate.value, __ScndBcktOutflwRate.set, None, 'SecondBucketOutflowRateWeekly outflows derived from the monthly outflows compared with available weekly liquid assets, considered as the sum of highly liquid assets and weekly maturing assets. Rate computed for assets considered in the second bucket according to the Regulation.')

    _ElementMap.update({
        __FrstBcktOutflwRate.name() : __FrstBcktOutflwRate,
        __ScndBcktOutflwRate.name() : __ScndBcktOutflwRate
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.OutflowImpact1 = OutflowImpact1
Namespace.addCategoryObject('typeBinding', 'OutflowImpact1', OutflowImpact1)


# Complex type {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}Party46Choice__1 with content type ELEMENT_ONLY
class Party46Choice__1 (pyxb.binding.basis.complexTypeDefinition):
    """Party46Choice__1Choice between issuer and sponsor information."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Party46Choice__1')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2941, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}IssrData uses Python identifier IssrData
    __IssrData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'IssrData'), 'IssrData', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_Party46Choice__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01IssrData', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2947, 12), )

    
    IssrData = property(__IssrData.value, __IssrData.set, None, 'IssuerDataSpecifies further details of the issuer.')

    _ElementMap.update({
        __IssrData.name() : __IssrData
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Party46Choice__1 = Party46Choice__1
Namespace.addCategoryObject('typeBinding', 'Party46Choice__1', Party46Choice__1)


# Complex type {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}Party46Choice__2 with content type ELEMENT_ONLY
class Party46Choice__2 (pyxb.binding.basis.complexTypeDefinition):
    """Party46Choice__2Choice between issuer and sponsor information."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Party46Choice__2')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2955, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}SpnsrData uses Python identifier SpnsrData
    __SpnsrData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SpnsrData'), 'SpnsrData', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_Party46Choice__2_urnisostdiso20022techxsdDRAFT3auth_093_001_01SpnsrData', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2961, 12), )

    
    SpnsrData = property(__SpnsrData.value, __SpnsrData.set, None, 'SponsorDataSpecifies further details of the sponsor.\r\n')

    _ElementMap.update({
        __SpnsrData.name() : __SpnsrData
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Party46Choice__2 = Party46Choice__2
Namespace.addCategoryObject('typeBinding', 'Party46Choice__2', Party46Choice__2)


# Complex type {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}Party46Choice__3 with content type ELEMENT_ONLY
class Party46Choice__3 (pyxb.binding.basis.complexTypeDefinition):
    """Party46Choice__3Choice between issuer and sponsor information."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Party46Choice__3')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2970, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}CtrPtyData uses Python identifier CtrPtyData
    __CtrPtyData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CtrPtyData'), 'CtrPtyData', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_Party46Choice__3_urnisostdiso20022techxsdDRAFT3auth_093_001_01CtrPtyData', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2976, 12), )

    
    CtrPtyData = property(__CtrPtyData.value, __CtrPtyData.set, None, 'CounterpartyDataProvides information about identification of the party that is a choice between the issuer of the money market instrument, the sponsor of the securitisation/asset backed commercial paper or the counterparty in the context of the derivative instrument, the repurchase agreement/reverse repurchase agreement or the deposit/ancillary liquid assets.')

    _ElementMap.update({
        __CtrPtyData.name() : __CtrPtyData
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Party46Choice__3 = Party46Choice__3
Namespace.addCategoryObject('typeBinding', 'Party46Choice__3', Party46Choice__3)


# Complex type {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}Party46Choice__4 with content type ELEMENT_ONLY
class Party46Choice__4 (pyxb.binding.basis.complexTypeDefinition):
    """Party46Choice__4Choice between issuer and sponsor information."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Party46Choice__4')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2984, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}CtrPtyData uses Python identifier CtrPtyData
    __CtrPtyData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CtrPtyData'), 'CtrPtyData', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_Party46Choice__4_urnisostdiso20022techxsdDRAFT3auth_093_001_01CtrPtyData', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2990, 12), )

    
    CtrPtyData = property(__CtrPtyData.value, __CtrPtyData.set, None, 'CounterpartyDataProvides information about identification of the party that is a choice between the issuer of the money market instrument, the sponsor of the securitisation/asset backed commercial paper or the counterparty in the context of the derivative instrument, the repurchase agreement/reverse repurchase agreement or the deposit/ancillary liquid assets.')

    _ElementMap.update({
        __CtrPtyData.name() : __CtrPtyData
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Party46Choice__4 = Party46Choice__4
Namespace.addCategoryObject('typeBinding', 'Party46Choice__4', Party46Choice__4)


# Complex type {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}PartyAndSector1__1 with content type ELEMENT_ONLY
class PartyAndSector1__1 (pyxb.binding.basis.complexTypeDefinition):
    """PartyAndSector1__1Specifies further details of the party.
"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PartyAndSector1__1')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2998, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}PtyId uses Python identifier PtyId
    __PtyId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PtyId'), 'PtyId', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_PartyAndSector1__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01PtyId', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3005, 12), )

    
    PtyId = property(__PtyId.value, __PtyId.set, None, 'PartyIdentificationProvides information about identification of the party.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}Sctr uses Python identifier Sctr
    __Sctr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Sctr'), 'Sctr', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_PartyAndSector1__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01Sctr', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3011, 12), )

    
    Sctr = property(__Sctr.value, __Sctr.set, None, 'SectorSpecifies the sector of the party involved as an issuer, a sponsor or a counterparty in the asset held by the fund.')

    _ElementMap.update({
        __PtyId.name() : __PtyId,
        __Sctr.name() : __Sctr
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.PartyAndSector1__1 = PartyAndSector1__1
Namespace.addCategoryObject('typeBinding', 'PartyAndSector1__1', PartyAndSector1__1)


# Complex type {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}PartyAndSector1__2 with content type ELEMENT_ONLY
class PartyAndSector1__2 (pyxb.binding.basis.complexTypeDefinition):
    """PartyAndSector1__2Specifies further details of the party.
"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PartyAndSector1__2')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3019, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}PtyId uses Python identifier PtyId
    __PtyId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PtyId'), 'PtyId', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_PartyAndSector1__2_urnisostdiso20022techxsdDRAFT3auth_093_001_01PtyId', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3026, 12), )

    
    PtyId = property(__PtyId.value, __PtyId.set, None, 'PartyIdentificationProvides information about identification of the party.')

    _ElementMap.update({
        __PtyId.name() : __PtyId
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.PartyAndSector1__2 = PartyAndSector1__2
Namespace.addCategoryObject('typeBinding', 'PartyAndSector1__2', PartyAndSector1__2)


# Complex type {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}PartyIdentification195__1 with content type ELEMENT_ONLY
class PartyIdentification195__1 (pyxb.binding.basis.complexTypeDefinition):
    """PartyIdentification195__1Company that is responsible for the management and operation of the fund, that is, determines the investment strategy, appoints the service providers, and makes major decisions for the fund. It is usually responsible for the distribution and marketing of the fund. 
For self-managed funds, this will often be a separate promoter or sponsor of the fund."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PartyIdentification195__1')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3034, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}LEI uses Python identifier LEI
    __LEI = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'LEI'), 'LEI', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_PartyIdentification195__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01LEI', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3041, 12), )

    
    LEI = property(__LEI.value, __LEI.set, None, 'LEILegal entity identification as an alternate identification for a party.\r\n')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}FndAuthrtyRegnNb uses Python identifier FndAuthrtyRegnNb
    __FndAuthrtyRegnNb = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'FndAuthrtyRegnNb'), 'FndAuthrtyRegnNb', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_PartyIdentification195__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01FndAuthrtyRegnNb', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3048, 12), )

    
    FndAuthrtyRegnNb = property(__FndAuthrtyRegnNb.value, __FndAuthrtyRegnNb.set, None, 'FundAuthorityRegistrationNumberNumber assigned by a national registration authority to an entity.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}FndMgmtCpnyAuthrtyRegnNb uses Python identifier FndMgmtCpnyAuthrtyRegnNb
    __FndMgmtCpnyAuthrtyRegnNb = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'FndMgmtCpnyAuthrtyRegnNb'), 'FndMgmtCpnyAuthrtyRegnNb', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_PartyIdentification195__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01FndMgmtCpnyAuthrtyRegnNb', True, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3054, 12), )

    
    FndMgmtCpnyAuthrtyRegnNb = property(__FndMgmtCpnyAuthrtyRegnNb.value, __FndMgmtCpnyAuthrtyRegnNb.set, None, 'FundManagementCompanyAuthorityRegistrationNumberNumber assigned by a national registration authority to an entity.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}AltrnId uses Python identifier AltrnId
    __AltrnId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AltrnId'), 'AltrnId', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_PartyIdentification195__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01AltrnId', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3060, 12), )

    
    AltrnId = property(__AltrnId.value, __AltrnId.set, None, 'AlternateIdentificationAlternate identification of the fund.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}Nm uses Python identifier Nm
    __Nm = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Nm'), 'Nm', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_PartyIdentification195__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01Nm', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3066, 12), )

    
    Nm = property(__Nm.value, __Nm.set, None, 'NameName of the fund management company.')

    _ElementMap.update({
        __LEI.name() : __LEI,
        __FndAuthrtyRegnNb.name() : __FndAuthrtyRegnNb,
        __FndMgmtCpnyAuthrtyRegnNb.name() : __FndMgmtCpnyAuthrtyRegnNb,
        __AltrnId.name() : __AltrnId,
        __Nm.name() : __Nm
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.PartyIdentification195__1 = PartyIdentification195__1
Namespace.addCategoryObject('typeBinding', 'PartyIdentification195__1', PartyIdentification195__1)


# Complex type {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}PartyIdentification212__1 with content type ELEMENT_ONLY
class PartyIdentification212__1 (pyxb.binding.basis.complexTypeDefinition):
    """PartyIdentification212__1Specifies the identification of an organisation."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PartyIdentification212__1')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3074, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}LEI uses Python identifier LEI
    __LEI = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'LEI'), 'LEI', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_PartyIdentification212__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01LEI', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3080, 12), )

    
    LEI = property(__LEI.value, __LEI.set, None, 'LEILegal entity identification for a party.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}NtlRegnNb uses Python identifier NtlRegnNb
    __NtlRegnNb = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NtlRegnNb'), 'NtlRegnNb', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_PartyIdentification212__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01NtlRegnNb', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3086, 12), )

    
    NtlRegnNb = property(__NtlRegnNb.value, __NtlRegnNb.set, None, 'NationalRegistrationNumberNumber assigned by a national registration authority to an entity.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}AltrnId uses Python identifier AltrnId
    __AltrnId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AltrnId'), 'AltrnId', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_PartyIdentification212__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01AltrnId', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3092, 12), )

    
    AltrnId = property(__AltrnId.value, __AltrnId.set, None, 'AlternateIdentificationAlternate identification of a party.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}Nm uses Python identifier Nm
    __Nm = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Nm'), 'Nm', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_PartyIdentification212__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01Nm', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3098, 12), )

    
    Nm = property(__Nm.value, __Nm.set, None, 'NameName of a party.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}CtryOfDmcl uses Python identifier CtryOfDmcl
    __CtryOfDmcl = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CtryOfDmcl'), 'CtryOfDmcl', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_PartyIdentification212__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01CtryOfDmcl', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3104, 12), )

    
    CtryOfDmcl = property(__CtryOfDmcl.value, __CtryOfDmcl.set, None, 'CountryOfDomicileCountry of the party.')

    _ElementMap.update({
        __LEI.name() : __LEI,
        __NtlRegnNb.name() : __NtlRegnNb,
        __AltrnId.name() : __AltrnId,
        __Nm.name() : __Nm,
        __CtryOfDmcl.name() : __CtryOfDmcl
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.PartyIdentification212__1 = PartyIdentification212__1
Namespace.addCategoryObject('typeBinding', 'PartyIdentification212__1', PartyIdentification212__1)


# Complex type {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}PartyIdentification212__2 with content type ELEMENT_ONLY
class PartyIdentification212__2 (pyxb.binding.basis.complexTypeDefinition):
    """PartyIdentification212__2Specifies the identification of an organisation."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PartyIdentification212__2')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3112, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}LEI uses Python identifier LEI
    __LEI = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'LEI'), 'LEI', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_PartyIdentification212__2_urnisostdiso20022techxsdDRAFT3auth_093_001_01LEI', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3118, 12), )

    
    LEI = property(__LEI.value, __LEI.set, None, 'LEILegal entity identification for a party.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}NtlRegnNb uses Python identifier NtlRegnNb
    __NtlRegnNb = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NtlRegnNb'), 'NtlRegnNb', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_PartyIdentification212__2_urnisostdiso20022techxsdDRAFT3auth_093_001_01NtlRegnNb', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3124, 12), )

    
    NtlRegnNb = property(__NtlRegnNb.value, __NtlRegnNb.set, None, 'NationalRegistrationNumberNumber assigned by a national registration authority to an entity.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}Nm uses Python identifier Nm
    __Nm = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Nm'), 'Nm', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_PartyIdentification212__2_urnisostdiso20022techxsdDRAFT3auth_093_001_01Nm', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3130, 12), )

    
    Nm = property(__Nm.value, __Nm.set, None, 'NameName of a party.')

    _ElementMap.update({
        __LEI.name() : __LEI,
        __NtlRegnNb.name() : __NtlRegnNb,
        __Nm.name() : __Nm
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.PartyIdentification212__2 = PartyIdentification212__2
Namespace.addCategoryObject('typeBinding', 'PartyIdentification212__2', PartyIdentification212__2)


# Complex type {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}PartyIdentification212__3 with content type ELEMENT_ONLY
class PartyIdentification212__3 (pyxb.binding.basis.complexTypeDefinition):
    """PartyIdentification212__3Specifies the identification of an organisation."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PartyIdentification212__3')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3138, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}LEI uses Python identifier LEI
    __LEI = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'LEI'), 'LEI', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_PartyIdentification212__3_urnisostdiso20022techxsdDRAFT3auth_093_001_01LEI', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3144, 12), )

    
    LEI = property(__LEI.value, __LEI.set, None, 'LEILegal entity identification for a party.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}NtlRegnNb uses Python identifier NtlRegnNb
    __NtlRegnNb = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NtlRegnNb'), 'NtlRegnNb', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_PartyIdentification212__3_urnisostdiso20022techxsdDRAFT3auth_093_001_01NtlRegnNb', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3150, 12), )

    
    NtlRegnNb = property(__NtlRegnNb.value, __NtlRegnNb.set, None, 'NationalRegistrationNumberNumber assigned by a national registration authority to an entity.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}Nm uses Python identifier Nm
    __Nm = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Nm'), 'Nm', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_PartyIdentification212__3_urnisostdiso20022techxsdDRAFT3auth_093_001_01Nm', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3156, 12), )

    
    Nm = property(__Nm.value, __Nm.set, None, 'NameName of a party.')

    _ElementMap.update({
        __LEI.name() : __LEI,
        __NtlRegnNb.name() : __NtlRegnNb,
        __Nm.name() : __Nm
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.PartyIdentification212__3 = PartyIdentification212__3
Namespace.addCategoryObject('typeBinding', 'PartyIdentification212__3', PartyIdentification212__3)


# Complex type {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}PartyIdentification212__4 with content type ELEMENT_ONLY
class PartyIdentification212__4 (pyxb.binding.basis.complexTypeDefinition):
    """PartyIdentification212__4Specifies the identification of an organisation."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PartyIdentification212__4')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3164, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}LEI uses Python identifier LEI
    __LEI = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'LEI'), 'LEI', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_PartyIdentification212__4_urnisostdiso20022techxsdDRAFT3auth_093_001_01LEI', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3170, 12), )

    
    LEI = property(__LEI.value, __LEI.set, None, 'LEILegal entity identification for a party.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}Nm uses Python identifier Nm
    __Nm = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Nm'), 'Nm', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_PartyIdentification212__4_urnisostdiso20022techxsdDRAFT3auth_093_001_01Nm', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3176, 12), )

    
    Nm = property(__Nm.value, __Nm.set, None, 'NameName of a party.')

    _ElementMap.update({
        __LEI.name() : __LEI,
        __Nm.name() : __Nm
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.PartyIdentification212__4 = PartyIdentification212__4
Namespace.addCategoryObject('typeBinding', 'PartyIdentification212__4', PartyIdentification212__4)


# Complex type {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}PerformanceFactors2__1 with content type ELEMENT_ONLY
class PerformanceFactors2__1 (pyxb.binding.basis.complexTypeDefinition):
    """PerformanceFactors2__1Provide the details of the performance indicators for the money market fund during the reporting period.
"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PerformanceFactors2__1')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3299, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}FndValtn uses Python identifier FndValtn
    __FndValtn = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'FndValtn'), 'FndValtn', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_PerformanceFactors2__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01FndValtn', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3306, 12), )

    
    FndValtn = property(__FndValtn.value, __FndValtn.set, None, 'FundValuationProvide the details of the valuation calculated for the money market fund during the reporting period.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}LqdtyInf uses Python identifier LqdtyInf
    __LqdtyInf = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'LqdtyInf'), 'LqdtyInf', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_PerformanceFactors2__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01LqdtyInf', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3312, 12), )

    
    LqdtyInf = property(__LqdtyInf.value, __LqdtyInf.set, None, 'LiquidityInformationProvide the details of the liquidity indicators calculated for the money market fund during the reporting period.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}Yld uses Python identifier Yld
    __Yld = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Yld'), 'Yld', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_PerformanceFactors2__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01Yld', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3318, 12), )

    
    Yld = property(__Yld.value, __Yld.set, None, 'YieldSpecifies the yield performance indicators for the fund.')

    _ElementMap.update({
        __FndValtn.name() : __FndValtn,
        __LqdtyInf.name() : __LqdtyInf,
        __Yld.name() : __Yld
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.PerformanceFactors2__1 = PerformanceFactors2__1
Namespace.addCategoryObject('typeBinding', 'PerformanceFactors2__1', PerformanceFactors2__1)


# Complex type {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}PerformanceValueType1Choice__1 with content type ELEMENT_ONLY
class PerformanceValueType1Choice__1 (pyxb.binding.basis.complexTypeDefinition):
    """PerformanceValueType1Choice__1The value assessing the performance for a specific time range is a choice between a rate or a value."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PerformanceValueType1Choice__1')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3326, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}Rate uses Python identifier Rate
    __Rate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Rate'), 'Rate', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_PerformanceValueType1Choice__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01Rate', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3332, 12), )

    
    Rate = property(__Rate.value, __Rate.set, None, 'RatePercentage indicating the performance of the instrument within each time range.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}NotAvlblVal uses Python identifier NotAvlblVal
    __NotAvlblVal = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NotAvlblVal'), 'NotAvlblVal', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_PerformanceValueType1Choice__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01NotAvlblVal', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3338, 12), )

    
    NotAvlblVal = property(__NotAvlblVal.value, __NotAvlblVal.set, None, 'NotAvailableValueSpecifies that value is not available for that range.')

    _ElementMap.update({
        __Rate.name() : __Rate,
        __NotAvlblVal.name() : __NotAvlblVal
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.PerformanceValueType1Choice__1 = PerformanceValueType1Choice__1
Namespace.addCategoryObject('typeBinding', 'PerformanceValueType1Choice__1', PerformanceValueType1Choice__1)


# Complex type {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}Period2 with content type ELEMENT_ONLY
class Period2 (pyxb.binding.basis.complexTypeDefinition):
    """Period2Time span defined by a start date and time, and an end date and time."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Period2')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3346, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}FrDt uses Python identifier FrDt
    __FrDt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'FrDt'), 'FrDt', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_Period2_urnisostdiso20022techxsdDRAFT3auth_093_001_01FrDt', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3352, 12), )

    
    FrDt = property(__FrDt.value, __FrDt.set, None, 'FromDateDate and time at which the range starts.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}ToDt uses Python identifier ToDt
    __ToDt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ToDt'), 'ToDt', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_Period2_urnisostdiso20022techxsdDRAFT3auth_093_001_01ToDt', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3358, 12), )

    
    ToDt = property(__ToDt.value, __ToDt.set, None, 'ToDateDate and time at which the range ends.')

    _ElementMap.update({
        __FrDt.name() : __FrDt,
        __ToDt.name() : __ToDt
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Period2 = Period2
Namespace.addCategoryObject('typeBinding', 'Period2', Period2)


# Complex type {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}Period4Choice__1 with content type ELEMENT_ONLY
class Period4Choice__1 (pyxb.binding.basis.complexTypeDefinition):
    """Period4Choice__1Choice between date and date-time for the specification of a period."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Period4Choice__1')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3366, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}FrDtToDt uses Python identifier FrDtToDt
    __FrDtToDt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'FrDtToDt'), 'FrDtToDt', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_Period4Choice__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01FrDtToDt', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3372, 12), )

    
    FrDtToDt = property(__FrDtToDt.value, __FrDtToDt.set, None, 'FromDateToDateTime span defined by a start date, and an end date.')

    _ElementMap.update({
        __FrDtToDt.name() : __FrDtToDt
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Period4Choice__1 = Period4Choice__1
Namespace.addCategoryObject('typeBinding', 'Period4Choice__1', Period4Choice__1)


# Complex type {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}QuantitativeData4__1 with content type ELEMENT_ONLY
class QuantitativeData4__1 (pyxb.binding.basis.complexTypeDefinition):
    """QuantitativeData4__1Provides the details of each money market fund quantitative information.
"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'QuantitativeData4__1')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3380, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}PrtflPrfrmnc uses Python identifier PrtflPrfrmnc
    __PrtflPrfrmnc = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PrtflPrfrmnc'), 'PrtflPrfrmnc', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_QuantitativeData4__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01PrtflPrfrmnc', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3387, 12), )

    
    PrtflPrfrmnc = property(__PrtflPrfrmnc.value, __PrtflPrfrmnc.set, None, 'PortfolioPerformanceProvide the details of the performance indicators for the money market fund during the reporting period.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}StrssTst uses Python identifier StrssTst
    __StrssTst = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'StrssTst'), 'StrssTst', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_QuantitativeData4__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01StrssTst', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3393, 12), )

    
    StrssTst = property(__StrssTst.value, __StrssTst.set, None, 'StressTestInformation on the results of the last stress tests performed by the fund.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}AsstInf uses Python identifier AsstInf
    __AsstInf = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AsstInf'), 'AsstInf', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_QuantitativeData4__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01AsstInf', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3399, 12), )

    
    AsstInf = property(__AsstInf.value, __AsstInf.set, None, 'AssetInformationInformation on the assets held by the money market fund.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}LbltyInf uses Python identifier LbltyInf
    __LbltyInf = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'LbltyInf'), 'LbltyInf', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_QuantitativeData4__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01LbltyInf', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3405, 12), )

    
    LbltyInf = property(__LbltyInf.value, __LbltyInf.set, None, 'LiabilityInformationInformation related to the liabilities of the fund.\r\n')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}LwVoltlyNetAsstValRptData uses Python identifier LwVoltlyNetAsstValRptData
    __LwVoltlyNetAsstValRptData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'LwVoltlyNetAsstValRptData'), 'LwVoltlyNetAsstValRptData', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_QuantitativeData4__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01LwVoltlyNetAsstValRptData', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3412, 12), )

    
    LwVoltlyNetAsstValRptData = property(__LwVoltlyNetAsstValRptData.value, __LwVoltlyNetAsstValRptData.set, None, 'LowVolatilityNetAssetValueReportDataReport schema for the low volatility net asset value money market fund.\r\n')

    _ElementMap.update({
        __PrtflPrfrmnc.name() : __PrtflPrfrmnc,
        __StrssTst.name() : __StrssTst,
        __AsstInf.name() : __AsstInf,
        __LbltyInf.name() : __LbltyInf,
        __LwVoltlyNetAsstValRptData.name() : __LwVoltlyNetAsstValRptData
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.QuantitativeData4__1 = QuantitativeData4__1
Namespace.addCategoryObject('typeBinding', 'QuantitativeData4__1', QuantitativeData4__1)


# Complex type {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}Quarter3__1 with content type ELEMENT_ONLY
class Quarter3__1 (pyxb.binding.basis.complexTypeDefinition):
    """Quarter3__1Information related with a quarter."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Quarter3__1')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3421, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}MnthInf uses Python identifier MnthInf
    __MnthInf = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'MnthInf'), 'MnthInf', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_Quarter3__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01MnthInf', True, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3427, 12), )

    
    MnthInf = property(__MnthInf.value, __MnthInf.set, None, 'MonthInformationInformation related with a month.')

    _ElementMap.update({
        __MnthInf.name() : __MnthInf
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Quarter3__1 = Quarter3__1
Namespace.addCategoryObject('typeBinding', 'Quarter3__1', Quarter3__1)


# Complex type {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}Quarter3__2 with content type ELEMENT_ONLY
class Quarter3__2 (pyxb.binding.basis.complexTypeDefinition):
    """Quarter3__2Information related with a quarter."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Quarter3__2')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3435, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}MnthInf uses Python identifier MnthInf
    __MnthInf = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'MnthInf'), 'MnthInf', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_Quarter3__2_urnisostdiso20022techxsdDRAFT3auth_093_001_01MnthInf', True, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3441, 12), )

    
    MnthInf = property(__MnthInf.value, __MnthInf.set, None, 'MonthInformationInformation related with a month.')

    _ElementMap.update({
        __MnthInf.name() : __MnthInf
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Quarter3__2 = Quarter3__2
Namespace.addCategoryObject('typeBinding', 'Quarter3__2', Quarter3__2)


# Complex type {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}Quarter3__3 with content type ELEMENT_ONLY
class Quarter3__3 (pyxb.binding.basis.complexTypeDefinition):
    """Quarter3__3Information related with a quarter."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Quarter3__3')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3449, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}MnthInf uses Python identifier MnthInf
    __MnthInf = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'MnthInf'), 'MnthInf', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_Quarter3__3_urnisostdiso20022techxsdDRAFT3auth_093_001_01MnthInf', True, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3455, 12), )

    
    MnthInf = property(__MnthInf.value, __MnthInf.set, None, 'MonthInformationInformation related with a month.')

    _ElementMap.update({
        __MnthInf.name() : __MnthInf
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Quarter3__3 = Quarter3__3
Namespace.addCategoryObject('typeBinding', 'Quarter3__3', Quarter3__3)


# Complex type {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}Quarter3__4 with content type ELEMENT_ONLY
class Quarter3__4 (pyxb.binding.basis.complexTypeDefinition):
    """Quarter3__4Information related with a quarter."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Quarter3__4')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3463, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}MnthInf uses Python identifier MnthInf
    __MnthInf = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'MnthInf'), 'MnthInf', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_Quarter3__4_urnisostdiso20022techxsdDRAFT3auth_093_001_01MnthInf', True, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3469, 12), )

    
    MnthInf = property(__MnthInf.value, __MnthInf.set, None, 'MonthInformationInformation related with a month.')

    _ElementMap.update({
        __MnthInf.name() : __MnthInf
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Quarter3__4 = Quarter3__4
Namespace.addCategoryObject('typeBinding', 'Quarter3__4', Quarter3__4)


# Complex type {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}Quarter3__5 with content type ELEMENT_ONLY
class Quarter3__5 (pyxb.binding.basis.complexTypeDefinition):
    """Quarter3__5Information related with a quarter."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Quarter3__5')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3477, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}MnthInf uses Python identifier MnthInf
    __MnthInf = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'MnthInf'), 'MnthInf', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_Quarter3__5_urnisostdiso20022techxsdDRAFT3auth_093_001_01MnthInf', True, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3483, 12), )

    
    MnthInf = property(__MnthInf.value, __MnthInf.set, None, 'MonthInformationInformation related with a month.')

    _ElementMap.update({
        __MnthInf.name() : __MnthInf
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Quarter3__5 = Quarter3__5
Namespace.addCategoryObject('typeBinding', 'Quarter3__5', Quarter3__5)


# Complex type {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}Quarter3__6 with content type ELEMENT_ONLY
class Quarter3__6 (pyxb.binding.basis.complexTypeDefinition):
    """Quarter3__6Information related with a quarter."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Quarter3__6')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3491, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}MnthInf uses Python identifier MnthInf
    __MnthInf = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'MnthInf'), 'MnthInf', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_Quarter3__6_urnisostdiso20022techxsdDRAFT3auth_093_001_01MnthInf', True, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3497, 12), )

    
    MnthInf = property(__MnthInf.value, __MnthInf.set, None, 'MonthInformationInformation related with a month.')

    _ElementMap.update({
        __MnthInf.name() : __MnthInf
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Quarter3__6 = Quarter3__6
Namespace.addCategoryObject('typeBinding', 'Quarter3__6', Quarter3__6)


# Complex type {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}Quarter3__7 with content type ELEMENT_ONLY
class Quarter3__7 (pyxb.binding.basis.complexTypeDefinition):
    """Quarter3__7Information related with a quarter."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Quarter3__7')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3505, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}MnthInf uses Python identifier MnthInf
    __MnthInf = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'MnthInf'), 'MnthInf', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_Quarter3__7_urnisostdiso20022techxsdDRAFT3auth_093_001_01MnthInf', True, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3511, 12), )

    
    MnthInf = property(__MnthInf.value, __MnthInf.set, None, 'MonthInformationInformation related with a month.')

    _ElementMap.update({
        __MnthInf.name() : __MnthInf
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Quarter3__7 = Quarter3__7
Namespace.addCategoryObject('typeBinding', 'Quarter3__7', Quarter3__7)


# Complex type {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}Quarter3__8 with content type ELEMENT_ONLY
class Quarter3__8 (pyxb.binding.basis.complexTypeDefinition):
    """Quarter3__8Information related with a quarter."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Quarter3__8')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3519, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}MnthInf uses Python identifier MnthInf
    __MnthInf = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'MnthInf'), 'MnthInf', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_Quarter3__8_urnisostdiso20022techxsdDRAFT3auth_093_001_01MnthInf', True, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3525, 12), )

    
    MnthInf = property(__MnthInf.value, __MnthInf.set, None, 'MonthInformationInformation related with a month.')

    _ElementMap.update({
        __MnthInf.name() : __MnthInf
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Quarter3__8 = Quarter3__8
Namespace.addCategoryObject('typeBinding', 'Quarter3__8', Quarter3__8)


# Complex type {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}QuarterPeriod1 with content type ELEMENT_ONLY
class QuarterPeriod1 (pyxb.binding.basis.complexTypeDefinition):
    """QuarterPeriod1Quarterly periods range."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'QuarterPeriod1')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3533, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}FrPrd uses Python identifier FrPrd
    __FrPrd = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'FrPrd'), 'FrPrd', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_QuarterPeriod1_urnisostdiso20022techxsdDRAFT3auth_093_001_01FrPrd', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3539, 12), )

    
    FrPrd = property(__FrPrd.value, __FrPrd.set, None, 'FromPeriodLower boundary of a range of periods.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}ToPrd uses Python identifier ToPrd
    __ToPrd = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ToPrd'), 'ToPrd', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_QuarterPeriod1_urnisostdiso20022techxsdDRAFT3auth_093_001_01ToPrd', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3545, 12), )

    
    ToPrd = property(__ToPrd.value, __ToPrd.set, None, 'ToPeriodUpper boundary of a range of periods.')

    _ElementMap.update({
        __FrPrd.name() : __FrPrd,
        __ToPrd.name() : __ToPrd
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.QuarterPeriod1 = QuarterPeriod1
Namespace.addCategoryObject('typeBinding', 'QuarterPeriod1', QuarterPeriod1)


# Complex type {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}RangeBreakdown1__1 with content type ELEMENT_ONLY
class RangeBreakdown1__1 (pyxb.binding.basis.complexTypeDefinition):
    """RangeBreakdown1__1Specifies the performance indicator within each time period."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RangeBreakdown1__1')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3553, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}RgTp uses Python identifier RgTp
    __RgTp = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RgTp'), 'RgTp', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_RangeBreakdown1__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01RgTp', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3559, 12), )

    
    RgTp = property(__RgTp.value, __RgTp.set, None, 'RangeTypeSpecifies the time range for which the performance indicator is assessed.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}PrfrmncVal uses Python identifier PrfrmncVal
    __PrfrmncVal = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PrfrmncVal'), 'PrfrmncVal', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_RangeBreakdown1__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01PrfrmncVal', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3565, 12), )

    
    PrfrmncVal = property(__PrfrmncVal.value, __PrfrmncVal.set, None, 'PerformanceValueValue assessing the performance for a specific time range.')

    _ElementMap.update({
        __RgTp.name() : __RgTp,
        __PrfrmncVal.name() : __PrfrmncVal
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.RangeBreakdown1__1 = RangeBreakdown1__1
Namespace.addCategoryObject('typeBinding', 'RangeBreakdown1__1', RangeBreakdown1__1)


# Complex type {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}RangeBreakdown1__2 with content type ELEMENT_ONLY
class RangeBreakdown1__2 (pyxb.binding.basis.complexTypeDefinition):
    """RangeBreakdown1__2Specifies the performance indicator within each time period."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RangeBreakdown1__2')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3573, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}RgTp uses Python identifier RgTp
    __RgTp = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RgTp'), 'RgTp', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_RangeBreakdown1__2_urnisostdiso20022techxsdDRAFT3auth_093_001_01RgTp', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3579, 12), )

    
    RgTp = property(__RgTp.value, __RgTp.set, None, 'RangeTypeSpecifies the time range for which the performance indicator is assessed.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}PrfrmncVal uses Python identifier PrfrmncVal
    __PrfrmncVal = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PrfrmncVal'), 'PrfrmncVal', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_RangeBreakdown1__2_urnisostdiso20022techxsdDRAFT3auth_093_001_01PrfrmncVal', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3585, 12), )

    
    PrfrmncVal = property(__PrfrmncVal.value, __PrfrmncVal.set, None, 'PerformanceValueValue assessing the performance for a specific time range.')

    _ElementMap.update({
        __RgTp.name() : __RgTp,
        __PrfrmncVal.name() : __PrfrmncVal
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.RangeBreakdown1__2 = RangeBreakdown1__2
Namespace.addCategoryObject('typeBinding', 'RangeBreakdown1__2', RangeBreakdown1__2)


# Complex type {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}RangeBreakdown1__3 with content type ELEMENT_ONLY
class RangeBreakdown1__3 (pyxb.binding.basis.complexTypeDefinition):
    """RangeBreakdown1__3Specifies the performance indicator within each time period."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RangeBreakdown1__3')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3593, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}RgTp uses Python identifier RgTp
    __RgTp = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RgTp'), 'RgTp', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_RangeBreakdown1__3_urnisostdiso20022techxsdDRAFT3auth_093_001_01RgTp', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3599, 12), )

    
    RgTp = property(__RgTp.value, __RgTp.set, None, 'RangeTypeSpecifies the time range for which the performance indicator is assessed.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}PrfrmncVal uses Python identifier PrfrmncVal
    __PrfrmncVal = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PrfrmncVal'), 'PrfrmncVal', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_RangeBreakdown1__3_urnisostdiso20022techxsdDRAFT3auth_093_001_01PrfrmncVal', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3605, 12), )

    
    PrfrmncVal = property(__PrfrmncVal.value, __PrfrmncVal.set, None, 'PerformanceValueValue assessing the performance for a specific time range.')

    _ElementMap.update({
        __RgTp.name() : __RgTp,
        __PrfrmncVal.name() : __PrfrmncVal
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.RangeBreakdown1__3 = RangeBreakdown1__3
Namespace.addCategoryObject('typeBinding', 'RangeBreakdown1__3', RangeBreakdown1__3)


# Complex type {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}RangeBreakdown1__4 with content type ELEMENT_ONLY
class RangeBreakdown1__4 (pyxb.binding.basis.complexTypeDefinition):
    """RangeBreakdown1__4Specifies the performance indicator within each time period."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RangeBreakdown1__4')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3613, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}RgTp uses Python identifier RgTp
    __RgTp = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RgTp'), 'RgTp', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_RangeBreakdown1__4_urnisostdiso20022techxsdDRAFT3auth_093_001_01RgTp', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3619, 12), )

    
    RgTp = property(__RgTp.value, __RgTp.set, None, 'RangeTypeSpecifies the time range for which the performance indicator is assessed.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}PrfrmncVal uses Python identifier PrfrmncVal
    __PrfrmncVal = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PrfrmncVal'), 'PrfrmncVal', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_RangeBreakdown1__4_urnisostdiso20022techxsdDRAFT3auth_093_001_01PrfrmncVal', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3625, 12), )

    
    PrfrmncVal = property(__PrfrmncVal.value, __PrfrmncVal.set, None, 'PerformanceValueValue assessing the performance for a specific time range.')

    _ElementMap.update({
        __RgTp.name() : __RgTp,
        __PrfrmncVal.name() : __PrfrmncVal
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.RangeBreakdown1__4 = RangeBreakdown1__4
Namespace.addCategoryObject('typeBinding', 'RangeBreakdown1__4', RangeBreakdown1__4)


# Complex type {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}RegisteredDistributionCountry2Choice__1 with content type ELEMENT_ONLY
class RegisteredDistributionCountry2Choice__1 (pyxb.binding.basis.complexTypeDefinition):
    """RegisteredDistributionCountry2Choice__1Provides the list of countries where the fund is registered for distribution or the reason why no registered distribution country may be reported for the money market fund."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RegisteredDistributionCountry2Choice__1')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3761, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}NonEurpnCtry uses Python identifier NonEurpnCtry
    __NonEurpnCtry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NonEurpnCtry'), 'NonEurpnCtry', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_RegisteredDistributionCountry2Choice__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01NonEurpnCtry', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3767, 12), )

    
    NonEurpnCtry = property(__NonEurpnCtry.value, __NonEurpnCtry.set, None, 'NonEuropeanCountryReason for which no country where the fund is registered for distribution is reported.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}Ctry uses Python identifier Ctry
    __Ctry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Ctry'), 'Ctry', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_RegisteredDistributionCountry2Choice__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01Ctry', True, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3773, 12), )

    
    Ctry = property(__Ctry.value, __Ctry.set, None, 'CountryProvides the list of countries where the fund is registered for distribution.')

    _ElementMap.update({
        __NonEurpnCtry.name() : __NonEurpnCtry,
        __Ctry.name() : __Ctry
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.RegisteredDistributionCountry2Choice__1 = RegisteredDistributionCountry2Choice__1
Namespace.addCategoryObject('typeBinding', 'RegisteredDistributionCountry2Choice__1', RegisteredDistributionCountry2Choice__1)


# Complex type {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}RelatedEvent2 with content type ELEMENT_ONLY
class RelatedEvent2 (pyxb.binding.basis.complexTypeDefinition):
    """RelatedEvent2The dates in relation with the money market fund life cycle."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RelatedEvent2')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3781, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}IncptnDt uses Python identifier IncptnDt
    __IncptnDt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'IncptnDt'), 'IncptnDt', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_RelatedEvent2_urnisostdiso20022techxsdDRAFT3auth_093_001_01IncptnDt', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3787, 12), )

    
    IncptnDt = property(__IncptnDt.value, __IncptnDt.set, None, 'InceptionDateDate at which the first net asset value of the fund was calculated under the Regulation.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}MrgrDt uses Python identifier MrgrDt
    __MrgrDt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'MrgrDt'), 'MrgrDt', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_RelatedEvent2_urnisostdiso20022techxsdDRAFT3auth_093_001_01MrgrDt', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3793, 12), )

    
    MrgrDt = property(__MrgrDt.value, __MrgrDt.set, None, 'MergerDateDate at which the last merger took place.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}LqdtnDt uses Python identifier LqdtnDt
    __LqdtnDt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'LqdtnDt'), 'LqdtnDt', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_RelatedEvent2_urnisostdiso20022techxsdDRAFT3auth_093_001_01LqdtnDt', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3799, 12), )

    
    LqdtnDt = property(__LqdtnDt.value, __LqdtnDt.set, None, 'LiquidationDateDate at which the liquidation took place.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}LastRptSnt uses Python identifier LastRptSnt
    __LastRptSnt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'LastRptSnt'), 'LastRptSnt', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_RelatedEvent2_urnisostdiso20022techxsdDRAFT3auth_093_001_01LastRptSnt', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3805, 12), )

    
    LastRptSnt = property(__LastRptSnt.value, __LastRptSnt.set, None, 'LastReportSentIndicates whether or not this report is the last report that will be sent by the submitting entity for that fund.')

    _ElementMap.update({
        __IncptnDt.name() : __IncptnDt,
        __MrgrDt.name() : __MrgrDt,
        __LqdtnDt.name() : __LqdtnDt,
        __LastRptSnt.name() : __LastRptSnt
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.RelatedEvent2 = RelatedEvent2
Namespace.addCategoryObject('typeBinding', 'RelatedEvent2', RelatedEvent2)


# Complex type {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}ReportData3Choice__1 with content type ELEMENT_ONLY
class ReportData3Choice__1 (pyxb.binding.basis.complexTypeDefinition):
    """ReportData3Choice__1Choice between a reason for no activity during the reporting period and the money market quantitative details for the reporting period.
"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ReportData3Choice__1')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3813, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}DataSetActn uses Python identifier DataSetActn
    __DataSetActn = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DataSetActn'), 'DataSetActn', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_ReportData3Choice__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01DataSetActn', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3820, 12), )

    
    DataSetActn = property(__DataSetActn.value, __DataSetActn.set, None, 'DataSetActionProvides the reason why no quantitative schema is being reported for a money market fund reporting period. ')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}QttvData uses Python identifier QttvData
    __QttvData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'QttvData'), 'QttvData', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_ReportData3Choice__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01QttvData', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3826, 12), )

    
    QttvData = property(__QttvData.value, __QttvData.set, None, 'QuantitativeDataReport activity schema for all money market fund types.')

    _ElementMap.update({
        __DataSetActn.name() : __DataSetActn,
        __QttvData.name() : __QttvData
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ReportData3Choice__1 = ReportData3Choice__1
Namespace.addCategoryObject('typeBinding', 'ReportData3Choice__1', ReportData3Choice__1)


# Complex type {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}ReportItemJustification1 with content type ELEMENT_ONLY
class ReportItemJustification1 (pyxb.binding.basis.complexTypeDefinition):
    """ReportItemJustification1Provides additional information such as the assumptions taken by the submitted entity for each reported item where the reporting entity considered it necessary."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ReportItemJustification1')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3834, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}PlcAndNm uses Python identifier PlcAndNm
    __PlcAndNm = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PlcAndNm'), 'PlcAndNm', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_ReportItemJustification1_urnisostdiso20022techxsdDRAFT3auth_093_001_01PlcAndNm', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3840, 12), )

    
    PlcAndNm = property(__PlcAndNm.value, __PlcAndNm.set, None, 'PlaceAndNameSpecifies from the root of the message the unambiguous reference to the location of the element for which the justification is applicable in the message instance.\r\nThis is expressed by a valid XPath.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}Justfn uses Python identifier Justfn
    __Justfn = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Justfn'), 'Justfn', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_ReportItemJustification1_urnisostdiso20022techxsdDRAFT3auth_093_001_01Justfn', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3847, 12), )

    
    Justfn = property(__Justfn.value, __Justfn.set, None, 'JustificationProvides justification that might be reported by the submitting entity o.')

    _ElementMap.update({
        __PlcAndNm.name() : __PlcAndNm,
        __Justfn.name() : __Justfn
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ReportItemJustification1 = ReportItemJustification1
Namespace.addCategoryObject('typeBinding', 'ReportItemJustification1', ReportItemJustification1)


# Complex type {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}SecurityIdentification31Choice with content type ELEMENT_ONLY
class SecurityIdentification31Choice (pyxb.binding.basis.complexTypeDefinition):
    """SecurityIdentification31ChoiceChoice between ISIN and an alternative format for the identification of a financial instrument. ISIN is the preferred format."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SecurityIdentification31Choice')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 4005, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}ISIN uses Python identifier ISIN
    __ISIN = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ISIN'), 'ISIN', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_SecurityIdentification31Choice_urnisostdiso20022techxsdDRAFT3auth_093_001_01ISIN', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 4011, 12), )

    
    ISIN = property(__ISIN.value, __ISIN.set, None, "ISINInternational Securities Identification Number (ISIN).  A numbering system designed by the United Nation's International Organisation for Standardisation (ISO). The ISIN is composed of a 2-character prefix representing the country of issue, followed by the national security number (if one exists), and a check digit. Each country has a national numbering agency that assigns ISIN numbers for securities in that country.")

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}Nm uses Python identifier Nm
    __Nm = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Nm'), 'Nm', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_SecurityIdentification31Choice_urnisostdiso20022techxsdDRAFT3auth_093_001_01Nm', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 4017, 12), )

    
    Nm = property(__Nm.value, __Nm.set, None, 'NameName used to identify the financial instrument.')

    _ElementMap.update({
        __ISIN.name() : __ISIN,
        __Nm.name() : __Nm
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.SecurityIdentification31Choice = SecurityIdentification31Choice
Namespace.addCategoryObject('typeBinding', 'SecurityIdentification31Choice', SecurityIdentification31Choice)


# Complex type {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}SecurityIdentification33 with content type ELEMENT_ONLY
class SecurityIdentification33 (pyxb.binding.basis.complexTypeDefinition):
    """SecurityIdentification33Specifies the identification of a financial instrument."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SecurityIdentification33')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 4025, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}ISIN uses Python identifier ISIN
    __ISIN = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ISIN'), 'ISIN', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_SecurityIdentification33_urnisostdiso20022techxsdDRAFT3auth_093_001_01ISIN', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 4031, 12), )

    
    ISIN = property(__ISIN.value, __ISIN.set, None, "ISINInternational Securities Identification Number (ISIN).  A numbering system designed by the United Nation's International Organisation for Standardisation (ISO). The ISIN is composed of a 2-character prefix representing the country of issue, followed by the national security number (if one exists), and a check digit. Each country has a national numbering agency that assigns ISIN numbers for securities in that country.")

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}ClssfctnTp uses Python identifier ClssfctnTp
    __ClssfctnTp = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ClssfctnTp'), 'ClssfctnTp', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_SecurityIdentification33_urnisostdiso20022techxsdDRAFT3auth_093_001_01ClssfctnTp', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 4037, 12), )

    
    ClssfctnTp = property(__ClssfctnTp.value, __ClssfctnTp.set, None, 'ClassificationTypeISO 10962 Classification of Financial Instrument (CFI).')

    _ElementMap.update({
        __ISIN.name() : __ISIN,
        __ClssfctnTp.name() : __ClssfctnTp
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.SecurityIdentification33 = SecurityIdentification33
Namespace.addCategoryObject('typeBinding', 'SecurityIdentification33', SecurityIdentification33)


# Complex type {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}ShareClassList1__1 with content type ELEMENT_ONLY
class ShareClassList1__1 (pyxb.binding.basis.complexTypeDefinition):
    """ShareClassList1__1Information on the identification of the share classes of the fund.
"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ShareClassList1__1')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 4045, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}Id uses Python identifier Id
    __Id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Id'), 'Id', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_ShareClassList1__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01Id', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 4052, 12), )

    
    Id = property(__Id.value, __Id.set, None, 'IdentificationIdentification of the fund or share class.\r\n')

    _ElementMap.update({
        __Id.name() : __Id
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ShareClassList1__1 = ShareClassList1__1
Namespace.addCategoryObject('typeBinding', 'ShareClassList1__1', ShareClassList1__1)


# Complex type {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}ShareClassList1__2 with content type ELEMENT_ONLY
class ShareClassList1__2 (pyxb.binding.basis.complexTypeDefinition):
    """ShareClassList1__2Information on the identification of the share classes of the fund.
"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ShareClassList1__2')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 4061, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}Id uses Python identifier Id
    __Id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Id'), 'Id', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_ShareClassList1__2_urnisostdiso20022techxsdDRAFT3auth_093_001_01Id', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 4068, 12), )

    
    Id = property(__Id.value, __Id.set, None, 'IdentificationIdentification of the fund or share class.\r\n')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}Ccy uses Python identifier Ccy
    __Ccy = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Ccy'), 'Ccy', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_ShareClassList1__2_urnisostdiso20022techxsdDRAFT3auth_093_001_01Ccy', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 4075, 12), )

    
    Ccy = property(__Ccy.value, __Ccy.set, None, 'CurrencyCurrency associated with the share class.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}HghstNetAsstVal uses Python identifier HghstNetAsstVal
    __HghstNetAsstVal = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'HghstNetAsstVal'), 'HghstNetAsstVal', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_ShareClassList1__2_urnisostdiso20022techxsdDRAFT3auth_093_001_01HghstNetAsstVal', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 4081, 12), )

    
    HghstNetAsstVal = property(__HghstNetAsstVal.value, __HghstNetAsstVal.set, None, 'HighestNetAssetValueIndicates whether the share class is the share class with the highest net asset value.')

    _ElementMap.update({
        __Id.name() : __Id,
        __Ccy.name() : __Ccy,
        __HghstNetAsstVal.name() : __HghstNetAsstVal
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ShareClassList1__2 = ShareClassList1__2
Namespace.addCategoryObject('typeBinding', 'ShareClassList1__2', ShareClassList1__2)


# Complex type {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}StressTestImpact1Choice with content type ELEMENT_ONLY
class StressTestImpact1Choice (pyxb.binding.basis.complexTypeDefinition):
    """StressTestImpact1ChoiceQuantitative results of the stress testing."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'StressTestImpact1Choice')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 4089, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}NetAsstValImpct uses Python identifier NetAsstValImpct
    __NetAsstValImpct = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NetAsstValImpct'), 'NetAsstValImpct', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_StressTestImpact1Choice_urnisostdiso20022techxsdDRAFT3auth_093_001_01NetAsstValImpct', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 4095, 12), )

    
    NetAsstValImpct = property(__NetAsstValImpct.value, __NetAsstValImpct.set, None, 'NetAssetValueImpactPercentage of the net asset value that is corresponding to the effects of a stressed scenario.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}OutflwImpct uses Python identifier OutflwImpct
    __OutflwImpct = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'OutflwImpct'), 'OutflwImpct', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_StressTestImpact1Choice_urnisostdiso20022techxsdDRAFT3auth_093_001_01OutflwImpct', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 4101, 12), )

    
    OutflwImpct = property(__OutflwImpct.value, __OutflwImpct.set, None, 'OutflowImpactWeekly outflows derived from the monthly outflows compared with available weekly liquid assets, considered as the sum of highly liquid assets and weekly maturing assets. Rate computed for assets considered in the first bucket according to the Regulation.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}NotAvlblVal uses Python identifier NotAvlblVal
    __NotAvlblVal = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NotAvlblVal'), 'NotAvlblVal', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_StressTestImpact1Choice_urnisostdiso20022techxsdDRAFT3auth_093_001_01NotAvlblVal', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 4107, 12), )

    
    NotAvlblVal = property(__NotAvlblVal.value, __NotAvlblVal.set, None, 'NotAvailableValueSpecifies that value is not available for that range.')

    _ElementMap.update({
        __NetAsstValImpct.name() : __NetAsstValImpct,
        __OutflwImpct.name() : __OutflwImpct,
        __NotAvlblVal.name() : __NotAvlblVal
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.StressTestImpact1Choice = StressTestImpact1Choice
Namespace.addCategoryObject('typeBinding', 'StressTestImpact1Choice', StressTestImpact1Choice)


# Complex type {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}StressTestReport1__1 with content type ELEMENT_ONLY
class StressTestReport1__1 (pyxb.binding.basis.complexTypeDefinition):
    """StressTestReport1__1Information on the results of the last stress tests performed by the fund."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'StressTestReport1__1')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 4115, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}StrssTstRslt uses Python identifier StrssTstRslt
    __StrssTstRslt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'StrssTstRslt'), 'StrssTstRslt', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_StressTestReport1__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01StrssTstRslt', True, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 4121, 12), )

    
    StrssTstRslt = property(__StrssTstRslt.value, __StrssTstRslt.set, None, 'StressTestResultInformation on the results of the last stress tests performed by the fund.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}ActnPlan uses Python identifier ActnPlan
    __ActnPlan = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ActnPlan'), 'ActnPlan', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_StressTestReport1__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01ActnPlan', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 4127, 12), )

    
    ActnPlan = property(__ActnPlan.value, __ActnPlan.set, None, 'ActionPlanAction plan that is proposed by the board of directors following a stress test that revealed any vulnerability of the fund.')

    _ElementMap.update({
        __StrssTstRslt.name() : __StrssTstRslt,
        __ActnPlan.name() : __ActnPlan
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.StressTestReport1__1 = StressTestReport1__1
Namespace.addCategoryObject('typeBinding', 'StressTestReport1__1', StressTestReport1__1)


# Complex type {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}StressTestResult2__1 with content type ELEMENT_ONLY
class StressTestResult2__1 (pyxb.binding.basis.complexTypeDefinition):
    """StressTestResult2__1Information on the results of the last stress tests performed by the fund to identify possible events or future changes in economic conditions which should have unfavourable effects on the fund."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'StressTestResult2__1')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 4135, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}StrssTstDt uses Python identifier StrssTstDt
    __StrssTstDt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'StrssTstDt'), 'StrssTstDt', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_StressTestResult2__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01StrssTstDt', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 4141, 12), )

    
    StrssTstDt = property(__StrssTstDt.value, __StrssTstDt.set, None, 'StressTestDateDate when the last stress test was performed.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}NetAsstValBsis uses Python identifier NetAsstValBsis
    __NetAsstValBsis = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NetAsstValBsis'), 'NetAsstValBsis', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_StressTestResult2__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01NetAsstValBsis', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 4147, 12), )

    
    NetAsstValBsis = property(__NetAsstValBsis.value, __NetAsstValBsis.set, None, 'NetAssetValueBasisIdentifies whether the net asset value used as a basis for the stress test scenario is the constant net asset value.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}StrssTstScnroCd uses Python identifier StrssTstScnroCd
    __StrssTstScnroCd = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'StrssTstScnroCd'), 'StrssTstScnroCd', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_StressTestResult2__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01StrssTstScnroCd', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 4153, 12), )

    
    StrssTstScnroCd = property(__StrssTstScnroCd.value, __StrssTstScnroCd.set, None, 'StressTestScenarioCodeIdentifies the scenario that is assessed.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}StrssTstImpct uses Python identifier StrssTstImpct
    __StrssTstImpct = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'StrssTstImpct'), 'StrssTstImpct', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_StressTestResult2__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01StrssTstImpct', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 4159, 12), )

    
    StrssTstImpct = property(__StrssTstImpct.value, __StrssTstImpct.set, None, 'StressTestImpactSpecifies the effects of several plausible scenarios on several factors.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}InptFctr uses Python identifier InptFctr
    __InptFctr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'InptFctr'), 'InptFctr', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_StressTestResult2__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01InptFctr', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 4165, 12), )

    
    InptFctr = property(__InptFctr.value, __InptFctr.set, None, 'InputFactorAny other additional factor used as an input in the stress test.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}Cmnt uses Python identifier Cmnt
    __Cmnt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Cmnt'), 'Cmnt', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_StressTestResult2__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01Cmnt', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 4171, 12), )

    
    Cmnt = property(__Cmnt.value, __Cmnt.set, None, 'CommentAny other additional information about the stress test result.')

    _ElementMap.update({
        __StrssTstDt.name() : __StrssTstDt,
        __NetAsstValBsis.name() : __NetAsstValBsis,
        __StrssTstScnroCd.name() : __StrssTstScnroCd,
        __StrssTstImpct.name() : __StrssTstImpct,
        __InptFctr.name() : __InptFctr,
        __Cmnt.name() : __Cmnt
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.StressTestResult2__1 = StressTestResult2__1
Namespace.addCategoryObject('typeBinding', 'StressTestResult2__1', StressTestResult2__1)


# Complex type {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}Yield1__1 with content type ELEMENT_ONLY
class Yield1__1 (pyxb.binding.basis.complexTypeDefinition):
    """Yield1__1Specifies the yield performance indicators for the fund."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Yield1__1')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 4279, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}CmltvRtrsBrkdwn uses Python identifier CmltvRtrsBrkdwn
    __CmltvRtrsBrkdwn = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CmltvRtrsBrkdwn'), 'CmltvRtrsBrkdwn', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_Yield1__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01CmltvRtrsBrkdwn', True, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 4285, 12), )

    
    CmltvRtrsBrkdwn = property(__CmltvRtrsBrkdwn.value, __CmltvRtrsBrkdwn.set, None, 'CumulativeReturnsBreakdownSpecifies the percentage of cumulative returns for each time period.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}StdPrtflVoltlyBrkdwn uses Python identifier StdPrtflVoltlyBrkdwn
    __StdPrtflVoltlyBrkdwn = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'StdPrtflVoltlyBrkdwn'), 'StdPrtflVoltlyBrkdwn', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_Yield1__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01StdPrtflVoltlyBrkdwn', True, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 4291, 12), )

    
    StdPrtflVoltlyBrkdwn = property(__StdPrtflVoltlyBrkdwn.value, __StdPrtflVoltlyBrkdwn.set, None, 'StandardPortfolioVolatilityBreakdownSpecifies the percentage of portfolio volatility for each time period for all types of money market funds.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}ShdwPrtflVoltlyBrkdwn uses Python identifier ShdwPrtflVoltlyBrkdwn
    __ShdwPrtflVoltlyBrkdwn = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ShdwPrtflVoltlyBrkdwn'), 'ShdwPrtflVoltlyBrkdwn', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_Yield1__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01ShdwPrtflVoltlyBrkdwn', True, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 4297, 12), )

    
    ShdwPrtflVoltlyBrkdwn = property(__ShdwPrtflVoltlyBrkdwn.value, __ShdwPrtflVoltlyBrkdwn.set, None, 'ShadowPortfolioVolatilityBreakdownSpecifies the percentage of shadow portfolio volatility for each time period for all types of money market funds.')

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}CalYrPrfrmncBrkdwn uses Python identifier CalYrPrfrmncBrkdwn
    __CalYrPrfrmncBrkdwn = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CalYrPrfrmncBrkdwn'), 'CalYrPrfrmncBrkdwn', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_Yield1__1_urnisostdiso20022techxsdDRAFT3auth_093_001_01CalYrPrfrmncBrkdwn', True, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 4303, 12), )

    
    CalYrPrfrmncBrkdwn = property(__CalYrPrfrmncBrkdwn.value, __CalYrPrfrmncBrkdwn.set, None, 'CalendarYearPerformanceBreakdownSpecifies the percentage of calendar year performance returns for each time period.')

    _ElementMap.update({
        __CmltvRtrsBrkdwn.name() : __CmltvRtrsBrkdwn,
        __StdPrtflVoltlyBrkdwn.name() : __StdPrtflVoltlyBrkdwn,
        __ShdwPrtflVoltlyBrkdwn.name() : __ShdwPrtflVoltlyBrkdwn,
        __CalYrPrfrmncBrkdwn.name() : __CalYrPrfrmncBrkdwn
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Yield1__1 = Yield1__1
Namespace.addCategoryObject('typeBinding', 'Yield1__1', Yield1__1)


# Complex type {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}ActiveCurrencyAndAmount__1 with content type SIMPLE
class ActiveCurrencyAndAmount__1 (pyxb.binding.basis.complexTypeDefinition):
    """ActiveCurrencyAndAmount__1A number of monetary units specified in an active currency where the unit of currency is explicit and compliant with ISO 4217."""
    _TypeDefinition = ActiveCurrencyAndAmount__1_SimpleType
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ActiveCurrencyAndAmount__1')
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 70, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is ActiveCurrencyAndAmount__1_SimpleType
    
    # Attribute Ccy uses Python identifier Ccy
    __Ccy = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Ccy'), 'Ccy', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_ActiveCurrencyAndAmount__1_Ccy', _module_typeBindings.ActiveCurrencyCode_fixed, required=True)
    __Ccy._DeclarationLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 77, 16)
    __Ccy._UseLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 77, 16)
    
    Ccy = property(__Ccy.value, __Ccy.set, None, 'CurrencyMedium of exchange of value.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Ccy.name() : __Ccy
    })
_module_typeBindings.ActiveCurrencyAndAmount__1 = ActiveCurrencyAndAmount__1
Namespace.addCategoryObject('typeBinding', 'ActiveCurrencyAndAmount__1', ActiveCurrencyAndAmount__1)


Document = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Document'), Document_, location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 41, 4))
Namespace.addCategoryObject('elementBinding', Document.name().localName(), Document)



ActionPlan1Choice__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NoVlnrblty'), NoVulnerability1Code_fixed, scope=ActionPlan1Choice__1, documentation='NoVulnerabilityIndicates that no vulnerability was revealed by the stress tests.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 49, 12)))

ActionPlan1Choice__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PropsdActnPlan'), Max2000Text, scope=ActionPlan1Choice__1, documentation='ProposedActionPlanSpecifies the action plan as proposed by the board of directors.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 55, 12)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ActionPlan1Choice__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NoVlnrblty')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 49, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ActionPlan1Choice__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PropsdActnPlan')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 55, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ActionPlan1Choice__1._Automaton = _BuildAutomaton()




AmortisedCostMethodPriceDeviationEvent1__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ValtnDt'), ISODate, scope=AmortisedCostMethodPriceDeviationEvent1__1, documentation='ValuationDateValuation date from which the price of an asset calculated in accordance with the mark-to-market or mark-to-model method deviates from the asset price calculated in accordance with the amortised cost method by more than 10 basis points.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 125, 12)))

AmortisedCostMethodPriceDeviationEvent1__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AsstId'), SecurityIdentification33, scope=AmortisedCostMethodPriceDeviationEvent1__1, documentation='AssetIdentificationIdentification of the instrument\r\n', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 131, 12)))

AmortisedCostMethodPriceDeviationEvent1__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RptgCcyMktPric'), ActiveCurrencyAndAmount__1, scope=AmortisedCostMethodPriceDeviationEvent1__1, documentation='ReportingCurrencyMarketPriceSpecifies the market price expressed in the reporting currency of the asset valued by using the mark-to-market or mark-to-model method.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 138, 12)))

AmortisedCostMethodPriceDeviationEvent1__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RptgCcyAmtsdCostPric'), ActiveCurrencyAndAmount__1, scope=AmortisedCostMethodPriceDeviationEvent1__1, documentation='ReportingCurrencyAmortisedCostPriceSpecifies the price expressed in the reporting currency of the asset valued by using the amortised cost method.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 144, 12)))

AmortisedCostMethodPriceDeviationEvent1__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NbOfDaysDvtn'), Max3Number, scope=AmortisedCostMethodPriceDeviationEvent1__1, documentation='NumberOfDaysDeviationSpecifies the number of days the price of an asset calculated in accordance with the mark-to-market or mark-to-model method deviates from the asset price calculated in accordance with the amortised cost method by more than 10 basis points.\r\n', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 150, 12)))

AmortisedCostMethodPriceDeviationEvent1__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AvrgBsisPtSprd'), DecimalNumber, scope=AmortisedCostMethodPriceDeviationEvent1__1, documentation='AverageBasisPointSpreadProvides the average number of basis points added to (if positive) or deducted from (if negative) the price of an asset calculated in accordance with the mark-to-market or mark-to-model method to calculate the asset price calculated in accordance with the amortised cost method when the two asset prices deviates by more than 10 basis points.\r\nUsed to express differences in interest rates, for example, a difference of 0.10 % is equivalent to a change of 10 basis points.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 157, 12)))

AmortisedCostMethodPriceDeviationEvent1__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LwstPricDvtn'), Max5Number, scope=AmortisedCostMethodPriceDeviationEvent1__1, documentation='LowestPriceDeviationMinimum price deviation between the price of an asset calculated in accordance with the mark-to-market or mark-to-model method and the asset price calculated in accordance with the amortised cost method.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 164, 12)))

AmortisedCostMethodPriceDeviationEvent1__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'HghstPricDvtn'), Max5Number, scope=AmortisedCostMethodPriceDeviationEvent1__1, documentation='HighestPriceDeviationMaximum price deviation between the price of an asset calculated in accordance with the mark-to-market or mark-to-model method and the asset price calculated in accordance with the amortised cost method.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 170, 12)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AmortisedCostMethodPriceDeviationEvent1__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ValtnDt')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 125, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AmortisedCostMethodPriceDeviationEvent1__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AsstId')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 131, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AmortisedCostMethodPriceDeviationEvent1__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RptgCcyMktPric')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 138, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AmortisedCostMethodPriceDeviationEvent1__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RptgCcyAmtsdCostPric')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 144, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AmortisedCostMethodPriceDeviationEvent1__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NbOfDaysDvtn')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 150, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AmortisedCostMethodPriceDeviationEvent1__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AvrgBsisPtSprd')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 157, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AmortisedCostMethodPriceDeviationEvent1__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'LwstPricDvtn')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 164, 12))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(AmortisedCostMethodPriceDeviationEvent1__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'HghstPricDvtn')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 170, 12))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
AmortisedCostMethodPriceDeviationEvent1__1._Automaton = _BuildAutomaton_()




AssetIdentification3__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ClssfctnTp'), CFIOct2015Identifier, scope=AssetIdentification3__1, documentation='ClassificationTypeClassification type of the financial instrument, as per the ISO classification of financial instrument (CFI) codification, that is common share with voting rights, fully paid, or registered.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 301, 12)))

AssetIdentification3__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'InstrmId'), InstrumentIdentification4Choice__1, scope=AssetIdentification3__1, documentation='InstrumentIdentificationIdentification of the instrument held by the money market fund.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 307, 12)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AssetIdentification3__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ClssfctnTp')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 301, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(AssetIdentification3__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'InstrmId')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 307, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
AssetIdentification3__1._Automaton = _BuildAutomaton_2()




AssetIdentification3__2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ClssfctnTp'), CFIOct2015Identifier, scope=AssetIdentification3__2, documentation='ClassificationTypeClassification type of the financial instrument, as per the ISO classification of financial instrument (CFI) codification, that is common share with voting rights, fully paid, or registered.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 321, 12)))

AssetIdentification3__2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'InstrmId'), InstrumentIdentification4Choice__2, scope=AssetIdentification3__2, documentation='InstrumentIdentificationIdentification of the instrument held by the money market fund.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 327, 12)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AssetIdentification3__2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ClssfctnTp')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 321, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(AssetIdentification3__2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'InstrmId')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 327, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
AssetIdentification3__2._Automaton = _BuildAutomaton_3()




AssetIdentification3__3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ClssfctnTp'), CFIOct2015Identifier, scope=AssetIdentification3__3, documentation='ClassificationTypeClassification type of the financial instrument, as per the ISO classification of financial instrument (CFI) codification, that is common share with voting rights, fully paid, or registered.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 341, 12)))

AssetIdentification3__3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'InstrmId'), InstrumentIdentification4Choice__1, scope=AssetIdentification3__3, documentation='InstrumentIdentificationIdentification of the instrument held by the money market fund.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 347, 12)))

AssetIdentification3__3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AsstLEI'), LEIIdentifier, scope=AssetIdentification3__3, documentation='AssetLEILegal entity identification of the fund as an alternate identification for a party.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 353, 12)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 353, 12))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AssetIdentification3__3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ClssfctnTp')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 341, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(AssetIdentification3__3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'InstrmId')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 347, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AssetIdentification3__3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AsstLEI')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 353, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
AssetIdentification3__3._Automaton = _BuildAutomaton_4()




AssetIdentification3__4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'InstrmId'), InstrumentIdentification4Choice__3, scope=AssetIdentification3__4, documentation='InstrumentIdentificationIdentification of the instrument held by the money market fund.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 367, 12)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(AssetIdentification3__4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'InstrmId')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 367, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
AssetIdentification3__4._Automaton = _BuildAutomaton_5()




AssetValuation2__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MtrtyDt'), ISODate, scope=AssetValuation2__1, documentation='MaturityDatePlanned final repayment date at the time of issuance.\r\nThe maturity date has to be reported for the money market instruments, the securitisations, asset backed commercial papers and financial derivatives.\r\n', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 381, 12)))

AssetValuation2__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NtnlCcyFrstLeg'), ActiveOrHistoricCurrencyCode, scope=AssetValuation2__1, documentation='NotionalCurrencyFirstLegCurrency of the financial instrument.\r\nThe currency first leg has to be reported for the money market instruments, the securitisations, asset backed commercial papers, deposits or ancillary services, repurchase agreements, reverse repurchase agreements, financial derivatives and shares or units of other funds.\r\nUsage: In the case of an interest rate or currency derivative contract, this will be the notional currency of first leg.\r\n', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 389, 12)))

AssetValuation2__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Qty'), FinancialInstrumentQuantity1Choice__1, scope=AssetValuation2__1, documentation='QuantityQuantity of the financial instrument held by the fund.\r\nThe quantity has to be reported for the money market instruments, the securitisations, asset backed commercial papers and shares or units of other funds.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 398, 12)))

AssetValuation2__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Pric'), CurrencyExchange1Choice__1, scope=AssetValuation2__1, documentation='PricePrice of the asset expressed as a clean price for the money market instruments, the securitisations or asset backed commercial papers. and as a net asset value per unit or share for other money market funds.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 405, 12)))

AssetValuation2__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AcrdIntrst'), CurrencyExchange1Choice__1, scope=AssetValuation2__1, documentation='AccruedInterestInterest amount that has accrued in between coupon payment periods.\r\n', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 411, 12)))

AssetValuation2__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TtlVal'), CurrencyExchange1Choice__1, scope=AssetValuation2__1, documentation='TotalValueThe end-of period total market value in base currency of the financial instrument in which the money market fund has invested.\r\nthe total value has to be reported for the money market instruments, the securitisations, asset backed commercial papers, the financial derivatives, the shares or units of other funds, the repurchase agreements and reverse repurchase agreements.\r\n', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 418, 12)))

AssetValuation2__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ValtnTp'), ValuationType2Code, scope=AssetValuation2__1, documentation='ValuationTypeIndicate whether valuation was performed mark to market, mark to model or in accordance with the cost amortised method.\r\nThe valuation type has to be reported for the money market instruments, securitisations and asset backed commercial papers.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 426, 12)))

AssetValuation2__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CdtAssmntRslt'), AssessmentResultType2Code, scope=AssetValuation2__1, documentation='CreditAssessmentResultSpecifies whether the credit assessment is favourable or unfavourable.\r\nThe credit assessment result has to be provided for the money market instruments, the securitisations and asset backed commercial papers and the repurchase agreements.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 433, 12)))

AssetValuation2__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RstDt'), ISODate, scope=AssetValuation2__1, documentation='ResetDateDate at which the interest rate of an interest bearing instrument will be reset, according to the terms of the issue.\r\nThe reset date has to be reported for money market instruments and financial derivatives.\r\n', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 440, 12)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 440, 12))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AssetValuation2__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'MtrtyDt')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 381, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AssetValuation2__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NtnlCcyFrstLeg')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 389, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AssetValuation2__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Qty')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 398, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AssetValuation2__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Pric')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 405, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AssetValuation2__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AcrdIntrst')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 411, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AssetValuation2__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TtlVal')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 418, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AssetValuation2__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ValtnTp')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 426, 12))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(AssetValuation2__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CdtAssmntRslt')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 433, 12))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AssetValuation2__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RstDt')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 440, 12))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
         ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_8._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
AssetValuation2__1._Automaton = _BuildAutomaton_6()




AssetValuation2__2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MtrtyDt'), ISODate, scope=AssetValuation2__2, documentation='MaturityDatePlanned final repayment date at the time of issuance.\r\nThe maturity date has to be reported for the money market instruments, the securitisations, asset backed commercial papers and financial derivatives.\r\n', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 456, 12)))

AssetValuation2__2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NtnlCcyFrstLeg'), ActiveOrHistoricCurrencyCode, scope=AssetValuation2__2, documentation='NotionalCurrencyFirstLegCurrency of the financial instrument.\r\nThe currency first leg has to be reported for the money market instruments, the securitisations, asset backed commercial papers, deposits or ancillary services, repurchase agreements, reverse repurchase agreements, financial derivatives and shares or units of other funds.\r\nUsage: In the case of an interest rate or currency derivative contract, this will be the notional currency of first leg.\r\n', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 464, 12)))

AssetValuation2__2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Qty'), FinancialInstrumentQuantity1Choice__1, scope=AssetValuation2__2, documentation='QuantityQuantity of the financial instrument held by the fund.\r\nThe quantity has to be reported for the money market instruments, the securitisations, asset backed commercial papers and shares or units of other funds.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 473, 12)))

AssetValuation2__2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Pric'), CurrencyExchange1Choice__1, scope=AssetValuation2__2, documentation='PricePrice of the asset expressed as a clean price for the money market instruments, the securitisations or asset backed commercial papers. and as a net asset value per unit or share for other money market funds.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 480, 12)))

AssetValuation2__2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AcrdIntrst'), CurrencyExchange1Choice__1, scope=AssetValuation2__2, documentation='AccruedInterestInterest amount that has accrued in between coupon payment periods.\r\n', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 486, 12)))

AssetValuation2__2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TtlVal'), CurrencyExchange1Choice__1, scope=AssetValuation2__2, documentation='TotalValueThe end-of period total market value in base currency of the financial instrument in which the money market fund has invested.\r\nthe total value has to be reported for the money market instruments, the securitisations, asset backed commercial papers, the financial derivatives, the shares or units of other funds, the repurchase agreements and reverse repurchase agreements.\r\n', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 493, 12)))

AssetValuation2__2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ValtnTp'), ValuationType2Code, scope=AssetValuation2__2, documentation='ValuationTypeIndicate whether valuation was performed mark to market, mark to model or in accordance with the cost amortised method.\r\nThe valuation type has to be reported for the money market instruments, securitisations and asset backed commercial papers.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 501, 12)))

AssetValuation2__2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CdtAssmntRslt'), AssessmentResultType2Code, scope=AssetValuation2__2, documentation='CreditAssessmentResultSpecifies whether the credit assessment is favourable or unfavourable.\r\nThe credit assessment result has to be provided for the money market instruments, the securitisations and asset backed commercial papers and the repurchase agreements.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 508, 12)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AssetValuation2__2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'MtrtyDt')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 456, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AssetValuation2__2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NtnlCcyFrstLeg')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 464, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AssetValuation2__2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Qty')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 473, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AssetValuation2__2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Pric')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 480, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AssetValuation2__2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AcrdIntrst')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 486, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AssetValuation2__2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TtlVal')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 493, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AssetValuation2__2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ValtnTp')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 501, 12))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(AssetValuation2__2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CdtAssmntRslt')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 508, 12))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
AssetValuation2__2._Automaton = _BuildAutomaton_7()




AssetValuation2__3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MtrtyDt'), ISODate, scope=AssetValuation2__3, documentation='MaturityDatePlanned final repayment date at the time of issuance.\r\nThe maturity date has to be reported for the money market instruments, the securitisations, asset backed commercial papers and financial derivatives.\r\n', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 523, 12)))

AssetValuation2__3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NtnlCcyFrstLeg'), ActiveOrHistoricCurrencyCode, scope=AssetValuation2__3, documentation='NotionalCurrencyFirstLegCurrency of the financial instrument.\r\nThe currency first leg has to be reported for the money market instruments, the securitisations, asset backed commercial papers, deposits or ancillary services, repurchase agreements, reverse repurchase agreements, financial derivatives and shares or units of other funds.\r\nUsage: In the case of an interest rate or currency derivative contract, this will be the notional currency of first leg.\r\n', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 531, 12)))

AssetValuation2__3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NtnlCcyScndLeg'), ActiveOrHistoricCurrencyCode, scope=AssetValuation2__3, documentation='NotionalCurrencySecondLegOther currency of the notional amount. \r\nThe currency second leg has to be reported for the financial derivatives with two currencies.\r\nUsage: In the case of an interest rate or currency derivative contract, this will be the notional currency of the second leg.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 540, 12)))

AssetValuation2__3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TtlVal'), CurrencyExchange1Choice__1, scope=AssetValuation2__3, documentation='TotalValueThe end-of period total market value in base currency of the financial instrument in which the money market fund has invested.\r\nthe total value has to be reported for the money market instruments, the securitisations, asset backed commercial papers, the financial derivatives, the shares or units of other funds, the repurchase agreements and reverse repurchase agreements.\r\n', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 548, 12)))

AssetValuation2__3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'XpsrVal'), CurrencyExchange1Choice__1, scope=AssetValuation2__3, documentation='ExposureValueExposure of the financial derivative instrument, the repurchase agreement, reverse repurchase agreement and the deposit or ancillary liquid assets. in the case of the reverse repurchase agreements, this is the amount of cash provided to the counterparty.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 556, 12)))

AssetValuation2__3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CollVal'), CurrencyExchange1Choice__1, scope=AssetValuation2__3, documentation='CollateralValueValue of the collateral at the end-of-period after taking into account the haircut.\r\nThe collateral value has to be reported for financial derivatives, repurchase agreements and reverse repurchase agreements. This is the amount of cash received by the fund as part of the repurchase agreements.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 562, 12)))

AssetValuation2__3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RstDt'), ISODate, scope=AssetValuation2__3, documentation='ResetDateDate at which the interest rate of an interest bearing instrument will be reset, according to the terms of the issue.\r\nThe reset date has to be reported for money market instruments and financial derivatives.\r\n', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 569, 12)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 540, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 569, 12))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AssetValuation2__3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'MtrtyDt')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 523, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AssetValuation2__3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NtnlCcyFrstLeg')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 531, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AssetValuation2__3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NtnlCcyScndLeg')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 540, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AssetValuation2__3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TtlVal')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 548, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AssetValuation2__3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'XpsrVal')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 556, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(AssetValuation2__3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CollVal')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 562, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(AssetValuation2__3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RstDt')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 569, 12))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
AssetValuation2__3._Automaton = _BuildAutomaton_8()




AssetValuation2__4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NtnlCcyFrstLeg'), ActiveOrHistoricCurrencyCode, scope=AssetValuation2__4, documentation='NotionalCurrencyFirstLegCurrency of the financial instrument.\r\nThe currency first leg has to be reported for the money market instruments, the securitisations, asset backed commercial papers, deposits or ancillary services, repurchase agreements, reverse repurchase agreements, financial derivatives and shares or units of other funds.\r\nUsage: In the case of an interest rate or currency derivative contract, this will be the notional currency of first leg.\r\n', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 585, 12)))

AssetValuation2__4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Qty'), FinancialInstrumentQuantity1Choice__1, scope=AssetValuation2__4, documentation='QuantityQuantity of the financial instrument held by the fund.\r\nThe quantity has to be reported for the money market instruments, the securitisations, asset backed commercial papers and shares or units of other funds.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 594, 12)))

AssetValuation2__4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Pric'), CurrencyExchange1Choice__1, scope=AssetValuation2__4, documentation='PricePrice of the asset expressed as a clean price for the money market instruments, the securitisations or asset backed commercial papers. and as a net asset value per unit or share for other money market funds.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 601, 12)))

AssetValuation2__4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TtlVal'), CurrencyExchange1Choice__1, scope=AssetValuation2__4, documentation='TotalValueThe end-of period total market value in base currency of the financial instrument in which the money market fund has invested.\r\nthe total value has to be reported for the money market instruments, the securitisations, asset backed commercial papers, the financial derivatives, the shares or units of other funds, the repurchase agreements and reverse repurchase agreements.\r\n', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 607, 12)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AssetValuation2__4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NtnlCcyFrstLeg')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 585, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AssetValuation2__4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Qty')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 594, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AssetValuation2__4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Pric')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 601, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(AssetValuation2__4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TtlVal')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 607, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
AssetValuation2__4._Automaton = _BuildAutomaton_9()




AssetValuation2__5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MtrtyDt'), ISODate, scope=AssetValuation2__5, documentation='MaturityDatePlanned final repayment date at the time of issuance.\r\nThe maturity date has to be reported for the money market instruments, the securitisations, asset backed commercial papers and financial derivatives.\r\n', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 623, 12)))

AssetValuation2__5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NtnlCcyFrstLeg'), ActiveOrHistoricCurrencyCode, scope=AssetValuation2__5, documentation='NotionalCurrencyFirstLegCurrency of the financial instrument.\r\nThe currency first leg has to be reported for the money market instruments, the securitisations, asset backed commercial papers, deposits or ancillary services, repurchase agreements, reverse repurchase agreements, financial derivatives and shares or units of other funds.\r\nUsage: In the case of an interest rate or currency derivative contract, this will be the notional currency of first leg.\r\n', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 631, 12)))

AssetValuation2__5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'XpsrVal'), CurrencyExchange1Choice__1, scope=AssetValuation2__5, documentation='ExposureValueExposure of the financial derivative instrument, the repurchase agreement, reverse repurchase agreement and the deposit or ancillary liquid assets. in the case of the reverse repurchase agreements, this is the amount of cash provided to the counterparty.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 640, 12)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AssetValuation2__5._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'MtrtyDt')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 623, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AssetValuation2__5._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NtnlCcyFrstLeg')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 631, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(AssetValuation2__5._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'XpsrVal')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 640, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
AssetValuation2__5._Automaton = _BuildAutomaton_10()




AssetValuation2__6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MtrtyDt'), ISODate, scope=AssetValuation2__6, documentation='MaturityDatePlanned final repayment date at the time of issuance.\r\nThe maturity date has to be reported for the money market instruments, the securitisations, asset backed commercial papers and financial derivatives.\r\n', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 654, 12)))

AssetValuation2__6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NtnlCcyFrstLeg'), ActiveOrHistoricCurrencyCode, scope=AssetValuation2__6, documentation='NotionalCurrencyFirstLegCurrency of the financial instrument.\r\nThe currency first leg has to be reported for the money market instruments, the securitisations, asset backed commercial papers, deposits or ancillary services, repurchase agreements, reverse repurchase agreements, financial derivatives and shares or units of other funds.\r\nUsage: In the case of an interest rate or currency derivative contract, this will be the notional currency of first leg.\r\n', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 662, 12)))

AssetValuation2__6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'XpsrVal'), CurrencyExchange1Choice__1, scope=AssetValuation2__6, documentation='ExposureValueExposure of the financial derivative instrument, the repurchase agreement, reverse repurchase agreement and the deposit or ancillary liquid assets. in the case of the reverse repurchase agreements, this is the amount of cash provided to the counterparty.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 671, 12)))

AssetValuation2__6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CollVal'), CurrencyExchange1Choice__1, scope=AssetValuation2__6, documentation='CollateralValueValue of the collateral at the end-of-period after taking into account the haircut.\r\nThe collateral value has to be reported for financial derivatives, repurchase agreements and reverse repurchase agreements. This is the amount of cash received by the fund as part of the repurchase agreements.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 677, 12)))

AssetValuation2__6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CdtAssmntRslt'), AssessmentResultType2Code, scope=AssetValuation2__6, documentation='CreditAssessmentResultSpecifies whether the credit assessment is favourable or unfavourable.\r\nThe credit assessment result has to be provided for the money market instruments, the securitisations and asset backed commercial papers and the repurchase agreements.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 684, 12)))

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AssetValuation2__6._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'MtrtyDt')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 654, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AssetValuation2__6._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NtnlCcyFrstLeg')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 662, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AssetValuation2__6._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'XpsrVal')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 671, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AssetValuation2__6._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CollVal')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 677, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(AssetValuation2__6._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CdtAssmntRslt')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 684, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
AssetValuation2__6._Automaton = _BuildAutomaton_11()




BreakdownByArrangement2__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ArrgmntTp'), ArrangementType4Code, scope=BreakdownByArrangement2__1, documentation='ArrangementTypeIndicates the types of arrangement to which the fund is subject on.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 709, 12)))

BreakdownByArrangement2__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NetAsstValRate'), PercentageBoundedRate, scope=BreakdownByArrangement2__1, documentation='NetAssetValueRatePortion of the net asset value subject to the arrangement type.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 715, 12)))

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BreakdownByArrangement2__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ArrgmntTp')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 709, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(BreakdownByArrangement2__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NetAsstValRate')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 715, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
BreakdownByArrangement2__1._Automaton = _BuildAutomaton_12()




BreakdownByCountry4__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CtryOfRes'), Country1Choice__3, scope=BreakdownByCountry4__1, documentation="CountryOfResidenceCountry in which a person resides (the place of a person's home). In the case of a company, it is the country from which the affairs of that company are directed.", location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 729, 12)))

BreakdownByCountry4__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Rate'), PercentageBoundedRate, scope=BreakdownByCountry4__1, documentation='RateSpecifies the percentage of the net asset value by country of domicile of investors.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 735, 12)))

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BreakdownByCountry4__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CtryOfRes')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 729, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(BreakdownByCountry4__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Rate')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 735, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
BreakdownByCountry4__1._Automaton = _BuildAutomaton_13()




ConstantNetAssetValueDeviationEvent1__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ValtnDt'), ISODate, scope=ConstantNetAssetValueDeviationEvent1__1, documentation='ValuationDateDate from which the price of an asset calculated in accordance with the mark-to-market or mark-to-model method deviates from the asset price calculated in accordance with the amortised cost method by more than 10 basis points.\r\n', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 758, 12)))

ConstantNetAssetValueDeviationEvent1__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CstNetAsstValPerUnit'), CurrencyExchange14__1, scope=ConstantNetAssetValueDeviationEvent1__1, documentation='ConstantNetAssetValuePerUnitConstant net asset value at the valuation date of a specific investment fund class calculated in accordance with the amortised cost method divided by the number of outstanding units or shares of the fund.\r\n', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 765, 12)))

ConstantNetAssetValueDeviationEvent1__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NetAsstValPerUnit'), CurrencyExchange14__1, scope=ConstantNetAssetValueDeviationEvent1__1, documentation="NetAssetValuePerUnitNet asset value at the valuation date of all the holdings, less the fund's liabilities, attributable to a specific investment fund class calculated in accordance with mark-to-market or mark-to-model divided by the number of outstanding units or shares of the fund.\r\n", location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 772, 12)))

ConstantNetAssetValueDeviationEvent1__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NbOfDaysDvtn'), Max3Number, scope=ConstantNetAssetValueDeviationEvent1__1, documentation='NumberOfDaysDeviationNumber of days the net asset value deviates from the constant net asset value per unit or share by more than 20 basis points.\r\n', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 779, 12)))

ConstantNetAssetValueDeviationEvent1__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AvrgBsisPtSprd'), DecimalNumber, scope=ConstantNetAssetValueDeviationEvent1__1, documentation='AverageBasisPointSpreadAverage number of basis points added to (if positive) or deducted from (if negative) the net asset value to calculate the constant net asset value per unit or share when the net asset value deviates from the constant net asset value per unit or share by more than 20 basis points.\r\nUsed to express differences in interest rates, for example, a difference of 0.10 % is equivalent to a change of 10 basis points.\r\r\n\r\r\r\n', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 786, 12)))

ConstantNetAssetValueDeviationEvent1__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LwstPricDvtn'), Max5Number, scope=ConstantNetAssetValueDeviationEvent1__1, documentation='LowestPriceDeviationMinimum price deviation between the net asset value and the constant net asset value per unit or share.\r\n', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 795, 12)))

ConstantNetAssetValueDeviationEvent1__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'HghstPricDvtn'), Max5Number, scope=ConstantNetAssetValueDeviationEvent1__1, documentation='HighestPriceDeviationMaximum price deviation between the net asset value and the constant net asset value per unit or share.\r\n', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 802, 12)))

def _BuildAutomaton_14 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ConstantNetAssetValueDeviationEvent1__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ValtnDt')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 758, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ConstantNetAssetValueDeviationEvent1__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CstNetAsstValPerUnit')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 765, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ConstantNetAssetValueDeviationEvent1__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NetAsstValPerUnit')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 772, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ConstantNetAssetValueDeviationEvent1__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NbOfDaysDvtn')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 779, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ConstantNetAssetValueDeviationEvent1__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AvrgBsisPtSprd')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 786, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ConstantNetAssetValueDeviationEvent1__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'LwstPricDvtn')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 795, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ConstantNetAssetValueDeviationEvent1__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'HghstPricDvtn')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 802, 12))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ConstantNetAssetValueDeviationEvent1__1._Automaton = _BuildAutomaton_14()




Country1Choice__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Ctry'), CountryCode, scope=Country1Choice__1, documentation='CountryCode to identify a country, a dependency, or another area of particular geopolitical interest, on the basis of country names obtained from the United Nations (ISO 3166, Alpha-2 code).', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 817, 12)))

def _BuildAutomaton_15 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Country1Choice__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Ctry')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 817, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Country1Choice__1._Automaton = _BuildAutomaton_15()




Country1Choice__2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Ctry'), CountryCode, scope=Country1Choice__2, documentation='CountryCode to identify a country, a dependency, or another area of particular geopolitical interest, on the basis of country names obtained from the United Nations (ISO 3166, Alpha-2 code).', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 831, 12)))

Country1Choice__2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SprntnlCtry'), TrueFalseIndicator_fixed__1, scope=Country1Choice__2, documentation='SupranationalCountrySpecifies that no predominant geographical focus is possible.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 837, 12)))

def _BuildAutomaton_16 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_16
    del _BuildAutomaton_16
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Country1Choice__2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Ctry')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 831, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Country1Choice__2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SprntnlCtry')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 837, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Country1Choice__2._Automaton = _BuildAutomaton_16()




Country1Choice__3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Ctry'), CountryCode, scope=Country1Choice__3, documentation='CountryCode to identify a country, a dependency, or another area of particular geopolitical interest, on the basis of country names obtained from the United Nations (ISO 3166, Alpha-2 code).', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 851, 12)))

Country1Choice__3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SprntnlCtry'), TrueFalseIndicator_fixed__1, scope=Country1Choice__3, documentation='SupranationalCountrySpecifies that no predominant geographical focus is possible.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 857, 12)))

Country1Choice__3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'UknwnCtry'), TrueFalseIndicator_fixed__1, scope=Country1Choice__3, documentation='UnknownCountrySpecifies that the country is not known.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 863, 12)))

def _BuildAutomaton_17 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_17
    del _BuildAutomaton_17
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Country1Choice__3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Ctry')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 851, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Country1Choice__3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SprntnlCtry')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 857, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Country1Choice__3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'UknwnCtry')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 863, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Country1Choice__3._Automaton = _BuildAutomaton_17()




CurrencyExchange14__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BaseCcyAmt'), ImpliedCurrencyAndAmount, scope=CurrencyExchange14__1, documentation='BaseCurrencyAmountAmount in the base currency of the fund.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 886, 12)))

CurrencyExchange14__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RptgCcyAmt'), ActiveCurrencyAndAmount__1, scope=CurrencyExchange14__1, documentation='ReportingCurrencyAmountAmount expressed in the reporting currency.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 892, 12)))

def _BuildAutomaton_18 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_18
    del _BuildAutomaton_18
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 892, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CurrencyExchange14__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'BaseCcyAmt')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 886, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CurrencyExchange14__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RptgCcyAmt')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 892, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CurrencyExchange14__1._Automaton = _BuildAutomaton_18()




CurrencyExchange1Choice__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Amt'), CurrencyExchange14__1, scope=CurrencyExchange1Choice__1, documentation='AmountAmount value.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 906, 12)))

CurrencyExchange1Choice__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NotAvlblVal'), NotAvailable1Code, scope=CurrencyExchange1Choice__1, documentation='NotAvailableValueThe value is not available.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 912, 12)))

def _BuildAutomaton_19 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_19
    del _BuildAutomaton_19
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CurrencyExchange1Choice__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Amt')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 906, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CurrencyExchange1Choice__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NotAvlblVal')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 912, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CurrencyExchange1Choice__1._Automaton = _BuildAutomaton_19()




DerivativeInstrument8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CtrctTp'), FinancialInstrumentContractType3Code, scope=DerivativeInstrument8, documentation='ContractTypeClassification of information according to contract type.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 936, 12)))

DerivativeInstrument8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'UndrlygTp'), UnderlyingDerivativeType2Code, scope=DerivativeInstrument8, documentation='UnderlyingTypeSpecifies the information related to the underlying instrument of the derivatives.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 942, 12)))

DerivativeInstrument8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'UndrlygId'), SecurityIdentification31Choice, scope=DerivativeInstrument8, documentation='UnderlyingIdentificationUnique identification to identify the direct underlying instrument.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 948, 12)))

def _BuildAutomaton_20 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_20
    del _BuildAutomaton_20
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DerivativeInstrument8._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CtrctTp')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 936, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DerivativeInstrument8._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'UndrlygTp')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 942, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(DerivativeInstrument8._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'UndrlygId')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 948, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
DerivativeInstrument8._Automaton = _BuildAutomaton_20()




Document_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MnyMktFndRpt'), MoneyMarketFundReportV01, scope=Document_, location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 958, 12)))

def _BuildAutomaton_21 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_21
    del _BuildAutomaton_21
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Document_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'MnyMktFndRpt')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 958, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Document_._Automaton = _BuildAutomaton_21()




FinancialInstrument60Choice__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NoShrClssInf'), ShareClassList1__1, scope=FinancialInstrument60Choice__1, documentation='NoShareClassInformationInformation on the identification of the fund when the fund is not divided into several share classes.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1131, 12)))

FinancialInstrument60Choice__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ShrClssList'), ShareClassList1__2, scope=FinancialInstrument60Choice__1, documentation='ShareClassListInformation on the share classes of the fund when the fund has several share classes.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1137, 12)))

def _BuildAutomaton_22 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_22
    del _BuildAutomaton_22
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(FinancialInstrument60Choice__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NoShrClssInf')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1131, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(FinancialInstrument60Choice__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ShrClssList')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1137, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
FinancialInstrument60Choice__1._Automaton = _BuildAutomaton_22()




FinancialInstrument80__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'FinInstrmId'), InstrumentIdentification3Choice__1, scope=FinancialInstrument80__1, documentation='FinancialInstrumentIdentificationIdentification of the fund.\r\n', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1152, 12)))

FinancialInstrument80__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DrgtnRcvdAssts'), TrueFalseIndicator, scope=FinancialInstrument80__1, documentation='DerogationReceivedAssetsIn the context of the reverse repurchase agreements, indicates whether there are any non-authorised assets that were received by the fund by derogation with the local regulation.\r\n', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1159, 12)))

FinancialInstrument80__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TtlVal'), CurrencyExchange14__1, scope=FinancialInstrument80__1, documentation='TotalValueTotal market value of the assets received by the money market fund in the context of a reverse repurchase agreement.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1166, 12)))

def _BuildAutomaton_23 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_23
    del _BuildAutomaton_23
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(FinancialInstrument80__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'FinInstrmId')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1152, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(FinancialInstrument80__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DrgtnRcvdAssts')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1159, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(FinancialInstrument80__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TtlVal')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1166, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
FinancialInstrument80__1._Automaton = _BuildAutomaton_23()




FinancialInstrument82__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'FndNttyId'), PartyIdentification212__1, scope=FinancialInstrument82__1, documentation='FundEntityIdentificationIdentification of the money market fund.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1180, 12)))

FinancialInstrument82__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'FndMgmtCpny'), PartyIdentification195__1, scope=FinancialInstrument82__1, documentation='FundManagementCompanyCompany that is responsible for the management and operation of the fund, eg, determines the investment strategy, appoints the service providers, and makes major decisions for the fund. It is usually responsible for the distribution and marketing of the fund. For self-managed funds, this will often be a separate promoter or sponsor of the fund.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1186, 12)))

FinancialInstrument82__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'FndAttrbts'), FinancialInstrumentAttributes101__1, scope=FinancialInstrument82__1, documentation='FundAttributesAttributes defining further details on the fund financial instrument.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1192, 12)))

def _BuildAutomaton_24 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_24
    del _BuildAutomaton_24
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(FinancialInstrument82__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'FndNttyId')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1180, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(FinancialInstrument82__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'FndMgmtCpny')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1186, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(FinancialInstrument82__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'FndAttrbts')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1192, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
FinancialInstrument82__1._Automaton = _BuildAutomaton_24()




FinancialInstrumentAttributes101__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Nm'), Max350Text, scope=FinancialInstrumentAttributes101__1, documentation='NameName of the financial instrument in free format text.\r\n', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1207, 12)))

FinancialInstrumentAttributes101__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LglFrmwk'), LegalFramework5Choice__1, scope=FinancialInstrumentAttributes101__1, documentation='LegalFrameworkLegal framework of the fund.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1214, 12)))

FinancialInstrumentAttributes101__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'StffWthSvgsPlan'), TrueFalseIndicator, scope=FinancialInstrumentAttributes101__1, documentation='StaffWithSavingsPlanIndicates whether the fund is attributed to a staff member with a savings plan.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1220, 12)))

FinancialInstrumentAttributes101__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RegdDstrbtnCtry'), RegisteredDistributionCountry2Choice__1, scope=FinancialInstrumentAttributes101__1, documentation='RegisteredDistributionCountryCountries where the fund is registered for distribution.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1226, 12)))

FinancialInstrumentAttributes101__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BaseCcy'), ActiveOrHistoricCurrencyCode, scope=FinancialInstrumentAttributes101__1, documentation='BaseCurrencyCurrency of the investment fund class.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1232, 12)))

FinancialInstrumentAttributes101__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DpstryId'), PartyIdentification212__2, scope=FinancialInstrumentAttributes101__1, documentation='DepositoryIdentificationProvides information about identification of the depository.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1238, 12)))

FinancialInstrumentAttributes101__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MnyMktFndTp'), MoneyMarketFundType1Choice__1, scope=FinancialInstrumentAttributes101__1, documentation='MoneyMarketFundTypeSpecifies the type of the money market fund.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1244, 12)))

FinancialInstrumentAttributes101__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MstrFnd'), MasterFundType1Code, scope=FinancialInstrumentAttributes101__1, documentation='MasterFundIndicates whether the fund is a master or a feeder fund.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1250, 12)))

FinancialInstrumentAttributes101__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MstrFndList'), PartyIdentification212__3, scope=FinancialInstrumentAttributes101__1, documentation='MasterFundListProvides information about identification of the master fund(s).\r\n', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1256, 12)))

FinancialInstrumentAttributes101__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ShrClssInd'), TrueFalseIndicator, scope=FinancialInstrumentAttributes101__1, documentation='ShareClassIndicatorIndicates whether the fund has share classes.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1263, 12)))

FinancialInstrumentAttributes101__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ShrClss'), FinancialInstrument60Choice__1, scope=FinancialInstrumentAttributes101__1, documentation='ShareClassInformation on the sub-fund or share classes of the fund.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1269, 12)))

FinancialInstrumentAttributes101__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'FndRltdEvt'), RelatedEvent2, scope=FinancialInstrumentAttributes101__1, documentation='FundRelatedEventSpecifies the dates in relation with the money market fund life cycle.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1275, 12)))

def _BuildAutomaton_25 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_25
    del _BuildAutomaton_25
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1256, 12))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(FinancialInstrumentAttributes101__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Nm')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1207, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(FinancialInstrumentAttributes101__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'LglFrmwk')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1214, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(FinancialInstrumentAttributes101__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'StffWthSvgsPlan')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1220, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(FinancialInstrumentAttributes101__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RegdDstrbtnCtry')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1226, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(FinancialInstrumentAttributes101__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'BaseCcy')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1232, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(FinancialInstrumentAttributes101__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DpstryId')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1238, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(FinancialInstrumentAttributes101__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'MnyMktFndTp')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1244, 12))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(FinancialInstrumentAttributes101__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'MstrFnd')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1250, 12))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(FinancialInstrumentAttributes101__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'MstrFndList')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1256, 12))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(FinancialInstrumentAttributes101__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ShrClssInd')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1263, 12))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(FinancialInstrumentAttributes101__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ShrClss')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1269, 12))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(FinancialInstrumentAttributes101__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'FndRltdEvt')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1275, 12))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
         ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
         ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    st_11._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
FinancialInstrumentAttributes101__1._Automaton = _BuildAutomaton_25()




FinancialInstrumentQuantity1Choice__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Unit'), NonNegativeDecimalNumber, scope=FinancialInstrumentQuantity1Choice__1, documentation='UnitQuantity expressed as a number, for example, a number of shares.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1362, 12)))

def _BuildAutomaton_26 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_26
    del _BuildAutomaton_26
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(FinancialInstrumentQuantity1Choice__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Unit')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1362, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
FinancialInstrumentQuantity1Choice__1._Automaton = _BuildAutomaton_26()




Financialinstrument81__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AsstTp'), FinancialAssetType2Code__1, scope=Financialinstrument81__1, documentation='AssetTypeSpecifies the type of financial assets.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1376, 12)))

Financialinstrument81__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AsstId'), AssetIdentification3__1, scope=Financialinstrument81__1, documentation='AssetIdentificationIdentification of the asset.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1382, 12)))

Financialinstrument81__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PtyData'), Party46Choice__1, scope=Financialinstrument81__1, documentation='PartyDataSpecifies further details of the party.\r\n', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1388, 12)))

Financialinstrument81__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AsstCtry'), Country1Choice__2, scope=Financialinstrument81__1, documentation='AssetCountryCountry of the asset as considered relevant under the Regulation.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1395, 12)))

Financialinstrument81__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AsstValtn'), AssetValuation2__1, scope=Financialinstrument81__1, documentation='AssetValuationInformation on the valuation of the assets.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1401, 12)))

def _BuildAutomaton_27 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_27
    del _BuildAutomaton_27
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Financialinstrument81__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AsstTp')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1376, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Financialinstrument81__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AsstId')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1382, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Financialinstrument81__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PtyData')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1388, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Financialinstrument81__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AsstCtry')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1395, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Financialinstrument81__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AsstValtn')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1401, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Financialinstrument81__1._Automaton = _BuildAutomaton_27()




Financialinstrument81__2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AsstTp'), FinancialAssetType2Code__2, scope=Financialinstrument81__2, documentation='AssetTypeSpecifies the type of financial assets.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1415, 12)))

Financialinstrument81__2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AsstId'), AssetIdentification3__1, scope=Financialinstrument81__2, documentation='AssetIdentificationIdentification of the asset.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1421, 12)))

Financialinstrument81__2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PtyData'), Party46Choice__2, scope=Financialinstrument81__2, documentation='PartyDataSpecifies further details of the party.\r\n', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1427, 12)))

Financialinstrument81__2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AsstCtry'), Country1Choice__2, scope=Financialinstrument81__2, documentation='AssetCountryCountry of the asset as considered relevant under the Regulation.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1434, 12)))

Financialinstrument81__2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AsstValtn'), AssetValuation2__2, scope=Financialinstrument81__2, documentation='AssetValuationInformation on the valuation of the assets.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1440, 12)))

Financialinstrument81__2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'FincgUndrlygTp'), FinancingUnderlyingType1Code, scope=Financialinstrument81__2, documentation='FinancingUnderlyingTypeUnderlying type of the financing instrument such as the asset backed commercial paper or securitisation.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1446, 12)))

def _BuildAutomaton_28 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_28
    del _BuildAutomaton_28
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Financialinstrument81__2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AsstTp')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1415, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Financialinstrument81__2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AsstId')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1421, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Financialinstrument81__2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PtyData')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1427, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Financialinstrument81__2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AsstCtry')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1434, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Financialinstrument81__2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AsstValtn')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1440, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Financialinstrument81__2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'FincgUndrlygTp')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1446, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Financialinstrument81__2._Automaton = _BuildAutomaton_28()




Financialinstrument81__3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AsstTp'), FinancialAssetType2Code__3, scope=Financialinstrument81__3, documentation='AssetTypeSpecifies the type of financial assets.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1460, 12)))

Financialinstrument81__3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AsstId'), AssetIdentification3__2, scope=Financialinstrument81__3, documentation='AssetIdentificationIdentification of the asset.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1466, 12)))

Financialinstrument81__3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PtyData'), Party46Choice__3, scope=Financialinstrument81__3, documentation='PartyDataSpecifies further details of the party.\r\n', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1472, 12)))

Financialinstrument81__3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AsstCtry'), Country1Choice__2, scope=Financialinstrument81__3, documentation='AssetCountryCountry of the asset as considered relevant under the Regulation.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1479, 12)))

Financialinstrument81__3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AsstValtn'), AssetValuation2__3, scope=Financialinstrument81__3, documentation='AssetValuationInformation on the valuation of the assets.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1485, 12)))

Financialinstrument81__3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DerivInstrmAttrbts'), DerivativeInstrument8, scope=Financialinstrument81__3, documentation='DerivativeInstrumentAttributesSpecifies the attributes specific for derivatives.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1491, 12)))

def _BuildAutomaton_29 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_29
    del _BuildAutomaton_29
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Financialinstrument81__3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AsstTp')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1460, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Financialinstrument81__3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AsstId')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1466, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Financialinstrument81__3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PtyData')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1472, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Financialinstrument81__3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AsstCtry')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1479, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Financialinstrument81__3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AsstValtn')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1485, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Financialinstrument81__3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DerivInstrmAttrbts')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1491, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Financialinstrument81__3._Automaton = _BuildAutomaton_29()




Financialinstrument81__4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AsstTp'), FinancialAssetType2Code__4, scope=Financialinstrument81__4, documentation='AssetTypeSpecifies the type of financial assets.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1505, 12)))

Financialinstrument81__4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AsstId'), AssetIdentification3__3, scope=Financialinstrument81__4, documentation='AssetIdentificationIdentification of the asset.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1511, 12)))

Financialinstrument81__4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AsstCtry'), Country1Choice__2, scope=Financialinstrument81__4, documentation='AssetCountryCountry of the asset as considered relevant under the Regulation.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1517, 12)))

Financialinstrument81__4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AsstValtn'), AssetValuation2__4, scope=Financialinstrument81__4, documentation='AssetValuationInformation on the valuation of the assets.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1523, 12)))

def _BuildAutomaton_30 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_30
    del _BuildAutomaton_30
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Financialinstrument81__4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AsstTp')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1505, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Financialinstrument81__4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AsstId')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1511, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Financialinstrument81__4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AsstCtry')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1517, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Financialinstrument81__4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AsstValtn')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1523, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Financialinstrument81__4._Automaton = _BuildAutomaton_30()




Financialinstrument81__5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AsstTp'), FinancialAssetType2Code__5, scope=Financialinstrument81__5, documentation='AssetTypeSpecifies the type of financial assets.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1537, 12)))

Financialinstrument81__5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AsstId'), AssetIdentification3__4, scope=Financialinstrument81__5, documentation='AssetIdentificationIdentification of the asset.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1543, 12)))

Financialinstrument81__5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PtyData'), Party46Choice__3, scope=Financialinstrument81__5, documentation='PartyDataSpecifies further details of the party.\r\n', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1549, 12)))

Financialinstrument81__5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AsstCtry'), Country1Choice__2, scope=Financialinstrument81__5, documentation='AssetCountryCountry of the asset as considered relevant under the Regulation.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1556, 12)))

Financialinstrument81__5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AsstValtn'), AssetValuation2__5, scope=Financialinstrument81__5, documentation='AssetValuationInformation on the valuation of the assets.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1562, 12)))

def _BuildAutomaton_31 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_31
    del _BuildAutomaton_31
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Financialinstrument81__5._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AsstTp')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1537, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Financialinstrument81__5._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AsstId')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1543, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Financialinstrument81__5._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PtyData')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1549, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Financialinstrument81__5._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AsstCtry')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1556, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Financialinstrument81__5._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AsstValtn')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1562, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Financialinstrument81__5._Automaton = _BuildAutomaton_31()




Financialinstrument81__6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AsstTp'), FinancialAssetType2Code__6, scope=Financialinstrument81__6, documentation='AssetTypeSpecifies the type of financial assets.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1576, 12)))

Financialinstrument81__6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AsstId'), AssetIdentification3__1, scope=Financialinstrument81__6, documentation='AssetIdentificationIdentification of the asset.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1582, 12)))

Financialinstrument81__6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PtyData'), Party46Choice__4, scope=Financialinstrument81__6, documentation='PartyDataSpecifies further details of the party.\r\n', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1588, 12)))

Financialinstrument81__6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AsstCtry'), Country1Choice__2, scope=Financialinstrument81__6, documentation='AssetCountryCountry of the asset as considered relevant under the Regulation.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1595, 12)))

Financialinstrument81__6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AsstValtn'), AssetValuation2__6, scope=Financialinstrument81__6, documentation='AssetValuationInformation on the valuation of the assets.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1601, 12)))

def _BuildAutomaton_32 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_32
    del _BuildAutomaton_32
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Financialinstrument81__6._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AsstTp')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1576, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Financialinstrument81__6._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AsstId')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1582, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Financialinstrument81__6._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PtyData')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1588, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Financialinstrument81__6._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AsstCtry')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1595, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Financialinstrument81__6._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AsstValtn')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1601, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Financialinstrument81__6._Automaton = _BuildAutomaton_32()




ForeignExchangeTerms36__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'UnitCcy'), ActiveOrHistoricCurrencyCode_fixed, scope=ForeignExchangeTerms36__1, documentation='UnitCurrencyCurrency in which the rate of exchange is expressed in a currency exchange. In the example 1GBP = xxxCUR, the unit currency is GBP.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1671, 12)))

ForeignExchangeTerms36__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'QtdCcy'), ActiveOrHistoricCurrencyCode, scope=ForeignExchangeTerms36__1, documentation='QuotedCurrencyCurrency into which the base currency is converted, in a currency exchange.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1677, 12)))

ForeignExchangeTerms36__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'XchgRate'), BaseOneRate, scope=ForeignExchangeTerms36__1, documentation='ExchangeRateThe value of one currency expressed in relation to another currency. ExchangeRate expresses the ratio between UnitCurrency and QuotedCurrency (ExchangeRate = UnitCurrency/QuotedCurrency).', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1683, 12)))

def _BuildAutomaton_33 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_33
    del _BuildAutomaton_33
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ForeignExchangeTerms36__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'UnitCcy')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1671, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ForeignExchangeTerms36__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'QtdCcy')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1677, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ForeignExchangeTerms36__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'XchgRate')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1683, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ForeignExchangeTerms36__1._Automaton = _BuildAutomaton_33()




FundLiquidity1__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DalyMtrgAsstRate'), PercentageBoundedRate, scope=FundLiquidity1__1, documentation='DailyMaturingAssetRateContains the percentage of assets held by the money market fund that are considered as daily maturing assets at the end of the reporting period.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1697, 12)))

FundLiquidity1__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'WklyMtrgAsstRate'), PercentageBoundedRate, scope=FundLiquidity1__1, documentation='WeeklyMaturingAssetRateContains the percentage of assets held by the money market fund that are considered as weekly maturing assets at the end of the reporting period.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1703, 12)))

FundLiquidity1__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PrtflLqdtyBrkdwn'), RangeBreakdown1__1, scope=FundLiquidity1__1, documentation='PortfolioLiquidityBreakdownSpecifies the percentage of total holdings capable of being liquidated within each time period.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1709, 12)))

def _BuildAutomaton_34 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_34
    del _BuildAutomaton_34
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=4, max=4, metadata=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1709, 12))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(FundLiquidity1__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DalyMtrgAsstRate')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1697, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(FundLiquidity1__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'WklyMtrgAsstRate')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1703, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(FundLiquidity1__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PrtflLqdtyBrkdwn')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1709, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
FundLiquidity1__1._Automaton = _BuildAutomaton_34()




FundReportCancellation2__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RptgYr'), ISOYear, scope=FundReportCancellation2__1, documentation='ReportingYearYear the report relates to.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1723, 12)))

FundReportCancellation2__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RptgPrdFrToQrtr'), QuarterPeriod1, scope=FundReportCancellation2__1, documentation='ReportingPeriodFromToQuarterQuarterly period range the report relates to.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1729, 12)))

FundReportCancellation2__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NtlRegnNb'), GenericOrganisationIdentification1__1, scope=FundReportCancellation2__1, documentation='NationalRegistrationNumberNumber assigned by a national registration authority to an entity.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1735, 12)))

def _BuildAutomaton_35 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_35
    del _BuildAutomaton_35
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(FundReportCancellation2__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RptgYr')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1723, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(FundReportCancellation2__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RptgPrdFrToQrtr')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1729, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(FundReportCancellation2__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NtlRegnNb')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1735, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
FundReportCancellation2__1._Automaton = _BuildAutomaton_35()




FundReportData1__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Cxl'), FundReportCancellation2__1, scope=FundReportData1__1, documentation='CancellationSpecifies the attributes for the cancellation of the money market fund report.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1749, 12)))

FundReportData1__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Upd'), FundReportUpdate2__1, scope=FundReportData1__1, documentation='UpdateSpecifies the attributes for the creation or correction of the money market fund report.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1755, 12)))

FundReportData1__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ElmtJustfn'), ReportItemJustification1, scope=FundReportData1__1, documentation='ElementJustificationProvides additional information or justification such as the assumptions taken by the submitted entity for each reported item where the reporting entity considered it necessary or the justification for reporting not available value [NOTA].\r\n', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1761, 12)))

def _BuildAutomaton_36 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_36
    del _BuildAutomaton_36
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1749, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1755, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1761, 12))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(FundReportData1__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Cxl')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1749, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(FundReportData1__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Upd')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1755, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(FundReportData1__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ElmtJustfn')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1761, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
FundReportData1__1._Automaton = _BuildAutomaton_36()




FundReportUpdate2__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RptgYr'), ISOYear, scope=FundReportUpdate2__1, documentation='ReportingYearYear the report relates to.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1776, 12)))

def _BuildAutomaton_37 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_37
    del _BuildAutomaton_37
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(FundReportUpdate2__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RptgYr')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1776, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
FundReportUpdate2__1._Automaton = _BuildAutomaton_37()




FundValuation1__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NetAsstValPerUnit'), CurrencyExchange14__1, scope=FundValuation1__1, documentation="NetAssetValuePerUnitValue at the end-of-period of all the holdings, less the fund's liabilities, attributable to a specific investment fund class calculated in accordance with mark-to-market or mark-to-model divided by the number of outstanding units or shares of the fund.", location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1814, 12)))

FundValuation1__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'WghtdAvrgMtrty'), DecimalNumber, scope=FundValuation1__1, documentation='WeightedAverageMaturityContains the weighted average maturity of the fund (expressed in days).', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1820, 12)))

FundValuation1__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'WghtdAvrgLife'), DecimalNumber, scope=FundValuation1__1, documentation='WeightedAverageLifeContains the weighted average life of the fund (expressed in days).', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1826, 12)))

def _BuildAutomaton_38 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_38
    del _BuildAutomaton_38
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(FundValuation1__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NetAsstValPerUnit')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1814, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(FundValuation1__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'WghtdAvrgMtrty')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1820, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(FundValuation1__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'WghtdAvrgLife')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1826, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
FundValuation1__1._Automaton = _BuildAutomaton_38()




GenericIdentification3__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Id'), Max35Text, scope=GenericIdentification3__1, documentation='IdentificationName or number assigned by an entity to enable recognition of that entity, for example, account identifier.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1840, 12)))

GenericIdentification3__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Issr'), Max35Text_fixed, scope=GenericIdentification3__1, documentation='IssuerEntity that assigns the identification.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1846, 12)))

def _BuildAutomaton_39 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_39
    del _BuildAutomaton_39
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(GenericIdentification3__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Id')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1840, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(GenericIdentification3__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Issr')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1846, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
GenericIdentification3__1._Automaton = _BuildAutomaton_39()




GenericOrganisationIdentification1__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Id'), Max35Text, scope=GenericOrganisationIdentification1__1, documentation='IdentificationIdentification assigned by an institution.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1860, 12)))

GenericOrganisationIdentification1__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Issr'), CountryCode, scope=GenericOrganisationIdentification1__1, documentation='IssuerEntity that assigns the identification.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1866, 12)))

def _BuildAutomaton_40 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_40
    del _BuildAutomaton_40
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(GenericOrganisationIdentification1__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Id')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1860, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(GenericOrganisationIdentification1__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Issr')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1866, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
GenericOrganisationIdentification1__1._Automaton = _BuildAutomaton_40()




GenericOrganisationIdentification1__2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Id'), Max35Text, scope=GenericOrganisationIdentification1__2, documentation='IdentificationIdentification assigned by an institution.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1880, 12)))

GenericOrganisationIdentification1__2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Issr'), Max35Text_fixed, scope=GenericOrganisationIdentification1__2, documentation='IssuerEntity that assigns the identification.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1886, 12)))

def _BuildAutomaton_41 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_41
    del _BuildAutomaton_41
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(GenericOrganisationIdentification1__2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Id')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1880, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(GenericOrganisationIdentification1__2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Issr')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1886, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
GenericOrganisationIdentification1__2._Automaton = _BuildAutomaton_41()




GenericOrganisationIdentification1__3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Id'), Max35Text, scope=GenericOrganisationIdentification1__3, documentation='IdentificationIdentification assigned by an institution.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1900, 12)))

def _BuildAutomaton_42 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_42
    del _BuildAutomaton_42
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(GenericOrganisationIdentification1__3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Id')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1900, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
GenericOrganisationIdentification1__3._Automaton = _BuildAutomaton_42()




HoldingAsset3__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MnyMktInstrmHldg'), Financialinstrument81__1, scope=HoldingAsset3__1, documentation='MoneyMarketInstrumentHoldingProvides details on the money market instruments held by the fund.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1914, 12)))

HoldingAsset3__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ScrtstnAsstBckdComrclPprHldg'), Financialinstrument81__2, scope=HoldingAsset3__1, documentation='SecuritisationAssetBackedCommercialPaperHoldingProvides details on the securitisations and asset backed commercial papers held by the fund.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1920, 12)))

HoldingAsset3__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DerivHldg'), Financialinstrument81__3, scope=HoldingAsset3__1, documentation='DerivativeHoldingProvides details on the financial derivatives held by the fund.\r\n', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1926, 12)))

HoldingAsset3__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MnyMktFndHldgInf'), Financialinstrument81__4, scope=HoldingAsset3__1, documentation='MoneyMarketFundHoldingInformationProvides details on the money market funds held by the fund.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1933, 12)))

HoldingAsset3__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DpstAncllryLqdAsstHldg'), Financialinstrument81__5, scope=HoldingAsset3__1, documentation='DepositAncillaryLiquidAssetHoldingProvides details on the deposits and ancillary liquid assets held by the fund.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1939, 12)))

HoldingAsset3__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RpAgrmtHldg'), Financialinstrument81__6, scope=HoldingAsset3__1, documentation='RepurchaseAgreementHoldingProvides details on the Repurchase agreements and reverse repurchase agreements held by the fund.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1945, 12)))

HoldingAsset3__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RvsRpAgrmtCollData'), FinancialInstrument80__1, scope=HoldingAsset3__1, documentation='ReverseRepurchaseAgreementCollateralDataInformation on the Collateral related to the reverse repurchase agreements.\r\n', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1951, 12)))

def _BuildAutomaton_43 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_43
    del _BuildAutomaton_43
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1914, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1920, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1926, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1933, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1939, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1945, 12))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1951, 12))
    counters.add(cc_6)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(HoldingAsset3__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'MnyMktInstrmHldg')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1914, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(HoldingAsset3__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ScrtstnAsstBckdComrclPprHldg')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1920, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(HoldingAsset3__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DerivHldg')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1926, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(HoldingAsset3__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'MnyMktFndHldgInf')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1933, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(HoldingAsset3__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DpstAncllryLqdAsstHldg')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1939, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(HoldingAsset3__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RpAgrmtHldg')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1945, 12))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(HoldingAsset3__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RvsRpAgrmtCollData')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 1951, 12))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
HoldingAsset3__1._Automaton = _BuildAutomaton_43()




InstrumentIdentification3Choice__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ISIN'), ISINOct2015Identifier, scope=InstrumentIdentification3Choice__1, documentation="ISINInternational Securities Identification Number (ISIN).  A numbering system designed by the United Nation's International Organisation for Standardisation (ISO). The ISIN is composed of a 2-character prefix representing the country of issue, followed by the national security number (if one exists), and a check digit. Each country has a national numbering agency that assigns ISIN numbers for securities in that country.", location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2001, 12)))

InstrumentIdentification3Choice__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'FullNm'), Max350Text, scope=InstrumentIdentification3Choice__1, documentation='FullNameFull name or description of the financial instrument.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2007, 12)))

def _BuildAutomaton_44 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_44
    del _BuildAutomaton_44
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(InstrumentIdentification3Choice__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ISIN')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2001, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(InstrumentIdentification3Choice__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'FullNm')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2007, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
InstrumentIdentification3Choice__1._Automaton = _BuildAutomaton_44()




InstrumentIdentification4Choice__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ISIN'), ISINOct2015Identifier, scope=InstrumentIdentification4Choice__1, documentation="ISINInternational Securities Identification Number (ISIN).  A numbering system designed by the United Nation's International Organisation for Standardisation (ISO). The ISIN is composed of a 2-character prefix representing the country of issue, followed by the national security number (if one exists), and a check digit. Each country has a national numbering agency that assigns ISIN numbers for securities in that country.", location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2021, 12)))

InstrumentIdentification4Choice__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Nm'), Max350Text, scope=InstrumentIdentification4Choice__1, documentation='NameName or description of the financial instrument.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2027, 12)))

def _BuildAutomaton_45 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_45
    del _BuildAutomaton_45
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(InstrumentIdentification4Choice__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ISIN')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2021, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(InstrumentIdentification4Choice__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Nm')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2027, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
InstrumentIdentification4Choice__1._Automaton = _BuildAutomaton_45()




InstrumentIdentification4Choice__2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ISIN'), ISINOct2015Identifier, scope=InstrumentIdentification4Choice__2, documentation="ISINInternational Securities Identification Number (ISIN).  A numbering system designed by the United Nation's International Organisation for Standardisation (ISO). The ISIN is composed of a 2-character prefix representing the country of issue, followed by the national security number (if one exists), and a check digit. Each country has a national numbering agency that assigns ISIN numbers for securities in that country.", location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2041, 12)))

InstrumentIdentification4Choice__2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'UnqPdctIdr'), Max52Text, scope=InstrumentIdentification4Choice__2, documentation='UniqueProductIdentifierIdentification through a unique product identifier.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2047, 12)))

InstrumentIdentification4Choice__2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Nm'), Max350Text, scope=InstrumentIdentification4Choice__2, documentation='NameName or description of the financial instrument.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2053, 12)))

def _BuildAutomaton_46 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_46
    del _BuildAutomaton_46
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(InstrumentIdentification4Choice__2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ISIN')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2041, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(InstrumentIdentification4Choice__2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'UnqPdctIdr')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2047, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(InstrumentIdentification4Choice__2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Nm')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2053, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
InstrumentIdentification4Choice__2._Automaton = _BuildAutomaton_46()




InstrumentIdentification4Choice__3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Nm'), Max350Text, scope=InstrumentIdentification4Choice__3, documentation='NameName or description of the financial instrument.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2067, 12)))

def _BuildAutomaton_47 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_47
    del _BuildAutomaton_47
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(InstrumentIdentification4Choice__3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Nm')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2067, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
InstrumentIdentification4Choice__3._Automaton = _BuildAutomaton_47()




InvestorConcentration1__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RtlInvstrRate'), Liability1__1, scope=InvestorConcentration1__1, documentation='RetailInvestorRatePercentage of the net asset value held by professional investors when precise information is available.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2081, 12)))

InvestorConcentration1__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PrfssnlInvstrRate'), Liability1__1, scope=InvestorConcentration1__1, documentation='ProfessionalInvestorRatePercentage of the net asset value held by professional investors when precise information is available.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2087, 12)))

def _BuildAutomaton_48 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_48
    del _BuildAutomaton_48
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvestorConcentration1__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RtlInvstrRate')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2081, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(InvestorConcentration1__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PrfssnlInvstrRate')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2087, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
InvestorConcentration1__1._Automaton = _BuildAutomaton_48()




InvestorGroupBreakdownType2__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BkRate'), PercentageBoundedRate, scope=InvestorGroupBreakdownType2__1, documentation='BankRateSpecifies the percentage of the net asset value by banks investor group.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2102, 12)))

InvestorGroupBreakdownType2__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'GnlGovntRate'), PercentageBoundedRate, scope=InvestorGroupBreakdownType2__1, documentation='GeneralGovernmentRateSpecifies the percentage of the net asset value by general government investor group.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2108, 12)))

InvestorGroupBreakdownType2__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'HsHldRate'), PercentageBoundedRate, scope=InvestorGroupBreakdownType2__1, documentation='HouseholdRateSpecifies the percentage of the net asset value by households investor group.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2114, 12)))

InvestorGroupBreakdownType2__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'InsrncCorptnRate'), PercentageBoundedRate, scope=InvestorGroupBreakdownType2__1, documentation='InsuranceCorporationRateSpecifies the percentage of the net asset value by insurance corporation investor group.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2120, 12)))

InvestorGroupBreakdownType2__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NonFinCorptnRate'), PercentageBoundedRate, scope=InvestorGroupBreakdownType2__1, documentation='NonFinancialCorporationRateSpecifies the percentage of the net asset value by non-financial corporations investor group.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2126, 12)))

InvestorGroupBreakdownType2__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NonMnyMktFndInvstmtFndRate'), PercentageBoundedRate, scope=InvestorGroupBreakdownType2__1, documentation='NonMoneyMarketFundInvestmentFundRateSpecifies the percentage of the net asset value by other collective investment undertakings investor group.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2132, 12)))

InvestorGroupBreakdownType2__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OthrFIRate'), PercentageBoundedRate, scope=InvestorGroupBreakdownType2__1, documentation='OtherFinancialInstitutionRateSpecifies the percentage of the net asset value by other financial institution investor group.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2138, 12)))

InvestorGroupBreakdownType2__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PnsnPlanOrFndRate'), PercentageBoundedRate, scope=InvestorGroupBreakdownType2__1, documentation='PensionPlanOrFundRateSpecifies the percentage of the net asset value by pension fund or funds investor group.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2144, 12)))

InvestorGroupBreakdownType2__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'UknwnRate'), PercentageBoundedRate, scope=InvestorGroupBreakdownType2__1, documentation='UnknownRateSpecifies the percentage of the net asset value for unknown investor group.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2150, 12)))

def _BuildAutomaton_49 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_49
    del _BuildAutomaton_49
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvestorGroupBreakdownType2__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'BkRate')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2102, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvestorGroupBreakdownType2__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'GnlGovntRate')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2108, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvestorGroupBreakdownType2__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'HsHldRate')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2114, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvestorGroupBreakdownType2__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'InsrncCorptnRate')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2120, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvestorGroupBreakdownType2__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NonFinCorptnRate')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2126, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvestorGroupBreakdownType2__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NonMnyMktFndInvstmtFndRate')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2132, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvestorGroupBreakdownType2__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'OthrFIRate')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2138, 12))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvestorGroupBreakdownType2__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PnsnPlanOrFndRate')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2144, 12))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(InvestorGroupBreakdownType2__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'UknwnRate')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2150, 12))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
         ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    st_8._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
InvestorGroupBreakdownType2__1._Automaton = _BuildAutomaton_49()




LegalFramework5Choice__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Cd'), LegalFramework2Code, scope=LegalFramework5Choice__1, documentation='CodeSpecifies the legal framework, in a coded form.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2193, 12)))

def _BuildAutomaton_50 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_50
    del _BuildAutomaton_50
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(LegalFramework5Choice__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Cd')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2193, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
LegalFramework5Choice__1._Automaton = _BuildAutomaton_50()




Liability1__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EstmtdRate'), PercentageBoundedRate, scope=Liability1__1, documentation='EstimatedRateEstimated percentage of the net asset value held by professional investors when no precise information is available.\r\n', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2207, 12)))

Liability1__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PreciseRate'), PercentageBoundedRate, scope=Liability1__1, documentation='PreciseRatePercentage of the net asset value held by retail investors when precise information is available.\r\n', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2214, 12)))

def _BuildAutomaton_51 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_51
    del _BuildAutomaton_51
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Liability1__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EstmtdRate')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2207, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Liability1__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PreciseRate')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2214, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Liability1__1._Automaton = _BuildAutomaton_51()




LiabilityData3__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'HghstBnfclOwnrRate'), PercentageBoundedRate, scope=LiabilityData3__1, documentation='HighestBeneficialOwnerRatePercentage of the net asset value that is beneficially owned by the five highest beneficial owners.\r\n', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2229, 12)))

LiabilityData3__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'InvstrCncntrtn'), InvestorConcentration1__1, scope=LiabilityData3__1, documentation='InvestorConcentrationInformation related to the investor concentration.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2236, 12)))

LiabilityData3__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'InvstrGrpBrkdwn'), InvestorGroupBreakdownType2__1, scope=LiabilityData3__1, documentation='InvestorGroupBreakdownSpecifies the rate of net asset value by type of investor group.\r\n', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2242, 12)))

LiabilityData3__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BrkdwnByCtry'), BreakdownByCountry4__1, scope=LiabilityData3__1, documentation='BreakdownByCountrySpecifies the rate of net asset value by country of residence of investors.\r\n', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2249, 12)))

LiabilityData3__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RedDealgFrqcy'), EventFrequency9Code__1, scope=LiabilityData3__1, documentation='RedemptionDealingFrequencyFrequency at which the redemptions are done.\r\n', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2256, 12)))

LiabilityData3__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NtceDays'), Max3Number, scope=LiabilityData3__1, documentation='NoticeDaysNumber of notice in days that must be given by either the issuer or the holder before redemption can take place.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2263, 12)))

LiabilityData3__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BrkdwnByArrgmnt'), BreakdownByArrangement2__1, scope=LiabilityData3__1, documentation='BreakdownByArrangementSpecifies the net asset value by type of arrangement.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2269, 12)))

LiabilityData3__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OthrArrgmntAddtlInf'), Max350Text, scope=LiabilityData3__1, documentation='OtherArrangementAdditionalInformationAdditional information about the other arrangement type.\r\n', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2275, 12)))

LiabilityData3__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MnthlyNetAsstValPerUnitInf'), MonthValue2__1, scope=LiabilityData3__1, documentation='MonthlyNetAssetValuePerUnitInformationInformation in relation with the net asset value per unit or share at the end of each month.\r\n', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2282, 12)))

LiabilityData3__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MnthlySbcptInf'), MonthValue2__1, scope=LiabilityData3__1, documentation='MonthlySubscriptionInformationInformation in relation with the subscription amounts at the end of each month.\r\n', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2289, 12)))

LiabilityData3__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MnthlyRedInf'), MonthValue2__1, scope=LiabilityData3__1, documentation='MonthlyRedemptionInformationInformation in relation with the redemption amounts at the end of each month.\r\n', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2296, 12)))

LiabilityData3__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MnthlyPmtToInvstrInf'), MonthValue2__1, scope=LiabilityData3__1, documentation='MonthlyPaymentToInvestorInformationInformation in relation with the payment-to-investors amounts at the end of each month.\r\n', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2303, 12)))

LiabilityData3__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MnthlyXchgRateInf'), MonthValue2__2, scope=LiabilityData3__1, documentation='MonthlyExchangeRateInformationInformation in relation with the foreign exchange rate of the last of each month.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2310, 12)))

def _BuildAutomaton_52 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_52
    del _BuildAutomaton_52
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=9, max=9, metadata=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2242, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=4, max=4, metadata=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2269, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2275, 12))
    counters.add(cc_2)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(LiabilityData3__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'HghstBnfclOwnrRate')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2229, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(LiabilityData3__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'InvstrCncntrtn')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2236, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(LiabilityData3__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'InvstrGrpBrkdwn')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2242, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(LiabilityData3__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'BrkdwnByCtry')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2249, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(LiabilityData3__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RedDealgFrqcy')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2256, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(LiabilityData3__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NtceDays')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2263, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(LiabilityData3__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'BrkdwnByArrgmnt')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2269, 12))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(LiabilityData3__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'OthrArrgmntAddtlInf')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2275, 12))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(LiabilityData3__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'MnthlyNetAsstValPerUnitInf')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2282, 12))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(LiabilityData3__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'MnthlySbcptInf')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2289, 12))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(LiabilityData3__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'MnthlyRedInf')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2296, 12))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(LiabilityData3__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'MnthlyPmtToInvstrInf')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2303, 12))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(LiabilityData3__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'MnthlyXchgRateInf')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2310, 12))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
         ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
         ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
         ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
         ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    st_12._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
LiabilityData3__1._Automaton = _BuildAutomaton_52()




LowVolatilityNetAssetValueReportData2__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AmtsdCostMtdPricDvtnEvt'), AmortisedCostMethodPriceDeviationEvent1__1, scope=LowVolatilityNetAssetValueReportData2__1, documentation='AmortisedCostMethodPriceDeviationEventDetails of the events where the price of an asset calculated in accordance with the mark-to-market or mark-to-model method deviates from the asset price calculated in accordance with the amortised cost method by more than 10 basis points.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2324, 12)))

LowVolatilityNetAssetValueReportData2__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CstNetAsstValDvtnEvt'), ConstantNetAssetValueDeviationEvent1__1, scope=LowVolatilityNetAssetValueReportData2__1, documentation='ConstantNetAssetValueDeviationEventDetails of the events where the constant net asset value per unit or share calculated in accordance with the amortised cost method deviates from the net asset value per unit or share calculated in accordance with the mark-to-market or mark-to-model method by more than 20 basis points.\r\n\r\n', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2330, 12)))

LowVolatilityNetAssetValueReportData2__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MtrgAsstThrshldEvt'), MaturingAssetThresholdEvent2, scope=LowVolatilityNetAssetValueReportData2__1, documentation='MaturingAssetThresholdEventDetails of the events where the fund is not compliant with the weekly liquidity thresholds applicable to public debt constant net asset value money market funds or the low volatility net asset value money market funds.\r\n', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2338, 12)))

def _BuildAutomaton_53 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_53
    del _BuildAutomaton_53
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2324, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2330, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2338, 12))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(LowVolatilityNetAssetValueReportData2__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AmtsdCostMtdPricDvtnEvt')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2324, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(LowVolatilityNetAssetValueReportData2__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CstNetAsstValDvtnEvt')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2330, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(LowVolatilityNetAssetValueReportData2__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'MtrgAsstThrshldEvt')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2338, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
LowVolatilityNetAssetValueReportData2__1._Automaton = _BuildAutomaton_53()




MarketSpecificAttribute1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Nm'), Max35Text, scope=MarketSpecificAttribute1, documentation='NameSpecifies the name of the market-specific attribute.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2353, 12)))

MarketSpecificAttribute1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Val'), Max350Text, scope=MarketSpecificAttribute1, documentation='ValueSpecifies the value of the market-specific attribute.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2359, 12)))

def _BuildAutomaton_54 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_54
    del _BuildAutomaton_54
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MarketSpecificAttribute1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Nm')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2353, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(MarketSpecificAttribute1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Val')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2359, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
MarketSpecificAttribute1._Automaton = _BuildAutomaton_54()




MaturingAssetThresholdEvent2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EvtDt'), ISODate, scope=MaturingAssetThresholdEvent2, documentation='EventDateDate on which the reportable event took place.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2399, 12)))

MaturingAssetThresholdEvent2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MeasrDt'), ISODate, scope=MaturingAssetThresholdEvent2, documentation='MeasureDateDate on which the decided measure was taken.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2405, 12)))

MaturingAssetThresholdEvent2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MeasrInf'), Measure2Choice, scope=MaturingAssetThresholdEvent2, documentation='MeasureInformationDetails on the measures decided by the board in case of non-compliance with the weekly liquidity thresholds applicable to public debt constant net asset value money market funds and low volatility net asset value money market funds.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2411, 12)))

def _BuildAutomaton_55 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_55
    del _BuildAutomaton_55
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MaturingAssetThresholdEvent2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EvtDt')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2399, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MaturingAssetThresholdEvent2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'MeasrDt')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2405, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(MaturingAssetThresholdEvent2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'MeasrInf')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2411, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
MaturingAssetThresholdEvent2._Automaton = _BuildAutomaton_55()




Measure2Choice._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'FrstMeasrTp'), ArrangementType5Code, scope=Measure2Choice, documentation='FirstMeasureTypeDefines the type of decision applied by the board in relation with the proportion of weekly maturing assets that is falling down below 30 % of its total assets whereas the net daily redemptions on a single working day exceed 10 % of total assets.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2497, 12)))

Measure2Choice._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ScndMeasrTp'), ArrangementType6Code, scope=Measure2Choice, documentation='SecondMeasureTypeDefines the type of decision applied by the board in relation with the proportion of weekly maturing assets that is falling down below 10 % of its total assets.\r\n', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2503, 12)))

def _BuildAutomaton_56 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_56
    del _BuildAutomaton_56
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Measure2Choice._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'FrstMeasrTp')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2497, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Measure2Choice._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ScndMeasrTp')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2503, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Measure2Choice._Automaton = _BuildAutomaton_56()




MoneyMarketFundReportV01._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'FndRpt'), FundReportData1__1, scope=MoneyMarketFundReportV01, documentation='FundReportSpecifies the attributes for the creation, correction or cancellation of the money market fund report.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2520, 12)))

def _BuildAutomaton_57 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_57
    del _BuildAutomaton_57
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(MoneyMarketFundReportV01._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'FndRpt')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2520, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
MoneyMarketFundReportV01._Automaton = _BuildAutomaton_57()




MoneyMarketFundType1Choice__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Cd'), MoneyMarketFundType1Code, scope=MoneyMarketFundType1Choice__1, documentation='CodeSpecifies the type of the money market fund.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2534, 12)))

def _BuildAutomaton_58 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_58
    del _BuildAutomaton_58
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(MoneyMarketFundType1Choice__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Cd')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2534, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
MoneyMarketFundType1Choice__1._Automaton = _BuildAutomaton_58()




MonthType3__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Mnth'), ReportingPeriodType2Code__1, scope=MonthType3__1, documentation='MonthInformation is related to one of the three months of the reporting quarter.\r\n', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2582, 12)))

MonthType3__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Val'), MonthlyValue2Choice__1, scope=MonthType3__1, documentation='ValueValue expressed in the reporting currency for each month of the reporting period.\r\n', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2589, 12)))

def _BuildAutomaton_59 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_59
    del _BuildAutomaton_59
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MonthType3__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Mnth')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2582, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(MonthType3__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Val')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2589, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
MonthType3__1._Automaton = _BuildAutomaton_59()




MonthType3__2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Mnth'), ReportingPeriodType2Code__2, scope=MonthType3__2, documentation='MonthInformation is related to one of the three months of the reporting quarter.\r\n', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2605, 12)))

MonthType3__2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Val'), MonthlyValue2Choice__1, scope=MonthType3__2, documentation='ValueValue expressed in the reporting currency for each month of the reporting period.\r\n', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2612, 12)))

def _BuildAutomaton_60 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_60
    del _BuildAutomaton_60
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MonthType3__2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Mnth')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2605, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(MonthType3__2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Val')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2612, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
MonthType3__2._Automaton = _BuildAutomaton_60()




MonthType3__3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Mnth'), ReportingPeriodType2Code__3, scope=MonthType3__3, documentation='MonthInformation is related to one of the three months of the reporting quarter.\r\n', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2628, 12)))

MonthType3__3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Val'), MonthlyValue2Choice__1, scope=MonthType3__3, documentation='ValueValue expressed in the reporting currency for each month of the reporting period.\r\n', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2635, 12)))

def _BuildAutomaton_61 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_61
    del _BuildAutomaton_61
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MonthType3__3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Mnth')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2628, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(MonthType3__3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Val')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2635, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
MonthType3__3._Automaton = _BuildAutomaton_61()




MonthType3__4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Mnth'), ReportingPeriodType2Code__4, scope=MonthType3__4, documentation='MonthInformation is related to one of the three months of the reporting quarter.\r\n', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2651, 12)))

MonthType3__4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Val'), MonthlyValue2Choice__1, scope=MonthType3__4, documentation='ValueValue expressed in the reporting currency for each month of the reporting period.\r\n', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2658, 12)))

def _BuildAutomaton_62 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_62
    del _BuildAutomaton_62
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MonthType3__4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Mnth')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2651, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(MonthType3__4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Val')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2658, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
MonthType3__4._Automaton = _BuildAutomaton_62()




MonthType3__5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Mnth'), ReportingPeriodType2Code__1, scope=MonthType3__5, documentation='MonthInformation is related to one of the three months of the reporting quarter.\r\n', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2674, 12)))

MonthType3__5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Val'), MonthlyValue2Choice__2, scope=MonthType3__5, documentation='ValueValue expressed in the reporting currency for each month of the reporting period.\r\n', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2681, 12)))

def _BuildAutomaton_63 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_63
    del _BuildAutomaton_63
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MonthType3__5._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Mnth')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2674, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(MonthType3__5._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Val')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2681, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
MonthType3__5._Automaton = _BuildAutomaton_63()




MonthType3__6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Mnth'), ReportingPeriodType2Code__2, scope=MonthType3__6, documentation='MonthInformation is related to one of the three months of the reporting quarter.\r\n', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2697, 12)))

MonthType3__6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Val'), MonthlyValue2Choice__2, scope=MonthType3__6, documentation='ValueValue expressed in the reporting currency for each month of the reporting period.\r\n', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2704, 12)))

def _BuildAutomaton_64 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_64
    del _BuildAutomaton_64
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MonthType3__6._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Mnth')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2697, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(MonthType3__6._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Val')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2704, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
MonthType3__6._Automaton = _BuildAutomaton_64()




MonthType3__7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Mnth'), ReportingPeriodType2Code__3, scope=MonthType3__7, documentation='MonthInformation is related to one of the three months of the reporting quarter.\r\n', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2720, 12)))

MonthType3__7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Val'), MonthlyValue2Choice__2, scope=MonthType3__7, documentation='ValueValue expressed in the reporting currency for each month of the reporting period.\r\n', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2727, 12)))

def _BuildAutomaton_65 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_65
    del _BuildAutomaton_65
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MonthType3__7._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Mnth')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2720, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(MonthType3__7._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Val')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2727, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
MonthType3__7._Automaton = _BuildAutomaton_65()




MonthType3__8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Mnth'), ReportingPeriodType2Code__4, scope=MonthType3__8, documentation='MonthInformation is related to one of the three months of the reporting quarter.\r\n', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2743, 12)))

MonthType3__8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Val'), MonthlyValue2Choice__2, scope=MonthType3__8, documentation='ValueValue expressed in the reporting currency for each month of the reporting period.\r\n', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2750, 12)))

def _BuildAutomaton_66 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_66
    del _BuildAutomaton_66
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MonthType3__8._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Mnth')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2743, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(MonthType3__8._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Val')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2750, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
MonthType3__8._Automaton = _BuildAutomaton_66()




MonthValue2__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'FrstQrtr'), Quarter3__1, scope=MonthValue2__1, documentation='FirstQuarterInformation is related with the full year period.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2765, 12)))

MonthValue2__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ScndQrtr'), Quarter3__2, scope=MonthValue2__1, documentation='SecondQuarterInformation is related with one quarter of the year.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2771, 12)))

MonthValue2__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ThrdQrtr'), Quarter3__3, scope=MonthValue2__1, documentation='ThirdQuarterInformation is related with the first half-year period.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2777, 12)))

MonthValue2__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'FrthQrtr'), Quarter3__4, scope=MonthValue2__1, documentation='FourthQuarterInformation is related with the second half-year period.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2783, 12)))

def _BuildAutomaton_67 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_67
    del _BuildAutomaton_67
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2765, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2771, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2777, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2783, 12))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(MonthValue2__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'FrstQrtr')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2765, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(MonthValue2__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ScndQrtr')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2771, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(MonthValue2__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ThrdQrtr')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2777, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(MonthValue2__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'FrthQrtr')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2783, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
MonthValue2__1._Automaton = _BuildAutomaton_67()




MonthValue2__2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'FrstQrtr'), Quarter3__5, scope=MonthValue2__2, documentation='FirstQuarterInformation is related with the full year period.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2797, 12)))

MonthValue2__2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ScndQrtr'), Quarter3__6, scope=MonthValue2__2, documentation='SecondQuarterInformation is related with one quarter of the year.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2803, 12)))

MonthValue2__2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ThrdQrtr'), Quarter3__7, scope=MonthValue2__2, documentation='ThirdQuarterInformation is related with the first half-year period.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2809, 12)))

MonthValue2__2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'FrthQrtr'), Quarter3__8, scope=MonthValue2__2, documentation='FourthQuarterInformation is related with the second half-year period.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2815, 12)))

def _BuildAutomaton_68 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_68
    del _BuildAutomaton_68
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2797, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2803, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2809, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2815, 12))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(MonthValue2__2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'FrstQrtr')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2797, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(MonthValue2__2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ScndQrtr')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2803, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(MonthValue2__2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ThrdQrtr')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2809, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(MonthValue2__2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'FrthQrtr')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2815, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
MonthValue2__2._Automaton = _BuildAutomaton_68()




MonthlyValue2Choice__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Val'), ImpliedCurrencyAndAmount, scope=MonthlyValue2Choice__1, documentation='ValueValue expressed in the reporting currency at the end-of-month for the net asset value, the redemptions, the subscriptions, the payment to investors.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2829, 12)))

MonthlyValue2Choice__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NotAvlblVal'), NotAvailable1Code, scope=MonthlyValue2Choice__1, documentation='NotAvailableValueThe value is not available.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2835, 12)))

def _BuildAutomaton_69 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_69
    del _BuildAutomaton_69
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(MonthlyValue2Choice__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Val')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2829, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(MonthlyValue2Choice__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NotAvlblVal')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2835, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
MonthlyValue2Choice__1._Automaton = _BuildAutomaton_69()




MonthlyValue2Choice__2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'FX'), ForeignExchangeTerms36__1, scope=MonthlyValue2Choice__2, documentation='ForeignExchangeInformation needed to process a currency exchange or conversion.\r\n', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2849, 12)))

MonthlyValue2Choice__2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NotAvlblVal'), NotAvailable1Code, scope=MonthlyValue2Choice__2, documentation='NotAvailableValueThe value is not available.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2856, 12)))

def _BuildAutomaton_70 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_70
    del _BuildAutomaton_70
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(MonthlyValue2Choice__2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'FX')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2849, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(MonthlyValue2Choice__2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NotAvlblVal')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2856, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
MonthlyValue2Choice__2._Automaton = _BuildAutomaton_70()




OutflowImpact1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'FrstBcktOutflwRate'), PercentageRate, scope=OutflowImpact1, documentation='FirstBucketOutflowRateWeekly outflows derived from the monthly outflows compared with available weekly liquid assets, considered as the sum of highly liquid assets and weekly maturing assets. Rate computed for assets considered in the first bucket according to the Regulation.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2927, 12)))

OutflowImpact1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ScndBcktOutflwRate'), PercentageRate, scope=OutflowImpact1, documentation='SecondBucketOutflowRateWeekly outflows derived from the monthly outflows compared with available weekly liquid assets, considered as the sum of highly liquid assets and weekly maturing assets. Rate computed for assets considered in the second bucket according to the Regulation.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2933, 12)))

def _BuildAutomaton_71 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_71
    del _BuildAutomaton_71
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OutflowImpact1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'FrstBcktOutflwRate')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2927, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(OutflowImpact1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ScndBcktOutflwRate')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2933, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
OutflowImpact1._Automaton = _BuildAutomaton_71()




Party46Choice__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'IssrData'), PartyAndSector1__1, scope=Party46Choice__1, documentation='IssuerDataSpecifies further details of the issuer.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2947, 12)))

def _BuildAutomaton_72 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_72
    del _BuildAutomaton_72
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Party46Choice__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'IssrData')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2947, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Party46Choice__1._Automaton = _BuildAutomaton_72()




Party46Choice__2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SpnsrData'), PartyAndSector1__2, scope=Party46Choice__2, documentation='SponsorDataSpecifies further details of the sponsor.\r\n', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2961, 12)))

def _BuildAutomaton_73 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_73
    del _BuildAutomaton_73
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Party46Choice__2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SpnsrData')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2961, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Party46Choice__2._Automaton = _BuildAutomaton_73()




Party46Choice__3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CtrPtyData'), PartyAndSector1__2, scope=Party46Choice__3, documentation='CounterpartyDataProvides information about identification of the party that is a choice between the issuer of the money market instrument, the sponsor of the securitisation/asset backed commercial paper or the counterparty in the context of the derivative instrument, the repurchase agreement/reverse repurchase agreement or the deposit/ancillary liquid assets.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2976, 12)))

def _BuildAutomaton_74 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_74
    del _BuildAutomaton_74
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Party46Choice__3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CtrPtyData')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2976, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Party46Choice__3._Automaton = _BuildAutomaton_74()




Party46Choice__4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CtrPtyData'), PartyAndSector1__1, scope=Party46Choice__4, documentation='CounterpartyDataProvides information about identification of the party that is a choice between the issuer of the money market instrument, the sponsor of the securitisation/asset backed commercial paper or the counterparty in the context of the derivative instrument, the repurchase agreement/reverse repurchase agreement or the deposit/ancillary liquid assets.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2990, 12)))

def _BuildAutomaton_75 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_75
    del _BuildAutomaton_75
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Party46Choice__4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CtrPtyData')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 2990, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Party46Choice__4._Automaton = _BuildAutomaton_75()




PartyAndSector1__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PtyId'), PartyIdentification212__4, scope=PartyAndSector1__1, documentation='PartyIdentificationProvides information about identification of the party.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3005, 12)))

PartyAndSector1__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Sctr'), PartySectorType1Code, scope=PartyAndSector1__1, documentation='SectorSpecifies the sector of the party involved as an issuer, a sponsor or a counterparty in the asset held by the fund.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3011, 12)))

def _BuildAutomaton_76 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_76
    del _BuildAutomaton_76
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PartyAndSector1__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PtyId')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3005, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(PartyAndSector1__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Sctr')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3011, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
PartyAndSector1__1._Automaton = _BuildAutomaton_76()




PartyAndSector1__2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PtyId'), PartyIdentification212__4, scope=PartyAndSector1__2, documentation='PartyIdentificationProvides information about identification of the party.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3026, 12)))

def _BuildAutomaton_77 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_77
    del _BuildAutomaton_77
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(PartyAndSector1__2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PtyId')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3026, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
PartyAndSector1__2._Automaton = _BuildAutomaton_77()




PartyIdentification195__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LEI'), LEIIdentifier, scope=PartyIdentification195__1, documentation='LEILegal entity identification as an alternate identification for a party.\r\n', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3041, 12)))

PartyIdentification195__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'FndAuthrtyRegnNb'), GenericOrganisationIdentification1__3, scope=PartyIdentification195__1, documentation='FundAuthorityRegistrationNumberNumber assigned by a national registration authority to an entity.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3048, 12)))

PartyIdentification195__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'FndMgmtCpnyAuthrtyRegnNb'), GenericOrganisationIdentification1__1, scope=PartyIdentification195__1, documentation='FundManagementCompanyAuthorityRegistrationNumberNumber assigned by a national registration authority to an entity.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3054, 12)))

PartyIdentification195__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AltrnId'), GenericIdentification3__1, scope=PartyIdentification195__1, documentation='AlternateIdentificationAlternate identification of the fund.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3060, 12)))

PartyIdentification195__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Nm'), Max350Text, scope=PartyIdentification195__1, documentation='NameName of the fund management company.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3066, 12)))

def _BuildAutomaton_78 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_78
    del _BuildAutomaton_78
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3041, 12))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PartyIdentification195__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'LEI')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3041, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PartyIdentification195__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'FndAuthrtyRegnNb')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3048, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PartyIdentification195__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'FndMgmtCpnyAuthrtyRegnNb')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3054, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PartyIdentification195__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AltrnId')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3060, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(PartyIdentification195__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Nm')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3066, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
PartyIdentification195__1._Automaton = _BuildAutomaton_78()




PartyIdentification212__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LEI'), LEIIdentifier, scope=PartyIdentification212__1, documentation='LEILegal entity identification for a party.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3080, 12)))

PartyIdentification212__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NtlRegnNb'), GenericOrganisationIdentification1__1, scope=PartyIdentification212__1, documentation='NationalRegistrationNumberNumber assigned by a national registration authority to an entity.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3086, 12)))

PartyIdentification212__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AltrnId'), GenericOrganisationIdentification1__2, scope=PartyIdentification212__1, documentation='AlternateIdentificationAlternate identification of a party.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3092, 12)))

PartyIdentification212__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Nm'), Max350Text, scope=PartyIdentification212__1, documentation='NameName of a party.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3098, 12)))

PartyIdentification212__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CtryOfDmcl'), Country1Choice__1, scope=PartyIdentification212__1, documentation='CountryOfDomicileCountry of the party.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3104, 12)))

def _BuildAutomaton_79 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_79
    del _BuildAutomaton_79
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3080, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3092, 12))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PartyIdentification212__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'LEI')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3080, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PartyIdentification212__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NtlRegnNb')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3086, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PartyIdentification212__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AltrnId')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3092, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PartyIdentification212__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Nm')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3098, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(PartyIdentification212__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CtryOfDmcl')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3104, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
PartyIdentification212__1._Automaton = _BuildAutomaton_79()




PartyIdentification212__2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LEI'), LEIIdentifier, scope=PartyIdentification212__2, documentation='LEILegal entity identification for a party.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3118, 12)))

PartyIdentification212__2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NtlRegnNb'), GenericOrganisationIdentification1__3, scope=PartyIdentification212__2, documentation='NationalRegistrationNumberNumber assigned by a national registration authority to an entity.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3124, 12)))

PartyIdentification212__2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Nm'), Max350Text, scope=PartyIdentification212__2, documentation='NameName of a party.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3130, 12)))

def _BuildAutomaton_80 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_80
    del _BuildAutomaton_80
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3118, 12))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PartyIdentification212__2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'LEI')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3118, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PartyIdentification212__2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NtlRegnNb')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3124, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(PartyIdentification212__2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Nm')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3130, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
PartyIdentification212__2._Automaton = _BuildAutomaton_80()




PartyIdentification212__3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LEI'), LEIIdentifier, scope=PartyIdentification212__3, documentation='LEILegal entity identification for a party.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3144, 12)))

PartyIdentification212__3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NtlRegnNb'), GenericOrganisationIdentification1__1, scope=PartyIdentification212__3, documentation='NationalRegistrationNumberNumber assigned by a national registration authority to an entity.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3150, 12)))

PartyIdentification212__3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Nm'), Max350Text, scope=PartyIdentification212__3, documentation='NameName of a party.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3156, 12)))

def _BuildAutomaton_81 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_81
    del _BuildAutomaton_81
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3144, 12))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PartyIdentification212__3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'LEI')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3144, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PartyIdentification212__3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NtlRegnNb')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3150, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(PartyIdentification212__3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Nm')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3156, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
PartyIdentification212__3._Automaton = _BuildAutomaton_81()




PartyIdentification212__4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LEI'), LEIIdentifier, scope=PartyIdentification212__4, documentation='LEILegal entity identification for a party.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3170, 12)))

PartyIdentification212__4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Nm'), Max350Text, scope=PartyIdentification212__4, documentation='NameName of a party.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3176, 12)))

def _BuildAutomaton_82 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_82
    del _BuildAutomaton_82
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3170, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3176, 12))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(PartyIdentification212__4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'LEI')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3170, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(PartyIdentification212__4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Nm')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3176, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
PartyIdentification212__4._Automaton = _BuildAutomaton_82()




PerformanceFactors2__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'FndValtn'), FundValuation1__1, scope=PerformanceFactors2__1, documentation='FundValuationProvide the details of the valuation calculated for the money market fund during the reporting period.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3306, 12)))

PerformanceFactors2__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LqdtyInf'), FundLiquidity1__1, scope=PerformanceFactors2__1, documentation='LiquidityInformationProvide the details of the liquidity indicators calculated for the money market fund during the reporting period.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3312, 12)))

PerformanceFactors2__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Yld'), Yield1__1, scope=PerformanceFactors2__1, documentation='YieldSpecifies the yield performance indicators for the fund.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3318, 12)))

def _BuildAutomaton_83 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_83
    del _BuildAutomaton_83
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PerformanceFactors2__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'FndValtn')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3306, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PerformanceFactors2__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'LqdtyInf')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3312, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(PerformanceFactors2__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Yld')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3318, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
PerformanceFactors2__1._Automaton = _BuildAutomaton_83()




PerformanceValueType1Choice__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Rate'), PercentageBoundedRate, scope=PerformanceValueType1Choice__1, documentation='RatePercentage indicating the performance of the instrument within each time range.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3332, 12)))

PerformanceValueType1Choice__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NotAvlblVal'), NotAvailable1Code, scope=PerformanceValueType1Choice__1, documentation='NotAvailableValueSpecifies that value is not available for that range.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3338, 12)))

def _BuildAutomaton_84 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_84
    del _BuildAutomaton_84
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(PerformanceValueType1Choice__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Rate')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3332, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(PerformanceValueType1Choice__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NotAvlblVal')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3338, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
PerformanceValueType1Choice__1._Automaton = _BuildAutomaton_84()




Period2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'FrDt'), ISODate, scope=Period2, documentation='FromDateDate and time at which the range starts.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3352, 12)))

Period2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ToDt'), ISODate, scope=Period2, documentation='ToDateDate and time at which the range ends.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3358, 12)))

def _BuildAutomaton_85 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_85
    del _BuildAutomaton_85
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Period2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'FrDt')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3352, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Period2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ToDt')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3358, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Period2._Automaton = _BuildAutomaton_85()




Period4Choice__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'FrDtToDt'), Period2, scope=Period4Choice__1, documentation='FromDateToDateTime span defined by a start date, and an end date.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3372, 12)))

def _BuildAutomaton_86 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_86
    del _BuildAutomaton_86
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Period4Choice__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'FrDtToDt')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3372, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Period4Choice__1._Automaton = _BuildAutomaton_86()




QuantitativeData4__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PrtflPrfrmnc'), PerformanceFactors2__1, scope=QuantitativeData4__1, documentation='PortfolioPerformanceProvide the details of the performance indicators for the money market fund during the reporting period.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3387, 12)))

QuantitativeData4__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'StrssTst'), StressTestReport1__1, scope=QuantitativeData4__1, documentation='StressTestInformation on the results of the last stress tests performed by the fund.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3393, 12)))

QuantitativeData4__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AsstInf'), HoldingAsset3__1, scope=QuantitativeData4__1, documentation='AssetInformationInformation on the assets held by the money market fund.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3399, 12)))

QuantitativeData4__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LbltyInf'), LiabilityData3__1, scope=QuantitativeData4__1, documentation='LiabilityInformationInformation related to the liabilities of the fund.\r\n', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3405, 12)))

QuantitativeData4__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LwVoltlyNetAsstValRptData'), LowVolatilityNetAssetValueReportData2__1, scope=QuantitativeData4__1, documentation='LowVolatilityNetAssetValueReportDataReport schema for the low volatility net asset value money market fund.\r\n', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3412, 12)))

def _BuildAutomaton_87 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_87
    del _BuildAutomaton_87
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3412, 12))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(QuantitativeData4__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PrtflPrfrmnc')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3387, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(QuantitativeData4__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'StrssTst')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3393, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(QuantitativeData4__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AsstInf')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3399, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(QuantitativeData4__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'LbltyInf')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3405, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(QuantitativeData4__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'LwVoltlyNetAsstValRptData')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3412, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
QuantitativeData4__1._Automaton = _BuildAutomaton_87()




Quarter3__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MnthInf'), MonthType3__1, scope=Quarter3__1, documentation='MonthInformationInformation related with a month.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3427, 12)))

def _BuildAutomaton_88 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_88
    del _BuildAutomaton_88
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=3, max=3, metadata=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3427, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Quarter3__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'MnthInf')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3427, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Quarter3__1._Automaton = _BuildAutomaton_88()




Quarter3__2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MnthInf'), MonthType3__2, scope=Quarter3__2, documentation='MonthInformationInformation related with a month.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3441, 12)))

def _BuildAutomaton_89 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_89
    del _BuildAutomaton_89
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=3, max=3, metadata=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3441, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Quarter3__2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'MnthInf')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3441, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Quarter3__2._Automaton = _BuildAutomaton_89()




Quarter3__3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MnthInf'), MonthType3__3, scope=Quarter3__3, documentation='MonthInformationInformation related with a month.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3455, 12)))

def _BuildAutomaton_90 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_90
    del _BuildAutomaton_90
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=3, max=3, metadata=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3455, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Quarter3__3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'MnthInf')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3455, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Quarter3__3._Automaton = _BuildAutomaton_90()




Quarter3__4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MnthInf'), MonthType3__4, scope=Quarter3__4, documentation='MonthInformationInformation related with a month.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3469, 12)))

def _BuildAutomaton_91 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_91
    del _BuildAutomaton_91
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=3, max=3, metadata=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3469, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Quarter3__4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'MnthInf')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3469, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Quarter3__4._Automaton = _BuildAutomaton_91()




Quarter3__5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MnthInf'), MonthType3__5, scope=Quarter3__5, documentation='MonthInformationInformation related with a month.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3483, 12)))

def _BuildAutomaton_92 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_92
    del _BuildAutomaton_92
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=3, max=3, metadata=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3483, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Quarter3__5._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'MnthInf')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3483, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Quarter3__5._Automaton = _BuildAutomaton_92()




Quarter3__6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MnthInf'), MonthType3__6, scope=Quarter3__6, documentation='MonthInformationInformation related with a month.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3497, 12)))

def _BuildAutomaton_93 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_93
    del _BuildAutomaton_93
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=3, max=3, metadata=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3497, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Quarter3__6._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'MnthInf')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3497, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Quarter3__6._Automaton = _BuildAutomaton_93()




Quarter3__7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MnthInf'), MonthType3__7, scope=Quarter3__7, documentation='MonthInformationInformation related with a month.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3511, 12)))

def _BuildAutomaton_94 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_94
    del _BuildAutomaton_94
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=3, max=3, metadata=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3511, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Quarter3__7._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'MnthInf')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3511, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Quarter3__7._Automaton = _BuildAutomaton_94()




Quarter3__8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MnthInf'), MonthType3__8, scope=Quarter3__8, documentation='MonthInformationInformation related with a month.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3525, 12)))

def _BuildAutomaton_95 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_95
    del _BuildAutomaton_95
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=3, max=3, metadata=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3525, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Quarter3__8._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'MnthInf')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3525, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Quarter3__8._Automaton = _BuildAutomaton_95()




QuarterPeriod1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'FrPrd'), ReportingPeriodType1Code, scope=QuarterPeriod1, documentation='FromPeriodLower boundary of a range of periods.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3539, 12)))

QuarterPeriod1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ToPrd'), ReportingPeriodType1Code, scope=QuarterPeriod1, documentation='ToPeriodUpper boundary of a range of periods.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3545, 12)))

def _BuildAutomaton_96 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_96
    del _BuildAutomaton_96
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(QuarterPeriod1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'FrPrd')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3539, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(QuarterPeriod1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ToPrd')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3545, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
QuarterPeriod1._Automaton = _BuildAutomaton_96()




RangeBreakdown1__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RgTp'), RangeType1Code__1, scope=RangeBreakdown1__1, documentation='RangeTypeSpecifies the time range for which the performance indicator is assessed.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3559, 12)))

RangeBreakdown1__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PrfrmncVal'), PerformanceValueType1Choice__1, scope=RangeBreakdown1__1, documentation='PerformanceValueValue assessing the performance for a specific time range.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3565, 12)))

def _BuildAutomaton_97 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_97
    del _BuildAutomaton_97
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RangeBreakdown1__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RgTp')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3559, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(RangeBreakdown1__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PrfrmncVal')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3565, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
RangeBreakdown1__1._Automaton = _BuildAutomaton_97()




RangeBreakdown1__2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RgTp'), RangeType1Code__2, scope=RangeBreakdown1__2, documentation='RangeTypeSpecifies the time range for which the performance indicator is assessed.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3579, 12)))

RangeBreakdown1__2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PrfrmncVal'), PerformanceValueType1Choice__1, scope=RangeBreakdown1__2, documentation='PerformanceValueValue assessing the performance for a specific time range.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3585, 12)))

def _BuildAutomaton_98 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_98
    del _BuildAutomaton_98
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RangeBreakdown1__2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RgTp')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3579, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(RangeBreakdown1__2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PrfrmncVal')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3585, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
RangeBreakdown1__2._Automaton = _BuildAutomaton_98()




RangeBreakdown1__3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RgTp'), RangeType1Code__3, scope=RangeBreakdown1__3, documentation='RangeTypeSpecifies the time range for which the performance indicator is assessed.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3599, 12)))

RangeBreakdown1__3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PrfrmncVal'), PerformanceValueType1Choice__1, scope=RangeBreakdown1__3, documentation='PerformanceValueValue assessing the performance for a specific time range.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3605, 12)))

def _BuildAutomaton_99 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_99
    del _BuildAutomaton_99
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RangeBreakdown1__3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RgTp')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3599, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(RangeBreakdown1__3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PrfrmncVal')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3605, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
RangeBreakdown1__3._Automaton = _BuildAutomaton_99()




RangeBreakdown1__4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RgTp'), RangeType1Code__4, scope=RangeBreakdown1__4, documentation='RangeTypeSpecifies the time range for which the performance indicator is assessed.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3619, 12)))

RangeBreakdown1__4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PrfrmncVal'), PerformanceValueType1Choice__1, scope=RangeBreakdown1__4, documentation='PerformanceValueValue assessing the performance for a specific time range.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3625, 12)))

def _BuildAutomaton_100 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_100
    del _BuildAutomaton_100
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RangeBreakdown1__4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RgTp')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3619, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(RangeBreakdown1__4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PrfrmncVal')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3625, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
RangeBreakdown1__4._Automaton = _BuildAutomaton_100()




RegisteredDistributionCountry2Choice__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NonEurpnCtry'), TrueFalseIndicator_fixed, scope=RegisteredDistributionCountry2Choice__1, documentation='NonEuropeanCountryReason for which no country where the fund is registered for distribution is reported.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3767, 12)))

RegisteredDistributionCountry2Choice__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Ctry'), CountryCode, scope=RegisteredDistributionCountry2Choice__1, documentation='CountryProvides the list of countries where the fund is registered for distribution.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3773, 12)))

def _BuildAutomaton_101 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_101
    del _BuildAutomaton_101
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(RegisteredDistributionCountry2Choice__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NonEurpnCtry')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3767, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(RegisteredDistributionCountry2Choice__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Ctry')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3773, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
RegisteredDistributionCountry2Choice__1._Automaton = _BuildAutomaton_101()




RelatedEvent2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'IncptnDt'), ISODate, scope=RelatedEvent2, documentation='InceptionDateDate at which the first net asset value of the fund was calculated under the Regulation.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3787, 12)))

RelatedEvent2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MrgrDt'), ISODate, scope=RelatedEvent2, documentation='MergerDateDate at which the last merger took place.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3793, 12)))

RelatedEvent2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LqdtnDt'), ISODate, scope=RelatedEvent2, documentation='LiquidationDateDate at which the liquidation took place.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3799, 12)))

RelatedEvent2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LastRptSnt'), TrueFalseIndicator, scope=RelatedEvent2, documentation='LastReportSentIndicates whether or not this report is the last report that will be sent by the submitting entity for that fund.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3805, 12)))

def _BuildAutomaton_102 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_102
    del _BuildAutomaton_102
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3787, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3793, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3799, 12))
    counters.add(cc_2)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RelatedEvent2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'IncptnDt')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3787, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RelatedEvent2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'MrgrDt')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3793, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RelatedEvent2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'LqdtnDt')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3799, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(RelatedEvent2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'LastRptSnt')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3805, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
RelatedEvent2._Automaton = _BuildAutomaton_102()




ReportData3Choice__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DataSetActn'), ReportPeriodActivity3Code__1, scope=ReportData3Choice__1, documentation='DataSetActionProvides the reason why no quantitative schema is being reported for a money market fund reporting period. ', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3820, 12)))

ReportData3Choice__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'QttvData'), QuantitativeData4__1, scope=ReportData3Choice__1, documentation='QuantitativeDataReport activity schema for all money market fund types.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3826, 12)))

def _BuildAutomaton_103 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_103
    del _BuildAutomaton_103
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ReportData3Choice__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataSetActn')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3820, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ReportData3Choice__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'QttvData')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3826, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ReportData3Choice__1._Automaton = _BuildAutomaton_103()




ReportItemJustification1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PlcAndNm'), Max350Text, scope=ReportItemJustification1, documentation='PlaceAndNameSpecifies from the root of the message the unambiguous reference to the location of the element for which the justification is applicable in the message instance.\r\nThis is expressed by a valid XPath.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3840, 12)))

ReportItemJustification1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Justfn'), MarketSpecificAttribute1, scope=ReportItemJustification1, documentation='JustificationProvides justification that might be reported by the submitting entity o.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3847, 12)))

def _BuildAutomaton_104 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_104
    del _BuildAutomaton_104
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ReportItemJustification1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PlcAndNm')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3840, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ReportItemJustification1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Justfn')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 3847, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ReportItemJustification1._Automaton = _BuildAutomaton_104()




SecurityIdentification31Choice._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ISIN'), ISINOct2015Identifier, scope=SecurityIdentification31Choice, documentation="ISINInternational Securities Identification Number (ISIN).  A numbering system designed by the United Nation's International Organisation for Standardisation (ISO). The ISIN is composed of a 2-character prefix representing the country of issue, followed by the national security number (if one exists), and a check digit. Each country has a national numbering agency that assigns ISIN numbers for securities in that country.", location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 4011, 12)))

SecurityIdentification31Choice._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Nm'), Max35Text, scope=SecurityIdentification31Choice, documentation='NameName used to identify the financial instrument.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 4017, 12)))

def _BuildAutomaton_105 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_105
    del _BuildAutomaton_105
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SecurityIdentification31Choice._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ISIN')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 4011, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SecurityIdentification31Choice._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Nm')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 4017, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
SecurityIdentification31Choice._Automaton = _BuildAutomaton_105()




SecurityIdentification33._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ISIN'), ISINOct2015Identifier, scope=SecurityIdentification33, documentation="ISINInternational Securities Identification Number (ISIN).  A numbering system designed by the United Nation's International Organisation for Standardisation (ISO). The ISIN is composed of a 2-character prefix representing the country of issue, followed by the national security number (if one exists), and a check digit. Each country has a national numbering agency that assigns ISIN numbers for securities in that country.", location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 4031, 12)))

SecurityIdentification33._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ClssfctnTp'), CFIOct2015Identifier, scope=SecurityIdentification33, documentation='ClassificationTypeISO 10962 Classification of Financial Instrument (CFI).', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 4037, 12)))

def _BuildAutomaton_106 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_106
    del _BuildAutomaton_106
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SecurityIdentification33._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ISIN')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 4031, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SecurityIdentification33._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ClssfctnTp')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 4037, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
SecurityIdentification33._Automaton = _BuildAutomaton_106()




ShareClassList1__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Id'), SecurityIdentification31Choice, scope=ShareClassList1__1, documentation='IdentificationIdentification of the fund or share class.\r\n', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 4052, 12)))

def _BuildAutomaton_107 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_107
    del _BuildAutomaton_107
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ShareClassList1__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Id')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 4052, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ShareClassList1__1._Automaton = _BuildAutomaton_107()




ShareClassList1__2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Id'), SecurityIdentification31Choice, scope=ShareClassList1__2, documentation='IdentificationIdentification of the fund or share class.\r\n', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 4068, 12)))

ShareClassList1__2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Ccy'), ActiveOrHistoricCurrencyCode, scope=ShareClassList1__2, documentation='CurrencyCurrency associated with the share class.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 4075, 12)))

ShareClassList1__2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'HghstNetAsstVal'), TrueFalseIndicator, scope=ShareClassList1__2, documentation='HighestNetAssetValueIndicates whether the share class is the share class with the highest net asset value.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 4081, 12)))

def _BuildAutomaton_108 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_108
    del _BuildAutomaton_108
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ShareClassList1__2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Id')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 4068, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ShareClassList1__2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Ccy')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 4075, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ShareClassList1__2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'HghstNetAsstVal')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 4081, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ShareClassList1__2._Automaton = _BuildAutomaton_108()




StressTestImpact1Choice._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NetAsstValImpct'), PercentageRate, scope=StressTestImpact1Choice, documentation='NetAssetValueImpactPercentage of the net asset value that is corresponding to the effects of a stressed scenario.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 4095, 12)))

StressTestImpact1Choice._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OutflwImpct'), OutflowImpact1, scope=StressTestImpact1Choice, documentation='OutflowImpactWeekly outflows derived from the monthly outflows compared with available weekly liquid assets, considered as the sum of highly liquid assets and weekly maturing assets. Rate computed for assets considered in the first bucket according to the Regulation.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 4101, 12)))

StressTestImpact1Choice._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NotAvlblVal'), NotAvailable1Code, scope=StressTestImpact1Choice, documentation='NotAvailableValueSpecifies that value is not available for that range.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 4107, 12)))

def _BuildAutomaton_109 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_109
    del _BuildAutomaton_109
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(StressTestImpact1Choice._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NetAsstValImpct')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 4095, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(StressTestImpact1Choice._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'OutflwImpct')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 4101, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(StressTestImpact1Choice._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NotAvlblVal')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 4107, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
StressTestImpact1Choice._Automaton = _BuildAutomaton_109()




StressTestReport1__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'StrssTstRslt'), StressTestResult2__1, scope=StressTestReport1__1, documentation='StressTestResultInformation on the results of the last stress tests performed by the fund.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 4121, 12)))

StressTestReport1__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ActnPlan'), ActionPlan1Choice__1, scope=StressTestReport1__1, documentation='ActionPlanAction plan that is proposed by the board of directors following a stress test that revealed any vulnerability of the fund.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 4127, 12)))

def _BuildAutomaton_110 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_110
    del _BuildAutomaton_110
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(StressTestReport1__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'StrssTstRslt')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 4121, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(StressTestReport1__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ActnPlan')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 4127, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
StressTestReport1__1._Automaton = _BuildAutomaton_110()




StressTestResult2__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'StrssTstDt'), ISODate, scope=StressTestResult2__1, documentation='StressTestDateDate when the last stress test was performed.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 4141, 12)))

StressTestResult2__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NetAsstValBsis'), NetAssetValueBasis1Code, scope=StressTestResult2__1, documentation='NetAssetValueBasisIdentifies whether the net asset value used as a basis for the stress test scenario is the constant net asset value.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 4147, 12)))

StressTestResult2__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'StrssTstScnroCd'), Max35Text, scope=StressTestResult2__1, documentation='StressTestScenarioCodeIdentifies the scenario that is assessed.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 4153, 12)))

StressTestResult2__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'StrssTstImpct'), StressTestImpact1Choice, scope=StressTestResult2__1, documentation='StressTestImpactSpecifies the effects of several plausible scenarios on several factors.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 4159, 12)))

StressTestResult2__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'InptFctr'), DecimalNumber, scope=StressTestResult2__1, documentation='InputFactorAny other additional factor used as an input in the stress test.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 4165, 12)))

StressTestResult2__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Cmnt'), Max350Text, scope=StressTestResult2__1, documentation='CommentAny other additional information about the stress test result.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 4171, 12)))

def _BuildAutomaton_111 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_111
    del _BuildAutomaton_111
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 4165, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 4171, 12))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(StressTestResult2__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'StrssTstDt')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 4141, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(StressTestResult2__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NetAsstValBsis')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 4147, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(StressTestResult2__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'StrssTstScnroCd')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 4153, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(StressTestResult2__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'StrssTstImpct')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 4159, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(StressTestResult2__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'InptFctr')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 4165, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(StressTestResult2__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Cmnt')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 4171, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
StressTestResult2__1._Automaton = _BuildAutomaton_111()




Yield1__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CmltvRtrsBrkdwn'), RangeBreakdown1__2, scope=Yield1__1, documentation='CumulativeReturnsBreakdownSpecifies the percentage of cumulative returns for each time period.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 4285, 12)))

Yield1__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'StdPrtflVoltlyBrkdwn'), RangeBreakdown1__3, scope=Yield1__1, documentation='StandardPortfolioVolatilityBreakdownSpecifies the percentage of portfolio volatility for each time period for all types of money market funds.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 4291, 12)))

Yield1__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ShdwPrtflVoltlyBrkdwn'), RangeBreakdown1__3, scope=Yield1__1, documentation='ShadowPortfolioVolatilityBreakdownSpecifies the percentage of shadow portfolio volatility for each time period for all types of money market funds.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 4297, 12)))

Yield1__1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CalYrPrfrmncBrkdwn'), RangeBreakdown1__4, scope=Yield1__1, documentation='CalendarYearPerformanceBreakdownSpecifies the percentage of calendar year performance returns for each time period.', location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 4303, 12)))

def _BuildAutomaton_112 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_112
    del _BuildAutomaton_112
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=6, max=6, metadata=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 4285, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=3, max=3, metadata=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 4291, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=3, metadata=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 4297, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=3, metadata=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 4303, 12))
    counters.add(cc_3)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Yield1__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CmltvRtrsBrkdwn')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 4285, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(Yield1__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'StdPrtflVoltlyBrkdwn')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 4291, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(Yield1__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ShdwPrtflVoltlyBrkdwn')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 4297, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(Yield1__1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CalYrPrfrmncBrkdwn')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd', 4303, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Yield1__1._Automaton = _BuildAutomaton_112()

