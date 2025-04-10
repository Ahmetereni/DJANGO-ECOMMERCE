from django.shortcuts import render
from .models import ShippingAddress,Order,OrderItem
from django.http import JsonResponse
from cart.cart import Cart

# Create your views here.


# Create your views here.
def checkout(request):


    return render(request,'checkout-v2-delivery.html')

def complete_order(request):

    if request.POST.get('action')=='post':

        name=request.POST.get('name')
        surname=request.POST.get('surname')
        email=request.POST.get('email')
        phonenumber=request.POST.get('phone-number')
        city=request.POST.get('city')
        zipcode=request.POST.get('zipcode')
        address=request.POST.get('address')


        shipping_address = (address + " \n " + city + " \n " + zipcode)

        full_name= (name + " " + surname)

        # Shopping cart information
        cart=Cart(request)

        # Get the total price of items
        total_cost = cart.get_total()

        order=Order.objects.create(full_name=full_name,email=email,shipping_address=shipping_address,
        amount_paid=total_cost)

        order_id=order.pk

        for item in cart:
            OrderItem.objects.create(order_id=order_id,product=item['product'],quantity=item['qty'], width=item['wid'], length=item['len'],
            price=item['price'])

    order_success=True
    response= JsonResponse({'success':order_success})
    return response


def payment_success(request):

    for key in list(request.session.keys()):

        if key == 'session_key':
            del request.session[key]

    return render(request,'payment/payment-success.html')

def payment_failed(request):

    return render(request,'payment/payment-failed.html')
