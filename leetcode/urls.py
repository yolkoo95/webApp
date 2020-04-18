from django.urls import path
from . import views

urlpatterns = [
    path('', views.codehome, name='codehome' ),
    path('<str:category>/<str:probName>/', views.codepage, name='codepage'),   
]