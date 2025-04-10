from django.contrib import admin
from console.models import Product, Blog, Product_category, Product_subcategory,Product_color
# Register your models here.
admin.site.register(Product)
admin.site.register(Blog)
admin.site.register(Product_category)
admin.site.register(Product_subcategory)
admin.site.register(Product_color)
