from django.shortcuts import render
from django.views import generic
from .models import Trades

class MakeMoney(generic.ListView):
    queryset = Trades.objects.order_by('-created_on')
    template_name = 'home.html'
