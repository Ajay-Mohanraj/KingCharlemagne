from django.urls import path, include
from django.views.generic.base import TemplateView # new

from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('signup/', views.SignUp.as_view(), name='signup'),
]
