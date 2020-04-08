from django.urls import path
from . import views

urlpatterns = [
    path('', views.appstore, name='appstore'),
]