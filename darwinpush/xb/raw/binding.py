# ./darwinpush/xb/raw/binding.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:9d19614910a8e83cbb93a86fc981bfb16ed4834a
# Generated 2015-04-23 16:42:14.515396 by PyXB version 1.2.4 using Python 3.4.1.final.0
# Namespace http://www.thalesgroup.com/rtti/XmlRefData/v3

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
Namespace = pyxb.namespace.NamespaceForURI('http://www.thalesgroup.com/rtti/XmlRefData/v3', create_if_missing=True)
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


# Atomic simple type: {http://www.thalesgroup.com/rtti/XmlRefData/v3}TimetableIdType
class TimetableIdType (pyxb.binding.datatypes.string):

    """Unique Timetable identifier """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TimetableIdType')
    _XSDLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiCTTReferenceSchema_v3.xsd', 23, 1)
    _Documentation = 'Unique Timetable identifier '
TimetableIdType._CF_length = pyxb.binding.facets.CF_length(value=pyxb.binding.datatypes.nonNegativeInteger(14))
TimetableIdType._InitializeFacetMap(TimetableIdType._CF_length)
Namespace.addCategoryObject('typeBinding', 'TimetableIdType', TimetableIdType)

# Atomic simple type: {http://www.thalesgroup.com/rtti/XmlRefData/v3}LocationNameType
class LocationNameType (pyxb.binding.datatypes.string):

    """English name of the location"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LocationNameType')
    _XSDLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiCTTReferenceSchema_v3.xsd', 31, 1)
    _Documentation = 'English name of the location'
LocationNameType._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
LocationNameType._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
LocationNameType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(30))
LocationNameType._InitializeFacetMap(LocationNameType._CF_minLength,
   LocationNameType._CF_whiteSpace,
   LocationNameType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'LocationNameType', LocationNameType)

# Atomic simple type: {http://www.thalesgroup.com/rtti/XmlRefData/v3}TiplocType
class TiplocType (pyxb.binding.datatypes.string):

    """Tiploc Type (This is the short version of a TIPLOC - without spaces)"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TiplocType')
    _XSDLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiCTTReferenceSchema_v3.xsd', 41, 1)
    _Documentation = 'Tiploc Type (This is the short version of a TIPLOC - without spaces)'
TiplocType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(7))
TiplocType._InitializeFacetMap(TiplocType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'TiplocType', TiplocType)

# Atomic simple type: {http://www.thalesgroup.com/rtti/XmlRefData/v3}TOCType
class TOCType (pyxb.binding.datatypes.string):

    """ATOC Code Type"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TOCType')
    _XSDLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiCTTReferenceSchema_v3.xsd', 49, 1)
    _Documentation = 'ATOC Code Type'
TOCType._CF_length = pyxb.binding.facets.CF_length(value=pyxb.binding.datatypes.nonNegativeInteger(2))
TOCType._InitializeFacetMap(TOCType._CF_length)
Namespace.addCategoryObject('typeBinding', 'TOCType', TOCType)

# Atomic simple type: {http://www.thalesgroup.com/rtti/XmlRefData/v3}CrsType
class CrsType (pyxb.binding.datatypes.string):

    """CRS Code Type"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CrsType')
    _XSDLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiCTTReferenceSchema_v3.xsd', 57, 1)
    _Documentation = 'CRS Code Type'
CrsType._CF_length = pyxb.binding.facets.CF_length(value=pyxb.binding.datatypes.nonNegativeInteger(3))
CrsType._InitializeFacetMap(CrsType._CF_length)
Namespace.addCategoryObject('typeBinding', 'CrsType', CrsType)

# Atomic simple type: {http://www.thalesgroup.com/rtti/XmlRefData/v3}ReasonCodeType
class ReasonCodeType (pyxb.binding.datatypes.int):

    """Reason code"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ReasonCodeType')
    _XSDLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiCTTReferenceSchema_v3.xsd', 65, 1)
    _Documentation = 'Reason code'
ReasonCodeType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'ReasonCodeType', ReasonCodeType)

# Atomic simple type: {http://www.thalesgroup.com/rtti/XmlRefData/v3}ReasonTextType
class ReasonTextType (pyxb.binding.datatypes.string):

    """Reason as text"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ReasonTextType')
    _XSDLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiCTTReferenceSchema_v3.xsd', 71, 1)
    _Documentation = 'Reason as text'
