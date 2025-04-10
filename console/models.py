from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from datetime import date
def product_media_upload_to():
    return
class Product_category(models.Model):
    product_category=models.TextField(max_length=2048)

    def __str__(self):
        return self.product_category

class Product_subcategory(models.Model):
    product_category=models.ForeignKey(Product_category, on_delete=models.CASCADE)
    product_subcategory=models.TextField(max_length=2048)

    def __str__(self):
        return self.product_subcategory


class Product(models.Model):
    product_code=models.CharField(max_length=8)
    product_subcategory=models.ForeignKey(Product_subcategory, on_delete=models.CASCADE)
    product_name=models.TextField(max_length=2048)
    product_price=models.FloatField(max_length=8)
    product_price_type=models.CharField(max_length=8,default='m2 ya da m') #m2 ya da m
    product_material=models.CharField(max_length=50) # ahşap jaluzi perde basswood ağacından üretilir.
    product_min_en=models.CharField(max_length=8,default='60') # ahşap jaluzi perde minimum en 60 cm dir
    product_max_en=models.CharField(max_length=8)
    product_min_boy=models.CharField(max_length=8,default='100') # ahşap jaluzi perde minimum boy 100 cm dir
    product_max_boy=models.CharField(max_length=8)
    task_media=models.FileField(upload_to='uploaded_files',blank=True)
    task_background_media=models.FileField(upload_to='uploaded_files',blank=True)
    task_media_3=models.FileField(upload_to='uploaded_files',blank=True)
    task_media_4=models.FileField(upload_to='uploaded_files',blank=True)

    product_temizlemeyontemi=models.CharField(max_length=30)
    product_aciklama=models.TextField(max_length=2048)
    product_urunbilgileri=models.TextField(max_length=2048)
    product_ozellikler=models.TextField(max_length=2048)
    product_garantibilgileri=models.TextField(max_length=2048)
    product_teslimatvekargo=models.TextField(max_length=2048)


    def ___str__(self):
        return self.product_name

class Product_color(models.Model):
    product_color_code=models.CharField(max_length=50)
    product_color_name=models.CharField(max_length=50)
    product_color_media=models.FileField(upload_to='uploaded_files/color',blank=True)
    product_code=models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_color_name

class Blog(models.Model):
    blog_code=models.CharField(max_length=8)
    blog_category=models.TextField(max_length=2048)
    blog_name=models.TextField(max_length=2048)
    blog_url=models.TextField(max_length=2048)
    blog_owner=models.CharField(max_length=8)
    blog_date=models.DateTimeField(default=datetime.now, blank=True)
    blog_media=models.FileField(upload_to='uploaded_files',blank=True)

    def ___str__(self):
        return self.blog_code
