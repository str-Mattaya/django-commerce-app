from django.contrib import admin

from store.models import Customer, Product


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['username', 'name', 'is_superuser']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass
