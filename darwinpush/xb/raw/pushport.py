# ./darwinpush/xb/raw/pushport.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:3c67301ef928782a8ba5508df5541ca85f7b0634
# Generated 2015-04-23 16:42:14.519011 by PyXB version 1.2.4 using Python 3.4.1.final.0
# Namespace http://www.thalesgroup.com/rtti/PushPort/v12

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
import darwinpush.xb.ta as _ImportedBinding_darwinpush_xb_ta
import darwinpush.xb.fc as _ImportedBinding_darwinpush_xb_for
import darwinpush.xb.alm as _ImportedBinding_darwinpush_xb_alm
import darwinpush.xb.status as _ImportedBinding_darwinpush_xb_status
import darwinpush.xb.ct as _ImportedBinding_darwinpush_xb_ct
import darwinpush.xb.sm as _ImportedBinding_darwinpush_xb_sm
import darwinpush.xb.td as _ImportedBinding_darwinpush_xb_td
import darwinpush.xb.sch as _ImportedBinding_darwinpush_xb_sch
import darwinpush.xb.tor as _ImportedBinding_darwinpush_xb_tor

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://www.thalesgroup.com/rtti/PushPort/v12', create_if_missing=True)
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


# Complex type {http://www.thalesgroup.com/rtti/PushPort/v12}DataResponse with content type ELEMENT_ONLY
class DataResponse (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.thalesgroup.com/rtti/PushPort/v12}DataResponse with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DataResponse')
    _XSDLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchema_v12.xsd', 28, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.thalesgroup.com/rtti/PushPort/v12}schedule uses Python identifier schedule
    __schedule = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'schedule'), 'schedule', '__httpwww_thalesgroup_comrttiPushPortv12_DataResponse_httpwww_thalesgroup_comrttiPushPortv12schedule', True, pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchema_v12.xsd', 30, 3), )

    
    schedule = property(__schedule.value, __schedule.set, None, 'Train Schedule')

    
    # Element {http://www.thalesgroup.com/rtti/PushPort/v12}deactivated uses Python identifier deactivated
    __deactivated = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'deactivated'), 'deactivated', '__httpwww_thalesgroup_comrttiPushPortv12_DataResponse_httpwww_thalesgroup_comrttiPushPortv12deactivated', True, pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchema_v12.xsd', 35, 3), )

    
    deactivated = property(__deactivated.value, __deactivated.set, None, 'Notification that a Train Schedule is now deactivated in Darwin.')

    
    # Element {http://www.thalesgroup.com/rtti/PushPort/v12}association uses Python identifier association
    __association = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'association'), 'association', '__httpwww_thalesgroup_comrttiPushPortv12_DataResponse_httpwww_thalesgroup_comrttiPushPortv12association', True, pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchema_v12.xsd', 40, 3), )

    
    association = property(__association.value, __association.set, None, 'Association between schedules')

    
    # Element {http://www.thalesgroup.com/rtti/PushPort/v12}TS uses Python identifier TS
    __TS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TS'), 'TS', '__httpwww_thalesgroup_comrttiPushPortv12_DataResponse_httpwww_thalesgroup_comrttiPushPortv12TS', True, pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchema_v12.xsd', 45, 3), )

    
    TS = property(__TS.value, __TS.set, None, 'Train Status')

    
    # Element {http://www.thalesgroup.com/rtti/PushPort/v12}OW uses Python identifier OW
    __OW = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'OW'), 'OW', '__httpwww_thalesgroup_comrttiPushPortv12_DataResponse_httpwww_thalesgroup_comrttiPushPortv12OW', True, pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchema_v12.xsd', 50, 3), )

    
    OW = property(__OW.value, __OW.set, None, 'Darwin Workstation Station Message')

    
    # Element {http://www.thalesgroup.com/rtti/PushPort/v12}trainAlert uses Python identifier trainAlert
    __trainAlert = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'trainAlert'), 'trainAlert', '__httpwww_thalesgroup_comrttiPushPortv12_DataResponse_httpwww_thalesgroup_comrttiPushPortv12trainAlert', True, pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchema_v12.xsd', 55, 3), )

    
    trainAlert = property(__trainAlert.value, __trainAlert.set, None, 'Train Alert')

    
    # Element {http://www.thalesgroup.com/rtti/PushPort/v12}trainOrder uses Python identifier trainOrder
    __trainOrder = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'trainOrder'), 'trainOrder', '__httpwww_thalesgroup_comrttiPushPortv12_DataResponse_httpwww_thalesgroup_comrttiPushPortv12trainOrder', True, pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchema_v12.xsd', 60, 3), )

    
    trainOrder = property(__trainOrder.value, __trainOrder.set, None, 'The order that trains are expected to call/pass a particular station platform')

    
    # Element {http://www.thalesgroup.com/rtti/PushPort/v12}trackingID uses Python identifier trackingID
    __trackingID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'trackingID'), 'trackingID', '__httpwww_thalesgroup_comrttiPushPortv12_DataResponse_httpwww_thalesgroup_comrttiPushPortv12trackingID', True, pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchema_v12.xsd', 65, 3), )

    
    trackingID = property(__trackingID.value, __trackingID.set, None, 'Indicate a corrected Tracking ID (headcode) for a service in a TD berth.')

    
    # Element {http://www.thalesgroup.com/rtti/PushPort/v12}alarm uses Python identifier alarm
    __alarm = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'alarm'), 'alarm', '__httpwww_thalesgroup_comrttiPushPortv12_DataResponse_httpwww_thalesgroup_comrttiPushPortv12alarm', True, pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchema_v12.xsd', 70, 3), )

    
    alarm = property(__alarm.value, __alarm.set, None, 'A Darwin alarm')

    _ElementMap.update({
        __schedule.name() : __schedule,
        __deactivated.name() : __deactivated,
        __association.name() : __association,
        __TS.name() : __TS,
        __OW.name() : __OW,
        __trainAlert.name() : __trainAlert,
        __trainOrder.name() : __trainOrder,
        __trackingID.name() : __trackingID,
        __alarm.name() : __alarm
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'DataResponse', DataResponse)


# Complex type [anonymous] with content type EMPTY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Request a standard snapshot of current database"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchema_v12.xsd', 106, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute viaftp uses Python identifier viaftp
    __viaftp = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'viaftp'), 'viaftp', '__httpwww_thalesgroup_comrttiPushPortv12_CTD_ANON_viaftp', pyxb.binding.datatypes.boolean, unicode_default='false')
    __viaftp._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchema_v12.xsd', 107, 6)
    __viaftp._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchema_v12.xsd', 107, 6)
    
    viaftp = property(__viaftp.value, __viaftp.set, None, 'If true, then resulting snapshot data is fetched by the client via FTP')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __viaftp.name() : __viaftp
    })



