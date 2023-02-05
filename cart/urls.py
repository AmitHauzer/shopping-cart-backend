from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart),       # customer_pk will be needed
    path('cartitems/<cart_pk>/', views.get_cart_items),
    path('cartitems/<cart_pk>/add/', views.add_item_to_cart),
    path('cartitems/<cart_pk>/delete/', views.delete_item_from_cart),
    path('cartitems/<cart_pk>/update/', views.update_item_in_cart),
]
