from django.urls import path
from . import views

urlpatterns = [
    path('', views.appstore, name='appstore'),
    path('app/checker', views.checker, name="checker"),
    path('app/check', views.check, name="check"),
    path('graphic/ticktock', views.ticktock, name="ticktock"),
    path('lab/radar', views.radar, name="radar"),
    path('design/logindemo', views.login, name='login'),
    path('design/logindemo/register/', views.register, name='register'),
]