from decimal import Decimal
from console.models import Product

class Cart():

    def __init__(self,request):
        self.session = request.session

        #returning user - obtain his her existing session

        cart = self.session.get('session_key')

        #new user - generate a new session key

        if 'session_key' not in request.session:

            cart=self.session['session_key']={}

        self.cart = cart

    def add(self,product, product_qty,product_wid,product_len,calculated_price):

        product_id = str(product.id)

        if product_id in self.cart:

            self.cart[product_id]['qty']= product_qty
            self.cart[product_id]['wid']= product_wid
            self.cart[product_id]['len']= product_len
            self.cart[product_id]['cal']= calculated_price

        else:
            self.cart[product_id] = {
                'price': str(product.product_price),
                'qty': product_qty,
                'wid': product_wid,
                'len': product_len,
            }
        self.session.modified = True

    def delete(self,product):

        product_id=str(product)

        if product_id in self.cart:

            del self.cart[product_id]

        self.session.modified = True


    def __len__(self):

        return sum(item['qty'] for item in self.cart.values())


    def __iter__(self):

        all_product_ids=self.cart.keys()

        products = Product.objects.filter(id__in=all_product_ids)

        cart=self.cart.copy()

        for product in products:

            cart[str(product.id)]['product']=product


        for item in cart.values():
            item['price']=Decimal(item['price'])
            item['wid']=Decimal(item['wid'])
            item['len']=Decimal(item['len'])
            item['price']=Decimal(item['price'])
            item['total']=item['price']*item['qty']*item['wid']*item['len']/1000

            yield item

    def get_total(self):
        return sum(Decimal(item['price'])*item['qty']*item['wid']*item['len']/1000 for item in self.cart.values())
