from django.shortcuts import render
from .forms import ListForm
from django.http import HttpResponseRedirect
import json

robinUser = ''
robinPass = ''
capitalToInvest = 0

def MakeMoney(request):
    if request.method == 'POST':
        form = ListForm(request.POST)
        if form.is_valid():
            robinUser = form.cleaned_data['robinUser']
            robinPass = form.cleaned_data['robinPass']
            capitalToInvest = form.cleaned_data['capitalToInvest']
            return HttpResponseRedirect('/index.html/')
    else:
        form = ListForm()

    return render(request, 'home.html', {'form': form})

def getJSON(filePathAndName):
    with open(filePathAndName, 'r') as fp:
        return json.load(fp)

def overwriteJSON(data):
    with open("./prices.json", 'w') as fp:
        json.dump(data, fp)

def StartProgram(request):
    rawJSON = getJSON('templates/prices.json')
    rawJSON['capital'] = int(capitalToInvest)
    with open('templates/prices.json', 'w') as fp:
        json.dump(rawJSON, fp)
    rawJSON2 = getJSON('templates/accountInfo.json')
    rawJSON2['email'] = robinUser
    rawJSON2['pass'] = robinPass
    with open("templates/accountInfo.json", 'w') as fp:
        json.dump(rawJSON2, fp)

    return render(request, 'index.html')
