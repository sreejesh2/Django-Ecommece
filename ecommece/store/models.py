from django.db import models
from accounts.models import CustomUser


# Create your models here.
class ProductCategory(models.Model):
    category_name=models.CharField(max_length=100,unique=True)
    image=models.ImageField(upload_to="category_img",null=True,blank=True)
    is_active=models.BooleanField(default=True)
    created_date=models.DateTimeField(auto_now_add=True)
    created_by=models.ForeignKey(CustomUser,on_delete=models.DO_NOTHING,related_name='category_created_user')
    is_modified=models.BooleanField(default=False)
    is_cancelled=models.BooleanField(default=False)

    def __str__(self):
        return self.category_name

class Product(models.Model):
    name=models.CharField(max_length=200)
    category=models.ForeignKey(ProductCategory,on_delete=models.CASCADE,related_name='cat_name')
    description=models.CharField(max_length=500)
    is_active=models.BooleanField(default=True)
    is_trending=models.BooleanField(default=False)
    created_date=models.DateTimeField(auto_now_add=True)
    created_by=models.ForeignKey(CustomUser,on_delete=models.DO_NOTHING,related_name='product_created_user')
    is_modified=models.BooleanField(default=False)
    is_cancelled=models.BooleanField(default=False)
    
    @property
    def get_product_image(self):
        im=ProductImage.objects.filter(product=self)
        for i in im:
            print(i)
        return i
    @property
    def get_price(self):
        return ProductPrice.objects.get(product=self)
    @property
    def get_img(self):
        return ProductImage.objects.filter(product=self)
    @property
    def get_colors(self):
        return ProductColor.objects.filter(product=self)
    
    @property
    def get_size(self):
        return ProductSize.objects.filter(product=self)

    def __str__(self):
        return self.name
    



class ProductPrice(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE)    
    product_price=models.PositiveIntegerField()
    sale_price=models.PositiveIntegerField()
    created_date=models.DateTimeField(auto_now_add=True)
    created_by=models.ForeignKey(CustomUser,on_delete=models.DO_NOTHING,related_name='product_price_created_user')
    is_modified=models.BooleanField(default=False)
    # modified_by=models.ForeignKey(CustomUser,on_delete=models.DO_NOTHING,related_name='product_price_modified_user')
    is_cancelled=models.BooleanField(default=False)

    def __str__(self):
        p=str(self.product_price)
        return p

class Size(models.Model):
    size=models.CharField(max_length=100,unique=True)
    is_active=models.BooleanField(default=True)
    created_date=models.DateTimeField(auto_now_add=True)
    created_by=models.ForeignKey(CustomUser,on_delete=models.DO_NOTHING,related_name='size_created_user')
    is_modified=models.BooleanField(default=False)
    # modified_by=models.ForeignKey(CustomUser,on_delete=models.DO_NOTHING,related_name='size_modified_user',null=True,blank=True)
    is_cancelled=models.BooleanField(default=False)
    

    def __str__(self):
        return self.size
  


class ProductSize(models.Model):
    product=models.ForeignKey(Product,on_delete=models.DO_NOTHING)
    size=models.ForeignKey(Size,models.DO_NOTHING,related_name="size_name")
    created_date=models.DateTimeField(auto_now_add=True)
    created_by=models.ForeignKey(CustomUser,models.DO_NOTHING,related_name='product_size_created_user')
    is_cancelled=models.BooleanField(default=False)
    def __str__(self):
        return f"{self.product.name} - {self.size}"
    
    @property
    def get_product_size_price(self):
        qs=ProductSizePrice.objects.get(product_size=self)
      
        return qs.sale_price


class ProductSizePrice(models.Model):
    product_size=models.ForeignKey(ProductSize,on_delete=models.DO_NOTHING)
    sale_price=models.PositiveIntegerField()
    created_by=models.ForeignKey(CustomUser,models.DO_NOTHING,related_name='product_size_price_created_user')
    is_cancelled=models.BooleanField(default=False)
    def __str__(self):
        return f"{self.product_size.product.name} - {self.product_size.size.size}-{self.sale_price}"
    

class Color(models.Model):
    color=models.CharField( max_length=50,unique=True)
    is_active=models.BooleanField(default=True)
    created_date=models.DateTimeField(auto_now_add=True)
    created_by=models.ForeignKey(CustomUser,on_delete=models.DO_NOTHING,related_name='color_created_user')
    is_cancelled=models.BooleanField(default=False)

    def __str__(self):
        return self.color
    


class ProductColor(models.Model):
    color=models.ForeignKey(Color,on_delete=models.DO_NOTHING)
    product=models.ForeignKey(Product,on_delete=models.DO_NOTHING)
    is_active=models.BooleanField(default=True)
    created_date=models.DateTimeField(auto_now_add=True)
    created_by=models.ForeignKey(CustomUser,on_delete=models.DO_NOTHING,related_name='product_color_created_user')
    is_cancelled=models.BooleanField(default=False)

    def __str__(self):
        return f"{self.product.name} - {self.color.color}"

class ProductImage(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    image=models.ImageField(upload_to="product_images",null=True,blank=True)