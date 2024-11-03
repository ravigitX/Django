from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('receipt/<int:pk>/', views.receipt, name='receipt'),
    path('view-booking/', views.view_booking, name='view_booking'),
]