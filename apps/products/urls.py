from django.urls import path
from .views import index,shop_grid,shop_detail

app_name = 'products'

urlpatterns = [
    path('', index),
    path('shop-grid/',shop_grid,name='shop_grid'),
    path('shop-detail/<int:pk>/',shop_detail,name='shop-detail')

]
