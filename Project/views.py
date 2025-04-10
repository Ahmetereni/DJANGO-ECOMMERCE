from django.shortcuts import render
from django.http import HttpResponse
from console.models import Product,Blog,Product_category,Product_subcategory,Product_color
from datetime import datetime,timedelta

def mainpage(request):
    #service_list= Service.objects.order_by('-service_created_date')[:5]
    #project_list= Project.objects.order_by('?')[:3]
    #dict={'services':service_list,'projects':project_list}
    return render(request,'home-furniture.html')

def shop(request):
    product_list=Product.objects.all()
    #service_list= Service.objects.order_by('-service_created_date')[:5]
    #project_list= Project.objects.order_by('?')[:3]
    dict={'product_list':product_list}
    return render(request,'shop-catalog-furniture.html',dict)

def product(request, product_id):
    product = Product.objects.get(id=product_id)
    color = Product_color.objects.filter(product_code=product_id)

    # İngilizce - Türkçe ay isimleri
    ay_isimleri = {
        "January": "Ocak", "February": "Şubat", "March": "Mart", "April": "Nisan",
        "May": "Mayıs", "June": "Haziran", "July": "Temmuz", "August": "Ağustos",
        "September": "Eylül", "October": "Ekim", "November": "Kasım", "December": "Aralık"
    }

    minimum_del=datetime.today() + timedelta(days=1)
    maximum_del=minimum_del + timedelta(days=11)

    ay_ing = minimum_del.strftime('%B')
    ay_turkce = ay_isimleri[ay_ing]  # 'Mart'


    minimum_delivery=minimum_del.strftime(f"%d {ay_turkce}")
    maximum_delivery=maximum_del.strftime(f"%d {ay_turkce}")

    #service_list= Service.objects.order_by('-service_created_date')[:5]
    #project_list= Project.objects.order_by('?')[:3]
    #dict={'services':service_list,'projects':project_list}
    dict={'product':product,
    'minimum_delivery':minimum_delivery,
    'maximum_delivery':maximum_delivery,
    'color':color}
    return render(request,'shop-product-furniture.html',dict)

def blog_list(request):
    blog_list=Blog.objects.all()
    #service_list= Service.objects.order_by('-service_created_date')[:5]
    #project_list= Project.objects.order_by('?')[:3]
    dict={'blog_list':blog_list}
    return render(request,'blog-grid-v2.html',dict)


def about(request):
    #service_list= Service.objects.order_by('-service_created_date')[:5]
    #project_list= Project.objects.order_by('?')[:3]
    #dict={'services':service_list,'projects':project_list}
    return render(request,'about-v2.html')

def contact(request):
    #service_list= Service.objects.order_by('-service_created_date')[:5]
    #project_list= Project.objects.order_by('?')[:3]
    #dict={'services':service_list,'projects':project_list}
    return render(request,'contact-v3.html')

def help(request):
    #service_list= Service.objects.order_by('-service_created_date')[:5]
    #project_list= Project.objects.order_by('?')[:3]
    #dict={'services':service_list,'projects':project_list}
    return render(request,'help-topics-v2.html')

def termsandconditions(request):
    #service_list= Service.objects.order_by('-service_created_date')[:5]
    #project_list= Project.objects.order_by('?')[:3]
    #dict={'services':service_list,'projects':project_list}
    return render(request,'terms-and-conditions.html')

def faq(request):
    #service_list= Service.objects.order_by('-service_created_date')[:5]
    #project_list= Project.objects.order_by('?')[:3]
    #dict={'services':service_list,'projects':project_list}
    return render(request,'faq.html')


def about(request):
    #service_list= Service.objects.order_by('-service_created_date')[:5]
    #project_list= Project.objects.order_by('?')[:3]
    #dict={'services':service_list,'projects':project_list}
    return render(request,'about-v2.html')

def certificates(request):
    #service_list= Service.objects.order_by('-service_created_date')[:5]
    #project_list= Project.objects.order_by('?')[:3]
    #dict={'services':service_list,'projects':project_list}
    return render(request,'certificates.html')

def policies(request):
    #service_list= Service.objects.order_by('-service_created_date')[:5]
    #project_list= Project.objects.order_by('?')[:3]
    #dict={'services':service_list,'projects':project_list}
    return render(request,'policies.html')

def socialresponsibility(request):
    #service_list= Service.objects.order_by('-service_created_date')[:5]
    #project_list= Project.objects.order_by('?')[:3]
    #dict={'services':service_list,'projects':project_list}
    return render(request,'socialresponsibility.html')

def sustainability(request):
    #service_list= Service.objects.order_by('-service_created_date')[:5]
    #project_list= Project.objects.order_by('?')[:3]
    #dict={'services':service_list,'projects':project_list}
    return render(request,'sustainability.html')

def getadvice(request):
    #service_list= Service.objects.order_by('-service_created_date')[:5]
    #project_list= Project.objects.order_by('?')[:3]
    #dict={'services':service_list,'projects':project_list}
    return render(request,'getadvice.html')
