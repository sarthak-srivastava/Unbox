from django.http import HttpResponse
from django.shortcuts import render
from uno.models import Question_m
from django.views.generic import FormView
from uno.forms import Question_f
import requests

def index(request):
    context_dict = {'boldmessage': "Unbox"}
    return render(request, 'index.html', context=context_dict)

def question(request):
    forma = Question_f()

    if request.method == 'POST':
        forma = Question_f(request.POST)
        if forma.is_valid():
            forma.save(commit=True)
            return index(request)

        else:
            print(forma.errors)

    return render(request, 'questions.html', {'form': forma})
