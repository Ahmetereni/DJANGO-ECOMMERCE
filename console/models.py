from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
import os

def product_media_upload_to(instance, filename):
    # Dynamically create folder structure based on the product_code
    return os.path.join('uploaded_files', instance.product_code, filename)

class Product(models.Model):
    product_code = models.CharField(max_length=8,unique=True)
    product_category = models.TextField(max_length=2048)
    product_subcategory = models.TextField(max_length=2048)
    product_name = models.TextField(max_length=2048)
    product_price = models.CharField(max_length=8)
    
    task_media = models.FileField(upload_to="uploaded_files", blank=True)
    task_background_media = models.FileField(upload_to="uploaded_files", blank=True)

    def __str__(self):
        return self.product_code

    url = models.URLField(max_length=200,default='https://sandbox.iyzi.link/AAENhA')


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    picture = models.FileField(upload_to='product_sub_images/')
