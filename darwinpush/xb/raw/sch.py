# ./darwinpush/xb/raw/sch.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:a4d0e93b3d986983d09f604844e6ca8969d2f70c
# Generated 2015-04-23 16:42:14.518511 by PyXB version 1.2.4 using Python 3.4.1.final.0
# Namespace http://www.thalesgroup.com/rtti/PushPort/Schedules/v1 [xmlns:sch]

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
Namespace = pyxb.namespace.NamespaceForURI('http://www.thalesgroup.com/rtti/PushPort/Schedules/v1', create_if_missing=True)
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


# Atomic simple type: {http://www.thalesgroup.com/rtti/PushPort/Schedules/v1}CategoryType
class CategoryType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Association Category Type: JJ=Join, VV=Split, LK=Linked, NP=Next-Working"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CategoryType')
    _XSDLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 15, 1)
    _Documentation = 'Association Category Type: JJ=Join, VV=Split, LK=Linked, NP=Next-Working'
CategoryType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=CategoryType, enum_prefix=None)
CategoryType.JJ = CategoryType._CF_enumeration.addEnumeration(unicode_value='JJ', tag='JJ')
CategoryType.VV = CategoryType._CF_enumeration.addEnumeration(unicode_value='VV', tag='VV')
CategoryType.LK = CategoryType._CF_enumeration.addEnumeration(unicode_value='LK', tag='LK')
CategoryType.NP = CategoryType._CF_enumeration.addEnumeration(unicode_value='NP', tag='NP')
CategoryType._InitializeFacetMap(CategoryType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'CategoryType', CategoryType)

# Complex type {http://www.thalesgroup.com/rtti/PushPort/Schedules/v1}AssocService with content type EMPTY
class AssocService (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.thalesgroup.com/rtti/PushPort/Schedules/v1}AssocService with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AssocService')
    _XSDLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 27, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute wta uses Python identifier wta
    __wta = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'wta'), 'wta', '__httpwww_thalesgroup_comrttiPushPortSchedulesv1_AssocService_wta', _ImportedBinding_darwinpush_xb_ct.WTimeType)
    __wta._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTCommonTypes_v1.xsd', 243, 2)
    __wta._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTCommonTypes_v1.xsd', 243, 2)
    
    wta = property(__wta.value, __wta.set, None, 'Working time of arrival.')

    
    # Attribute wtd uses Python identifier wtd
    __wtd = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'wtd'), 'wtd', '__httpwww_thalesgroup_comrttiPushPortSchedulesv1_AssocService_wtd', _ImportedBinding_darwinpush_xb_ct.WTimeType)
    __wtd._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTCommonTypes_v1.xsd', 248, 2)
    __wtd._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTCommonTypes_v1.xsd', 248, 2)
    
    wtd = property(__wtd.value, __wtd.set, None, 'Working time of departure.')

    
    # Attribute wtp uses Python identifier wtp
    __wtp = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'wtp'), 'wtp', '__httpwww_thalesgroup_comrttiPushPortSchedulesv1_AssocService_wtp', _ImportedBinding_darwinpush_xb_ct.WTimeType)
    __wtp._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTCommonTypes_v1.xsd', 253, 2)
    __wtp._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTCommonTypes_v1.xsd', 253, 2)
    
    wtp = property(__wtp.value, __wtp.set, None, 'Working time of pass.')

    
    # Attribute pta uses Python identifier pta
    __pta = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'pta'), 'pta', '__httpwww_thalesgroup_comrttiPushPortSchedulesv1_AssocService_pta', _ImportedBinding_darwinpush_xb_ct.RTTITimeType)
    __pta._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTCommonTypes_v1.xsd', 258, 2)
    __pta._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTCommonTypes_v1.xsd', 258, 2)
    
    pta = property(__pta.value, __pta.set, None, 'Public time of arrival.')

    
    # Attribute ptd uses Python identifier ptd
    __ptd = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ptd'), 'ptd', '__httpwww_thalesgroup_comrttiPushPortSchedulesv1_AssocService_ptd', _ImportedBinding_darwinpush_xb_ct.RTTITimeType)
    __ptd._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTCommonTypes_v1.xsd', 263, 2)
    __ptd._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTCommonTypes_v1.xsd', 263, 2)
    
    ptd = property(__ptd.value, __ptd.set, None, 'Public time of departure.')

    
    # Attribute rid uses Python identifier rid
    __rid = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'rid'), 'rid', '__httpwww_thalesgroup_comrttiPushPortSchedulesv1_AssocService_rid', _ImportedBinding_darwinpush_xb_ct.RIDType, required=True)
    __rid._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 28, 2)
    __rid._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 28, 2)
    
    rid = property(__rid.value, __rid.set, None, 'RTTI Train ID. Note that since this is an RID, the service must already exist within Darwin.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __wta.name() : __wta,
        __wtd.name() : __wtd,
        __wtp.name() : __wtp,
        __pta.name() : __pta,
        __ptd.name() : __ptd,
        __rid.name() : __rid
    })
Namespace.addCategoryObject('typeBinding', 'AssocService', AssocService)


