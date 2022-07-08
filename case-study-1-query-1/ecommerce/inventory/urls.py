from django.urls import path
from . import views

urlpatterns = [
    path('ex1/', views.all_products)
]
