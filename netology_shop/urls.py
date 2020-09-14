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
from django.urls import path, include

import auth1.views
import main.views
import phones.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main.views.index, name = 'index'),
    # path('', main.views.test, name = 'index2'),
    # path('/<str:type>', main.views.test, name = 'test'),
    # path('smartphones/', phones.views.smartphones, name = 'smartphones'),
    # path('tablets/', phones.views.tablets, name = 'tablets'),
    # path('accessories/', phones.views.accessories, name = 'accessories'),
    path('product/<slug:slug>/', phones.views.product_view, name = 'product_view'),
    # path('empty/', phones.views.empty, name = 'empty'),
    path('cart/', main.views.cart, name = 'cart'),
    path('login/', auth1.views.login_request, name ='login'),
    path('logout/', auth1.views.logout_request, name = 'logout'),
    path('signup/', auth1.views.signup),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns