from django.db import models
from django.contrib.auth.models import User

# # Create your models here.

# class ProductCategory(models.Model):
#     category_name=models.CharField(max_length=100,unique=True)
#     image=models.ImageField(upload_to="category_img",null=True,blank=True)
#     is_active=models.BooleanField(default=True)
#     created_date=models.DateTimeField(auto_now_add=True)
#     created_by=models.ForeignKey(User,on_delete=models.DO_NOTHING)
#     is_modified=models.BooleanField(default=False)
#     is_cancelled=models.BooleanField(default=False)

# class Product(models.Model):
#     name=models.CharField(max_length=200)
#     category=models.ForeignKey(ProductCategory,on_delete=models.CASCADE)
#     description=models.CharField(max_length=500)
#     is_active=models.BooleanField(default=True)
#     is_trending=models.BooleanField(default=False)
#     created_date=models.DateTimeField(auto_now_add=True)
#     created_by=models.ForeignKey(User,on_delete=models.DO_NOTHING)
#     is_modified=models.BooleanField(default=False)
#     is_cancelled=models.BooleanField(default=False)


# class Gender(models.Model):
#     gender=models.CharField(max_length=100)
#     created_date=models.DateTimeField(auto_now_add=True)
#     is_cancelled=models.BooleanField(default=False)

# class ProductGender(models.model):
#     Product=models.ManyToManyField(Product)
#     gender=models.ForeignKey(Gender,on_delete=models.DO_NOTHING)
#     created_date=models.DateTimeField(auto_now_add=True)
#     is_canselled=models.BooleanField(default=False)


# class ProductPrice(models.Model):
#     product=models.ForeignKey(Product, on_delete=models.CASCADE)    
#     product_price=models.PositiveIntegerField()
#     sale_price=models.PositiveIntegerField()
#     created_date=models.DateTimeField(auto_now_add=True)
#     created_by=models.ForeignKey(User,on_delete=models.DO_NOTHING)
#     is_modified=models.BooleanField(default=False)
#     modified_by=models.ForeignKey(User,on_delete=models.DO_NOTHING)
#     is_cancelled=models.BooleanField(default=False)

# class Size(models.Model):
#     size=models.CharField(max_length=100)
#     is_active=models.BooleanField(default=True)
#     created_date=models.DateTimeField(auto_now_add=True)
#     created_by=models.ForeignKey(User,on_delete=models.DO_NOTHING)
#     is_modified=models.BooleanField(default=False)
#     modified_by=models.ForeignKey(User,on_delete=models.DO_NOTHING)
#     is_cancelled=models.BooleanField(default=False)


# class ProductSize(models.Model):
#     product=models.ForeignKey(Product,on_delete=models.DO_NOTHING)
#     size=models.ForeignKey(Size,models.DO_NOTHING)
#     created_date=models.DateTimeField(auto_now_add=True)
#     created_by=models.ForeignKey(User,models.DO_NOTHING)
#     is_cancelled=models.BooleanField(default=False)


# class ProductSizePrice(models.Model):
#     product_size=models.ForeignKey(ProductSize,on_delete=models.DO_NOTHING)
#     product_price=models.PositiveIntegerField()
#     sale_price=models.PositiveIntegerField()
#     created_by=models.ForeignKey(User,models.DO_NOTHING)
#     is_cancelled=models.BooleanField(default=False)
    

# class Color(models.Model):
#     color=models.CharField( max_length=50,unique=True)
#     is_active=models.BooleanField(default=True)
#     created_date=models.DateTimeField(auto_now_add=True)
#     created_by=models.ForeignKey(User,on_delete=models.DO_NOTHING)
#     is_cancelled=models.BooleanField(default=False)
        
# class ProductColor(models.Model):
#     color=models.ForeignKey(Color,on_delete=models.DO_NOTHING)
#     product=models.ForeignKey(Product,on_delete=models.DO_NOTHING)
#     is_active=models.BooleanField(default=True)
#     created_date=models.DateTimeField(auto_now_add=True)
#     created_by=models.ForeignKey(User,on_delete=models.DO_NOTHING)
#     is_cancelled=models.BooleanField(default=False)


# class Cart(models.Model):
#     user=models.OneToOneField(User,on_delete=models.CASCADE)
#     product=models.ForeignKey(Product,on_delete=models.CASCADE)
#     product_size=models.ForeignKey(ProductSize,on_delete=models.DO_NOTHING)
#     product_gender=models.ForeignKey(ProductGender,on_delete=models.DO_NOTHING)
#     product_color=models.ForeignKey(ProductColor,models.DO_NOTHING)
#     is_active=models.BooleanField(default=True)
#     created_date=models.DateTimeField(auto_now_add=True)
#     created_by=models.ForeignKey(User,on_delete=models.DO_NOTHING)
#     is_cancelled=models.BooleanField(default=False)





from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_short_name(self):
        return self.first_name

    def __str__(self):
        return self.get_full_name()



class Profile(models.Model):
    user=models.OneToOneField(CustomUser, on_delete=models.CASCADE,related_name="current_user")
    auth_token=models.CharField(max_length=100)
    is_verified=models.BooleanField(default=False)
    created_date=models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.user.get_full_name()
    
