from django.urls import path
from . import views

urlpatterns = [
    path('<cart_pk>/', views.order)
]