# Complex type [anonymous] with content type EMPTY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """Request a full snapshot of current database"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchema_v12.xsd', 118, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute viaftp uses Python identifier viaftp
    __viaftp = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'viaftp'), 'viaftp', '__httpwww_thalesgroup_comrttiPushPortv12_CTD_ANON__viaftp', pyxb.binding.datatypes.boolean, unicode_default='false')
    __viaftp._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchema_v12.xsd', 119, 6)
    __viaftp._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchema_v12.xsd', 119, 6)
    
    viaftp = property(__viaftp.value, __viaftp.set, None, 'If true, then resulting snapshot data is fetched by the client via FTP')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __viaftp.name() : __viaftp
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    """Push Ports Schema"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchema_v12.xsd', 82, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.thalesgroup.com/rtti/PushPort/v12}QueryTimetable uses Python identifier QueryTimetable
    __QueryTimetable = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'QueryTimetable'), 'QueryTimetable', '__httpwww_thalesgroup_comrttiPushPortv12_CTD_ANON_2_httpwww_thalesgroup_comrttiPushPortv12QueryTimetable', False, pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchema_v12.xsd', 84, 4), )

    
    QueryTimetable = property(__QueryTimetable.value, __QueryTimetable.set, None, 'Query for the current timetable ID')

    
    # Element {http://www.thalesgroup.com/rtti/PushPort/v12}TimeTableId uses Python identifier TimeTableId
    __TimeTableId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TimeTableId'), 'TimeTableId', '__httpwww_thalesgroup_comrttiPushPortv12_CTD_ANON_2_httpwww_thalesgroup_comrttiPushPortv12TimeTableId', False, pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchema_v12.xsd', 89, 4), )

    
    TimeTableId = property(__TimeTableId.value, __TimeTableId.set, None, 'Response for the current timetable ID')

    
    # Element {http://www.thalesgroup.com/rtti/PushPort/v12}GetSnapshotReq uses Python identifier GetSnapshotReq
    __GetSnapshotReq = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'GetSnapshotReq'), 'GetSnapshotReq', '__httpwww_thalesgroup_comrttiPushPortv12_CTD_ANON_2_httpwww_thalesgroup_comrttiPushPortv12GetSnapshotReq', False, pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchema_v12.xsd', 102, 4), )

    
    GetSnapshotReq = property(__GetSnapshotReq.value, __GetSnapshotReq.set, None, 'Request a standard snapshot of current database')

    
    # Element {http://www.thalesgroup.com/rtti/PushPort/v12}GetFullSnapshotReq uses Python identifier GetFullSnapshotReq
    __GetFullSnapshotReq = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'GetFullSnapshotReq'), 'GetFullSnapshotReq', '__httpwww_thalesgroup_comrttiPushPortv12_CTD_ANON_2_httpwww_thalesgroup_comrttiPushPortv12GetFullSnapshotReq', False, pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchema_v12.xsd', 114, 4), )

    
    GetFullSnapshotReq = property(__GetFullSnapshotReq.value, __GetFullSnapshotReq.set, None, 'Request a full snapshot of current database')

    
    # Element {http://www.thalesgroup.com/rtti/PushPort/v12}SnapshotId uses Python identifier SnapshotId
    __SnapshotId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SnapshotId'), 'SnapshotId', '__httpwww_thalesgroup_comrttiPushPortv12_CTD_ANON_2_httpwww_thalesgroup_comrttiPushPortv12SnapshotId', False, pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchema_v12.xsd', 126, 4), )

    
    SnapshotId = property(__SnapshotId.value, __SnapshotId.set, None, 'Defines an ID for recovering snapshot data via FTP')

    
    # Element {http://www.thalesgroup.com/rtti/PushPort/v12}StartUpdateReq uses Python identifier StartUpdateReq
    __StartUpdateReq = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'StartUpdateReq'), 'StartUpdateReq', '__httpwww_thalesgroup_comrttiPushPortv12_CTD_ANON_2_httpwww_thalesgroup_comrttiPushPortv12StartUpdateReq', False, pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchema_v12.xsd', 131, 4), )

    
    StartUpdateReq = property(__StartUpdateReq.value, __StartUpdateReq.set, None, 'Start sending available updates.')

    
    # Element {http://www.thalesgroup.com/rtti/PushPort/v12}StopUpdateReq uses Python identifier StopUpdateReq
    __StopUpdateReq = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'StopUpdateReq'), 'StopUpdateReq', '__httpwww_thalesgroup_comrttiPushPortv12_CTD_ANON_2_httpwww_thalesgroup_comrttiPushPortv12StopUpdateReq', False, pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchema_v12.xsd', 136, 4), )

    
    StopUpdateReq = property(__StopUpdateReq.value, __StopUpdateReq.set, None, 'Stop sending available updates.')

    
    # Element {http://www.thalesgroup.com/rtti/PushPort/v12}FailureResp uses Python identifier FailureResp
    __FailureResp = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'FailureResp'), 'FailureResp', '__httpwww_thalesgroup_comrttiPushPortv12_CTD_ANON_2_httpwww_thalesgroup_comrttiPushPortv12FailureResp', False, pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchema_v12.xsd', 141, 4), )

    
    FailureResp = property(__FailureResp.value, __FailureResp.set, None, 'Failure Response')

    
    # Element {http://www.thalesgroup.com/rtti/PushPort/v12}uR uses Python identifier uR
    __uR = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'uR'), 'uR', '__httpwww_thalesgroup_comrttiPushPortv12_CTD_ANON_2_httpwww_thalesgroup_comrttiPushPortv12uR', False, pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchema_v12.xsd', 162, 4), )

    
    uR = property(__uR.value, __uR.set, None, 'Update Response')

    
    # Element {http://www.thalesgroup.com/rtti/PushPort/v12}sR uses Python identifier sR
    __sR = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'sR'), 'sR', '__httpwww_thalesgroup_comrttiPushPortv12_CTD_ANON_2_httpwww_thalesgroup_comrttiPushPortv12sR', False, pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchema_v12.xsd', 188, 4), )

    
    sR = property(__sR.value, __sR.set, None, 'Snapshot Response')

    
    # Attribute ts uses Python identifier ts
    __ts = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ts'), 'ts', '__httpwww_thalesgroup_comrttiPushPortv12_CTD_ANON_2_ts', _ImportedBinding_darwinpush_xb_ct.RTTIDateTimeType, required=True)
    __ts._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchema_v12.xsd', 194, 3)
    __ts._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchema_v12.xsd', 194, 3)
    
    ts = property(__ts.value, __ts.set, None, 'Local Timestamp')

    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'version'), 'version', '__httpwww_thalesgroup_comrttiPushPortv12_CTD_ANON_2_version', pyxb.binding.datatypes.string, required=True)
    __version._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchema_v12.xsd', 199, 3)
    __version._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchema_v12.xsd', 199, 3)
    
    version = property(__version.value, __version.set, None, None)

    _ElementMap.update({
        __QueryTimetable.name() : __QueryTimetable,
        __TimeTableId.name() : __TimeTableId,
        __GetSnapshotReq.name() : __GetSnapshotReq,
        __GetFullSnapshotReq.name() : __GetFullSnapshotReq,
        __SnapshotId.name() : __SnapshotId,
        __StartUpdateReq.name() : __StartUpdateReq,
        __StopUpdateReq.name() : __StopUpdateReq,
        __FailureResp.name() : __FailureResp,
        __uR.name() : __uR,
        __sR.name() : __sR
    })
    _AttributeMap.update({
        __ts.name() : __ts,
        __version.name() : __version
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_3 (pyxb.binding.basis.complexTypeDefinition):
    """Response for the current timetable ID"""
    _TypeDefinition = _ImportedBinding_darwinpush_xb_ct.TimetableIDType
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchema_v12.xsd', 93, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is _ImportedBinding_darwinpush_xb_ct.TimetableIDType
    
    # Attribute ttfile uses Python identifier ttfile
    __ttfile = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ttfile'), 'ttfile', '__httpwww_thalesgroup_comrttiPushPortv12_CTD_ANON_3_ttfile', _ImportedBinding_darwinpush_xb_ct.TimetableFilenameType, required=True)
    __ttfile._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchema_v12.xsd', 96, 8)
    __ttfile._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchema_v12.xsd', 96, 8)
    
    ttfile = property(__ttfile.value, __ttfile.set, None, None)

    
    # Attribute ttreffile uses Python identifier ttreffile
    __ttreffile = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ttreffile'), 'ttreffile', '__httpwww_thalesgroup_comrttiPushPortv12_CTD_ANON_3_ttreffile', _ImportedBinding_darwinpush_xb_ct.TimetableFilenameType, required=True)
    __ttreffile._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchema_v12.xsd', 97, 8)
    __ttreffile._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchema_v12.xsd', 97, 8)
    
    ttreffile = property(__ttreffile.value, __ttreffile.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __ttfile.name() : __ttfile,
        __ttreffile.name() : __ttreffile
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_4 (DataResponse):
    """Update Response"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchema_v12.xsd', 166, 5)
    _ElementMap = DataResponse._ElementMap.copy()
    _AttributeMap = DataResponse._AttributeMap.copy()
    # Base type is DataResponse
    
    # Element schedule ({http://www.thalesgroup.com/rtti/PushPort/v12}schedule) inherited from {http://www.thalesgroup.com/rtti/PushPort/v12}DataResponse
    
    # Element deactivated ({http://www.thalesgroup.com/rtti/PushPort/v12}deactivated) inherited from {http://www.thalesgroup.com/rtti/PushPort/v12}DataResponse
    
    # Element association ({http://www.thalesgroup.com/rtti/PushPort/v12}association) inherited from {http://www.thalesgroup.com/rtti/PushPort/v12}DataResponse
    
    # Element TS ({http://www.thalesgroup.com/rtti/PushPort/v12}TS) inherited from {http://www.thalesgroup.com/rtti/PushPort/v12}DataResponse
    
    # Element OW ({http://www.thalesgroup.com/rtti/PushPort/v12}OW) inherited from {http://www.thalesgroup.com/rtti/PushPort/v12}DataResponse
    
    # Element trainAlert ({http://www.thalesgroup.com/rtti/PushPort/v12}trainAlert) inherited from {http://www.thalesgroup.com/rtti/PushPort/v12}DataResponse
    
    # Element trainOrder ({http://www.thalesgroup.com/rtti/PushPort/v12}trainOrder) inherited from {http://www.thalesgroup.com/rtti/PushPort/v12}DataResponse
    
    # Element trackingID ({http://www.thalesgroup.com/rtti/PushPort/v12}trackingID) inherited from {http://www.thalesgroup.com/rtti/PushPort/v12}DataResponse
    
    # Element alarm ({http://www.thalesgroup.com/rtti/PushPort/v12}alarm) inherited from {http://www.thalesgroup.com/rtti/PushPort/v12}DataResponse
    
    # Attribute updateOrigin uses Python identifier updateOrigin
    __updateOrigin = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'updateOrigin'), 'updateOrigin', '__httpwww_thalesgroup_comrttiPushPortv12_CTD_ANON_4_updateOrigin', pyxb.binding.datatypes.string)
    __updateOrigin._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchema_v12.xsd', 169, 8)
    __updateOrigin._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchema_v12.xsd', 169, 8)
    
    updateOrigin = property(__updateOrigin.value, __updateOrigin.set, None, 'A string describing the type of system that originated this update, e.g. "CIS" or "Darwin".')

    
    # Attribute requestSource uses Python identifier requestSource
    __requestSource = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'requestSource'), 'requestSource', '__httpwww_thalesgroup_comrttiPushPortv12_CTD_ANON_4_requestSource', _ImportedBinding_darwinpush_xb_ct.SourceTypeInst)
    __requestSource._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchema_v12.xsd', 174, 8)
    __requestSource._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchema_v12.xsd', 174, 8)
    
    requestSource = property(__requestSource.value, __requestSource.set, None, 'The source instance that generated this update, usually a CIS instance.')

    
    # Attribute requestID uses Python identifier requestID
    __requestID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'requestID'), 'requestID', '__httpwww_thalesgroup_comrttiPushPortv12_CTD_ANON_4_requestID', _ImportedBinding_darwinpush_xb_ct.DCISRequestID)
    __requestID._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchema_v12.xsd', 179, 8)
    __requestID._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchema_v12.xsd', 179, 8)
    
    requestID = property(__requestID.value, __requestID.set, None, 'The DCISRequestID value provided by the originator of this update. Used in conjunction with the requestSource attribute to ensure uniqueness')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __updateOrigin.name() : __updateOrigin,
        __requestSource.name() : __requestSource,
        __requestID.name() : __requestID
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_5 (_ImportedBinding_darwinpush_xb_status.StatusType):
    """Failure Response"""
    _TypeDefinition = _ImportedBinding_darwinpush_xb_status.ErrorMsgType
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchema_v12.xsd', 145, 5)
    _ElementMap = _ImportedBinding_darwinpush_xb_status.StatusType._ElementMap.copy()
    _AttributeMap = _ImportedBinding_darwinpush_xb_status.StatusType._AttributeMap.copy()
    # Base type is _ImportedBinding_darwinpush_xb_status.StatusType
    
    # Attribute code inherited from {http://thalesgroup.com/RTTI/PushPortStatus/root_1}StatusType
    
    # Attribute requestSource uses Python identifier requestSource
    __requestSource = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'requestSource'), 'requestSource', '__httpwww_thalesgroup_comrttiPushPortv12_CTD_ANON_5_requestSource', _ImportedBinding_darwinpush_xb_ct.SourceTypeInst)
    __requestSource._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchema_v12.xsd', 148, 8)
    __requestSource._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchema_v12.xsd', 148, 8)
    
    requestSource = property(__requestSource.value, __requestSource.set, None, 'The DCIS source that generated this update')

    
    # Attribute requestID uses Python identifier requestID
    __requestID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'requestID'), 'requestID', '__httpwww_thalesgroup_comrttiPushPortv12_CTD_ANON_5_requestID', _ImportedBinding_darwinpush_xb_ct.DCISRequestID)
    __requestID._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchema_v12.xsd', 153, 8)
    __requestID._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchema_v12.xsd', 153, 8)
    
    requestID = property(__requestID.value, __requestID.set, None, 'The DCISRequestID value provided by the originator of this update. Used in conjunction with the updateSource attribute to ensure uniqueness')

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=pyxb.binding.content.Wildcard.NC_any)
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __requestSource.name() : __requestSource,
        __requestID.name() : __requestID
    })



