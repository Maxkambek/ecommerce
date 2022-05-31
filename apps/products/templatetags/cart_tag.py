from django import template
from apps.carts.models import Cart, WishList

register = template.Library()


@register.simple_tag(takes_context=True)
def get_user_cart(context):
    request = context['request']
    user = request.user
    cart=None
    try:
        cart = Cart.objects.get(client=user, is_ordered=False)
    except:
        cart=None

    return cart


@register.simple_tag(takes_context=True)
def get_user_wishlist(context):
    request = context['request']
    user = request.user
    try:
        wlist = WishList.objects.filter(user=user)
        wlist_products = [product.product.id for product in wlist]
    except:
        wlist_products=[]
    return wlist_products



