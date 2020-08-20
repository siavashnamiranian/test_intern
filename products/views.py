from django.shortcuts import render, get_object_or_404

from products.models import Product


def home_page(request):
    all_products = Product.objects.filter(is_enable=True)
    context = {'products': all_products}
    return render(request, 'products/home.html', context=context)


def product_detail(request, pk):
    prod = get_object_or_404(Product, id=pk)
    context = {'obj': prod}
    return render(request, 'products/detail.html', context)