Pport = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Pport'), CTD_ANON_2, documentation='Push Ports Schema', location=pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchema_v12.xsd', 78, 1))
Namespace.addCategoryObject('elementBinding', Pport.name().localName(), Pport)



DataResponse._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'schedule'), _ImportedBinding_darwinpush_xb_sch.Schedule, scope=DataResponse, documentation='Train Schedule', location=pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchema_v12.xsd', 30, 3)))

DataResponse._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'deactivated'), _ImportedBinding_darwinpush_xb_sch.DeactivatedSchedule, scope=DataResponse, documentation='Notification that a Train Schedule is now deactivated in Darwin.', location=pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchema_v12.xsd', 35, 3)))

DataResponse._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'association'), _ImportedBinding_darwinpush_xb_sch.Association, scope=DataResponse, documentation='Association between schedules', location=pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchema_v12.xsd', 40, 3)))

DataResponse._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TS'), _ImportedBinding_darwinpush_xb_for.TS, scope=DataResponse, documentation='Train Status', location=pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchema_v12.xsd', 45, 3)))

DataResponse._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OW'), _ImportedBinding_darwinpush_xb_sm.StationMessage, scope=DataResponse, documentation='Darwin Workstation Station Message', location=pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchema_v12.xsd', 50, 3)))

DataResponse._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'trainAlert'), _ImportedBinding_darwinpush_xb_ta.TrainAlert, scope=DataResponse, documentation='Train Alert', location=pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchema_v12.xsd', 55, 3)))

