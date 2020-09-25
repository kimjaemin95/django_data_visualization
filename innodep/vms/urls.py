from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home),
    path('vms_device/', views.vms_device),
    path('vms_device_analysis/', views.vms_device_analysis)
]
