from modeltranslation.translator import translator, TranslationOptions

from .models import Product, Category


class ProductTranslationOptions(TranslationOptions):
    fields = ('title',  'category')


translator.register(Product, ProductTranslationOptions)


class CategoryTranslationOptions(TranslationOptions):
    fields = 'title'


translator.register(Category, CategoryTranslationOptions)