# Complex type {http://www.thalesgroup.com/rtti/PushPort/Schedules/v1}Association with content type ELEMENT_ONLY
class Association (pyxb.binding.basis.complexTypeDefinition):
    """Type describing an association between schedules"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Association')
    _XSDLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 39, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.thalesgroup.com/rtti/PushPort/Schedules/v1}main uses Python identifier main
    __main = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'main'), 'main', '__httpwww_thalesgroup_comrttiPushPortSchedulesv1_Association_httpwww_thalesgroup_comrttiPushPortSchedulesv1main', False, pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 44, 3), )

    
    main = property(__main.value, __main.set, None, 'The through, previous working or link-to service')

    
    # Element {http://www.thalesgroup.com/rtti/PushPort/Schedules/v1}assoc uses Python identifier assoc
    __assoc = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'assoc'), 'assoc', '__httpwww_thalesgroup_comrttiPushPortSchedulesv1_Association_httpwww_thalesgroup_comrttiPushPortSchedulesv1assoc', False, pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 49, 3), )

    
    assoc = property(__assoc.value, __assoc.set, None, 'The starting, terminating, subsequent working or link-from service')

    
    # Attribute tiploc uses Python identifier tiploc
    __tiploc = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'tiploc'), 'tiploc', '__httpwww_thalesgroup_comrttiPushPortSchedulesv1_Association_tiploc', _ImportedBinding_darwinpush_xb_ct.TiplocType, required=True)
    __tiploc._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 55, 2)
    __tiploc._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 55, 2)
    
    tiploc = property(__tiploc.value, __tiploc.set, None, 'The TIPLOC of the location where the association occurs.')

    
    # Attribute category uses Python identifier category
    __category = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'category'), 'category', '__httpwww_thalesgroup_comrttiPushPortSchedulesv1_Association_category', CategoryType, required=True)
    __category._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 60, 2)
    __category._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 60, 2)
    
    category = property(__category.value, __category.set, None, 'Association category')

    
    # Attribute isCancelled uses Python identifier isCancelled
    __isCancelled = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'isCancelled'), 'isCancelled', '__httpwww_thalesgroup_comrttiPushPortSchedulesv1_Association_isCancelled', pyxb.binding.datatypes.boolean, unicode_default='false')
    __isCancelled._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 65, 2)
    __isCancelled._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 65, 2)
    
    isCancelled = property(__isCancelled.value, __isCancelled.set, None, 'True if this association is cancelled, i.e. the association exists but will no longer happen.')

    
    # Attribute isDeleted uses Python identifier isDeleted
    __isDeleted = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'isDeleted'), 'isDeleted', '__httpwww_thalesgroup_comrttiPushPortSchedulesv1_Association_isDeleted', pyxb.binding.datatypes.boolean, unicode_default='false')
    __isDeleted._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 70, 2)
    __isDeleted._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 70, 2)
    
    isDeleted = property(__isDeleted.value, __isDeleted.set, None, 'True if this association is deleted, i.e. the association no longer exists.')

    _ElementMap.update({
        __main.name() : __main,
        __assoc.name() : __assoc
    })
    _AttributeMap.update({
        __tiploc.name() : __tiploc,
        __category.name() : __category,
        __isCancelled.name() : __isCancelled,
        __isDeleted.name() : __isDeleted
    })
Namespace.addCategoryObject('typeBinding', 'Association', Association)


# Complex type {http://www.thalesgroup.com/rtti/PushPort/Schedules/v1}OR with content type EMPTY
class OR (pyxb.binding.basis.complexTypeDefinition):
    """Defines a Passenger Origin Calling Point"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'OR')
    _XSDLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 116, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute tpl uses Python identifier tpl
    __tpl = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'tpl'), 'tpl', '__httpwww_thalesgroup_comrttiPushPortSchedulesv1_OR_tpl', _ImportedBinding_darwinpush_xb_ct.TiplocType, required=True)
    __tpl._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 80, 2)
    __tpl._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 80, 2)
    
    tpl = property(__tpl.value, __tpl.set, None, 'TIPLOC')

    
    # Attribute act uses Python identifier act
    __act = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'act'), 'act', '__httpwww_thalesgroup_comrttiPushPortSchedulesv1_OR_act', _ImportedBinding_darwinpush_xb_ct.ActivityType, unicode_default='  ')
    __act._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 85, 2)
    __act._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 85, 2)
    
    act = property(__act.value, __act.set, None, 'Current Activity Codes')

    
    # Attribute planAct uses Python identifier planAct
    __planAct = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'planAct'), 'planAct', '__httpwww_thalesgroup_comrttiPushPortSchedulesv1_OR_planAct', _ImportedBinding_darwinpush_xb_ct.ActivityType)
    __planAct._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 90, 2)
    __planAct._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 90, 2)
    
    planAct = property(__planAct.value, __planAct.set, None, 'Planned Activity Codes (if different to current activities)')

    
    # Attribute can uses Python identifier can
    __can = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'can'), 'can', '__httpwww_thalesgroup_comrttiPushPortSchedulesv1_OR_can', pyxb.binding.datatypes.boolean, unicode_default='false')
    __can._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 95, 2)
    __can._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 95, 2)
    
    can = property(__can.value, __can.set, None, 'Cancelled')

    
    # Attribute pta uses Python identifier pta
    __pta = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'pta'), 'pta', '__httpwww_thalesgroup_comrttiPushPortSchedulesv1_OR_pta', _ImportedBinding_darwinpush_xb_ct.RTTITimeType)
    __pta._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 105, 2)
    __pta._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 105, 2)
    
    pta = property(__pta.value, __pta.set, None, 'Public Scheduled Time of Arrival')

    
    # Attribute ptd uses Python identifier ptd
    __ptd = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ptd'), 'ptd', '__httpwww_thalesgroup_comrttiPushPortSchedulesv1_OR_ptd', _ImportedBinding_darwinpush_xb_ct.RTTITimeType)
    __ptd._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 110, 2)
    __ptd._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 110, 2)
    
    ptd = property(__ptd.value, __ptd.set, None, 'Public Scheduled Time of Departure')

    
    # Attribute wta uses Python identifier wta
    __wta = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'wta'), 'wta', '__httpwww_thalesgroup_comrttiPushPortSchedulesv1_OR_wta', _ImportedBinding_darwinpush_xb_ct.WTimeType)
    __wta._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 122, 2)
    __wta._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 122, 2)
    
    wta = property(__wta.value, __wta.set, None, 'Working Scheduled Time of Arrival')

    
    # Attribute wtd uses Python identifier wtd
    __wtd = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'wtd'), 'wtd', '__httpwww_thalesgroup_comrttiPushPortSchedulesv1_OR_wtd', _ImportedBinding_darwinpush_xb_ct.WTimeType, required=True)
    __wtd._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 127, 2)
    __wtd._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 127, 2)
    
    wtd = property(__wtd.value, __wtd.set, None, 'Working Scheduled Time of Departure')

    
    # Attribute fd uses Python identifier fd
    __fd = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'fd'), 'fd', '__httpwww_thalesgroup_comrttiPushPortSchedulesv1_OR_fd', _ImportedBinding_darwinpush_xb_ct.TiplocType)
    __fd._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 132, 2)
    __fd._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 132, 2)
    
    fd = property(__fd.value, __fd.set, None, 'TIPLOC of False Destination to be used at this location')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __tpl.name() : __tpl,
        __act.name() : __act,
        __planAct.name() : __planAct,
        __can.name() : __can,
        __pta.name() : __pta,
        __ptd.name() : __ptd,
        __wta.name() : __wta,
        __wtd.name() : __wtd,
        __fd.name() : __fd
    })
