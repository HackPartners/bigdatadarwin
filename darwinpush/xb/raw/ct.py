# ./darwinpush/xb/raw/ct.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:af43703e8d819309b697945a843ebd1a8c55b1af
# Generated 2015-04-23 16:42:14.513469 by PyXB version 1.2.4 using Python 3.4.1.final.0
# Namespace http://www.thalesgroup.com/rtti/PushPort/CommonTypes/v1 [xmlns:ct]

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

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://www.thalesgroup.com/rtti/PushPort/CommonTypes/v1', create_if_missing=True)
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


# Atomic simple type: {http://www.thalesgroup.com/rtti/PushPort/CommonTypes/v1}RIDType
class RIDType (pyxb.binding.datatypes.string):

    """RTTI Train ID Type"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RIDType')
    _XSDLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTCommonTypes_v1.xsd', 13, 1)
    _Documentation = 'RTTI Train ID Type'
RIDType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(16))
RIDType._InitializeFacetMap(RIDType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'RIDType', RIDType)

# Atomic simple type: {http://www.thalesgroup.com/rtti/PushPort/CommonTypes/v1}UIDType
class UIDType (pyxb.binding.datatypes.string):

    """Train UID Type"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'UIDType')
    _XSDLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTCommonTypes_v1.xsd', 21, 1)
    _Documentation = 'Train UID Type'
UIDType._CF_length = pyxb.binding.facets.CF_length(value=pyxb.binding.datatypes.nonNegativeInteger(6))
UIDType._InitializeFacetMap(UIDType._CF_length)
Namespace.addCategoryObject('typeBinding', 'UIDType', UIDType)

# Atomic simple type: {http://www.thalesgroup.com/rtti/PushPort/CommonTypes/v1}TrainIdType
class TrainIdType (pyxb.binding.datatypes.string):

    """Train ID or Head Code Type"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TrainIdType')
    _XSDLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTCommonTypes_v1.xsd', 29, 1)
    _Documentation = 'Train ID or Head Code Type'
TrainIdType._CF_length = pyxb.binding.facets.CF_length(value=pyxb.binding.datatypes.nonNegativeInteger(4))
TrainIdType._CF_pattern = pyxb.binding.facets.CF_pattern()
TrainIdType._CF_pattern.addPattern(pattern='[0-9][A-Z][0-9][0-9]')
TrainIdType._InitializeFacetMap(TrainIdType._CF_length,
   TrainIdType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'TrainIdType', TrainIdType)

# Atomic simple type: {http://www.thalesgroup.com/rtti/PushPort/CommonTypes/v1}TOCType
class TOCType (pyxb.binding.datatypes.string):

    """ATOC Code Type"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TOCType')
    _XSDLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTCommonTypes_v1.xsd', 38, 1)
    _Documentation = 'ATOC Code Type'
TOCType._CF_length = pyxb.binding.facets.CF_length(value=pyxb.binding.datatypes.nonNegativeInteger(2))
TOCType._InitializeFacetMap(TOCType._CF_length)
Namespace.addCategoryObject('typeBinding', 'TOCType', TOCType)

# Atomic simple type: {http://www.thalesgroup.com/rtti/PushPort/CommonTypes/v1}TiplocType
class TiplocType (pyxb.binding.datatypes.string):

    """Tiploc Type (This is the short version of a TIPLOC - without spaces)"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TiplocType')
    _XSDLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTCommonTypes_v1.xsd', 46, 1)
    _Documentation = 'Tiploc Type (This is the short version of a TIPLOC - without spaces)'
TiplocType._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
TiplocType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(7))
TiplocType._InitializeFacetMap(TiplocType._CF_minLength,
   TiplocType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'TiplocType', TiplocType)

# Atomic simple type: {http://www.thalesgroup.com/rtti/PushPort/CommonTypes/v1}CrsType
class CrsType (pyxb.binding.datatypes.string):

    """CRS Code Type"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CrsType')
    _XSDLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTCommonTypes_v1.xsd', 55, 1)
    _Documentation = 'CRS Code Type'
CrsType._CF_length = pyxb.binding.facets.CF_length(value=pyxb.binding.datatypes.nonNegativeInteger(3))
CrsType._InitializeFacetMap(CrsType._CF_length)
Namespace.addCategoryObject('typeBinding', 'CrsType', CrsType)

