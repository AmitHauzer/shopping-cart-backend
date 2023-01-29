from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart),       # customer_pk will be needed   
    path('cartitems/<cart_pk>/', views.get_cart_items),
]