Namespace.addCategoryObject('typeBinding', 'OR', OR)


# Complex type {http://www.thalesgroup.com/rtti/PushPort/Schedules/v1}OPOR with content type EMPTY
class OPOR (pyxb.binding.basis.complexTypeDefinition):
    """Defines an Operational Origin Calling Point"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'OPOR')
    _XSDLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 138, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute tpl uses Python identifier tpl
    __tpl = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'tpl'), 'tpl', '__httpwww_thalesgroup_comrttiPushPortSchedulesv1_OPOR_tpl', _ImportedBinding_darwinpush_xb_ct.TiplocType, required=True)
    __tpl._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 80, 2)
    __tpl._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 80, 2)
    
    tpl = property(__tpl.value, __tpl.set, None, 'TIPLOC')

    
    # Attribute act uses Python identifier act
    __act = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'act'), 'act', '__httpwww_thalesgroup_comrttiPushPortSchedulesv1_OPOR_act', _ImportedBinding_darwinpush_xb_ct.ActivityType, unicode_default='  ')
    __act._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 85, 2)
    __act._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 85, 2)
    
    act = property(__act.value, __act.set, None, 'Current Activity Codes')

    
    # Attribute planAct uses Python identifier planAct
    __planAct = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'planAct'), 'planAct', '__httpwww_thalesgroup_comrttiPushPortSchedulesv1_OPOR_planAct', _ImportedBinding_darwinpush_xb_ct.ActivityType)
    __planAct._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 90, 2)
    __planAct._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 90, 2)
    
    planAct = property(__planAct.value, __planAct.set, None, 'Planned Activity Codes (if different to current activities)')

    
    # Attribute can uses Python identifier can
    __can = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'can'), 'can', '__httpwww_thalesgroup_comrttiPushPortSchedulesv1_OPOR_can', pyxb.binding.datatypes.boolean, unicode_default='false')
    __can._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 95, 2)
    __can._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 95, 2)
    
    can = property(__can.value, __can.set, None, 'Cancelled')

    
    # Attribute wta uses Python identifier wta
    __wta = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'wta'), 'wta', '__httpwww_thalesgroup_comrttiPushPortSchedulesv1_OPOR_wta', _ImportedBinding_darwinpush_xb_ct.WTimeType)
    __wta._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 143, 2)
    __wta._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 143, 2)
    
    wta = property(__wta.value, __wta.set, None, 'Working Scheduled Time of Arrival')

    
    # Attribute wtd uses Python identifier wtd
    __wtd = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'wtd'), 'wtd', '__httpwww_thalesgroup_comrttiPushPortSchedulesv1_OPOR_wtd', _ImportedBinding_darwinpush_xb_ct.WTimeType, required=True)
    __wtd._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 148, 2)
    __wtd._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 148, 2)
    
    wtd = property(__wtd.value, __wtd.set, None, 'Working Scheduled Time of Departure')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __tpl.name() : __tpl,
        __act.name() : __act,
        __planAct.name() : __planAct,
        __can.name() : __can,
        __wta.name() : __wta,
        __wtd.name() : __wtd
    })
Namespace.addCategoryObject('typeBinding', 'OPOR', OPOR)


# Complex type {http://www.thalesgroup.com/rtti/PushPort/Schedules/v1}IP with content type EMPTY
class IP (pyxb.binding.basis.complexTypeDefinition):
    """Defines aPassenger Intermediate Calling Point"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'IP')
    _XSDLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 154, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute tpl uses Python identifier tpl
    __tpl = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'tpl'), 'tpl', '__httpwww_thalesgroup_comrttiPushPortSchedulesv1_IP_tpl', _ImportedBinding_darwinpush_xb_ct.TiplocType, required=True)
    __tpl._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 80, 2)
    __tpl._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 80, 2)
    
    tpl = property(__tpl.value, __tpl.set, None, 'TIPLOC')

    
    # Attribute act uses Python identifier act
    __act = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'act'), 'act', '__httpwww_thalesgroup_comrttiPushPortSchedulesv1_IP_act', _ImportedBinding_darwinpush_xb_ct.ActivityType, unicode_default='  ')
    __act._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 85, 2)
    __act._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 85, 2)
    
    act = property(__act.value, __act.set, None, 'Current Activity Codes')

    
    # Attribute planAct uses Python identifier planAct
    __planAct = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'planAct'), 'planAct', '__httpwww_thalesgroup_comrttiPushPortSchedulesv1_IP_planAct', _ImportedBinding_darwinpush_xb_ct.ActivityType)
    __planAct._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 90, 2)
    __planAct._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 90, 2)
    
    planAct = property(__planAct.value, __planAct.set, None, 'Planned Activity Codes (if different to current activities)')

    
    # Attribute can uses Python identifier can
    __can = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'can'), 'can', '__httpwww_thalesgroup_comrttiPushPortSchedulesv1_IP_can', pyxb.binding.datatypes.boolean, unicode_default='false')
    __can._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 95, 2)
    __can._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 95, 2)
    
    can = property(__can.value, __can.set, None, 'Cancelled')

    
    # Attribute pta uses Python identifier pta
    __pta = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'pta'), 'pta', '__httpwww_thalesgroup_comrttiPushPortSchedulesv1_IP_pta', _ImportedBinding_darwinpush_xb_ct.RTTITimeType)
    __pta._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 105, 2)
    __pta._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 105, 2)
    
    pta = property(__pta.value, __pta.set, None, 'Public Scheduled Time of Arrival')

    
    # Attribute ptd uses Python identifier ptd
    __ptd = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ptd'), 'ptd', '__httpwww_thalesgroup_comrttiPushPortSchedulesv1_IP_ptd', _ImportedBinding_darwinpush_xb_ct.RTTITimeType)
    __ptd._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 110, 2)
    __ptd._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 110, 2)
    
    ptd = property(__ptd.value, __ptd.set, None, 'Public Scheduled Time of Departure')

    
    # Attribute wta uses Python identifier wta
    __wta = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'wta'), 'wta', '__httpwww_thalesgroup_comrttiPushPortSchedulesv1_IP_wta', _ImportedBinding_darwinpush_xb_ct.WTimeType, required=True)
    __wta._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 160, 2)
    __wta._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 160, 2)
    
    wta = property(__wta.value, __wta.set, None, 'Working Scheduled Time of Arrival')

    
    # Attribute wtd uses Python identifier wtd
    __wtd = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'wtd'), 'wtd', '__httpwww_thalesgroup_comrttiPushPortSchedulesv1_IP_wtd', _ImportedBinding_darwinpush_xb_ct.WTimeType, required=True)
    __wtd._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 165, 2)
    __wtd._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 165, 2)
    
    wtd = property(__wtd.value, __wtd.set, None, 'Working Scheduled Time of Departure')

    
    # Attribute rdelay uses Python identifier rdelay
    __rdelay = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'rdelay'), 'rdelay', '__httpwww_thalesgroup_comrttiPushPortSchedulesv1_IP_rdelay', _ImportedBinding_darwinpush_xb_ct.DelayValueType, unicode_default='0')
    __rdelay._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 170, 2)
    __rdelay._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 170, 2)
    
    rdelay = property(__rdelay.value, __rdelay.set, None, "A delay value that is implied by a change to the service's route. This value has been added to the forecast lateness of the service at the previous schedule location when calculating the expected lateness of arrival at this location.")

    
    # Attribute fd uses Python identifier fd
    __fd = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'fd'), 'fd', '__httpwww_thalesgroup_comrttiPushPortSchedulesv1_IP_fd', _ImportedBinding_darwinpush_xb_ct.TiplocType)
    __fd._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 175, 2)
    __fd._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 175, 2)
    
    fd = property(__fd.value, __fd.set, None, 'TIPLOC of False Destination to be used at this location')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __tpl.name() : __tpl,
        __act.name() : __act,
        __planAct.name() : __planAct,
        __can.name() : __can,
        __pta.name() : __pta,
        __ptd.name() : __ptd,
        __wta.name() : __wta,
        __wtd.name() : __wtd,
        __rdelay.name() : __rdelay,
        __fd.name() : __fd
    })