# Atomic simple type: {http://www.thalesgroup.com/rtti/PushPort/CommonTypes/v1}SuffixType
class SuffixType (pyxb.binding.datatypes.string):

    """Denotes the suffix for a TIPLOC that identifies the instance on a circular route"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SuffixType')
    _XSDLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTCommonTypes_v1.xsd', 63, 1)
    _Documentation = 'Denotes the suffix for a TIPLOC that identifies the instance on a circular route'
SuffixType._CF_length = pyxb.binding.facets.CF_length(value=pyxb.binding.datatypes.nonNegativeInteger(1))
SuffixType._InitializeFacetMap(SuffixType._CF_length)
Namespace.addCategoryObject('typeBinding', 'SuffixType', SuffixType)

# Atomic simple type: {http://www.thalesgroup.com/rtti/PushPort/CommonTypes/v1}PlatformType
class PlatformType (pyxb.binding.datatypes.string):

    """Defines a platform number"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PlatformType')
    _XSDLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTCommonTypes_v1.xsd', 71, 1)
    _Documentation = 'Defines a platform number'
PlatformType._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
PlatformType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(3))
PlatformType._InitializeFacetMap(PlatformType._CF_minLength,
   PlatformType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'PlatformType', PlatformType)

# Atomic simple type: {http://www.thalesgroup.com/rtti/PushPort/CommonTypes/v1}TrainLengthType
class TrainLengthType (pyxb.binding.datatypes.unsignedShort):

    """Defines the length of a train"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TrainLengthType')
    _XSDLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTCommonTypes_v1.xsd', 80, 1)
    _Documentation = 'Defines the length of a train'
TrainLengthType._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value=pyxb.binding.datatypes.unsignedShort(99), value_datatype=TrainLengthType)
TrainLengthType._InitializeFacetMap(TrainLengthType._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'TrainLengthType', TrainLengthType)

# Atomic simple type: {http://www.thalesgroup.com/rtti/PushPort/CommonTypes/v1}ActivityType
class ActivityType (pyxb.binding.datatypes.string):

    """Activity Type (a set of 6 x 2 character strings).  Full details are provided in Common Interface File End User Specification."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ActivityType')
    _XSDLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTCommonTypes_v1.xsd', 88, 1)
    _Documentation = 'Activity Type (a set of 6 x 2 character strings).  Full details are provided in Common Interface File End User Specification.'
ActivityType._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(2))
ActivityType._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
ActivityType._CF_pattern = pyxb.binding.facets.CF_pattern()
ActivityType._CF_pattern.addPattern(pattern='([A-Z0-9\\- ][A-Z0-9\\- ]){1,6}')
ActivityType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(12))
ActivityType._InitializeFacetMap(ActivityType._CF_minLength,
   ActivityType._CF_whiteSpace,
   ActivityType._CF_pattern,
   ActivityType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'ActivityType', ActivityType)

# Atomic simple type: {http://www.thalesgroup.com/rtti/PushPort/CommonTypes/v1}CIFTrainStatusType
class CIFTrainStatusType (pyxb.binding.datatypes.string):

    """Defines the transport service type using CIF Train Status value"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CIFTrainStatusType')
    _XSDLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTCommonTypes_v1.xsd', 99, 1)
    _Documentation = 'Defines the transport service type using CIF Train Status value'
CIFTrainStatusType._CF_length = pyxb.binding.facets.CF_length(value=pyxb.binding.datatypes.nonNegativeInteger(1))
CIFTrainStatusType._CF_pattern = pyxb.binding.facets.CF_pattern()
CIFTrainStatusType._CF_pattern.addPattern(pattern='[BFPST12345]')
CIFTrainStatusType._InitializeFacetMap(CIFTrainStatusType._CF_length,
   CIFTrainStatusType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'CIFTrainStatusType', CIFTrainStatusType)

# Atomic simple type: {http://www.thalesgroup.com/rtti/PushPort/CommonTypes/v1}CIFTrainCategoryType
class CIFTrainCategoryType (pyxb.binding.datatypes.string):

    """Defines the train category"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CIFTrainCategoryType')
    _XSDLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTCommonTypes_v1.xsd', 108, 1)
    _Documentation = 'Defines the train category'
CIFTrainCategoryType._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(0))
CIFTrainCategoryType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(2))
CIFTrainCategoryType._InitializeFacetMap(CIFTrainCategoryType._CF_minLength,
   CIFTrainCategoryType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'CIFTrainCategoryType', CIFTrainCategoryType)

# Atomic simple type: {http://www.thalesgroup.com/rtti/PushPort/CommonTypes/v1}RTTITimeType
class RTTITimeType (pyxb.binding.datatypes.string):

    """Time as HH:MM"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RTTITimeType')
    _XSDLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTCommonTypes_v1.xsd', 117, 1)
    _Documentation = 'Time as HH:MM'
RTTITimeType._CF_pattern = pyxb.binding.facets.CF_pattern()
RTTITimeType._CF_pattern.addPattern(pattern='([0-1][0-9]|2[0-3]):[0-5][0-9]')
RTTITimeType._InitializeFacetMap(RTTITimeType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'RTTITimeType', RTTITimeType)

# Atomic simple type: {http://www.thalesgroup.com/rtti/PushPort/CommonTypes/v1}WTimeType
class WTimeType (pyxb.binding.datatypes.string):

    """Working scheduled time as HH:MM[:SS]"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'WTimeType')
    _XSDLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTCommonTypes_v1.xsd', 125, 1)
    _Documentation = 'Working scheduled time as HH:MM[:SS]'
