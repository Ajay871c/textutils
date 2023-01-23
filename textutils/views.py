from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index2.html')

def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    removespace = request.POST.get('removespace', 'off')
    capitalize = request.POST.get('capitalize', 'off')

    if removepunc == 'on':
        punctuations = '''.,:;<>/?{}[]'"*^%$#@!'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        parameters = {
            'purpose': 'removed punctuations',
            'analyzed_text': analyzed
        }
        return render(request, 'textutils.html', parameters)

    elif removespace == 'on':
        space = ''' '''
        analyzed = ""
        for char in djtext:
            if char not in space:
                analyzed = analyzed + char
        parameters = {
            'purpose': 'remove space',
            'analyzed_text': analyzed
        }
        return render(request, 'textutils.html', parameters)

    elif capitalize == 'on':
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        parameters = {
            'purpose': 'capitalize',
            'analyzed_text': analyzed
        }
        return render(request, 'textutils.html', parameters)

    else:
        return HttpResponse("Error")
