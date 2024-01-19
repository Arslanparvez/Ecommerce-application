from django.contrib import admin
from .models import product

# Register your models here.

# admin.site.register(product)


class ProductAdmin(admin.ModelAdmin):
    list_display=['id','name','price','pdetails','cat','is_active']
    list_filter=['cat','is_active']


admin.site.register(product,ProductAdmin)