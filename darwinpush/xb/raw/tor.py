# ./darwinpush/xb/raw/tor.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:454478a728396cf19a8fffa7ba6764ae205b33f8
# Generated 2015-04-23 16:42:14.516405 by PyXB version 1.2.4 using Python 3.4.1.final.0
# Namespace http://www.thalesgroup.com/rtti/PushPort/TrainOrder/v1 [xmlns:tor]

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
Namespace = pyxb.namespace.NamespaceForURI('http://www.thalesgroup.com/rtti/PushPort/TrainOrder/v1', create_if_missing=True)
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


# Complex type {http://www.thalesgroup.com/rtti/PushPort/TrainOrder/v1}TrainOrderItem with content type ELEMENT_ONLY
class TrainOrderItem (pyxb.binding.basis.complexTypeDefinition):
    """Describes the identifier of a train in the train order"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TrainOrderItem')
    _XSDLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTTrainOrder_v1.xsd', 16, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.thalesgroup.com/rtti/PushPort/TrainOrder/v1}rid uses Python identifier rid
    __rid = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'rid'), 'rid', '__httpwww_thalesgroup_comrttiPushPortTrainOrderv1_TrainOrderItem_httpwww_thalesgroup_comrttiPushPortTrainOrderv1rid', False, pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTTrainOrder_v1.xsd', 21, 3), )

    
    rid = property(__rid.value, __rid.set, None, 'For trains in the train order where the train is the Darwin timetable, it will be identified by its RID')

    
    # Element {http://www.thalesgroup.com/rtti/PushPort/TrainOrder/v1}trainID uses Python identifier trainID
    __trainID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'trainID'), 'trainID', '__httpwww_thalesgroup_comrttiPushPortTrainOrderv1_TrainOrderItem_httpwww_thalesgroup_comrttiPushPortTrainOrderv1trainID', False, pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTTrainOrder_v1.xsd', 37, 3), )

    
    trainID = property(__trainID.value, __trainID.set, None, 'Where a train in the train order is not in the Darwin timetable, a Train ID (headcode) will be supplied')

    _ElementMap.update({
        __rid.name() : __rid,
        __trainID.name() : __trainID
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'TrainOrderItem', TrainOrderItem)


# Complex type {http://www.thalesgroup.com/rtti/PushPort/TrainOrder/v1}TrainOrderData with content type ELEMENT_ONLY
class TrainOrderData (pyxb.binding.basis.complexTypeDefinition):
    """Defines the sequence of trains making up the train order"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TrainOrderData')
    _XSDLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTTrainOrder_v1.xsd', 44, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.thalesgroup.com/rtti/PushPort/TrainOrder/v1}first uses Python identifier first
    __first = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'first'), 'first', '__httpwww_thalesgroup_comrttiPushPortTrainOrderv1_TrainOrderData_httpwww_thalesgroup_comrttiPushPortTrainOrderv1first', False, pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTTrainOrder_v1.xsd', 49, 3), )

    
    first = property(__first.value, __first.set, None, 'The first train in the train order.')

    
    # Element {http://www.thalesgroup.com/rtti/PushPort/TrainOrder/v1}second uses Python identifier second
    __second = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'second'), 'second', '__httpwww_thalesgroup_comrttiPushPortTrainOrderv1_TrainOrderData_httpwww_thalesgroup_comrttiPushPortTrainOrderv1second', False, pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTTrainOrder_v1.xsd', 55, 4), )

    
    second = property(__second.value, __second.set, None, 'The second train in the train order.')

    
    # Element {http://www.thalesgroup.com/rtti/PushPort/TrainOrder/v1}third uses Python identifier third
    __third = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'third'), 'third', '__httpwww_thalesgroup_comrttiPushPortTrainOrderv1_TrainOrderData_httpwww_thalesgroup_comrttiPushPortTrainOrderv1third', False, pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTTrainOrder_v1.xsd', 60, 4), )

    
    third = property(__third.value, __third.set, None, 'The third train in the train order.')

    _ElementMap.update({
        __first.name() : __first,
        __second.name() : __second,
        __third.name() : __third
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'TrainOrderData', TrainOrderData)


# Complex type [anonymous] with content type SIMPLE
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """For trains in the train order where the train is the Darwin timetable, it will be identified by its RID"""
    _TypeDefinition = _ImportedBinding_darwinpush_xb_ct.RIDType
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTTrainOrder_v1.xsd', 25, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is _ImportedBinding_darwinpush_xb_ct.RIDType
    
    # Attribute wta uses Python identifier wta
    __wta = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'wta'), 'wta', '__httpwww_thalesgroup_comrttiPushPortTrainOrderv1_CTD_ANON_wta', _ImportedBinding_darwinpush_xb_ct.WTimeType)
    __wta._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTCommonTypes_v1.xsd', 243, 2)
    __wta._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTCommonTypes_v1.xsd', 243, 2)
    
    wta = property(__wta.value, __wta.set, None, 'Working time of arrival.')

    
    # Attribute wtd uses Python identifier wtd
    __wtd = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'wtd'), 'wtd', '__httpwww_thalesgroup_comrttiPushPortTrainOrderv1_CTD_ANON_wtd', _ImportedBinding_darwinpush_xb_ct.WTimeType)
    __wtd._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTCommonTypes_v1.xsd', 248, 2)
    __wtd._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTCommonTypes_v1.xsd', 248, 2)
    
    wtd = property(__wtd.value, __wtd.set, None, 'Working time of departure.')

    
    # Attribute wtp uses Python identifier wtp
    __wtp = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'wtp'), 'wtp', '__httpwww_thalesgroup_comrttiPushPortTrainOrderv1_CTD_ANON_wtp', _ImportedBinding_darwinpush_xb_ct.WTimeType)
    __wtp._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTCommonTypes_v1.xsd', 253, 2)
    __wtp._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTCommonTypes_v1.xsd', 253, 2)
    
    wtp = property(__wtp.value, __wtp.set, None, 'Working time of pass.')

    
    # Attribute pta uses Python identifier pta
    __pta = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'pta'), 'pta', '__httpwww_thalesgroup_comrttiPushPortTrainOrderv1_CTD_ANON_pta', _ImportedBinding_darwinpush_xb_ct.RTTITimeType)
    __pta._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTCommonTypes_v1.xsd', 258, 2)
    __pta._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTCommonTypes_v1.xsd', 258, 2)
    
    pta = property(__pta.value, __pta.set, None, 'Public time of arrival.')

    
    # Attribute ptd uses Python identifier ptd
    __ptd = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ptd'), 'ptd', '__httpwww_thalesgroup_comrttiPushPortTrainOrderv1_CTD_ANON_ptd', _ImportedBinding_darwinpush_xb_ct.RTTITimeType)
    __ptd._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTCommonTypes_v1.xsd', 263, 2)
    __ptd._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTCommonTypes_v1.xsd', 263, 2)
    
    ptd = property(__ptd.value, __ptd.set, None, 'Public time of departure.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __wta.name() : __wta,
        __wtd.name() : __wtd,
        __wtp.name() : __wtp,
        __pta.name() : __pta,
        __ptd.name() : __ptd
    })



