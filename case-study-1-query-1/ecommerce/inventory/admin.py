from django.contrib import admin
from .models import (
    Attribute,
    AttributeValue,
    Category,
    Image,
    Inventory,
    Product,
    StockControl,
)

# admin.site.register(Category)
# admin.site.register(Attribute)
# admin.site.register(AttributeValue)
# admin.site.register(Image)
# admin.site.register(Inventory)
# admin.site.register(Product)
# admin.site.register(StockControl)

class ProductImageInline(admin.TabularInline):
    model = Image

class AttributeValueInline(admin.TabularInline):
    model = AttributeValue

class StockControlInline(admin.TabularInline):
    model = StockControl

@admin.register(Inventory)
class ProductInventoryAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline, StockControlInline]

@admin.register(Attribute)
class ProductAdmin(admin.ModelAdmin):
    inlines = [
        AttributeValueInline,
    ]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        "slug": ("name",),
    }

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        "slug": ("name",),
    }