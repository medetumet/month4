from django.shortcuts import render, redirect
from product.models import Product, Review, Category
from product.forms import ProductCreateForm, ReviewCreateForm
from django.views.generic import ListView, CreateView, DetailView
from users.get_user_request import get_user_request

# Create your views here.

PAGINATION_LIMIT = 3

class MainView(ListView):
    model = Product
    template_name = 'layouts/index.html'




class ProductsView(ListView):
    model = Product
    template_name = 'product/product.html'


    def get (self, request, *args, **kwargs):
        product = Product.objects.all()
        category_id = request.GET.get('category')
        search = request.GET.get('search')
        page = int(request.GET.get('page', 1))
        if search is not None:
            products = Product.objects.filter(
                title__icontains=search
            )

        max_page = product.__len__() / PAGINATION_LIMIT
        if round(max_page) < max_page:
            max_page = round(max_page) + 1
        else:
            max_page = round(max_page)

        products = products[PAGINATION_LIMIT * (page - 1):PAGINATION_LIMIT * page]


        if category_id:
            products = Product.objects.filter(category=Category.objects.get(id=category_id))

        context = {
            'products': product,
            'user': get_user_request(self.request),
            'max_page': range(1, kwargs['max_page'] + 1)
        }

        return render(request, self.template_name, context=context)




class ProductDetailView(DetailView):
    model = Product
    template_name = 'product/detail.html'
    pk_url_kwarg = 'id'
    def get(self, request, id):
        product_obj = Product.objects.get(id=id)
        reviews = Review.objects.filter(product=product_obj)

        context = {
            'product': product_obj,
            'reviews': reviews,
            'form': ReviewCreateForm,
        }
        return render(request, self.template_name, context=context)

    def post(self, request, id):
        product_obj = Product.objects.get(id=id)
        reviews = Review.objects.filter(product=product_obj)
        form = ReviewCreateForm(data=request.POST)
        if form.is_valid() and not request.user.is_anonymous:
            Review.objects.create(
                author_id=request.user.id,
                title=form.cleaned_data.get('title'),
                product=product_obj
            )
            return redirect(f'/products/{product_obj.id}/')
        else:
            form.add_error('title', 'ti ne zaregan')
        return render(request, self.template_name, context={
            'product': product_obj,
            'reviews': reviews,
            'form': form
        })

class CategoryView(ListView):
    model = Category
    template_name = 'product/category.html'

    def get(self, request, **kwargs):
        categories = Category.objects.all()
        context = {
            'categories': categories,
        }

        return render(request, self.template_name, context=context)


class CreateProductView(ListView, CreateView):
    model = Product
    template_name = 'product/create.html'
    form = ProductCreateForm

    def get(self, request, **kwargs):
        if request.method == 'GET' and not request.user.is_anonymous:
            context = {
                'form': ProductCreateForm
            }
            return render(request, 'product/create.html', context=context)
        elif request.user.is_anonymous:
            return redirect('/products')

    def post(self, request, **kwargs):
        form = ProductCreateForm(request.POST, request.FILES)

        if form.is_valid():
            Product.objects.create(
                image=form.cleaned_data.get('image'),
                title=form.cleaned_data.get('title'),
                description=form.cleaned_data.get('description'),
                price=form.cleaned_data['price'] if form.cleaned_data['price'] is not None else 0,
                rate=form.cleaned_data['rate'] if form.cleaned_data['rate'] is not None else 5,
            )
            return redirect('/products/')
        return render(request, 'product/create.html', context={
            'form': form
        })