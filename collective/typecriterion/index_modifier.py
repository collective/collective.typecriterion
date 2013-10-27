# -*- coding: utf8 -*-

from zope.interface import implements
from plone.app.querystring.interfaces import IParsedQueryIndexModifier
from plone.registry.interfaces import IRegistry 
from collective.typecriterion.interfaces import ITypesCriterionSettings


class GeneralTypeIndexModifier(object):
    """When querying for general_type you are asking for a set of portal_type"""

    implements(IParsedQueryIndexModifier)

    def __call__(self, value):
        import pdb;pdb.set_trace()
        registry = queryUtility(IRegistry)
        settings = registry.forInterface(ITypesCriterionSettings, check=False)
        for conf in settings.type_criterion_defined:
            pass
        return ('portal_type', value)
