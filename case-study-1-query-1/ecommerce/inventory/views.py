from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator

def all_products(request):
    objs = Product.objects.all()

    paginator = Paginator(objs, 8)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'grid-output.html', {'page_obj':page_obj})
