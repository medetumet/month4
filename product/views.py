from django.shortcuts import render, redirect
from product.models import *
from product.forms import *

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

def create_product_view(request):
    if request.method == 'GET':
        context = {
            'form': ProductCreateForm
        }
        return render(request, 'product/create.html', context=context)

    if request.method == 'POST':
        form = ProductCreateForm(data=request.POST)

        if form.is_valid():
            Product.objects.create(
                title=form.cleaned_data.get('title'),
                description=form.cleaned_data.get('description'),
                price=form.cleaned_data['price'] if form.cleaned_data['price'] is not None else 0,

            )
            return redirect('/products/')
        return render(request, 'product/create.html', context={
            'form': form
        })
