from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart),       # customer_pk will be needed
    path('<cart_pk>/cartitems/', views.get_cart_items),
    path('cartitems/add/', views.add_item_to_cart),
    path('cartitems/delete/', views.delete_item_from_cart),
    path('cartitems/update/', views.update_item_in_cart),
]
