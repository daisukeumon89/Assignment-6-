from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_client, name='add_client'),  # Ensure this view exists
    path('add_product/', views.add_product, name='add_product'),  # Ensure this view exists
]
