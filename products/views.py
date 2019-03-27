from django.http import HttpResponse
from django.shortcuts import render
from .models import Product


# Create your views here.
# This functions get called when the browser
# sends a HTTP request to the server
def index(request):
    products = Product.objects.all() # Returns all products in our database
    return render(request, 'index.html', {'products': products})


def new(request):
    return HttpResponse('New Products')