ReasonTextType._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
ReasonTextType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(256))
ReasonTextType._InitializeFacetMap(ReasonTextType._CF_minLength,
   ReasonTextType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'ReasonTextType', ReasonTextType)

# Atomic simple type: {http://www.thalesgroup.com/rtti/XmlRefData/v3}ViaTextType
class ViaTextType (pyxb.binding.datatypes.string):

    """The text displayed for a via"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ViaTextType')
    _XSDLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiCTTReferenceSchema_v3.xsd', 80, 1)
    _Documentation = 'The text displayed for a via'
ViaTextType._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
ViaTextType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(256))
ViaTextType._InitializeFacetMap(ViaTextType._CF_minLength,
   ViaTextType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'ViaTextType', ViaTextType)

# Atomic simple type: {http://www.thalesgroup.com/rtti/XmlRefData/v3}TOCNameType
class TOCNameType (pyxb.binding.datatypes.string):

    """The name of the TOC"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TOCNameType')
    _XSDLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiCTTReferenceSchema_v3.xsd', 89, 1)
    _Documentation = 'The name of the TOC'
TOCNameType._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(0))
TOCNameType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(256))
TOCNameType._InitializeFacetMap(TOCNameType._CF_minLength,
   TOCNameType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'TOCNameType', TOCNameType)

# Atomic simple type: {http://www.thalesgroup.com/rtti/XmlRefData/v3}UrlType
class UrlType (pyxb.binding.datatypes.string):

    """A URL"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'UrlType')
    _XSDLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiCTTReferenceSchema_v3.xsd', 98, 1)
    _Documentation = 'A URL'
UrlType._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(0))
UrlType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(512))
UrlType._InitializeFacetMap(UrlType._CF_minLength,
   UrlType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'UrlType', UrlType)

# Atomic simple type: {http://www.thalesgroup.com/rtti/XmlRefData/v3}CISSourceCode
class CISSourceCode (pyxb.binding.datatypes.string):

    """A CIS source code"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CISSourceCode')
    _XSDLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiCTTReferenceSchema_v3.xsd', 107, 1)
    _Documentation = 'A CIS source code'
CISSourceCode._CF_length = pyxb.binding.facets.CF_length(value=pyxb.binding.datatypes.nonNegativeInteger(4))
CISSourceCode._InitializeFacetMap(CISSourceCode._CF_length)
Namespace.addCategoryObject('typeBinding', 'CISSourceCode', CISSourceCode)

