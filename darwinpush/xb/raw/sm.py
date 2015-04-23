# ./darwinpush/xb/raw/sm.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:8eb48f8f0e727f488907a816c69d6ed98ba221c7
# Generated 2015-04-23 16:42:14.513978 by PyXB version 1.2.4 using Python 3.4.1.final.0
# Namespace http://www.thalesgroup.com/rtti/PushPort/StationMessages/v1 [xmlns:sm]

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
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:5049f1de-e9cf-11e4-bb50-a0481ca50ab0')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.4'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes
import darwinpush.xb.ct as _ImportedBinding_darwinpush_xb_ct

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://www.thalesgroup.com/rtti/PushPort/StationMessages/v1', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
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


# Atomic simple type: {http://www.thalesgroup.com/rtti/PushPort/StationMessages/v1}MsgCategoryType
class MsgCategoryType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """The category of operator message"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MsgCategoryType')
    _XSDLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTStationMessages_v1.xsd', 15, 1)
    _Documentation = 'The category of operator message'
MsgCategoryType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=MsgCategoryType, enum_prefix=None)
MsgCategoryType.Train = MsgCategoryType._CF_enumeration.addEnumeration(unicode_value='Train', tag='Train')
MsgCategoryType.Station = MsgCategoryType._CF_enumeration.addEnumeration(unicode_value='Station', tag='Station')
MsgCategoryType.Connections = MsgCategoryType._CF_enumeration.addEnumeration(unicode_value='Connections', tag='Connections')
MsgCategoryType.System = MsgCategoryType._CF_enumeration.addEnumeration(unicode_value='System', tag='System')
MsgCategoryType.Misc = MsgCategoryType._CF_enumeration.addEnumeration(unicode_value='Misc', tag='Misc')
MsgCategoryType.PriorTrains = MsgCategoryType._CF_enumeration.addEnumeration(unicode_value='PriorTrains', tag='PriorTrains')
MsgCategoryType.PriorOther = MsgCategoryType._CF_enumeration.addEnumeration(unicode_value='PriorOther', tag='PriorOther')
MsgCategoryType._InitializeFacetMap(MsgCategoryType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'MsgCategoryType', MsgCategoryType)

# Atomic simple type: {http://www.thalesgroup.com/rtti/PushPort/StationMessages/v1}MsgSeverityType
class MsgSeverityType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """The severity of operator message"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MsgSeverityType')
    _XSDLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTStationMessages_v1.xsd', 29, 1)
    _Documentation = 'The severity of operator message'
MsgSeverityType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=MsgSeverityType, enum_prefix=None)
MsgSeverityType.n0 = MsgSeverityType._CF_enumeration.addEnumeration(unicode_value='0', tag='n0')
MsgSeverityType.n1 = MsgSeverityType._CF_enumeration.addEnumeration(unicode_value='1', tag='n1')
MsgSeverityType.n2 = MsgSeverityType._CF_enumeration.addEnumeration(unicode_value='2', tag='n2')
MsgSeverityType.n3 = MsgSeverityType._CF_enumeration.addEnumeration(unicode_value='3', tag='n3')
MsgSeverityType._InitializeFacetMap(MsgSeverityType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'MsgSeverityType', MsgSeverityType)

