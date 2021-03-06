"""djtest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url,include
from django.conf.urls.static import static
from django.contrib import admin
from djtest import settings
from users.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('orders.urls')),
    url(r'^', include('landing.urls')),
    url(r'^', include('products.urls')),
    url(r'^login/', login_view, name='login'),
    # url(r'^orders/', orders_view, name='orders'),
    url(r'^logout/', logout_view, name='logout'),
    url(r'^register/', register_view, name='register'),


]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)