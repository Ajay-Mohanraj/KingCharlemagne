from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.MakeMoney.as_view(), name="home"),
]