Namespace.addCategoryObject('typeBinding', 'IP', IP)


# Complex type {http://www.thalesgroup.com/rtti/PushPort/Schedules/v1}OPIP with content type EMPTY
class OPIP (pyxb.binding.basis.complexTypeDefinition):
    """Defines an Operational Intermediate Calling Point"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'OPIP')
    _XSDLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 181, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute tpl uses Python identifier tpl
    __tpl = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'tpl'), 'tpl', '__httpwww_thalesgroup_comrttiPushPortSchedulesv1_OPIP_tpl', _ImportedBinding_darwinpush_xb_ct.TiplocType, required=True)
    __tpl._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 80, 2)
    __tpl._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 80, 2)
    
    tpl = property(__tpl.value, __tpl.set, None, 'TIPLOC')

    
    # Attribute act uses Python identifier act
    __act = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'act'), 'act', '__httpwww_thalesgroup_comrttiPushPortSchedulesv1_OPIP_act', _ImportedBinding_darwinpush_xb_ct.ActivityType, unicode_default='  ')
    __act._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 85, 2)
    __act._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 85, 2)
    
    act = property(__act.value, __act.set, None, 'Current Activity Codes')

    
    # Attribute planAct uses Python identifier planAct
    __planAct = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'planAct'), 'planAct', '__httpwww_thalesgroup_comrttiPushPortSchedulesv1_OPIP_planAct', _ImportedBinding_darwinpush_xb_ct.ActivityType)
    __planAct._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 90, 2)
    __planAct._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 90, 2)
    
    planAct = property(__planAct.value, __planAct.set, None, 'Planned Activity Codes (if different to current activities)')

    
    # Attribute can uses Python identifier can
    __can = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'can'), 'can', '__httpwww_thalesgroup_comrttiPushPortSchedulesv1_OPIP_can', pyxb.binding.datatypes.boolean, unicode_default='false')
    __can._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 95, 2)
    __can._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 95, 2)
    
    can = property(__can.value, __can.set, None, 'Cancelled')

    
    # Attribute wta uses Python identifier wta
    __wta = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'wta'), 'wta', '__httpwww_thalesgroup_comrttiPushPortSchedulesv1_OPIP_wta', _ImportedBinding_darwinpush_xb_ct.WTimeType, required=True)
    __wta._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 186, 2)
    __wta._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 186, 2)
    
    wta = property(__wta.value, __wta.set, None, 'Working Scheduled Time of Arrival')

    
    # Attribute wtd uses Python identifier wtd
    __wtd = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'wtd'), 'wtd', '__httpwww_thalesgroup_comrttiPushPortSchedulesv1_OPIP_wtd', _ImportedBinding_darwinpush_xb_ct.WTimeType, required=True)
    __wtd._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 191, 2)
    __wtd._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 191, 2)
    
    wtd = property(__wtd.value, __wtd.set, None, 'Working Scheduled Time of Departure')

    
    # Attribute rdelay uses Python identifier rdelay
    __rdelay = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'rdelay'), 'rdelay', '__httpwww_thalesgroup_comrttiPushPortSchedulesv1_OPIP_rdelay', _ImportedBinding_darwinpush_xb_ct.DelayValueType, unicode_default='0')
    __rdelay._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 196, 2)
    __rdelay._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 196, 2)
    
    rdelay = property(__rdelay.value, __rdelay.set, None, "A delay value that is implied by a change to the service's route. This value has been added to the forecast lateness of the service at the previous schedule location when calculating the expected lateness of arrival at this location.")

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __tpl.name() : __tpl,
        __act.name() : __act,
        __planAct.name() : __planAct,
        __can.name() : __can,
        __wta.name() : __wta,
        __wtd.name() : __wtd,
        __rdelay.name() : __rdelay
    })
Namespace.addCategoryObject('typeBinding', 'OPIP', OPIP)


# Complex type {http://www.thalesgroup.com/rtti/PushPort/Schedules/v1}PP with content type EMPTY
class PP (pyxb.binding.basis.complexTypeDefinition):
    """Defines an Intermediate Passing Point"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PP')
    _XSDLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 202, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute tpl uses Python identifier tpl
    __tpl = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'tpl'), 'tpl', '__httpwww_thalesgroup_comrttiPushPortSchedulesv1_PP_tpl', _ImportedBinding_darwinpush_xb_ct.TiplocType, required=True)
    __tpl._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 80, 2)
    __tpl._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 80, 2)
    
    tpl = property(__tpl.value, __tpl.set, None, 'TIPLOC')

    
    # Attribute act uses Python identifier act
    __act = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'act'), 'act', '__httpwww_thalesgroup_comrttiPushPortSchedulesv1_PP_act', _ImportedBinding_darwinpush_xb_ct.ActivityType, unicode_default='  ')
    __act._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 85, 2)
    __act._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 85, 2)
    
    act = property(__act.value, __act.set, None, 'Current Activity Codes')

    
    # Attribute planAct uses Python identifier planAct
    __planAct = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'planAct'), 'planAct', '__httpwww_thalesgroup_comrttiPushPortSchedulesv1_PP_planAct', _ImportedBinding_darwinpush_xb_ct.ActivityType)
    __planAct._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 90, 2)
    __planAct._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 90, 2)
    
    planAct = property(__planAct.value, __planAct.set, None, 'Planned Activity Codes (if different to current activities)')

    
    # Attribute can uses Python identifier can
    __can = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'can'), 'can', '__httpwww_thalesgroup_comrttiPushPortSchedulesv1_PP_can', pyxb.binding.datatypes.boolean, unicode_default='false')
    __can._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 95, 2)
    __can._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 95, 2)
    
    can = property(__can.value, __can.set, None, 'Cancelled')

    
    # Attribute wtp uses Python identifier wtp
    __wtp = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'wtp'), 'wtp', '__httpwww_thalesgroup_comrttiPushPortSchedulesv1_PP_wtp', _ImportedBinding_darwinpush_xb_ct.WTimeType, required=True)
    __wtp._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 207, 2)
    __wtp._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 207, 2)
    
    wtp = property(__wtp.value, __wtp.set, None, 'Working Scheduled Time of Passing')

    
    # Attribute rdelay uses Python identifier rdelay
    __rdelay = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'rdelay'), 'rdelay', '__httpwww_thalesgroup_comrttiPushPortSchedulesv1_PP_rdelay', _ImportedBinding_darwinpush_xb_ct.DelayValueType, unicode_default='0')
    __rdelay._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 212, 2)
    __rdelay._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 212, 2)
    
    rdelay = property(__rdelay.value, __rdelay.set, None, "A delay value that is implied by a change to the service's route. This value has been added to the forecast lateness of the service at the previous schedule location when calculating the expected lateness of passing this location.")

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __tpl.name() : __tpl,
        __act.name() : __act,
        __planAct.name() : __planAct,
        __can.name() : __can,
        __wtp.name() : __wtp,
        __rdelay.name() : __rdelay
    })
