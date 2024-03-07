from django.contrib import admin
from .models import Product,ProductImage,Category,City

admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(Category)
admin.site.register(City)
