from django.http import HttpResponse
from django.shortcuts import render
from uno.models import Question_m
from django.views.generic import FormView
from uno.forms import Question_f
import requests
from uno.info import information
from copy import deepcopy

def data_handling(budget, profession, gender, age, task, location, prefer_to_chinese, majoruse):
    phones = {}
    for i in information:
        if budget == "Less than 5000":
            if i[0] <= 10000:
                phones[i] = information[i]
        elif budget == "Less than 10000":
            if i[0] <= 15000:
                phones[i] = information[i]
        elif budget == "Less than 20000":
            if i[0] <= 25000 and i[0] >= 10000:
                phones[i] = information[i]
        elif budget == "Less than 50000":
            if i[0] <= 55000 and i[0] >= 30000:
                phones[i] = information[i]
        elif budget == "No constraint":
            if i[0] >= 30000:
                phones[i] = information[i]
        print(phones[i])

def index(request):
    context_dict = {'boldmessage': "Unbox"}
    return render(request, 'index.html', context=context_dict)

def question(request):
    forma = Question_f()

    if request.method == 'POST':
        forma = Question_f(request.POST)
        if forma.is_valid():

            print("\nPrinting\n", forma.cleaned_data['budget'])
            forma.save(commit=True)
            return index(request)

        else:
            print(forma.errors)

    return render(request, 'questions.html', {'form': forma})