# Atomic simple type: {http://www.thalesgroup.com/rtti/XmlRefData/v3}CISSourceName
class CISSourceName (pyxb.binding.datatypes.string):

    """A CIS source name"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CISSourceName')
    _XSDLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiCTTReferenceSchema_v3.xsd', 115, 1)
    _Documentation = 'A CIS source name'
CISSourceName._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(0))
CISSourceName._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(30))
CISSourceName._InitializeFacetMap(CISSourceName._CF_minLength,
   CISSourceName._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'CISSourceName', CISSourceName)

# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiCTTReferenceSchema_v3.xsd', 134, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.thalesgroup.com/rtti/XmlRefData/v3}Reason uses Python identifier Reason
    __Reason = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Reason'), 'Reason', '__httpwww_thalesgroup_comrttiXmlRefDatav3_CTD_ANON_httpwww_thalesgroup_comrttiXmlRefDatav3Reason', True, pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiCTTReferenceSchema_v3.xsd', 198, 1), )

    
    Reason = property(__Reason.value, __Reason.set, None, 'Defines a mapping bewteen a reason code and the corresponding text')

    _ElementMap.update({
        __Reason.name() : __Reason
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiCTTReferenceSchema_v3.xsd', 141, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.thalesgroup.com/rtti/XmlRefData/v3}Reason uses Python identifier Reason
    __Reason = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Reason'), 'Reason', '__httpwww_thalesgroup_comrttiXmlRefDatav3_CTD_ANON__httpwww_thalesgroup_comrttiXmlRefDatav3Reason', True, pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiCTTReferenceSchema_v3.xsd', 198, 1), )

    
    Reason = property(__Reason.value, __Reason.set, None, 'Defines a mapping bewteen a reason code and the corresponding text')

    _ElementMap.update({
        __Reason.name() : __Reason
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    """Push Port Timetable Reference Schema """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiCTTReferenceSchema_v3.xsd', 129, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.thalesgroup.com/rtti/XmlRefData/v3}LateRunningReasons uses Python identifier LateRunningReasons
    __LateRunningReasons = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'LateRunningReasons'), 'LateRunningReasons', '__httpwww_thalesgroup_comrttiXmlRefDatav3_CTD_ANON_2_httpwww_thalesgroup_comrttiXmlRefDatav3LateRunningReasons', False, pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiCTTReferenceSchema_v3.xsd', 133, 4), )

    
    LateRunningReasons = property(__LateRunningReasons.value, __LateRunningReasons.set, None, None)

    
    # Element {http://www.thalesgroup.com/rtti/XmlRefData/v3}CancellationReasons uses Python identifier CancellationReasons
    __CancellationReasons = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CancellationReasons'), 'CancellationReasons', '__httpwww_thalesgroup_comrttiXmlRefDatav3_CTD_ANON_2_httpwww_thalesgroup_comrttiXmlRefDatav3CancellationReasons', False, pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiCTTReferenceSchema_v3.xsd', 140, 4), )

    
    CancellationReasons = property(__CancellationReasons.value, __CancellationReasons.set, None, None)

    
    # Element {http://www.thalesgroup.com/rtti/XmlRefData/v3}LocationRef uses Python identifier LocationRef
    __LocationRef = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'LocationRef'), 'LocationRef', '__httpwww_thalesgroup_comrttiXmlRefDatav3_CTD_ANON_2_httpwww_thalesgroup_comrttiXmlRefDatav3LocationRef', True, pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiCTTReferenceSchema_v3.xsd', 153, 1), )

    
    LocationRef = property(__LocationRef.value, __LocationRef.set, None, 'Defines a location')

    
    # Element {http://www.thalesgroup.com/rtti/XmlRefData/v3}TocRef uses Python identifier TocRef
    __TocRef = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TocRef'), 'TocRef', '__httpwww_thalesgroup_comrttiXmlRefDatav3_CTD_ANON_2_httpwww_thalesgroup_comrttiXmlRefDatav3TocRef', True, pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiCTTReferenceSchema_v3.xsd', 180, 1), )

    
    TocRef = property(__TocRef.value, __TocRef.set, None, 'Defines a mapping between a TOC and a displayable name')

    
    # Element {http://www.thalesgroup.com/rtti/XmlRefData/v3}Via uses Python identifier Via
    __Via = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Via'), 'Via', '__httpwww_thalesgroup_comrttiXmlRefDatav3_CTD_ANON_2_httpwww_thalesgroup_comrttiXmlRefDatav3Via', True, pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiCTTReferenceSchema_v3.xsd', 207, 1), )

    
    Via = property(__Via.value, __Via.set, None, 'Defines the locations a journey must be viewed from, go to and pass through for the corresponding via text to be displayed')

    
    # Element {http://www.thalesgroup.com/rtti/XmlRefData/v3}CISSource uses Python identifier CISSource
    __CISSource = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CISSource'), 'CISSource', '__httpwww_thalesgroup_comrttiXmlRefDatav3_CTD_ANON_2_httpwww_thalesgroup_comrttiXmlRefDatav3CISSource', True, pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiCTTReferenceSchema_v3.xsd', 239, 1), )

    
    CISSource = property(__CISSource.value, __CISSource.set, None, 'Defines the mapping between 4 letter CIS codes and the CIS name')

    
    # Attribute timetableId uses Python identifier timetableId
    __timetableId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'timetableId'), 'timetableId', '__httpwww_thalesgroup_comrttiXmlRefDatav3_CTD_ANON_2_timetableId', TimetableIdType, required=True)
    __timetableId._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiCTTReferenceSchema_v3.xsd', 150, 3)
    __timetableId._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiCTTReferenceSchema_v3.xsd', 150, 3)
    
    timetableId = property(__timetableId.value, __timetableId.set, None, None)

    _ElementMap.update({
        __LateRunningReasons.name() : __LateRunningReasons,
        __CancellationReasons.name() : __CancellationReasons,
        __LocationRef.name() : __LocationRef,
        __TocRef.name() : __TocRef,
        __Via.name() : __Via,
        __CISSource.name() : __CISSource
    })
    _AttributeMap.update({
        __timetableId.name() : __timetableId
    })



# Complex type [anonymous] with content type EMPTY
class CTD_ANON_3 (pyxb.binding.basis.complexTypeDefinition):
    """Defines a location"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiCTTReferenceSchema_v3.xsd', 157, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute tpl uses Python identifier tpl
    __tpl = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'tpl'), 'tpl', '__httpwww_thalesgroup_comrttiXmlRefDatav3_CTD_ANON_3_tpl', TiplocType, required=True)
    __tpl._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiCTTReferenceSchema_v3.xsd', 158, 3)
    __tpl._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiCTTReferenceSchema_v3.xsd', 158, 3)
    
    tpl = property(__tpl.value, __tpl.set, None, 'TIPLOC code')

    
    # Attribute crs uses Python identifier crs
    __crs = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'crs'), 'crs', '__httpwww_thalesgroup_comrttiXmlRefDatav3_CTD_ANON_3_crs', CrsType)
    __crs._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiCTTReferenceSchema_v3.xsd', 163, 3)
    __crs._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiCTTReferenceSchema_v3.xsd', 163, 3)
    
    crs = property(__crs.value, __crs.set, None, 'CRS code')

    
    # Attribute toc uses Python identifier toc
    __toc = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'toc'), 'toc', '__httpwww_thalesgroup_comrttiXmlRefDatav3_CTD_ANON_3_toc', TOCType)
    __toc._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiCTTReferenceSchema_v3.xsd', 168, 3)
    __toc._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiCTTReferenceSchema_v3.xsd', 168, 3)
    
    toc = property(__toc.value, __toc.set, None, 'Train Operating Company that manages the station (may be non-TOC code, e.g. Network Rail).')

    
    # Attribute locname uses Python identifier locname
    __locname = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'locname'), 'locname', '__httpwww_thalesgroup_comrttiXmlRefDatav3_CTD_ANON_3_locname', LocationNameType, required=True)
    __locname._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiCTTReferenceSchema_v3.xsd', 173, 3)
    __locname._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiCTTReferenceSchema_v3.xsd', 173, 3)
    
    locname = property(__locname.value, __locname.set, None, 'English name of location')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __tpl.name() : __tpl,
        __crs.name() : __crs,
        __toc.name() : __toc,
        __locname.name() : __locname
    })



