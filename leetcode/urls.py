from django.urls import path
from . import views

urlpatterns = [
    path('', views.codehome, name='codehome' ),
    path('<str:category>/<str:probName>/', views.codepage, name='codepage'),
    # path('datastructure/', views.datastructure, name='datastructure'),
    # path('cs50/', views.cs50, name='cs50'),
    # path('webapp/', views.webapp, name='webapp'),
    
]