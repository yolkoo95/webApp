from django.urls import path
from . import views

urlpatterns = [
    path('', views.codehome, name='codehome' ),
    path('<str:category>/<str:problemName>/', views.codepage, name='codepage'),
]