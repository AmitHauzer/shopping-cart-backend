from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_products),
    path('<pk>/', views.single_product),
    path('adminaddproduct/', views.admin_add_product),
    path('search/1/', views.search),
]
