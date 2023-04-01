from django.urls import path
from rest_framework import routers
from products.views import *

urlpatterns = [
    path('cart/', Cart.as_view(), name='cart'),
    path('orders/', Orders.as_view(), name='сlearance'),

    # Rest
    path('change-currency/<str:currency>/', Change_Currency.as_view(), name='change_currency'),
    path('add-to-cart/<str:key>/', Add_Or_Del_From_Cart.as_view(), name='add_to_cart'),
    path('del-from-cart/<str:key>/', Add_Or_Del_From_Cart.as_view(), name='del_from_cart'),
    path('add-order/', Add_Or_Del_Order.as_view(), name='add_order'),
    path('del-order/', Add_Or_Del_From_Cart.as_view(), name='del_order'),

    path('<str:model>/', ProductsList.as_view(), name='products_list'),
    path('<str:model>/<str:key>/', AloneProduct.as_view(), name='alone_product'),
]


# urlpatterns = router.urls