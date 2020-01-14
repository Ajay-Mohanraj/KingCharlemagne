from django.urls import path
from . import views

urlpatterns = [
    path('index.html', views.MakeMoney, name='index'),
    path('home.html', views.StartProgram, name='home')
]
