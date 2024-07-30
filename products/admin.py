from django.contrib import admin

from products.models import Category, Subcategory, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'preview', ]


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'preview', 'category',]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'slug', 'preview_small',
                    'preview_middle', 'preview_big', 'price', 'subcategory']
