from django import forms
from .models import Trades
class ListForm(forms.Form):
    robinUser = forms.EmailField(label='Robinhood Email')
    robinPass = forms.CharField(label='Robinhood Password', max_length=100)
    capitalToInvest = forms.IntegerField(label='Amount of Capital You Want to Invest')