DataResponse._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'trainOrder'), _ImportedBinding_darwinpush_xb_tor.TrainOrder, scope=DataResponse, documentation='The order that trains are expected to call/pass a particular station platform', location=pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchema_v12.xsd', 60, 3)))

DataResponse._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'trackingID'), _ImportedBinding_darwinpush_xb_td.TrackingID, scope=DataResponse, documentation='Indicate a corrected Tracking ID (headcode) for a service in a TD berth.', location=pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchema_v12.xsd', 65, 3)))

DataResponse._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'alarm'), _ImportedBinding_darwinpush_xb_alm.RTTIAlarm, scope=DataResponse, documentation='A Darwin alarm', location=pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchema_v12.xsd', 70, 3)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchema_v12.xsd', 30, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchema_v12.xsd', 35, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchema_v12.xsd', 40, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchema_v12.xsd', 45, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchema_v12.xsd', 50, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchema_v12.xsd', 55, 3))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchema_v12.xsd', 60, 3))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchema_v12.xsd', 65, 3))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchema_v12.xsd', 70, 3))
    counters.add(cc_8)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(DataResponse._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'schedule')), pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchema_v12.xsd', 30, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(DataResponse._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'deactivated')), pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchema_v12.xsd', 35, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(DataResponse._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'association')), pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchema_v12.xsd', 40, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(DataResponse._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TS')), pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchema_v12.xsd', 45, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(DataResponse._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'OW')), pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchema_v12.xsd', 50, 3))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(DataResponse._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'trainAlert')), pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchema_v12.xsd', 55, 3))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(DataResponse._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'trainOrder')), pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchema_v12.xsd', 60, 3))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(DataResponse._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'trackingID')), pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchema_v12.xsd', 65, 3))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(DataResponse._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'alarm')), pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchema_v12.xsd', 70, 3))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
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
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
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
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
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
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
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
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True) ]))
    st_8._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
