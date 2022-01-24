from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Categories, Product
# Create your views here.

@login_required
def product_page(request):
    categories = Categories.objects.all()
    context={'categories':categories}
    return render(request,"product/product.html", context=context)


@login_required
def product_list(request,pk):
    categories = Categories.objects.all()
    context={'categories':categories}
    return render(request,"product/product.html", context=context)