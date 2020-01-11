# ./exa2.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:2f7fa5f5afdd2d587bab2d949cd2ee356861f34d
# Generated 2019-12-10 10:10:40.938466 by PyXB version 1.2.6 using Python 3.7.5.final.0
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
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:f00ff554-1b2c-11ea-b008-88e9fe84fcb4')

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


# Atomic simple type: [anonymous]
class STD_ANON (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/example.xsd', 14, 10)
    _Documentation = None
STD_ANON._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON, enum_prefix=None)
STD_ANON.IN = STD_ANON._CF_enumeration.addEnumeration(unicode_value='IN', tag='IN')
STD_ANON.DE = STD_ANON._CF_enumeration.addEnumeration(unicode_value='DE', tag='DE')
STD_ANON.ES = STD_ANON._CF_enumeration.addEnumeration(unicode_value='ES', tag='ES')
STD_ANON.UK = STD_ANON._CF_enumeration.addEnumeration(unicode_value='UK', tag='UK')
STD_ANON.US = STD_ANON._CF_enumeration.addEnumeration(unicode_value='US', tag='US')
STD_ANON._InitializeFacetMap(STD_ANON._CF_enumeration)
_module_typeBindings.STD_ANON = STD_ANON

# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/example.xsd', 5, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}FullName uses Python identifier FullName
    __FullName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'FullName'), 'FullName', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_CTD_ANON_urnisostdiso20022techxsdDRAFT3auth_093_001_01FullName', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/example.xsd', 7, 8), )

    
    FullName = property(__FullName.value, __FullName.set, None, None)

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}House uses Python identifier House
    __House = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'House'), 'House', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_CTD_ANON_urnisostdiso20022techxsdDRAFT3auth_093_001_01House', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/example.xsd', 8, 8), )

    
    House = property(__House.value, __House.set, None, None)

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}Street uses Python identifier Street
    __Street = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Street'), 'Street', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_CTD_ANON_urnisostdiso20022techxsdDRAFT3auth_093_001_01Street', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/example.xsd', 9, 8), )

    
    Street = property(__Street.value, __Street.set, None, None)

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}Town uses Python identifier Town
    __Town = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Town'), 'Town', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_CTD_ANON_urnisostdiso20022techxsdDRAFT3auth_093_001_01Town', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/example.xsd', 10, 8), )

    
    Town = property(__Town.value, __Town.set, None, None)

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}County uses Python identifier County
    __County = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'County'), 'County', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_CTD_ANON_urnisostdiso20022techxsdDRAFT3auth_093_001_01County', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/example.xsd', 11, 8), )

    
    County = property(__County.value, __County.set, None, None)

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}PostCode uses Python identifier PostCode
    __PostCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PostCode'), 'PostCode', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_CTD_ANON_urnisostdiso20022techxsdDRAFT3auth_093_001_01PostCode', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/example.xsd', 12, 8), )

    
    PostCode = property(__PostCode.value, __PostCode.set, None, None)

    
    # Element {urn:iso:std:iso:20022:tech:xsd:DRAFT3auth.093.001.01}Country uses Python identifier Country
    __Country = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Country'), 'Country', '__urnisostdiso20022techxsdDRAFT3auth_093_001_01_CTD_ANON_urnisostdiso20022techxsdDRAFT3auth_093_001_01Country', False, pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/example.xsd', 13, 8), )

    
    Country = property(__Country.value, __Country.set, None, None)

    _ElementMap.update({
        __FullName.name() : __FullName,
        __House.name() : __House,
        __Street.name() : __Street,
        __Town.name() : __Town,
        __County.name() : __County,
        __PostCode.name() : __PostCode,
        __Country.name() : __Country
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON = CTD_ANON


Address = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Address'), CTD_ANON, location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/example.xsd', 4, 2))
Namespace.addCategoryObject('elementBinding', Address.name().localName(), Address)



CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'FullName'), pyxb.binding.datatypes.string, scope=CTD_ANON, location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/example.xsd', 7, 8)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'House'), pyxb.binding.datatypes.string, scope=CTD_ANON, location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/example.xsd', 8, 8)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Street'), pyxb.binding.datatypes.string, scope=CTD_ANON, location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/example.xsd', 9, 8)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Town'), pyxb.binding.datatypes.string, scope=CTD_ANON, location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/example.xsd', 10, 8)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'County'), pyxb.binding.datatypes.string, scope=CTD_ANON, location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/example.xsd', 11, 8)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PostCode'), pyxb.binding.datatypes.string, scope=CTD_ANON, location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/example.xsd', 12, 8)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Country'), STD_ANON, scope=CTD_ANON, location=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/example.xsd', 13, 8)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/example.xsd', 11, 8))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/example.xsd', 13, 8))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'FullName')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/example.xsd', 7, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'House')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/example.xsd', 8, 8))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Street')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/example.xsd', 9, 8))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Town')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/example.xsd', 10, 8))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'County')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/example.xsd', 11, 8))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PostCode')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/example.xsd', 12, 8))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Country')), pyxb.utils.utility.Location('/Users/plo/PyCharm/mmfr/schema/example.xsd', 13, 8))
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
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton()

