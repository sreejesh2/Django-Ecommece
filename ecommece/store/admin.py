from django.contrib import admin
from .models import ProductCategory,Product,Gender,ProductGender,ProductPrice,Size,ProductSize,ProductSizePrice,Color,ProductColor,ProductImage

# Register your models here.
admin.site.register(ProductCategory)
admin.site.register(Product)
admin.site.register(Gender)
admin.site.register(ProductGender)
admin.site.register(ProductPrice)
admin.site.register(Size)
admin.site.register(ProductSize)
admin.site.register(ProductSizePrice)
admin.site.register(Color)
admin.site.register(ProductColor)
admin.site.register(ProductImage)
