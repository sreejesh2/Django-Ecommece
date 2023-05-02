from django.shortcuts import render,redirect
from django.views.generic import TemplateView,View,ListView,DetailView
from random import sample

from .models import ProductCategory,Product
# Create your views here.
class IndexView(View):
    def get(self,request,*args, **kwargs):
        cats=ProductCategory.objects.all()
        if len(cats)>3:
            cats= sample(list(cats),3)

        context={"category":cats}
        return render(request,"home.html",context)
    
class CategoryView(ListView):
    model=ProductCategory
    template_name='all-category.html'
    context_object_name='category'  


class ProductListView(View):
    def get(self,request,*args, **kwargs):
        cat_id=kwargs.get("pk")
        cat=ProductCategory.objects.get(id=cat_id)
        product=Product.objects.filter(category=cat)
        cat=ProductCategory.objects.all()
        return render(request,'products.html',{"product":product,"ct":cat})     
    
class ProductDetailView(View):
    def get(self,request,*args, **kwargs):
        id = kwargs.get("pk")
        prdt_obj=Product.objects.get(id=id)
        return render(request,"product-detail.html",{"product":prdt_obj})