WTimeType._CF_pattern = pyxb.binding.facets.CF_pattern()
WTimeType._CF_pattern.addPattern(pattern='([0-1][0-9]|2[0-3]):[0-5][0-9](:[0-5][0-9])?')
WTimeType._InitializeFacetMap(WTimeType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'WTimeType', WTimeType)

# Atomic simple type: {http://www.thalesgroup.com/rtti/PushPort/CommonTypes/v1}RTTIDateType
class RTTIDateType (pyxb.binding.datatypes.date):

    """RTTI Date Type (basic XML date)"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RTTIDateType')
    _XSDLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTCommonTypes_v1.xsd', 133, 1)
    _Documentation = 'RTTI Date Type (basic XML date)'
RTTIDateType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'RTTIDateType', RTTIDateType)

# Atomic simple type: {http://www.thalesgroup.com/rtti/PushPort/CommonTypes/v1}RTTIDateTimeType
class RTTIDateTimeType (pyxb.binding.datatypes.dateTime):

    """RTTI DateTime Type (basic XML date/time)"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RTTIDateTimeType')
    _XSDLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTCommonTypes_v1.xsd', 139, 1)
    _Documentation = 'RTTI DateTime Type (basic XML date/time)'
RTTIDateTimeType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'RTTIDateTimeType', RTTIDateTimeType)

# Atomic simple type: {http://www.thalesgroup.com/rtti/PushPort/CommonTypes/v1}TimetableIDType
class TimetableIDType (pyxb.binding.datatypes.string):

    """Unique Timetable identifier """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TimetableIDType')
    _XSDLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTCommonTypes_v1.xsd', 145, 1)
    _Documentation = 'Unique Timetable identifier '
TimetableIDType._CF_length = pyxb.binding.facets.CF_length(value=pyxb.binding.datatypes.nonNegativeInteger(14))
TimetableIDType._InitializeFacetMap(TimetableIDType._CF_length)
Namespace.addCategoryObject('typeBinding', 'TimetableIDType', TimetableIDType)

# Atomic simple type: {http://www.thalesgroup.com/rtti/PushPort/CommonTypes/v1}TimetableFilenameType
class TimetableFilenameType (pyxb.binding.datatypes.string):

    """The name of a timetable file that can be downloaded via FTP."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TimetableFilenameType')
    _XSDLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTCommonTypes_v1.xsd', 153, 1)
    _Documentation = 'The name of a timetable file that can be downloaded via FTP.'
TimetableFilenameType._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
TimetableFilenameType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(128))
TimetableFilenameType._InitializeFacetMap(TimetableFilenameType._CF_minLength,
   TimetableFilenameType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'TimetableFilenameType', TimetableFilenameType)

# Atomic simple type: {http://www.thalesgroup.com/rtti/PushPort/CommonTypes/v1}SnapshotIDType
class SnapshotIDType (pyxb.binding.datatypes.string):

    """Defines the ID for a snapshot file to be recovered via FTP"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SnapshotIDType')
    _XSDLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTCommonTypes_v1.xsd', 162, 1)
    _Documentation = 'Defines the ID for a snapshot file to be recovered via FTP'
SnapshotIDType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(40))
SnapshotIDType._InitializeFacetMap(SnapshotIDType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'SnapshotIDType', SnapshotIDType)

# Atomic simple type: {http://www.thalesgroup.com/rtti/PushPort/CommonTypes/v1}SourceTypeInst
class SourceTypeInst (pyxb.binding.datatypes.string):

    """RTTI CIS code, provided if forecast or actual source type is CIS"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SourceTypeInst')
    _XSDLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTCommonTypes_v1.xsd', 170, 1)
    _Documentation = 'RTTI CIS code, provided if forecast or actual source type is CIS'
SourceTypeInst._CF_length = pyxb.binding.facets.CF_length(value=pyxb.binding.datatypes.nonNegativeInteger(4))
SourceTypeInst._InitializeFacetMap(SourceTypeInst._CF_length)
Namespace.addCategoryObject('typeBinding', 'SourceTypeInst', SourceTypeInst)

# Atomic simple type: {http://www.thalesgroup.com/rtti/PushPort/CommonTypes/v1}ReasonCodeType
class ReasonCodeType (pyxb.binding.datatypes.short):

    """A Darwin Reason Code"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ReasonCodeType')
    _XSDLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTCommonTypes_v1.xsd', 178, 1)
    _Documentation = 'A Darwin Reason Code'
