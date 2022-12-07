from django.urls import path

from store.views import *


urlpatterns = [
    path('products', ProductList.as_view(), name='products_list'),
    path('product/<int:id>', ProductInfo.as_view(), name='product_info_data'),
    path('customer/register', RegisterPage.as_view(), name='user_register'),
    path('customer/login', LoginPage.as_view(), name='customer_login'),
    path('customer/logout', customer_logout, name='customer_logout'),
    path('customer/profile', OwnerInfo.as_view(), name='customer_profile'),
    path('customer/cart/add_product', AddToCart.as_view(), name='add_product_to_cart'),
    path('customer/<str:username>', CustomerInfo.as_view(), name='user_info_data'),
]
