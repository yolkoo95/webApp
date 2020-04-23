from django.urls import path
from . import views

urlpatterns = [
    path('PATH', views.PLACEHOLDER, name='NAME')
]