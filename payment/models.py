from django.db import models
from console.models import Product


# Create your models here.




class ShippingAddress(models.Model):

    name=models.CharField(max_length=300)
    surname=models.CharField(max_length=300)
    email=models.EmailField(max_length=300)
    phonenumber=models.CharField(max_length=300)
    city=models.CharField(max_length=300)
    zipcode=models.CharField(max_length=300)
    address=models.CharField(max_length=300)


    class Meta:
        verbose_name_plural = 'Shipping Address'

    def __str__(self):

        return 'Shipping Address - ' + str(self.id)



class Order(models.Model):

    full_name=models.CharField(max_length=300)
    email=models.EmailField(max_length=300)
    shipping_address = models.TextField(max_length=2048)

    amount_paid = models.DecimalField(max_digits=8,decimal_places=2)

    date_ordered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Sipariş No-#' + str(self.id)


class OrderItem(models.Model):


    #FK->
    order = models.ForeignKey(Order,on_delete=models.CASCADE,null=True)
    product = models.ForeignKey(Product,on_delete=models.CASCADE,null=True)

    quantity = models.PositiveBigIntegerField(default=1)
    width = models.PositiveBigIntegerField(default=1)
    length = models.PositiveBigIntegerField(default=1)

    price= models.DecimalField(max_digits=8,decimal_places=2)

    def __str__(self):
        return 'Sipariş Detayı No-#' + str(self.id)
