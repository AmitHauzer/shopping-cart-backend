from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart),       # customer_pk will be needed
    path('<cart_pk>/cartitems/', views.all_cart_items),
    path('<cart_pk>/cartitems/<product_id>', views.single_cartitem),
]
