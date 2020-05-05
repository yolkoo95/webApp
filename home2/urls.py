from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage2'),
    path('terms', views.terms, name='terms')
]