ReasonCodeType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'ReasonCodeType', ReasonCodeType)

# Atomic simple type: {http://www.thalesgroup.com/rtti/PushPort/CommonTypes/v1}DelayValueType
class DelayValueType (pyxb.binding.datatypes.short):

    """A signed delay value as a number of minutes"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DelayValueType')
    _XSDLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTCommonTypes_v1.xsd', 184, 1)
    _Documentation = 'A signed delay value as a number of minutes'
DelayValueType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'DelayValueType', DelayValueType)

# Atomic simple type: {http://www.thalesgroup.com/rtti/PushPort/CommonTypes/v1}TDAreaIDType
class TDAreaIDType (pyxb.binding.datatypes.string):

    """A TD area identifier."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TDAreaIDType')
    _XSDLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTCommonTypes_v1.xsd', 190, 1)
    _Documentation = 'A TD area identifier.'
TDAreaIDType._CF_length = pyxb.binding.facets.CF_length(value=pyxb.binding.datatypes.nonNegativeInteger(2))
TDAreaIDType._InitializeFacetMap(TDAreaIDType._CF_length)
Namespace.addCategoryObject('typeBinding', 'TDAreaIDType', TDAreaIDType)

# Atomic simple type: {http://www.thalesgroup.com/rtti/PushPort/CommonTypes/v1}TDBerthIDType
class TDBerthIDType (pyxb.binding.datatypes.string):

    """A TD berth identifier."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TDBerthIDType')
    _XSDLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTCommonTypes_v1.xsd', 198, 1)
    _Documentation = 'A TD berth identifier.'
TDBerthIDType._CF_length = pyxb.binding.facets.CF_length(value=pyxb.binding.datatypes.nonNegativeInteger(4))
TDBerthIDType._InitializeFacetMap(TDBerthIDType._CF_length)
Namespace.addCategoryObject('typeBinding', 'TDBerthIDType', TDBerthIDType)

# Atomic simple type: {http://www.thalesgroup.com/rtti/PushPort/CommonTypes/v1}DCISRequestID
class DCISRequestID (pyxb.binding.datatypes.string):

    """A DCIS client request identifier"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DCISRequestID')
    _XSDLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTCommonTypes_v1.xsd', 206, 1)
    _Documentation = 'A DCIS client request identifier'
DCISRequestID._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
DCISRequestID._CF_pattern = pyxb.binding.facets.CF_pattern()
DCISRequestID._CF_pattern.addPattern(pattern='[-_A-Za-z0-9]{1,16}')
DCISRequestID._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(16))
DCISRequestID._InitializeFacetMap(DCISRequestID._CF_minLength,
   DCISRequestID._CF_pattern,
   DCISRequestID._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'DCISRequestID', DCISRequestID)

# Complex type {http://www.thalesgroup.com/rtti/PushPort/CommonTypes/v1}DisruptionReasonType with content type SIMPLE
class DisruptionReasonType (pyxb.binding.basis.complexTypeDefinition):
    """Type used to represent a cancellation or late running reason"""
    _TypeDefinition = ReasonCodeType
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DisruptionReasonType')
    _XSDLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTCommonTypes_v1.xsd', 217, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is ReasonCodeType
    
    # Attribute tiploc uses Python identifier tiploc
    __tiploc = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'tiploc'), 'tiploc', '__httpwww_thalesgroup_comrttiPushPortCommonTypesv1_DisruptionReasonType_tiploc', TiplocType)
    __tiploc._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTCommonTypes_v1.xsd', 223, 4)
    __tiploc._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTCommonTypes_v1.xsd', 223, 4)
    
    tiploc = property(__tiploc.value, __tiploc.set, None, 'Optional TIPLOC where the reason refers to, e.g. "signalling failure at Cheadle Hulme".')

    
    # Attribute near uses Python identifier near
    __near = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'near'), 'near', '__httpwww_thalesgroup_comrttiPushPortCommonTypesv1_DisruptionReasonType_near', pyxb.binding.datatypes.boolean, unicode_default='false')
    __near._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTCommonTypes_v1.xsd', 228, 4)
    __near._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTCommonTypes_v1.xsd', 228, 4)
    
    near = property(__near.value, __near.set, None, 'If true, the tiploc attribute should be interpreted as "near", e.g. "signalling failure near Cheadle Hulme".')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __tiploc.name() : __tiploc,
        __near.name() : __near
    })
Namespace.addCategoryObject('typeBinding', 'DisruptionReasonType', DisruptionReasonType)

