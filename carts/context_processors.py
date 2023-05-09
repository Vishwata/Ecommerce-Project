from .models import Cart, CartItem
from carts.views import _cart_id

def counter(request):
    cart_count = 0
    if 'admin' in request.path: #the dont see admin which cart is added in the user side
        return {} #hence return empty
    
    else:
        try:
            cart = Cart.objects.filter(cart_id = _cart_id(request))
            cart_items = CartItem.objects.all().filter(cart=cart[:1]) #counter for one by one add
            for cart_item in cart_items:
                cart_count += cart_item.quantity
        except Cart.DoesNotExist:
            cart_count = 0
    return dict(cart_count = cart_count)