from django.contrib import admin

from products.models import Product, store

admin.site.register(Product)
admin.site.register(store)
