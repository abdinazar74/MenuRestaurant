from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Restaurant, Category, MenuItem, Order

@admin.register(Restaurant)
class RestaurantAdmin(TranslationAdmin):
    list_display = ("name", "address", "phone", "created_at")

@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    list_display = ("name",)

@admin.register(MenuItem)
class MenuItemAdmin(TranslationAdmin):
    list_display = ("name", "restaurant", "price", "is_available")

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "restaurant", "customer_name", "status", "created_at")

