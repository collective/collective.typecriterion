# -*- coding: utf-8 -*-

from zope.interface import implements
from zope.component import queryUtility
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from plone.registry.interfaces import IRegistry
from collective.typecriterion.interfaces import ITypesCriterionSettings
from collective.typecriterion import _

class TypeCriterionDefined(object):
    """Vocabulary for getting all defined type criterion
    """
    implements(IVocabularyFactory)

    def __call__(self, context):
        
        registry = queryUtility(IRegistry)
        settings = registry.forInterface(ITypesCriterionSettings, check=False)
        terms = []
        
        for conf in settings.type_criterion_defined:
            msgid = _(conf.type_name)
            terms.append(SimpleTerm(conf.type_name, msgid))
        
        return SimpleVocabulary(terms)

typeCriterionDefinedVocabularyFactory = TypeCriterionDefined()