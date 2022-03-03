from django.contrib import admin
from parler.admin import TranslatableAdmin
from store.models import Product


class ProductAdmin(TranslatableAdmin):
    list_display = ('product_name', 'price', 'category', 'modified_date', 'is_available')

    def get_prepopulated_fields(self, request, obj=None):
        return {
            'slug': ('product_name',)
        }

admin.site.register(Product, ProductAdmin)