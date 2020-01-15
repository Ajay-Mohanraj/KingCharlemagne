from django.shortcuts import render
from .forms import ListForm
from django.http import HttpResponseRedirect
import json
import os
from django.conf import settings

pricesFile = os.path.join(settings.BASE_DIR, 'CharlemagneApp/static/prices.json')
accountInfoFile = os.path.join(settings.BASE_DIR, 'CharlemagneApp/static/accountInfo.json')

def MakeMoney(request):
    if request.method == 'POST':
        form = ListForm(request.POST)
        if form.is_valid():
            def getJSON(filePathAndName):
                with open(filePathAndName, 'r') as fp:
                    return json.load(fp)

            def overwriteJSON(data):
                with open("./prices.json", 'w') as fp:
                    json.dump(data, fp)

            def StartProgram(request):
                rawJSON = getJSON(pricesFile)
                rawJSON['capital'] = int(form.cleaned_data['capitalToInvest'])
                with open(pricesFile, 'w') as fp:
                    json.dump(rawJSON, fp)
                rawJSON2 = getJSON(accountInfoFile)
                rawJSON2['email'] = form.cleaned_data['robinUser']
                rawJSON2['pass'] = form.cleaned_data['robinPass']
                with open(accountInfoFile, 'w') as fp:
                    json.dump(rawJSON2, fp)

                return render(request, 'index.html')

            StartProgram()

            return HttpResponseRedirect('/index.html/')
    else:
        form = ListForm()

    return render(request, 'home.html', {'form': form})


def Pass(request):
    return render(request, 'index.html')