# Complex type [anonymous] with content type EMPTY
class CTD_ANON_4 (pyxb.binding.basis.complexTypeDefinition):
    """Defines a mapping between a TOC and a displayable name"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiCTTReferenceSchema_v3.xsd', 184, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute toc uses Python identifier toc
    __toc = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'toc'), 'toc', '__httpwww_thalesgroup_comrttiXmlRefDatav3_CTD_ANON_4_toc', TOCType, required=True)
    __toc._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiCTTReferenceSchema_v3.xsd', 185, 3)
    __toc._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiCTTReferenceSchema_v3.xsd', 185, 3)
    
    toc = property(__toc.value, __toc.set, None, 'The TOC code')

    
    # Attribute tocname uses Python identifier tocname
    __tocname = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'tocname'), 'tocname', '__httpwww_thalesgroup_comrttiXmlRefDatav3_CTD_ANON_4_tocname', TOCNameType, required=True)
    __tocname._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiCTTReferenceSchema_v3.xsd', 190, 3)
    __tocname._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiCTTReferenceSchema_v3.xsd', 190, 3)
    
    tocname = property(__tocname.value, __tocname.set, None, 'The name of the TOC')

    
    # Attribute url uses Python identifier url
    __url = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'url'), 'url', '__httpwww_thalesgroup_comrttiXmlRefDatav3_CTD_ANON_4_url', UrlType)
    __url._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiCTTReferenceSchema_v3.xsd', 195, 3)
    __url._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiCTTReferenceSchema_v3.xsd', 195, 3)
    
    url = property(__url.value, __url.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __toc.name() : __toc,
        __tocname.name() : __tocname,
        __url.name() : __url
    })



# Complex type [anonymous] with content type EMPTY
class CTD_ANON_5 (pyxb.binding.basis.complexTypeDefinition):
    """Defines a mapping bewteen a reason code and the corresponding text"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiCTTReferenceSchema_v3.xsd', 202, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute code uses Python identifier code
    __code = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'code'), 'code', '__httpwww_thalesgroup_comrttiXmlRefDatav3_CTD_ANON_5_code', ReasonCodeType, required=True)
    __code._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiCTTReferenceSchema_v3.xsd', 203, 3)
    __code._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiCTTReferenceSchema_v3.xsd', 203, 3)
    
    code = property(__code.value, __code.set, None, None)

    
    # Attribute reasontext uses Python identifier reasontext
    __reasontext = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'reasontext'), 'reasontext', '__httpwww_thalesgroup_comrttiXmlRefDatav3_CTD_ANON_5_reasontext', ReasonTextType, required=True)
    __reasontext._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiCTTReferenceSchema_v3.xsd', 204, 3)
    __reasontext._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiCTTReferenceSchema_v3.xsd', 204, 3)
    
    reasontext = property(__reasontext.value, __reasontext.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __code.name() : __code,
        __reasontext.name() : __reasontext
    })