Namespace.addCategoryObject('typeBinding', 'PP', PP)


# Complex type {http://www.thalesgroup.com/rtti/PushPort/Schedules/v1}DT with content type EMPTY
class DT (pyxb.binding.basis.complexTypeDefinition):
    """Defines a Passenger Destination Calling point"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DT')
    _XSDLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 218, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute tpl uses Python identifier tpl
    __tpl = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'tpl'), 'tpl', '__httpwww_thalesgroup_comrttiPushPortSchedulesv1_DT_tpl', _ImportedBinding_darwinpush_xb_ct.TiplocType, required=True)
    __tpl._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 80, 2)
    __tpl._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 80, 2)
    
    tpl = property(__tpl.value, __tpl.set, None, 'TIPLOC')

    
    # Attribute act uses Python identifier act
    __act = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'act'), 'act', '__httpwww_thalesgroup_comrttiPushPortSchedulesv1_DT_act', _ImportedBinding_darwinpush_xb_ct.ActivityType, unicode_default='  ')
    __act._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 85, 2)
    __act._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 85, 2)
    
    act = property(__act.value, __act.set, None, 'Current Activity Codes')

    
    # Attribute planAct uses Python identifier planAct
    __planAct = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'planAct'), 'planAct', '__httpwww_thalesgroup_comrttiPushPortSchedulesv1_DT_planAct', _ImportedBinding_darwinpush_xb_ct.ActivityType)
    __planAct._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 90, 2)
    __planAct._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 90, 2)
    
    planAct = property(__planAct.value, __planAct.set, None, 'Planned Activity Codes (if different to current activities)')

    
    # Attribute can uses Python identifier can
    __can = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'can'), 'can', '__httpwww_thalesgroup_comrttiPushPortSchedulesv1_DT_can', pyxb.binding.datatypes.boolean, unicode_default='false')
    __can._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 95, 2)
    __can._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 95, 2)
    
    can = property(__can.value, __can.set, None, 'Cancelled')

    
    # Attribute pta uses Python identifier pta
    __pta = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'pta'), 'pta', '__httpwww_thalesgroup_comrttiPushPortSchedulesv1_DT_pta', _ImportedBinding_darwinpush_xb_ct.RTTITimeType)
    __pta._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 105, 2)
    __pta._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 105, 2)
    
    pta = property(__pta.value, __pta.set, None, 'Public Scheduled Time of Arrival')

    
    # Attribute ptd uses Python identifier ptd
    __ptd = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ptd'), 'ptd', '__httpwww_thalesgroup_comrttiPushPortSchedulesv1_DT_ptd', _ImportedBinding_darwinpush_xb_ct.RTTITimeType)
    __ptd._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 110, 2)
    __ptd._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 110, 2)
    
    ptd = property(__ptd.value, __ptd.set, None, 'Public Scheduled Time of Departure')

    
    # Attribute wta uses Python identifier wta
    __wta = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'wta'), 'wta', '__httpwww_thalesgroup_comrttiPushPortSchedulesv1_DT_wta', _ImportedBinding_darwinpush_xb_ct.WTimeType, required=True)
    __wta._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 224, 2)
    __wta._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 224, 2)
    
    wta = property(__wta.value, __wta.set, None, 'Working Scheduled Time of Arrival')

    
    # Attribute wtd uses Python identifier wtd
    __wtd = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'wtd'), 'wtd', '__httpwww_thalesgroup_comrttiPushPortSchedulesv1_DT_wtd', _ImportedBinding_darwinpush_xb_ct.WTimeType)
    __wtd._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 229, 2)
    __wtd._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 229, 2)
    
    wtd = property(__wtd.value, __wtd.set, None, 'Working Scheduled Time of Departure')

    
    # Attribute rdelay uses Python identifier rdelay
    __rdelay = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'rdelay'), 'rdelay', '__httpwww_thalesgroup_comrttiPushPortSchedulesv1_DT_rdelay', _ImportedBinding_darwinpush_xb_ct.DelayValueType, unicode_default='0')
    __rdelay._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 234, 2)
    __rdelay._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 234, 2)
    
    rdelay = property(__rdelay.value, __rdelay.set, None, "A delay value that is implied by a change to the service's route. This value has been added to the forecast lateness of the service at the previous schedule location when calculating the expected lateness of arrival at this location.")

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __tpl.name() : __tpl,
        __act.name() : __act,
        __planAct.name() : __planAct,
        __can.name() : __can,
        __pta.name() : __pta,
        __ptd.name() : __ptd,
        __wta.name() : __wta,
        __wtd.name() : __wtd,
        __rdelay.name() : __rdelay
    })
Namespace.addCategoryObject('typeBinding', 'DT', DT)


# Complex type {http://www.thalesgroup.com/rtti/PushPort/Schedules/v1}OPDT with content type EMPTY
class OPDT (pyxb.binding.basis.complexTypeDefinition):
    """Defines an Operational Destination Calling point"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'OPDT')
    _XSDLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 240, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute tpl uses Python identifier tpl
    __tpl = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'tpl'), 'tpl', '__httpwww_thalesgroup_comrttiPushPortSchedulesv1_OPDT_tpl', _ImportedBinding_darwinpush_xb_ct.TiplocType, required=True)
    __tpl._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 80, 2)
    __tpl._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 80, 2)
    
    tpl = property(__tpl.value, __tpl.set, None, 'TIPLOC')

    
    # Attribute act uses Python identifier act
    __act = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'act'), 'act', '__httpwww_thalesgroup_comrttiPushPortSchedulesv1_OPDT_act', _ImportedBinding_darwinpush_xb_ct.ActivityType, unicode_default='  ')
    __act._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 85, 2)
    __act._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 85, 2)
    
    act = property(__act.value, __act.set, None, 'Current Activity Codes')

    
    # Attribute planAct uses Python identifier planAct
    __planAct = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'planAct'), 'planAct', '__httpwww_thalesgroup_comrttiPushPortSchedulesv1_OPDT_planAct', _ImportedBinding_darwinpush_xb_ct.ActivityType)
    __planAct._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 90, 2)
    __planAct._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 90, 2)
    
    planAct = property(__planAct.value, __planAct.set, None, 'Planned Activity Codes (if different to current activities)')

    
    # Attribute can uses Python identifier can
    __can = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'can'), 'can', '__httpwww_thalesgroup_comrttiPushPortSchedulesv1_OPDT_can', pyxb.binding.datatypes.boolean, unicode_default='false')
    __can._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 95, 2)
    __can._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 95, 2)
    
    can = property(__can.value, __can.set, None, 'Cancelled')

    
    # Attribute wta uses Python identifier wta
    __wta = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'wta'), 'wta', '__httpwww_thalesgroup_comrttiPushPortSchedulesv1_OPDT_wta', _ImportedBinding_darwinpush_xb_ct.WTimeType, required=True)
    __wta._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 245, 2)
    __wta._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 245, 2)
    
    wta = property(__wta.value, __wta.set, None, 'Working Scheduled Time of Arrival')

    
    # Attribute wtd uses Python identifier wtd
    __wtd = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'wtd'), 'wtd', '__httpwww_thalesgroup_comrttiPushPortSchedulesv1_OPDT_wtd', _ImportedBinding_darwinpush_xb_ct.WTimeType)
    __wtd._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 250, 2)
    __wtd._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 250, 2)
    
    wtd = property(__wtd.value, __wtd.set, None, 'Working Scheduled Time of Departure')

    
    # Attribute rdelay uses Python identifier rdelay
    __rdelay = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'rdelay'), 'rdelay', '__httpwww_thalesgroup_comrttiPushPortSchedulesv1_OPDT_rdelay', _ImportedBinding_darwinpush_xb_ct.DelayValueType, unicode_default='0')
    __rdelay._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 255, 2)
    __rdelay._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 255, 2)
    
    rdelay = property(__rdelay.value, __rdelay.set, None, "A delay value that is implied by a change to the service's route. This value has been added to the forecast lateness of the service at the previous schedule location when calculating the expected lateness of arrival at this location.")

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __tpl.name() : __tpl,
        __act.name() : __act,
        __planAct.name() : __planAct,
        __can.name() : __can,
        __wta.name() : __wta,
        __wtd.name() : __wtd,
        __rdelay.name() : __rdelay
    })
