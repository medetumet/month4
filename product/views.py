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