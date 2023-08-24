from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product

def home(request):
    products = Product.objects.all().filter(is_available=True)

    context = {
        'products': products,
    }
    return render(request, 'home.html', context)


def error_404(request, exception):

    #return render(request, '404/404.html', status=404)
    return render(request, '404/404.html', status=404)