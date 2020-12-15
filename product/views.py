from django.http import Http404
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from product.models import Product, SubCategory, Category


# Create your views here.


class ProductList(ListView):
    model = Product
    paginate_by = 1
    template_name = 'product_list.html'
    context_object_name = 'products'
    queryset = Product.objects.only('name', 'price', 'image')

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['categories'] = Category.objects.all()
    #     return context


# def product_list(request):
#     products = Product.objects.only('name', 'price', 'image')
#     categories = Category.objects.all()
#     context = {
#         'products': products,
#         'categories': categories
#     }
#     return render(request, 'product_list.html', context)


class ProductDetail(DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'

    def get_queryset(self):
        print(self.request.GET.get('pk'))
        print(self.kwargs['pk'])
        product_id = self.kwargs['pk']
        qs = Product.objects.filter(id=product_id)
        return qs


# class CategoryList(ListView):
#     queryset = Category.objects.all()
#     template_name = 'product_list.html'
#     context_object_name = 'categories'


class ShowByCategory(ListView):
    template_name = 'product_list.html'
    model = SubCategory
    context_object_name = 'products'

    def get_queryset(self):
        subcategory_name = self.kwargs['cat_name']
        products = Product.objects.filter(subcategory__title=subcategory_name)
        return products