Namespace.addCategoryObject('typeBinding', 'OPDT', OPDT)


# Complex type {http://www.thalesgroup.com/rtti/PushPort/Schedules/v1}Schedule with content type ELEMENT_ONLY
class Schedule (pyxb.binding.basis.complexTypeDefinition):
    """Train Schedule"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Schedule')
    _XSDLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 261, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.thalesgroup.com/rtti/PushPort/Schedules/v1}OR uses Python identifier OR
    __OR = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'OR'), 'OR', '__httpwww_thalesgroup_comrttiPushPortSchedulesv1_Schedule_httpwww_thalesgroup_comrttiPushPortSchedulesv1OR', True, pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 267, 4), )

    
    OR = property(__OR.value, __OR.set, None, None)

    
    # Element {http://www.thalesgroup.com/rtti/PushPort/Schedules/v1}OPOR uses Python identifier OPOR
    __OPOR = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'OPOR'), 'OPOR', '__httpwww_thalesgroup_comrttiPushPortSchedulesv1_Schedule_httpwww_thalesgroup_comrttiPushPortSchedulesv1OPOR', True, pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 268, 4), )

    
    OPOR = property(__OPOR.value, __OPOR.set, None, None)

    
    # Element {http://www.thalesgroup.com/rtti/PushPort/Schedules/v1}IP uses Python identifier IP
    __IP = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'IP'), 'IP', '__httpwww_thalesgroup_comrttiPushPortSchedulesv1_Schedule_httpwww_thalesgroup_comrttiPushPortSchedulesv1IP', True, pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 269, 4), )

    
    IP = property(__IP.value, __IP.set, None, None)

    
    # Element {http://www.thalesgroup.com/rtti/PushPort/Schedules/v1}OPIP uses Python identifier OPIP
    __OPIP = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'OPIP'), 'OPIP', '__httpwww_thalesgroup_comrttiPushPortSchedulesv1_Schedule_httpwww_thalesgroup_comrttiPushPortSchedulesv1OPIP', True, pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 270, 4), )

    
    OPIP = property(__OPIP.value, __OPIP.set, None, None)

    
    # Element {http://www.thalesgroup.com/rtti/PushPort/Schedules/v1}PP uses Python identifier PP
    __PP = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PP'), 'PP', '__httpwww_thalesgroup_comrttiPushPortSchedulesv1_Schedule_httpwww_thalesgroup_comrttiPushPortSchedulesv1PP', True, pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 271, 4), )

    
    PP = property(__PP.value, __PP.set, None, None)

    
    # Element {http://www.thalesgroup.com/rtti/PushPort/Schedules/v1}DT uses Python identifier DT
    __DT = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DT'), 'DT', '__httpwww_thalesgroup_comrttiPushPortSchedulesv1_Schedule_httpwww_thalesgroup_comrttiPushPortSchedulesv1DT', True, pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 272, 4), )

    
    DT = property(__DT.value, __DT.set, None, None)

    
    # Element {http://www.thalesgroup.com/rtti/PushPort/Schedules/v1}OPDT uses Python identifier OPDT
    __OPDT = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'OPDT'), 'OPDT', '__httpwww_thalesgroup_comrttiPushPortSchedulesv1_Schedule_httpwww_thalesgroup_comrttiPushPortSchedulesv1OPDT', True, pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 273, 4), )

    
    OPDT = property(__OPDT.value, __OPDT.set, None, None)

    
    # Element {http://www.thalesgroup.com/rtti/PushPort/Schedules/v1}cancelReason uses Python identifier cancelReason
    __cancelReason = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'cancelReason'), 'cancelReason', '__httpwww_thalesgroup_comrttiPushPortSchedulesv1_Schedule_httpwww_thalesgroup_comrttiPushPortSchedulesv1cancelReason', False, pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 275, 3), )

    
    cancelReason = property(__cancelReason.value, __cancelReason.set, None, None)

    
    # Attribute rid uses Python identifier rid
    __rid = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'rid'), 'rid', '__httpwww_thalesgroup_comrttiPushPortSchedulesv1_Schedule_rid', _ImportedBinding_darwinpush_xb_ct.RIDType, required=True)
    __rid._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 277, 2)
    __rid._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 277, 2)
    
    rid = property(__rid.value, __rid.set, None, 'RTTI unique Train ID')

    
    # Attribute uid uses Python identifier uid
    __uid = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uid'), 'uid', '__httpwww_thalesgroup_comrttiPushPortSchedulesv1_Schedule_uid', _ImportedBinding_darwinpush_xb_ct.UIDType, required=True)
    __uid._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 282, 2)
    __uid._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 282, 2)
    
    uid = property(__uid.value, __uid.set, None, 'Train UID')

    
    # Attribute trainId uses Python identifier trainId
    __trainId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'trainId'), 'trainId', '__httpwww_thalesgroup_comrttiPushPortSchedulesv1_Schedule_trainId', _ImportedBinding_darwinpush_xb_ct.TrainIdType, required=True)
    __trainId._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 287, 2)
    __trainId._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 287, 2)
    
    trainId = property(__trainId.value, __trainId.set, None, 'Train ID (Headcode)')

    
    # Attribute ssd uses Python identifier ssd
    __ssd = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ssd'), 'ssd', '__httpwww_thalesgroup_comrttiPushPortSchedulesv1_Schedule_ssd', _ImportedBinding_darwinpush_xb_ct.RTTIDateType, required=True)
    __ssd._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 292, 2)
    __ssd._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 292, 2)
    
    ssd = property(__ssd.value, __ssd.set, None, 'Scheduled Start Date')

    
    # Attribute toc uses Python identifier toc
    __toc = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'toc'), 'toc', '__httpwww_thalesgroup_comrttiPushPortSchedulesv1_Schedule_toc', _ImportedBinding_darwinpush_xb_ct.TOCType, required=True)
    __toc._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 297, 2)
    __toc._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 297, 2)
    
    toc = property(__toc.value, __toc.set, None, 'ATOC Code')

    
    # Attribute status uses Python identifier status
    __status = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'status'), 'status', '__httpwww_thalesgroup_comrttiPushPortSchedulesv1_Schedule_status', _ImportedBinding_darwinpush_xb_ct.CIFTrainStatusType, unicode_default='P')
    __status._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 302, 2)
    __status._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 302, 2)
    
    status = property(__status.value, __status.set, None, 'Type of service, i.e. Train/Bus/Ship.')

    
    # Attribute trainCat uses Python identifier trainCat
    __trainCat = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'trainCat'), 'trainCat', '__httpwww_thalesgroup_comrttiPushPortSchedulesv1_Schedule_trainCat', _ImportedBinding_darwinpush_xb_ct.CIFTrainCategoryType, unicode_default='OO')
    __trainCat._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 307, 2)
    __trainCat._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 307, 2)
    
    trainCat = property(__trainCat.value, __trainCat.set, None, 'Category of service.')

    
    # Attribute isPassengerSvc uses Python identifier isPassengerSvc
    __isPassengerSvc = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'isPassengerSvc'), 'isPassengerSvc', '__httpwww_thalesgroup_comrttiPushPortSchedulesv1_Schedule_isPassengerSvc', pyxb.binding.datatypes.boolean, unicode_default='true')
    __isPassengerSvc._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 312, 2)
    __isPassengerSvc._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 312, 2)
    
    isPassengerSvc = property(__isPassengerSvc.value, __isPassengerSvc.set, None, 'True if Darwin classifies the train category as a passenger service.')

    
    # Attribute isActive uses Python identifier isActive
    __isActive = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'isActive'), 'isActive', '__httpwww_thalesgroup_comrttiPushPortSchedulesv1_Schedule_isActive', pyxb.binding.datatypes.boolean, unicode_default='true')
    __isActive._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 317, 2)
    __isActive._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 317, 2)
    
    isActive = property(__isActive.value, __isActive.set, None, 'Indicates if this service is active in Darwin. Note that schedules should be assumed to be inactive until a message is received to indicate otherwise.')

    
    # Attribute deleted uses Python identifier deleted
    __deleted = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'deleted'), 'deleted', '__httpwww_thalesgroup_comrttiPushPortSchedulesv1_Schedule_deleted', pyxb.binding.datatypes.boolean, unicode_default='false')
    __deleted._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 322, 2)
    __deleted._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 322, 2)
    
    deleted = property(__deleted.value, __deleted.set, None, 'Service has been deleted and should not be used/displayed.')

    
    # Attribute isCharter uses Python identifier isCharter
    __isCharter = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'isCharter'), 'isCharter', '__httpwww_thalesgroup_comrttiPushPortSchedulesv1_Schedule_isCharter', pyxb.binding.datatypes.boolean, unicode_default='false')
    __isCharter._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 327, 2)
    __isCharter._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 327, 2)
    
    isCharter = property(__isCharter.value, __isCharter.set, None, 'Indicates if this service is a charter service.')

    _ElementMap.update({
        __OR.name() : __OR,
        __OPOR.name() : __OPOR,
        __IP.name() : __IP,
        __OPIP.name() : __OPIP,
        __PP.name() : __PP,
        __DT.name() : __DT,
        __OPDT.name() : __OPDT,
        __cancelReason.name() : __cancelReason
    })
    _AttributeMap.update({
        __rid.name() : __rid,
        __uid.name() : __uid,
        __trainId.name() : __trainId,
        __ssd.name() : __ssd,
        __toc.name() : __toc,
        __status.name() : __status,
        __trainCat.name() : __trainCat,
        __isPassengerSvc.name() : __isPassengerSvc,
        __isActive.name() : __isActive,
        __deleted.name() : __deleted,
        __isCharter.name() : __isCharter
    })
Namespace.addCategoryObject('typeBinding', 'Schedule', Schedule)


# Complex type {http://www.thalesgroup.com/rtti/PushPort/Schedules/v1}DeactivatedSchedule with content type EMPTY
class DeactivatedSchedule (pyxb.binding.basis.complexTypeDefinition):
    """Notification that a Train Schedule is now deactivated in Darwin."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DeactivatedSchedule')
    _XSDLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 333, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute rid uses Python identifier rid
    __rid = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'rid'), 'rid', '__httpwww_thalesgroup_comrttiPushPortSchedulesv1_DeactivatedSchedule_rid', _ImportedBinding_darwinpush_xb_ct.RIDType, required=True)
    __rid._DeclarationLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 337, 2)
    __rid._UseLocation = pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 337, 2)
    
    rid = property(__rid.value, __rid.set, None, 'RTTI unique Train ID')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __rid.name() : __rid
    })
