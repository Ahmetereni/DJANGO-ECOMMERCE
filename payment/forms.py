from django import forms

from .models import ShippingAddress

class ShippingForm(forms.ModelForm):

    class Meta:
        model= ShippingAddress

        fields=['name','surname','email','phonenumber','city','zipcode','address']
