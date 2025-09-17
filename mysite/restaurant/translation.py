from modeltranslation.translator import register, TranslationOptions
from .models import Restaurant, Category, MenuItem


@register(Restaurant)
class RestaurantTranslationOptions(TranslationOptions):
    fields = ('name', 'address',)


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(MenuItem)
class MenuItemTranslationOptions(TranslationOptions):
    fields = ('name', 'description',)
