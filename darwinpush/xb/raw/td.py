# ./darwinpush/xb/raw/td.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:ec3ff59c2418d971c0c03ea43d7e8b23a3496599
# Generated 2015-04-23 16:42:14.517941 by PyXB version 1.2.4 using Python 3.4.1.final.0
# Namespace http://www.thalesgroup.com/rtti/PushPort/TDData/v1 [xmlns:td]

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
Namespace = pyxb.namespace.NamespaceForURI('http://www.thalesgroup.com/rtti/PushPort/TDData/v1', create_if_missing=True)
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


# Complex type {http://www.thalesgroup.com/rtti/PushPort/TDData/v1}TrackingID with content type ELEMENT_ONLY
class TrackingID (pyxb.binding.basis.complexTypeDefinition):
    """Indicate a corrected Tracking ID (headcode) for a service in a TD berth."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TrackingID')
    _XSDLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTTDData_v1.xsd', 23, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.thalesgroup.com/rtti/PushPort/TDData/v1}berth uses Python identifier berth
    __berth = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'berth'), 'berth', '__httpwww_thalesgroup_comrttiPushPortTDDatav1_TrackingID_httpwww_thalesgroup_comrttiPushPortTDDatav1berth', False, pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTTDData_v1.xsd', 28, 3), )

    
    berth = property(__berth.value, __berth.set, None, 'The TD berth where the incorrectly reported train has been identified to be. Note that this berth is that which was reported to Darwin and there is no guarantee that the train is still in this berth at any subsequent point in time.')

    
    # Element {http://www.thalesgroup.com/rtti/PushPort/TDData/v1}incorrectTrainID uses Python identifier incorrectTrainID
    __incorrectTrainID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'incorrectTrainID'), 'incorrectTrainID', '__httpwww_thalesgroup_comrttiPushPortTDDatav1_TrackingID_httpwww_thalesgroup_comrttiPushPortTDDatav1incorrectTrainID', False, pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTTDData_v1.xsd', 33, 3), )

    
    incorrectTrainID = property(__incorrectTrainID.value, __incorrectTrainID.set, None, 'The incorrect Train ID (headcode) that is being reported by TD.NET.')

    
    # Element {http://www.thalesgroup.com/rtti/PushPort/TDData/v1}correctTrainID uses Python identifier correctTrainID
    __correctTrainID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'correctTrainID'), 'correctTrainID', '__httpwww_thalesgroup_comrttiPushPortTDDatav1_TrackingID_httpwww_thalesgroup_comrttiPushPortTDDatav1correctTrainID', False, pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTTDData_v1.xsd', 38, 3), )

    
    correctTrainID = property(__correctTrainID.value, __correctTrainID.set, None, 'The correct Train ID (headcode) that should be reported by TD.NET.')

    _ElementMap.update({
        __berth.name() : __berth,
        __incorrectTrainID.name() : __incorrectTrainID,
        __correctTrainID.name() : __correctTrainID
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'TrackingID', TrackingID)


# Complex type {http://www.thalesgroup.com/rtti/PushPort/TDData/v1}FullTDBerthID with content type SIMPLE
class FullTDBerthID (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.thalesgroup.com/rtti/PushPort/TDData/v1}FullTDBerthID with content type SIMPLE"""
    _TypeDefinition = _ImportedBinding_darwinpush_xb_ct.TDBerthIDType
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'FullTDBerthID')
    _XSDLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTTDData_v1.xsd', 16, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is _ImportedBinding_darwinpush_xb_ct.TDBerthIDType
    
    # Attribute area uses Python identifier area
    __area = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'area'), 'area', '__httpwww_thalesgroup_comrttiPushPortTDDatav1_FullTDBerthID_area', _ImportedBinding_darwinpush_xb_ct.TDAreaIDType, required=True)
    __area._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTTDData_v1.xsd', 19, 4)
    __area._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTTDData_v1.xsd', 19, 4)
    
    area = property(__area.value, __area.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __area.name() : __area
    })
Namespace.addCategoryObject('typeBinding', 'FullTDBerthID', FullTDBerthID)




TrackingID._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'berth'), FullTDBerthID, scope=TrackingID, documentation='The TD berth where the incorrectly reported train has been identified to be. Note that this berth is that which was reported to Darwin and there is no guarantee that the train is still in this berth at any subsequent point in time.', location=pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTTDData_v1.xsd', 28, 3)))

TrackingID._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'incorrectTrainID'), _ImportedBinding_darwinpush_xb_ct.TrainIdType, scope=TrackingID, documentation='The incorrect Train ID (headcode) that is being reported by TD.NET.', location=pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTTDData_v1.xsd', 33, 3)))

TrackingID._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'correctTrainID'), _ImportedBinding_darwinpush_xb_ct.TrainIdType, scope=TrackingID, documentation='The correct Train ID (headcode) that should be reported by TD.NET.', location=pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTTDData_v1.xsd', 38, 3)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TrackingID._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'berth')), pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTTDData_v1.xsd', 28, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TrackingID._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'incorrectTrainID')), pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTTDData_v1.xsd', 33, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TrackingID._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'correctTrainID')), pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTTDData_v1.xsd', 38, 3))
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
TrackingID._Automaton = _BuildAutomaton()

