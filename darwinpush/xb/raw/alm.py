# ./darwinpush/xb/raw/alm.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:9fa3e4956e5b72d2d009e00b95bfe9aac5c5bfce
# Generated 2015-04-23 16:42:14.514926 by PyXB version 1.2.4 using Python 3.4.1.final.0
# Namespace http://www.thalesgroup.com/rtti/PushPort/Alarms/v1 [xmlns:alm]

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
Namespace = pyxb.namespace.NamespaceForURI('http://www.thalesgroup.com/rtti/PushPort/Alarms/v1', create_if_missing=True)
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


# Atomic simple type: {http://www.thalesgroup.com/rtti/PushPort/Alarms/v1}AlarmID
class AlarmID (pyxb.binding.datatypes.string):

    """Type representing a unique Darwin alarm identifier."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AlarmID')
    _XSDLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTAlarms_v1.xsd', 15, 1)
    _Documentation = 'Type representing a unique Darwin alarm identifier.'
AlarmID._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'AlarmID', AlarmID)

# Complex type {http://www.thalesgroup.com/rtti/PushPort/Alarms/v1}RTTIAlarm with content type ELEMENT_ONLY
class RTTIAlarm (pyxb.binding.basis.complexTypeDefinition):
    """An update to a Darwin alarm."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RTTIAlarm')
    _XSDLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTAlarms_v1.xsd', 49, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.thalesgroup.com/rtti/PushPort/Alarms/v1}set uses Python identifier set_
    __set = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'set'), 'set_', '__httpwww_thalesgroup_comrttiPushPortAlarmsv1_RTTIAlarm_httpwww_thalesgroup_comrttiPushPortAlarmsv1set', False, pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTAlarms_v1.xsd', 54, 3), )

    
    set_ = property(__set.value, __set.set, None, 'Set a new alarm.')

    
    # Element {http://www.thalesgroup.com/rtti/PushPort/Alarms/v1}clear uses Python identifier clear
    __clear = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'clear'), 'clear', '__httpwww_thalesgroup_comrttiPushPortAlarmsv1_RTTIAlarm_httpwww_thalesgroup_comrttiPushPortAlarmsv1clear', False, pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTAlarms_v1.xsd', 59, 3), )

    
    clear = property(__clear.value, __clear.set, None, 'Clear an existing alarm. The contents identify the unique alarm identifier that has been cleared.')

    _ElementMap.update({
        __set.name() : __set,
        __clear.name() : __clear
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'RTTIAlarm', RTTIAlarm)


# Complex type {http://www.thalesgroup.com/rtti/PushPort/Alarms/v1}RTTIAlarmData with content type ELEMENT_ONLY
class RTTIAlarmData (pyxb.binding.basis.complexTypeDefinition):
    """Type describing each type of alarm that can be set."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RTTIAlarmData')
    _XSDLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTAlarms_v1.xsd', 22, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.thalesgroup.com/rtti/PushPort/Alarms/v1}tdAreaFail uses Python identifier tdAreaFail
    __tdAreaFail = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'tdAreaFail'), 'tdAreaFail', '__httpwww_thalesgroup_comrttiPushPortAlarmsv1_RTTIAlarmData_httpwww_thalesgroup_comrttiPushPortAlarmsv1tdAreaFail', False, pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTAlarms_v1.xsd', 27, 3), )

    
    tdAreaFail = property(__tdAreaFail.value, __tdAreaFail.set, None, 'Alarm for a single TD area failure. Contents identify the failed area code.')

    
    # Element {http://www.thalesgroup.com/rtti/PushPort/Alarms/v1}tdFeedFail uses Python identifier tdFeedFail
    __tdFeedFail = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'tdFeedFail'), 'tdFeedFail', '__httpwww_thalesgroup_comrttiPushPortAlarmsv1_RTTIAlarmData_httpwww_thalesgroup_comrttiPushPortAlarmsv1tdFeedFail', False, pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTAlarms_v1.xsd', 32, 3), )

    
    tdFeedFail = property(__tdFeedFail.value, __tdFeedFail.set, None, 'Alarm for the failure of the entire TD feed into Darwin.')

    
    # Element {http://www.thalesgroup.com/rtti/PushPort/Alarms/v1}tyrellFeedFail uses Python identifier tyrellFeedFail
    __tyrellFeedFail = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'tyrellFeedFail'), 'tyrellFeedFail', '__httpwww_thalesgroup_comrttiPushPortAlarmsv1_RTTIAlarmData_httpwww_thalesgroup_comrttiPushPortAlarmsv1tyrellFeedFail', False, pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTAlarms_v1.xsd', 37, 3), )

    
    tyrellFeedFail = property(__tyrellFeedFail.value, __tyrellFeedFail.set, None, 'Alarm for the failure of the Tyrell feed into Darwin.')

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__httpwww_thalesgroup_comrttiPushPortAlarmsv1_RTTIAlarmData_id', AlarmID, required=True)
    __id._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTAlarms_v1.xsd', 43, 2)
    __id._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTAlarms_v1.xsd', 43, 2)
    
    id = property(__id.value, __id.set, None, 'Unique identifier for this alarm')

    _ElementMap.update({
        __tdAreaFail.name() : __tdAreaFail,
        __tdFeedFail.name() : __tdFeedFail,
        __tyrellFeedFail.name() : __tyrellFeedFail
    })
    _AttributeMap.update({
        __id.name() : __id
    })
Namespace.addCategoryObject('typeBinding', 'RTTIAlarmData', RTTIAlarmData)




RTTIAlarm._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'set'), RTTIAlarmData, scope=RTTIAlarm, documentation='Set a new alarm.', location=pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTAlarms_v1.xsd', 54, 3)))

RTTIAlarm._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'clear'), AlarmID, scope=RTTIAlarm, documentation='Clear an existing alarm. The contents identify the unique alarm identifier that has been cleared.', location=pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTAlarms_v1.xsd', 59, 3)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(RTTIAlarm._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'set')), pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTAlarms_v1.xsd', 54, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(RTTIAlarm._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'clear')), pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTAlarms_v1.xsd', 59, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
RTTIAlarm._Automaton = _BuildAutomaton()




RTTIAlarmData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'tdAreaFail'), _ImportedBinding_darwinpush_xb_ct.TDAreaIDType, scope=RTTIAlarmData, documentation='Alarm for a single TD area failure. Contents identify the failed area code.', location=pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTAlarms_v1.xsd', 27, 3)))

RTTIAlarmData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'tdFeedFail'), pyxb.binding.datatypes.anyType, scope=RTTIAlarmData, documentation='Alarm for the failure of the entire TD feed into Darwin.', location=pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTAlarms_v1.xsd', 32, 3)))

RTTIAlarmData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'tyrellFeedFail'), pyxb.binding.datatypes.anyType, scope=RTTIAlarmData, documentation='Alarm for the failure of the Tyrell feed into Darwin.', location=pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTAlarms_v1.xsd', 37, 3)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(RTTIAlarmData._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'tdAreaFail')), pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTAlarms_v1.xsd', 27, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(RTTIAlarmData._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'tdFeedFail')), pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTAlarms_v1.xsd', 32, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(RTTIAlarmData._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'tyrellFeedFail')), pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTAlarms_v1.xsd', 37, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
RTTIAlarmData._Automaton = _BuildAutomaton_()

