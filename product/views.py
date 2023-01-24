from django.shortcuts import render
from product.models import *

def main_views(request):
    return render(request, 'layouts/index.html')


def products_view(request):
    if request.method == 'GET':
        products = Product.objects.all()
        dict = {
            'product': products,
        }
        return render(request, 'product/product.html', context=dict)

def product_detail_view(request, id):
    if request.method == "GET":
        product = Product.objects.get(id=id)
        reviews = Review.objects.filter(product=product)
        dict = {
            'product': product,
            'reviews': reviews
        }
        return render(request, 'product/detail.html', context=dict)

def category_view(request):
    if request.method == "GET":
        category = Category.objects.all()
        dict = {
            'category': category,
        }

        return render(request, 'product/category.html', context=dict)
