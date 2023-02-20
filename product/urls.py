from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_products),
    path('<int:pk>/', views.single_product),
    path('search/', views.search),
]