DataResponse._Automaton = _BuildAutomaton()




CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'QueryTimetable'), pyxb.binding.datatypes.anyType, scope=CTD_ANON_2, documentation='Query for the current timetable ID', location=pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchema_v12.xsd', 84, 4)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TimeTableId'), CTD_ANON_3, scope=CTD_ANON_2, documentation='Response for the current timetable ID', location=pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchema_v12.xsd', 89, 4)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'GetSnapshotReq'), CTD_ANON, scope=CTD_ANON_2, documentation='Request a standard snapshot of current database', location=pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchema_v12.xsd', 102, 4)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'GetFullSnapshotReq'), CTD_ANON_, scope=CTD_ANON_2, documentation='Request a full snapshot of current database', location=pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchema_v12.xsd', 114, 4)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SnapshotId'), _ImportedBinding_darwinpush_xb_ct.SnapshotIDType, scope=CTD_ANON_2, documentation='Defines an ID for recovering snapshot data via FTP', location=pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchema_v12.xsd', 126, 4)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'StartUpdateReq'), pyxb.binding.datatypes.anyType, scope=CTD_ANON_2, documentation='Start sending available updates.', location=pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchema_v12.xsd', 131, 4)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'StopUpdateReq'), pyxb.binding.datatypes.anyType, scope=CTD_ANON_2, documentation='Stop sending available updates.', location=pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchema_v12.xsd', 136, 4)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'FailureResp'), CTD_ANON_5, scope=CTD_ANON_2, documentation='Failure Response', location=pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchema_v12.xsd', 141, 4)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'uR'), CTD_ANON_4, scope=CTD_ANON_2, documentation='Update Response', location=pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchema_v12.xsd', 162, 4)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'sR'), DataResponse, scope=CTD_ANON_2, documentation='Snapshot Response', location=pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchema_v12.xsd', 188, 4)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'QueryTimetable')), pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchema_v12.xsd', 84, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TimeTableId')), pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchema_v12.xsd', 89, 4))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'GetSnapshotReq')), pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchema_v12.xsd', 102, 4))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'GetFullSnapshotReq')), pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchema_v12.xsd', 114, 4))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SnapshotId')), pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchema_v12.xsd', 126, 4))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'StartUpdateReq')), pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchema_v12.xsd', 131, 4))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'StopUpdateReq')), pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchema_v12.xsd', 136, 4))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'FailureResp')), pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchema_v12.xsd', 141, 4))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'uR')), pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchema_v12.xsd', 162, 4))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'sR')), pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchema_v12.xsd', 188, 4))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    transitions = []
    st_4._set_transitionSet(transitions)
    transitions = []
    st_5._set_transitionSet(transitions)
    transitions = []
    st_6._set_transitionSet(transitions)
    transitions = []
    st_7._set_transitionSet(transitions)
    transitions = []
    st_8._set_transitionSet(transitions)
    transitions = []
    st_9._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_2._Automaton = _BuildAutomaton_()




def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchema_v12.xsd', 30, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchema_v12.xsd', 35, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchema_v12.xsd', 40, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchema_v12.xsd', 45, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchema_v12.xsd', 50, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchema_v12.xsd', 55, 3))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchema_v12.xsd', 60, 3))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchema_v12.xsd', 65, 3))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchema_v12.xsd', 70, 3))
    counters.add(cc_8)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'schedule')), pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchema_v12.xsd', 30, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'deactivated')), pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchema_v12.xsd', 35, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'association')), pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchema_v12.xsd', 40, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TS')), pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchema_v12.xsd', 45, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'OW')), pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchema_v12.xsd', 50, 3))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'trainAlert')), pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchema_v12.xsd', 55, 3))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'trainOrder')), pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchema_v12.xsd', 60, 3))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'trackingID')), pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchema_v12.xsd', 65, 3))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'alarm')), pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchema_v12.xsd', 70, 3))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
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
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
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
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
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
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
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
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True) ]))
    st_8._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_4._Automaton = _BuildAutomaton_2()

