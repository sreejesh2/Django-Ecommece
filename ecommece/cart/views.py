from django.shortcuts import render,redirect
from django.views.generic import View
from .models import Cart
from store.models import Product
from .forms import AddToCartForm

# Create your views here.

class CartView(View):
    def get(self,request,*args, **kwargs):
        qs=Cart.objects.filter(user=request.user,is_active=True, is_cancelled=False)
        return render(request,"cart.html",{"cart_products":qs})
   

def add_to_cart(request,*args, **kwargs):
    id=kwargs.get("pk")
    prod_obj=Product.objects.get(id=id) 
    form=AddToCartForm(request.POST)
   
    if form.is_valid():
       print("==================================")
       print(form.cleaned_data)
       size=form.cleaned_data.get('product_size')
       clr=form.cleaned_data.get('product_color')
       price=form.cleaned_data.get('price')
       Cart.objects.create(user=request.user,product=prod_obj,product_size=size,product_color=clr,price=price)
       return redirect('cart')
    return render(request,'home.html')




