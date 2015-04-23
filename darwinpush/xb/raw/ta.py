# ./darwinpush/xb/raw/ta.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:697e0ad31a5bd138fa72077ce2e9fb240afaf510
# Generated 2015-04-23 16:42:14.514455 by PyXB version 1.2.4 using Python 3.4.1.final.0
# Namespace http://www.thalesgroup.com/rtti/PushPort/TrainAlerts/v1 [xmlns:ta]

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
Namespace = pyxb.namespace.NamespaceForURI('http://www.thalesgroup.com/rtti/PushPort/TrainAlerts/v1', create_if_missing=True)
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


# Atomic simple type: {http://www.thalesgroup.com/rtti/PushPort/TrainAlerts/v1}AlertAudienceType
class AlertAudienceType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Alert Audience Data Type"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AlertAudienceType')
    _XSDLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTTrainAlerts_v1.xsd', 15, 1)
    _Documentation = 'Alert Audience Data Type'
AlertAudienceType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=AlertAudienceType, enum_prefix=None)
AlertAudienceType.Customer = AlertAudienceType._CF_enumeration.addEnumeration(unicode_value='Customer', tag='Customer')
AlertAudienceType.Staff = AlertAudienceType._CF_enumeration.addEnumeration(unicode_value='Staff', tag='Staff')
AlertAudienceType.Operations = AlertAudienceType._CF_enumeration.addEnumeration(unicode_value='Operations', tag='Operations')
AlertAudienceType._InitializeFacetMap(AlertAudienceType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'AlertAudienceType', AlertAudienceType)

# Atomic simple type: {http://www.thalesgroup.com/rtti/PushPort/TrainAlerts/v1}AlertType
class AlertType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Alert Type Data Type"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AlertType')
    _XSDLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTTrainAlerts_v1.xsd', 25, 1)
    _Documentation = 'Alert Type Data Type'
AlertType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=AlertType, enum_prefix=None)
AlertType.Normal = AlertType._CF_enumeration.addEnumeration(unicode_value='Normal', tag='Normal')
AlertType.Forced = AlertType._CF_enumeration.addEnumeration(unicode_value='Forced', tag='Forced')
AlertType._InitializeFacetMap(AlertType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'AlertType', AlertType)

