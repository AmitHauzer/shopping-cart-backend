from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('', views.all_products),
    path('<pk>/', views.single_product),
    path('adminaddproduct/', views.admin_add_product),
]

urlpatterns = format_suffix_patterns(urlpatterns)