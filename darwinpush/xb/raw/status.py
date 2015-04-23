# ./darwinpush/xb/raw/status.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:f66e44dd3449dc5dc5d2458641f69984bb31ccea
# Generated 2015-04-23 16:42:14.517447 by PyXB version 1.2.4 using Python 3.4.1.final.0
# Namespace http://thalesgroup.com/RTTI/PushPortStatus/root_1 [xmlns:status]

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
Namespace = pyxb.namespace.NamespaceForURI('http://thalesgroup.com/RTTI/PushPortStatus/root_1', create_if_missing=True)
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


# Atomic simple type: {http://thalesgroup.com/RTTI/PushPortStatus/root_1}ErrorMsgType
class ErrorMsgType (pyxb.binding.datatypes.string):

    """Error Message Type"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ErrorMsgType')
    _XSDLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTStatus_v1.xsd', 3, 1)
    _Documentation = 'Error Message Type'
ErrorMsgType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(128))
ErrorMsgType._InitializeFacetMap(ErrorMsgType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'ErrorMsgType', ErrorMsgType)

# Atomic simple type: {http://thalesgroup.com/RTTI/PushPortStatus/root_1}ErrorCodeType
class ErrorCodeType (pyxb.binding.datatypes.string):

    """Error Code Type"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ErrorCodeType')
    _XSDLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTStatus_v1.xsd', 11, 1)
    _Documentation = 'Error Code Type'
ErrorCodeType._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
ErrorCodeType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(32))
ErrorCodeType._InitializeFacetMap(ErrorCodeType._CF_minLength,
   ErrorCodeType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'ErrorCodeType', ErrorCodeType)

# Atomic simple type: [anonymous]
class STD_ANON (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTStatus_v1.xsd', 50, 4)
    _Documentation = None
STD_ANON._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON._InitializeFacetMap(STD_ANON._CF_minLength)

# Atomic simple type: [anonymous]
class STD_ANON_ (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTStatus_v1.xsd', 60, 4)
    _Documentation = None
STD_ANON_._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_._InitializeFacetMap(STD_ANON_._CF_minLength)

# Atomic simple type: [anonymous]
class STD_ANON_2 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTStatus_v1.xsd', 70, 4)
    _Documentation = None
STD_ANON_2._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_2._InitializeFacetMap(STD_ANON_2._CF_minLength)

# Complex type {http://thalesgroup.com/RTTI/PushPortStatus/root_1}StatusType with content type SIMPLE
class StatusType (pyxb.binding.basis.complexTypeDefinition):
    """Status Code Type"""
    _TypeDefinition = ErrorMsgType
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'StatusType')
    _XSDLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTStatus_v1.xsd', 20, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is ErrorMsgType
    
    # Attribute code uses Python identifier code
    __code = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'code'), 'code', '__httpthalesgroup_comRTTIPushPortStatusroot_1_StatusType_code', ErrorCodeType, required=True)
    __code._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTStatus_v1.xsd', 26, 4)
    __code._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTStatus_v1.xsd', 26, 4)
    
    code = property(__code.value, __code.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=pyxb.binding.content.Wildcard.NC_any)
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __code.name() : __code
    })
Namespace.addCategoryObject('typeBinding', 'StatusType', StatusType)


# Complex type [anonymous] with content type EMPTY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Request the schema versions required by the client"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTStatus_v1.xsd', 45, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'version'), 'version', '__httpthalesgroup_comRTTIPushPortStatusroot_1_CTD_ANON_version', STD_ANON, required=True)
    __version._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTStatus_v1.xsd', 46, 3)
    __version._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTStatus_v1.xsd', 46, 3)
    
    version = property(__version.value, __version.set, None, 'The namespace of the Push Port data schema supported by the client.')

    
    # Attribute ttversion uses Python identifier ttversion
    __ttversion = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ttversion'), 'ttversion', '__httpthalesgroup_comRTTIPushPortStatusroot_1_CTD_ANON_ttversion', STD_ANON_, required=True)
    __ttversion._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTStatus_v1.xsd', 56, 3)
    __ttversion._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTStatus_v1.xsd', 56, 3)
    
    ttversion = property(__ttversion.value, __ttversion.set, None, 'The namespace of the Push Port Timetable schema supported by the client.')

    
    # Attribute ttrefversion uses Python identifier ttrefversion
    __ttrefversion = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ttrefversion'), 'ttrefversion', '__httpthalesgroup_comRTTIPushPortStatusroot_1_CTD_ANON_ttrefversion', STD_ANON_2, required=True)
    __ttrefversion._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTStatus_v1.xsd', 66, 3)
    __ttrefversion._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTStatus_v1.xsd', 66, 3)
    
    ttrefversion = property(__ttrefversion.value, __ttrefversion.set, None, 'The namespace of the Push Port Timetable Reference data schema supported by the client.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __version.name() : __version,
        __ttversion.name() : __ttversion,
        __ttrefversion.name() : __ttrefversion
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_ (StatusType):
    """Setup phase status/heartbeat response"""
    _TypeDefinition = ErrorMsgType
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTStatus_v1.xsd', 35, 2)
    _ElementMap = StatusType._ElementMap.copy()
    _AttributeMap = StatusType._AttributeMap.copy()
    # Base type is StatusType
    
    # Attribute code inherited from {http://thalesgroup.com/RTTI/PushPortStatus/root_1}StatusType
    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=pyxb.binding.content.Wildcard.NC_any)
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })



PPConnect = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PPConnect'), pyxb.binding.datatypes.anyType, documentation='Signal end of the setup phase and switch to use the requested PP data schema.', location=pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTStatus_v1.xsd', 78, 1))
Namespace.addCategoryObject('elementBinding', PPConnect.name().localName(), PPConnect)

PPReqVersion = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PPReqVersion'), CTD_ANON, documentation='Request the schema versions required by the client', location=pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTStatus_v1.xsd', 41, 1))
Namespace.addCategoryObject('elementBinding', PPReqVersion.name().localName(), PPReqVersion)

PPStatus = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PPStatus'), CTD_ANON_, documentation='Setup phase status/heartbeat response', location=pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTStatus_v1.xsd', 31, 1))
Namespace.addCategoryObject('elementBinding', PPStatus.name().localName(), PPStatus)
