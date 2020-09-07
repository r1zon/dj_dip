"""netology_shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
# from django.contrib.auth import views as auth_views
from django.urls import path

import auth.views
import main.views
import phones.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main.views.index, name = 'index'),
    path('smartphones/', phones.views.smartphones, name = 'smartphones'),
    path('phone/<int:pk>/', phones.views.product_view, name = 'product_view'),
    path('empty/', phones.views.empty, name = 'empty'),
    path('cart/', main.views.cart, name = 'cart'),
    path('login/', auth.views.CustomLoginView.as_view(), name ='login'),
    path('logout/', auth.views.logout, name = 'logout'),
    path('signup/', auth.views.signup),
]
