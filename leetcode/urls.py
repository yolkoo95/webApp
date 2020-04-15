from django.urls import path
from . import views

urlpatterns = [
    path('leetcode/', views.leetcode, name='leetcode'),
    path('datastructure/', views.datastructure, name='datastructure'),
    path('cs50/', views.cs50, name='cs50'),
    path('webapp/', views.webapp, name='webapp'),
    path('', views.codehome, name='codehome' )
]