Namespace.addCategoryObject('typeBinding', 'DeactivatedSchedule', DeactivatedSchedule)




Association._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'main'), AssocService, scope=Association, documentation='The through, previous working or link-to service', location=pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 44, 3)))

Association._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'assoc'), AssocService, scope=Association, documentation='The starting, terminating, subsequent working or link-from service', location=pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 49, 3)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Association._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'main')), pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 44, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Association._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'assoc')), pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 49, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Association._Automaton = _BuildAutomaton()




Schedule._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OR'), OR, scope=Schedule, location=pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 267, 4)))

Schedule._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OPOR'), OPOR, scope=Schedule, location=pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 268, 4)))

Schedule._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'IP'), IP, scope=Schedule, location=pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 269, 4)))

Schedule._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OPIP'), OPIP, scope=Schedule, location=pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 270, 4)))

Schedule._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PP'), PP, scope=Schedule, location=pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 271, 4)))

Schedule._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DT'), DT, scope=Schedule, location=pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 272, 4)))

Schedule._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OPDT'), OPDT, scope=Schedule, location=pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 273, 4)))

Schedule._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'cancelReason'), _ImportedBinding_darwinpush_xb_ct.DisruptionReasonType, scope=Schedule, location=pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 275, 3)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=2, max=None, metadata=pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 266, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 275, 3))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Schedule._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'OR')), pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 267, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Schedule._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'OPOR')), pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 268, 4))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Schedule._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'IP')), pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 269, 4))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Schedule._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'OPIP')), pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 270, 4))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Schedule._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PP')), pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 271, 4))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Schedule._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DT')), pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 272, 4))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Schedule._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'OPDT')), pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 273, 4))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(Schedule._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'cancelReason')), pyxb.utils.utility.Location('/home/gberg/code/src/fstr/darwinpush/xsd/rttiPPTSchedules_v1.xsd', 275, 3))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Schedule._Automaton = _BuildAutomaton_()

