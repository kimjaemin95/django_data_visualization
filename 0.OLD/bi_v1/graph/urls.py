from django.urls import path
from . import views


urlpatterns = [
    path('line/', views.line),
]