# Complex type [anonymous] with content type EMPTY
class CTD_ANON_6 (pyxb.binding.basis.complexTypeDefinition):
    """Defines the locations a journey must be viewed from, go to and pass through for the corresponding via text to be displayed"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiCTTReferenceSchema_v3.xsd', 211, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute at uses Python identifier at
    __at = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'at'), 'at', '__httpwww_thalesgroup_comrttiXmlRefDatav3_CTD_ANON_6_at', CrsType, required=True)
    __at._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiCTTReferenceSchema_v3.xsd', 212, 3)
    __at._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiCTTReferenceSchema_v3.xsd', 212, 3)
    
    at = property(__at.value, __at.set, None, 'This is the station for which the via is defined')

    
    # Attribute dest uses Python identifier dest
    __dest = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'dest'), 'dest', '__httpwww_thalesgroup_comrttiXmlRefDatav3_CTD_ANON_6_dest', TiplocType, required=True)
    __dest._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiCTTReferenceSchema_v3.xsd', 217, 3)
    __dest._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiCTTReferenceSchema_v3.xsd', 217, 3)
    
    dest = property(__dest.value, __dest.set, None, 'The destination of the journey must match this before the via text is valid')

    
    # Attribute loc1 uses Python identifier loc1
    __loc1 = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'loc1'), 'loc1', '__httpwww_thalesgroup_comrttiXmlRefDatav3_CTD_ANON_6_loc1', TiplocType, required=True)
    __loc1._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiCTTReferenceSchema_v3.xsd', 222, 3)
    __loc1._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiCTTReferenceSchema_v3.xsd', 222, 3)
    
    loc1 = property(__loc1.value, __loc1.set, None, 'The journey must call at this station before the via text is valid.')

    
    # Attribute loc2 uses Python identifier loc2
    __loc2 = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'loc2'), 'loc2', '__httpwww_thalesgroup_comrttiXmlRefDatav3_CTD_ANON_6_loc2', TiplocType)
    __loc2._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiCTTReferenceSchema_v3.xsd', 227, 3)
    __loc2._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiCTTReferenceSchema_v3.xsd', 227, 3)
    
    loc2 = property(__loc2.value, __loc2.set, None, 'The journey must call at this station (after the call at loc1) before the via text is valid.')

    
    # Attribute viatext uses Python identifier viatext
    __viatext = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'viatext'), 'viatext', '__httpwww_thalesgroup_comrttiXmlRefDatav3_CTD_ANON_6_viatext', ViaTextType, required=True)
    __viatext._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiCTTReferenceSchema_v3.xsd', 232, 3)
    __viatext._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiCTTReferenceSchema_v3.xsd', 232, 3)
    
    viatext = property(__viatext.value, __viatext.set, None, 'The via text to display if a journey matches the previous attributes')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __at.name() : __at,
        __dest.name() : __dest,
        __loc1.name() : __loc1,
        __loc2.name() : __loc2,
        __viatext.name() : __viatext
    })



# Complex type [anonymous] with content type EMPTY
class CTD_ANON_7 (pyxb.binding.basis.complexTypeDefinition):
    """Defines the mapping between 4 letter CIS codes and the CIS name"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiCTTReferenceSchema_v3.xsd', 243, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute code uses Python identifier code
    __code = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'code'), 'code', '__httpwww_thalesgroup_comrttiXmlRefDatav3_CTD_ANON_7_code', CISSourceCode, required=True)
    __code._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiCTTReferenceSchema_v3.xsd', 244, 3)
    __code._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiCTTReferenceSchema_v3.xsd', 244, 3)
    
    code = property(__code.value, __code.set, None, 'This is the 4 letter CIS code')

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__httpwww_thalesgroup_comrttiXmlRefDatav3_CTD_ANON_7_name', CISSourceName, required=True)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiCTTReferenceSchema_v3.xsd', 249, 3)
    __name._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiCTTReferenceSchema_v3.xsd', 249, 3)
    
    name = property(__name.value, __name.set, None, 'The CIS name')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __code.name() : __code,
        __name.name() : __name
    })



