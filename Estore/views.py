from django.shortcuts import render
from .models import Product
# Create your views here.
def homepage(request):
    product = Product.objects.all()
    return render(request, 'Estore/index.html', {'product': product})