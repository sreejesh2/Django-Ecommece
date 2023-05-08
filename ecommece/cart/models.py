from django.db import models

from accounts.models import CustomUser
from store.models import Product,ProductSize,ProductColor,ProductPrice,ProductSizePrice

# Create your models here.


class Cart(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cartitem')
    # product_price = models.ForeignKey(ProductPrice, on_delete=models.SET_NULL, related_name='price', null=True, blank=True)
    product_size = models.ForeignKey(ProductSize, on_delete=models.SET_NULL, null=True, blank=True)
    product_color = models.ForeignKey(ProductColor, on_delete=models.SET_NULL, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    is_cancelled = models.BooleanField(default=False)
    quantity = models.PositiveIntegerField(default=1)
    price=models.FloatField()
    # productSizePrice = models.ForeignKey(ProductSizePrice, on_delete=models.SET_NULL,null=True, blank=True)

   