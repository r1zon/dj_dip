from django.contrib import admin

from phones.models import Product, Review, Order, ProductCounts, ProductType


class ProductAdmin(admin.ModelAdmin):
    pass

class ProductTypeAdmin(admin.ModelAdmin):
    pass

class ReviewAdmin(admin.ModelAdmin):
    pass

class RelationshipInline(admin.TabularInline):
    model = ProductCounts

class OrderAdmin(admin.ModelAdmin):
    inlines = [RelationshipInline]

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductType, ProductTypeAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Order, OrderAdmin)
