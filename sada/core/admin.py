from django.contrib import admin

# Register your models here.
from .models import Product, Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category', 'created_at', 'updated_at', 'is_published']
    search_fields = ('id', 'title')
    list_filter = ('is_published', 'category')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    prepopulated_fields = {'slug': ('title',)}
    list_display_links = ('id', 'title')