PportTimetableRef = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PportTimetableRef'), CTD_ANON_2, documentation='Push Port Timetable Reference Schema ', location=pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiCTTReferenceSchema_v3.xsd', 125, 1))
Namespace.addCategoryObject('elementBinding', PportTimetableRef.name().localName(), PportTimetableRef)

LocationRef = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LocationRef'), CTD_ANON_3, documentation='Defines a location', location=pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiCTTReferenceSchema_v3.xsd', 153, 1))
Namespace.addCategoryObject('elementBinding', LocationRef.name().localName(), LocationRef)

TocRef = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TocRef'), CTD_ANON_4, documentation='Defines a mapping between a TOC and a displayable name', location=pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiCTTReferenceSchema_v3.xsd', 180, 1))
Namespace.addCategoryObject('elementBinding', TocRef.name().localName(), TocRef)

Reason = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Reason'), CTD_ANON_5, documentation='Defines a mapping bewteen a reason code and the corresponding text', location=pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiCTTReferenceSchema_v3.xsd', 198, 1))
Namespace.addCategoryObject('elementBinding', Reason.name().localName(), Reason)

Via = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Via'), CTD_ANON_6, documentation='Defines the locations a journey must be viewed from, go to and pass through for the corresponding via text to be displayed', location=pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiCTTReferenceSchema_v3.xsd', 207, 1))
Namespace.addCategoryObject('elementBinding', Via.name().localName(), Via)

CISSource = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CISSource'), CTD_ANON_7, documentation='Defines the mapping between 4 letter CIS codes and the CIS name', location=pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiCTTReferenceSchema_v3.xsd', 239, 1))
Namespace.addCategoryObject('elementBinding', CISSource.name().localName(), CISSource)



CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Reason'), CTD_ANON_5, scope=CTD_ANON, documentation='Defines a mapping bewteen a reason code and the corresponding text', location=pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiCTTReferenceSchema_v3.xsd', 198, 1)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Reason')), pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiCTTReferenceSchema_v3.xsd', 136, 7))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton()




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Reason'), CTD_ANON_5, scope=CTD_ANON_, documentation='Defines a mapping bewteen a reason code and the corresponding text', location=pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiCTTReferenceSchema_v3.xsd', 198, 1)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Reason')), pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiCTTReferenceSchema_v3.xsd', 143, 7))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_._Automaton = _BuildAutomaton_()




CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LateRunningReasons'), CTD_ANON, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiCTTReferenceSchema_v3.xsd', 133, 4)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CancellationReasons'), CTD_ANON_, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiCTTReferenceSchema_v3.xsd', 140, 4)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LocationRef'), CTD_ANON_3, scope=CTD_ANON_2, documentation='Defines a location', location=pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiCTTReferenceSchema_v3.xsd', 153, 1)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TocRef'), CTD_ANON_4, scope=CTD_ANON_2, documentation='Defines a mapping between a TOC and a displayable name', location=pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiCTTReferenceSchema_v3.xsd', 180, 1)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Via'), CTD_ANON_6, scope=CTD_ANON_2, documentation='Defines the locations a journey must be viewed from, go to and pass through for the corresponding via text to be displayed', location=pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiCTTReferenceSchema_v3.xsd', 207, 1)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CISSource'), CTD_ANON_7, scope=CTD_ANON_2, documentation='Defines the mapping between 4 letter CIS codes and the CIS name', location=pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiCTTReferenceSchema_v3.xsd', 239, 1)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiCTTReferenceSchema_v3.xsd', 131, 4))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiCTTReferenceSchema_v3.xsd', 132, 4))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiCTTReferenceSchema_v3.xsd', 133, 4))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiCTTReferenceSchema_v3.xsd', 140, 4))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiCTTReferenceSchema_v3.xsd', 147, 4))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiCTTReferenceSchema_v3.xsd', 148, 4))
    counters.add(cc_5)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'LocationRef')), pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiCTTReferenceSchema_v3.xsd', 131, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TocRef')), pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiCTTReferenceSchema_v3.xsd', 132, 4))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'LateRunningReasons')), pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiCTTReferenceSchema_v3.xsd', 133, 4))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CancellationReasons')), pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiCTTReferenceSchema_v3.xsd', 140, 4))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Via')), pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiCTTReferenceSchema_v3.xsd', 147, 4))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CISSource')), pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiCTTReferenceSchema_v3.xsd', 148, 4))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
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
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_2._Automaton = _BuildAutomaton_2()

