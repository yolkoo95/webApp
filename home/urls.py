from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('terms/', views.terms, name='terms'),
]