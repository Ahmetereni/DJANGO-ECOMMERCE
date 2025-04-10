from django.shortcuts import render
from .cart import Cart
from console.models import Product
from django.shortcuts import get_object_or_404
from django.http import JsonResponse


# Create your views here.
def cart_summary(request):
    cart = Cart(request)
    print(cart)
    return render(request,"checkout-v2-cart.html",{'cart':cart})

def cart_add(request):

    cart = Cart(request)

    if request.POST.get('action')=='post':

        product_id=int(request.POST.get('product_id'))
        product_quantity=int(request.POST.get('product_quantity'))

        product_width=int(request.POST.get('product_width'))
        product_length=int(request.POST.get('product_length'))


        product = get_object_or_404(Product,id=product_id)

        # Calculate total price (Price * Width * Length * Quantity)
        calculated_price = product.product_price * product_width * product_length * product_quantity /1000

        cart.add(product=product,product_qty=product_quantity, product_wid=product_width,product_len=product_length,calculated_price=calculated_price)

        cart_quantity = cart.__len__()

        response = JsonResponse({'qty':cart_quantity,'wid':product_width,'len':product_length,'cal':calculated_price})

        return response


def cart_delete(request):

    cart = Cart(request)

    if request.POST.get('action')=='post':

        product_id=int(request.POST.get('product_id'))

        cart.delete(product=product_id)

        cart_quantity = cart.__len__()

        cart_total = cart.get_total()

        response = JsonResponse({'qty':cart_quantity,'total':cart_total})

        return response

def cart_update(request):

    pass