# Complex type [anonymous] with content type MIXED
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """The content of the message"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTStationMessages_v1.xsd', 58, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.thalesgroup.com/rtti/PushPort/StationMessages/v1}p uses Python identifier p
    __p = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'p'), 'p', '__httpwww_thalesgroup_comrttiPushPortStationMessagesv1_CTD_ANON_httpwww_thalesgroup_comrttiPushPortStationMessagesv1p', True, pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTStationMessages_v1.xsd', 84, 1), )

    
    p = property(__p.value, __p.set, None, 'Defines an HTML paragraph')

    
    # Element {http://www.thalesgroup.com/rtti/PushPort/StationMessages/v1}a uses Python identifier a
    __a = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'a'), 'a', '__httpwww_thalesgroup_comrttiPushPortStationMessagesv1_CTD_ANON_httpwww_thalesgroup_comrttiPushPortStationMessagesv1a', True, pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTStationMessages_v1.xsd', 94, 1), )

    
    a = property(__a.value, __a.set, None, 'Defines an HTML anchor')

    _ElementMap.update({
        __p.name() : __p,
        __a.name() : __a
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type MIXED
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """Defines an HTML paragraph"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTStationMessages_v1.xsd', 88, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.thalesgroup.com/rtti/PushPort/StationMessages/v1}a uses Python identifier a
    __a = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'a'), 'a', '__httpwww_thalesgroup_comrttiPushPortStationMessagesv1_CTD_ANON__httpwww_thalesgroup_comrttiPushPortStationMessagesv1a', True, pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTStationMessages_v1.xsd', 94, 1), )

    
    a = property(__a.value, __a.set, None, 'Defines an HTML anchor')

    _ElementMap.update({
        __a.name() : __a
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    """Defines an HTML anchor"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTStationMessages_v1.xsd', 98, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute href uses Python identifier href
    __href = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'href'), 'href', '__httpwww_thalesgroup_comrttiPushPortStationMessagesv1_CTD_ANON_2_href', pyxb.binding.datatypes.string, required=True)
    __href._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTStationMessages_v1.xsd', 101, 5)
    __href._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTStationMessages_v1.xsd', 101, 5)
    
    href = property(__href.value, __href.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __href.name() : __href
    })



# Complex type {http://www.thalesgroup.com/rtti/PushPort/StationMessages/v1}StationMessage with content type ELEMENT_ONLY
class StationMessage (pyxb.binding.basis.complexTypeDefinition):
    """Darwin Workstation Station Message"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'StationMessage')
    _XSDLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTStationMessages_v1.xsd', 41, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.thalesgroup.com/rtti/PushPort/StationMessages/v1}Station uses Python identifier Station
    __Station = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Station'), 'Station', '__httpwww_thalesgroup_comrttiPushPortStationMessagesv1_StationMessage_httpwww_thalesgroup_comrttiPushPortStationMessagesv1Station', True, pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTStationMessages_v1.xsd', 46, 3), )

    
    Station = property(__Station.value, __Station.set, None, 'The Stations the message is being applied to')

    
    # Element {http://www.thalesgroup.com/rtti/PushPort/StationMessages/v1}Msg uses Python identifier Msg
    __Msg = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Msg'), 'Msg', '__httpwww_thalesgroup_comrttiPushPortStationMessagesv1_StationMessage_httpwww_thalesgroup_comrttiPushPortStationMessagesv1Msg', False, pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTStationMessages_v1.xsd', 54, 3), )

    
    Msg = property(__Msg.value, __Msg.set, None, 'The content of the message')

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__httpwww_thalesgroup_comrttiPushPortStationMessagesv1_StationMessage_id', pyxb.binding.datatypes.int, required=True)
    __id._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTStationMessages_v1.xsd', 66, 2)
    __id._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTStationMessages_v1.xsd', 66, 2)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute cat uses Python identifier cat
    __cat = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'cat'), 'cat', '__httpwww_thalesgroup_comrttiPushPortStationMessagesv1_StationMessage_cat', MsgCategoryType, required=True)
    __cat._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTStationMessages_v1.xsd', 67, 2)
    __cat._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTStationMessages_v1.xsd', 67, 2)
    
    cat = property(__cat.value, __cat.set, None, 'The category of message')

    
    # Attribute sev uses Python identifier sev
    __sev = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'sev'), 'sev', '__httpwww_thalesgroup_comrttiPushPortStationMessagesv1_StationMessage_sev', MsgSeverityType, required=True)
    __sev._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTStationMessages_v1.xsd', 72, 2)
    __sev._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTStationMessages_v1.xsd', 72, 2)
    
    sev = property(__sev.value, __sev.set, None, 'The severity of the message')

    
    # Attribute suppress uses Python identifier suppress
    __suppress = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'suppress'), 'suppress', '__httpwww_thalesgroup_comrttiPushPortStationMessagesv1_StationMessage_suppress', pyxb.binding.datatypes.boolean, unicode_default='false')
    __suppress._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTStationMessages_v1.xsd', 77, 2)
    __suppress._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTStationMessages_v1.xsd', 77, 2)
    
    suppress = property(__suppress.value, __suppress.set, None, 'Whether the train running information is suppressed to the public')

    _ElementMap.update({
        __Station.name() : __Station,
        __Msg.name() : __Msg
    })
    _AttributeMap.update({
        __id.name() : __id,
        __cat.name() : __cat,
        __sev.name() : __sev,
        __suppress.name() : __suppress
    })
Namespace.addCategoryObject('typeBinding', 'StationMessage', StationMessage)


# Complex type [anonymous] with content type EMPTY
class CTD_ANON_3 (pyxb.binding.basis.complexTypeDefinition):
    """The Stations the message is being applied to"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTStationMessages_v1.xsd', 50, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute crs uses Python identifier crs
    __crs = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'crs'), 'crs', '__httpwww_thalesgroup_comrttiPushPortStationMessagesv1_CTD_ANON_3_crs', _ImportedBinding_darwinpush_xb_ct.CrsType, required=True)
    __crs._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTStationMessages_v1.xsd', 51, 5)
    __crs._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTStationMessages_v1.xsd', 51, 5)
    
    crs = property(__crs.value, __crs.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __crs.name() : __crs
    })



p = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'p'), CTD_ANON_, documentation='Defines an HTML paragraph', location=pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTStationMessages_v1.xsd', 84, 1))
Namespace.addCategoryObject('elementBinding', p.name().localName(), p)

a = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'a'), CTD_ANON_2, documentation='Defines an HTML anchor', location=pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTStationMessages_v1.xsd', 94, 1))
Namespace.addCategoryObject('elementBinding', a.name().localName(), a)



CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'p'), CTD_ANON_, scope=CTD_ANON, documentation='Defines an HTML paragraph', location=pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTStationMessages_v1.xsd', 84, 1)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'a'), CTD_ANON_2, scope=CTD_ANON, documentation='Defines an HTML anchor', location=pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTStationMessages_v1.xsd', 94, 1)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTStationMessages_v1.xsd', 60, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTStationMessages_v1.xsd', 61, 6))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'p')), pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTStationMessages_v1.xsd', 60, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'a')), pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTStationMessages_v1.xsd', 61, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton()




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'a'), CTD_ANON_2, scope=CTD_ANON_, documentation='Defines an HTML anchor', location=pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTStationMessages_v1.xsd', 94, 1)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTStationMessages_v1.xsd', 90, 4))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'a')), pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTStationMessages_v1.xsd', 90, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_._Automaton = _BuildAutomaton_()




StationMessage._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Station'), CTD_ANON_3, scope=StationMessage, documentation='The Stations the message is being applied to', location=pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTStationMessages_v1.xsd', 46, 3)))

StationMessage._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Msg'), CTD_ANON, scope=StationMessage, documentation='The content of the message', location=pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTStationMessages_v1.xsd', 54, 3)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTStationMessages_v1.xsd', 46, 3))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(StationMessage._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Station')), pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTStationMessages_v1.xsd', 46, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(StationMessage._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Msg')), pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTStationMessages_v1.xsd', 54, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
StationMessage._Automaton = _BuildAutomaton_2()

