from django.urls import path
from .views import add_wishlist, my_wishlist, add_cart, my_cart_view, \
    plus_quantity, minus_quantity, delete_cart_item_view, checkout_view

app_name = 'carts'

urlpatterns = [
    path('add-wishlist/', add_wishlist, name='add-wishlist'),
    path('my-wishlist/', my_wishlist, name='my-wishlist'),
    path('add-cart/', add_cart, name='add-cart'),
    path('my-cart/', my_cart_view, name='my-cart'),
    path('checkout/', checkout_view, name='checkout'),

    path('minus-quantity/', minus_quantity, name='minus-quantity'),  # carts/minus-quantity/
    path('plus-quantity/', plus_quantity, name='plus-quantity'),
    path('delete-cart-item-view/', delete_cart_item_view, name='delete-cart-item-view'),

]
