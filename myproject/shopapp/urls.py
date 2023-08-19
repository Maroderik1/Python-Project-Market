from django.urls import path

from .views import shop_index, groups_list, products_list, order_list


app_name = 'shopapp'

urlpatterns = [
    path('', shop_index, name='index'),
    path('groups/', groups_list, name='groups_list'),
    path('products/', products_list, name='products_list'),
    path('order/', order_list, name='order_list'),
]