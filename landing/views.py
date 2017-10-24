from django.shortcuts import render
from products.models import *
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
)

# Create your views here.
def home(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    products_images_phones = products_images.filter(product__category__id=2)
    products_images_laptop = products_images.filter(product__category__id=3)
    products_images_personal = products_images.filter(product__category__id=4)
    return render(request, 'home.html', locals())