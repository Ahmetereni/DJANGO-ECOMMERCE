"""
URL configuration for Project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from django.conf.urls import include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from cart import urls as cart_urls
from payment import urls as payment_urls

urlpatterns = [
    path('',views.mainpage,name='mainpage'),
    path('shop',views.shop,name='shop'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('help',views.help,name='help'),
    path('termsandconditions',views.termsandconditions,name='termsandconditions'),
    path('faq',views.faq,name='faq'),

    path('certificates',views.certificates,name='certificates'),
    path('policies',views.policies,name='policies'),
    path('socialresponsibility',views.socialresponsibility,name='socialresponsibility'),
    path('sustainability',views.sustainability,name='sustainability'),
    path('getadvice',views.getadvice,name='getadvice'),

    path('product/<int:product_id>/', views.product, name='product'),
    path('blog_list',views.blog_list,name='blog_list'),
    path('admin/', admin.site.urls),


    #cart app

    path('cart/',include(cart_urls)),

    #payment app

    path('payment/',include(payment_urls)),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
