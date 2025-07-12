from django.shortcuts import render, redirect, get_object_or_404
from .models import Phone

def index(request):
    return redirect('catalog')


# def show_catalog(request):
#     template = 'catalog.html'
#     context = {}
#     return render(request, template, context)


# def show_product(request, slug):
#     template = 'product.html'
#     context = {}
#     return render(request, template, context)

def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort', 'name')
    if sort == 'name':
        phones = Phone.objects.all().order_by('name')
    elif sort == 'min_price':
        phones = Phone.objects.all().order_by('price')
    elif sort == 'max_price':
        phones = Phone.objects.all().order_by('-price')
    else:
        phones = Phone.objects.all()
    
    context = {
        'phones': phones,
        'sort': sort
    }
    return render(request, template, context)

def show_product(request, slug):
    template = 'product.html'   
    phone = get_object_or_404(Phone, slug=slug)
    context = {
        'phone': phone
    }
    return render(request, template, context)