# Complex type {http://www.thalesgroup.com/rtti/PushPort/TrainAlerts/v1}TrainAlert with content type ELEMENT_ONLY
class TrainAlert (pyxb.binding.basis.complexTypeDefinition):
    """Train Alert"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TrainAlert')
    _XSDLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTTrainAlerts_v1.xsd', 35, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.thalesgroup.com/rtti/PushPort/TrainAlerts/v1}AlertID uses Python identifier AlertID
    __AlertID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AlertID'), 'AlertID', '__httpwww_thalesgroup_comrttiPushPortTrainAlertsv1_TrainAlert_httpwww_thalesgroup_comrttiPushPortTrainAlertsv1AlertID', False, pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTTrainAlerts_v1.xsd', 40, 3), )

    
    AlertID = property(__AlertID.value, __AlertID.set, None, 'TODO')

    
    # Element {http://www.thalesgroup.com/rtti/PushPort/TrainAlerts/v1}AlertServices uses Python identifier AlertServices
    __AlertServices = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AlertServices'), 'AlertServices', '__httpwww_thalesgroup_comrttiPushPortTrainAlertsv1_TrainAlert_httpwww_thalesgroup_comrttiPushPortTrainAlertsv1AlertServices', False, pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTTrainAlerts_v1.xsd', 45, 3), )

    
    AlertServices = property(__AlertServices.value, __AlertServices.set, None, 'TODO')

    
    # Element {http://www.thalesgroup.com/rtti/PushPort/TrainAlerts/v1}SendAlertBySMS uses Python identifier SendAlertBySMS
    __SendAlertBySMS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SendAlertBySMS'), 'SendAlertBySMS', '__httpwww_thalesgroup_comrttiPushPortTrainAlertsv1_TrainAlert_httpwww_thalesgroup_comrttiPushPortTrainAlertsv1SendAlertBySMS', False, pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTTrainAlerts_v1.xsd', 50, 3), )

    
    SendAlertBySMS = property(__SendAlertBySMS.value, __SendAlertBySMS.set, None, 'TODO')

    
    # Element {http://www.thalesgroup.com/rtti/PushPort/TrainAlerts/v1}SendAlertByEmail uses Python identifier SendAlertByEmail
    __SendAlertByEmail = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SendAlertByEmail'), 'SendAlertByEmail', '__httpwww_thalesgroup_comrttiPushPortTrainAlertsv1_TrainAlert_httpwww_thalesgroup_comrttiPushPortTrainAlertsv1SendAlertByEmail', False, pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTTrainAlerts_v1.xsd', 55, 3), )

    
    SendAlertByEmail = property(__SendAlertByEmail.value, __SendAlertByEmail.set, None, 'TODO')

    
    # Element {http://www.thalesgroup.com/rtti/PushPort/TrainAlerts/v1}SendAlertByTwitter uses Python identifier SendAlertByTwitter
    __SendAlertByTwitter = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SendAlertByTwitter'), 'SendAlertByTwitter', '__httpwww_thalesgroup_comrttiPushPortTrainAlertsv1_TrainAlert_httpwww_thalesgroup_comrttiPushPortTrainAlertsv1SendAlertByTwitter', False, pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTTrainAlerts_v1.xsd', 60, 3), )

    
    SendAlertByTwitter = property(__SendAlertByTwitter.value, __SendAlertByTwitter.set, None, 'TODO')

    
    # Element {http://www.thalesgroup.com/rtti/PushPort/TrainAlerts/v1}Source uses Python identifier Source
    __Source = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Source'), 'Source', '__httpwww_thalesgroup_comrttiPushPortTrainAlertsv1_TrainAlert_httpwww_thalesgroup_comrttiPushPortTrainAlertsv1Source', False, pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTTrainAlerts_v1.xsd', 65, 3), )

    
    Source = property(__Source.value, __Source.set, None, 'TODO')

    
    # Element {http://www.thalesgroup.com/rtti/PushPort/TrainAlerts/v1}AlertText uses Python identifier AlertText
    __AlertText = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AlertText'), 'AlertText', '__httpwww_thalesgroup_comrttiPushPortTrainAlertsv1_TrainAlert_httpwww_thalesgroup_comrttiPushPortTrainAlertsv1AlertText', False, pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTTrainAlerts_v1.xsd', 70, 3), )

    
    AlertText = property(__AlertText.value, __AlertText.set, None, 'TODO')

    
    # Element {http://www.thalesgroup.com/rtti/PushPort/TrainAlerts/v1}Audience uses Python identifier Audience
    __Audience = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Audience'), 'Audience', '__httpwww_thalesgroup_comrttiPushPortTrainAlertsv1_TrainAlert_httpwww_thalesgroup_comrttiPushPortTrainAlertsv1Audience', False, pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTTrainAlerts_v1.xsd', 75, 3), )

    
    Audience = property(__Audience.value, __Audience.set, None, 'TODO')

    
    # Element {http://www.thalesgroup.com/rtti/PushPort/TrainAlerts/v1}AlertType uses Python identifier AlertType
    __AlertType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AlertType'), 'AlertType', '__httpwww_thalesgroup_comrttiPushPortTrainAlertsv1_TrainAlert_httpwww_thalesgroup_comrttiPushPortTrainAlertsv1AlertType', False, pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTTrainAlerts_v1.xsd', 80, 3), )

    
    AlertType = property(__AlertType.value, __AlertType.set, None, 'TODO')

    
    # Element {http://www.thalesgroup.com/rtti/PushPort/TrainAlerts/v1}CopiedFromAlertID uses Python identifier CopiedFromAlertID
    __CopiedFromAlertID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CopiedFromAlertID'), 'CopiedFromAlertID', '__httpwww_thalesgroup_comrttiPushPortTrainAlertsv1_TrainAlert_httpwww_thalesgroup_comrttiPushPortTrainAlertsv1CopiedFromAlertID', False, pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTTrainAlerts_v1.xsd', 85, 3), )

    
    CopiedFromAlertID = property(__CopiedFromAlertID.value, __CopiedFromAlertID.set, None, 'TODO')

    
    # Element {http://www.thalesgroup.com/rtti/PushPort/TrainAlerts/v1}CopiedFromSource uses Python identifier CopiedFromSource
    __CopiedFromSource = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CopiedFromSource'), 'CopiedFromSource', '__httpwww_thalesgroup_comrttiPushPortTrainAlertsv1_TrainAlert_httpwww_thalesgroup_comrttiPushPortTrainAlertsv1CopiedFromSource', False, pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTTrainAlerts_v1.xsd', 90, 3), )

    
    CopiedFromSource = property(__CopiedFromSource.value, __CopiedFromSource.set, None, 'TODO')

    _ElementMap.update({
        __AlertID.name() : __AlertID,
        __AlertServices.name() : __AlertServices,
        __SendAlertBySMS.name() : __SendAlertBySMS,
        __SendAlertByEmail.name() : __SendAlertByEmail,
        __SendAlertByTwitter.name() : __SendAlertByTwitter,
        __Source.name() : __Source,
        __AlertText.name() : __AlertText,
        __Audience.name() : __Audience,
        __AlertType.name() : __AlertType,
        __CopiedFromAlertID.name() : __CopiedFromAlertID,
        __CopiedFromSource.name() : __CopiedFromSource
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'TrainAlert', TrainAlert)


# Complex type {http://www.thalesgroup.com/rtti/PushPort/TrainAlerts/v1}AlertServices with content type ELEMENT_ONLY
class AlertServices (pyxb.binding.basis.complexTypeDefinition):
    """A list of services to which the alert applies"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AlertServices')
    _XSDLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTTrainAlerts_v1.xsd', 124, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.thalesgroup.com/rtti/PushPort/TrainAlerts/v1}AlertService uses Python identifier AlertService
    __AlertService = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AlertService'), 'AlertService', '__httpwww_thalesgroup_comrttiPushPortTrainAlertsv1_AlertServices_httpwww_thalesgroup_comrttiPushPortTrainAlertsv1AlertService', True, pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTTrainAlerts_v1.xsd', 129, 3), )

    
    AlertService = property(__AlertService.value, __AlertService.set, None, 'TODO')

    _ElementMap.update({
        __AlertService.name() : __AlertService
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'AlertServices', AlertServices)


# Complex type {http://www.thalesgroup.com/rtti/PushPort/TrainAlerts/v1}AlertService with content type ELEMENT_ONLY
class AlertService (pyxb.binding.basis.complexTypeDefinition):
    """TODO"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AlertService')
    _XSDLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTTrainAlerts_v1.xsd', 97, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.thalesgroup.com/rtti/PushPort/TrainAlerts/v1}Location uses Python identifier Location
    __Location = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Location'), 'Location', '__httpwww_thalesgroup_comrttiPushPortTrainAlertsv1_AlertService_httpwww_thalesgroup_comrttiPushPortTrainAlertsv1Location', True, pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTTrainAlerts_v1.xsd', 102, 3), )

    
    Location = property(__Location.value, __Location.set, None, 'TODO')

    
    # Attribute RID uses Python identifier RID
    __RID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'RID'), 'RID', '__httpwww_thalesgroup_comrttiPushPortTrainAlertsv1_AlertService_RID', _ImportedBinding_darwinpush_xb_ct.RIDType)
    __RID._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTTrainAlerts_v1.xsd', 108, 2)
    __RID._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTTrainAlerts_v1.xsd', 108, 2)
    
    RID = property(__RID.value, __RID.set, None, 'TODO')

    
    # Attribute UID uses Python identifier UID
    __UID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'UID'), 'UID', '__httpwww_thalesgroup_comrttiPushPortTrainAlertsv1_AlertService_UID', _ImportedBinding_darwinpush_xb_ct.UIDType)
    __UID._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTTrainAlerts_v1.xsd', 113, 2)
    __UID._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTTrainAlerts_v1.xsd', 113, 2)
    
    UID = property(__UID.value, __UID.set, None, 'TODO')

    
    # Attribute SSD uses Python identifier SSD
    __SSD = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'SSD'), 'SSD', '__httpwww_thalesgroup_comrttiPushPortTrainAlertsv1_AlertService_SSD', pyxb.binding.datatypes.date)
    __SSD._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTTrainAlerts_v1.xsd', 118, 2)
    __SSD._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTTrainAlerts_v1.xsd', 118, 2)
    
    SSD = property(__SSD.value, __SSD.set, None, 'TODO')

    _ElementMap.update({
        __Location.name() : __Location
    })
    _AttributeMap.update({
        __RID.name() : __RID,
        __UID.name() : __UID,
        __SSD.name() : __SSD
    })
Namespace.addCategoryObject('typeBinding', 'AlertService', AlertService)




TrainAlert._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AlertID'), pyxb.binding.datatypes.string, scope=TrainAlert, documentation='TODO', location=pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTTrainAlerts_v1.xsd', 40, 3)))

TrainAlert._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AlertServices'), AlertServices, scope=TrainAlert, documentation='TODO', location=pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTTrainAlerts_v1.xsd', 45, 3)))

TrainAlert._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SendAlertBySMS'), pyxb.binding.datatypes.boolean, scope=TrainAlert, documentation='TODO', location=pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTTrainAlerts_v1.xsd', 50, 3)))

TrainAlert._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SendAlertByEmail'), pyxb.binding.datatypes.boolean, scope=TrainAlert, documentation='TODO', location=pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTTrainAlerts_v1.xsd', 55, 3)))

TrainAlert._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SendAlertByTwitter'), pyxb.binding.datatypes.boolean, scope=TrainAlert, documentation='TODO', location=pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTTrainAlerts_v1.xsd', 60, 3)))

TrainAlert._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Source'), pyxb.binding.datatypes.string, scope=TrainAlert, documentation='TODO', location=pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTTrainAlerts_v1.xsd', 65, 3)))

TrainAlert._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AlertText'), pyxb.binding.datatypes.string, scope=TrainAlert, documentation='TODO', location=pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTTrainAlerts_v1.xsd', 70, 3)))

TrainAlert._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Audience'), AlertAudienceType, scope=TrainAlert, documentation='TODO', location=pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTTrainAlerts_v1.xsd', 75, 3)))

TrainAlert._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AlertType'), AlertType, scope=TrainAlert, documentation='TODO', location=pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTTrainAlerts_v1.xsd', 80, 3)))

TrainAlert._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CopiedFromAlertID'), pyxb.binding.datatypes.string, scope=TrainAlert, documentation='TODO', location=pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTTrainAlerts_v1.xsd', 85, 3)))

TrainAlert._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CopiedFromSource'), pyxb.binding.datatypes.string, scope=TrainAlert, documentation='TODO', location=pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTTrainAlerts_v1.xsd', 90, 3)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTTrainAlerts_v1.xsd', 85, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTTrainAlerts_v1.xsd', 90, 3))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TrainAlert._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AlertID')), pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTTrainAlerts_v1.xsd', 40, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TrainAlert._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AlertServices')), pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTTrainAlerts_v1.xsd', 45, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TrainAlert._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SendAlertBySMS')), pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTTrainAlerts_v1.xsd', 50, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TrainAlert._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SendAlertByEmail')), pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTTrainAlerts_v1.xsd', 55, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TrainAlert._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SendAlertByTwitter')), pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTTrainAlerts_v1.xsd', 60, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TrainAlert._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Source')), pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTTrainAlerts_v1.xsd', 65, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TrainAlert._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AlertText')), pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTTrainAlerts_v1.xsd', 70, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TrainAlert._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Audience')), pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTTrainAlerts_v1.xsd', 75, 3))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TrainAlert._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AlertType')), pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTTrainAlerts_v1.xsd', 80, 3))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TrainAlert._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CopiedFromAlertID')), pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTTrainAlerts_v1.xsd', 85, 3))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(TrainAlert._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CopiedFromSource')), pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTTrainAlerts_v1.xsd', 90, 3))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
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
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_10._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TrainAlert._Automaton = _BuildAutomaton()




AlertServices._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AlertService'), AlertService, scope=AlertServices, documentation='TODO', location=pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTTrainAlerts_v1.xsd', 129, 3)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTTrainAlerts_v1.xsd', 129, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AlertServices._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AlertService')), pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTTrainAlerts_v1.xsd', 129, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
AlertServices._Automaton = _BuildAutomaton_()




AlertService._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Location'), pyxb.binding.datatypes.string, scope=AlertService, documentation='TODO', location=pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTTrainAlerts_v1.xsd', 102, 3)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(AlertService._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Location')), pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTTrainAlerts_v1.xsd', 102, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
AlertService._Automaton = _BuildAutomaton_2()