# Complex type {http://www.thalesgroup.com/rtti/PushPort/TrainOrder/v1}TrainOrder with content type ELEMENT_ONLY
class TrainOrder (pyxb.binding.basis.complexTypeDefinition):
    """Defines the expected Train order at a platform"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TrainOrder')
    _XSDLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTTrainOrder_v1.xsd', 68, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.thalesgroup.com/rtti/PushPort/TrainOrder/v1}set uses Python identifier set_
    __set = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'set'), 'set_', '__httpwww_thalesgroup_comrttiPushPortTrainOrderv1_TrainOrder_httpwww_thalesgroup_comrttiPushPortTrainOrderv1set', False, pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTTrainOrder_v1.xsd', 73, 3), )

    
    set_ = property(__set.value, __set.set, None, None)

    
    # Element {http://www.thalesgroup.com/rtti/PushPort/TrainOrder/v1}clear uses Python identifier clear
    __clear = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'clear'), 'clear', '__httpwww_thalesgroup_comrttiPushPortTrainOrderv1_TrainOrder_httpwww_thalesgroup_comrttiPushPortTrainOrderv1clear', False, pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTTrainOrder_v1.xsd', 74, 3), )

    
    clear = property(__clear.value, __clear.set, None, 'Clear the current train order')

    
    # Attribute tiploc uses Python identifier tiploc
    __tiploc = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'tiploc'), 'tiploc', '__httpwww_thalesgroup_comrttiPushPortTrainOrderv1_TrainOrder_tiploc', _ImportedBinding_darwinpush_xb_ct.TiplocType, required=True)
    __tiploc._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTTrainOrder_v1.xsd', 80, 2)
    __tiploc._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTTrainOrder_v1.xsd', 80, 2)
    
    tiploc = property(__tiploc.value, __tiploc.set, None, 'The tiploc where the train order applies')

    
    # Attribute crs uses Python identifier crs
    __crs = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'crs'), 'crs', '__httpwww_thalesgroup_comrttiPushPortTrainOrderv1_TrainOrder_crs', _ImportedBinding_darwinpush_xb_ct.CrsType, required=True)
    __crs._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTTrainOrder_v1.xsd', 85, 2)
    __crs._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTTrainOrder_v1.xsd', 85, 2)
    
    crs = property(__crs.value, __crs.set, None, 'The CRS code of the station where the train order applies')

    
    # Attribute platform uses Python identifier platform
    __platform = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'platform'), 'platform', '__httpwww_thalesgroup_comrttiPushPortTrainOrderv1_TrainOrder_platform', _ImportedBinding_darwinpush_xb_ct.PlatformType, required=True)
    __platform._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTTrainOrder_v1.xsd', 90, 2)
    __platform._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTTrainOrder_v1.xsd', 90, 2)
    
    platform = property(__platform.value, __platform.set, None, 'The platform number where the train order applies')

    _ElementMap.update({
        __set.name() : __set,
        __clear.name() : __clear
    })
    _AttributeMap.update({
        __tiploc.name() : __tiploc,
        __crs.name() : __crs,
        __platform.name() : __platform
    })
Namespace.addCategoryObject('typeBinding', 'TrainOrder', TrainOrder)




TrainOrderItem._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'rid'), CTD_ANON, scope=TrainOrderItem, documentation='For trains in the train order where the train is the Darwin timetable, it will be identified by its RID', location=pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTTrainOrder_v1.xsd', 21, 3)))

TrainOrderItem._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'trainID'), _ImportedBinding_darwinpush_xb_ct.TrainIdType, scope=TrainOrderItem, documentation='Where a train in the train order is not in the Darwin timetable, a Train ID (headcode) will be supplied', location=pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTTrainOrder_v1.xsd', 37, 3)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TrainOrderItem._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'rid')), pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTTrainOrder_v1.xsd', 21, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TrainOrderItem._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'trainID')), pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTTrainOrder_v1.xsd', 37, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TrainOrderItem._Automaton = _BuildAutomaton()




TrainOrderData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'first'), TrainOrderItem, scope=TrainOrderData, documentation='The first train in the train order.', location=pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTTrainOrder_v1.xsd', 49, 3)))

TrainOrderData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'second'), TrainOrderItem, scope=TrainOrderData, documentation='The second train in the train order.', location=pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTTrainOrder_v1.xsd', 55, 4)))

TrainOrderData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'third'), TrainOrderItem, scope=TrainOrderData, documentation='The third train in the train order.', location=pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTTrainOrder_v1.xsd', 60, 4)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTTrainOrder_v1.xsd', 54, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTTrainOrder_v1.xsd', 60, 4))
    counters.add(cc_1)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TrainOrderData._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'first')), pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTTrainOrder_v1.xsd', 49, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TrainOrderData._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'second')), pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTTrainOrder_v1.xsd', 55, 4))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(TrainOrderData._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'third')), pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTTrainOrder_v1.xsd', 60, 4))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TrainOrderData._Automaton = _BuildAutomaton_()




TrainOrder._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'set'), TrainOrderData, scope=TrainOrder, location=pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTTrainOrder_v1.xsd', 73, 3)))

TrainOrder._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'clear'), pyxb.binding.datatypes.anyType, scope=TrainOrder, documentation='Clear the current train order', location=pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTTrainOrder_v1.xsd', 74, 3)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TrainOrder._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'set')), pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTTrainOrder_v1.xsd', 73, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TrainOrder._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'clear')), pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTTrainOrder_v1.xsd', 74, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TrainOrder._Automaton = _BuildAutomaton_2()

