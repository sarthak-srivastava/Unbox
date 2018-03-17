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
            if information[i][0] <= 10000:
                phones[i] = information[i]
        elif budget == "Less than 10000":
            if information[i][0] <= 15000:
                phones[i] = information[i]
        elif budget == "Less than 20000":
            if information[i][0] <= 25000 and information[i][0] >= 10000:
                phones[i] = information[i]
        elif budget == "Less than 50000":
            if information[i][0] <= 55000 and information[i][0] >= 30000:
                phones[i] = information[i]
        elif budget == "No constraint":
            if information[i][0] >= 30000:
                phones[i] = information[i]
        

def index(request):
    context_dict = {'boldmessage': "Unbox"}
    return render(request, 'index.html', context=context_dict)

def question(request):
    forma = Question_f()

    if request.method == 'POST':
        forma = Question_f(request.POST)
        if forma.is_valid():

            print("\nPrinting\n", forma.cleaned_data['budget'])
            data_handling(forma.cleaned_data['budget'], forma.cleaned_data['profession'], forma.cleaned_data['gender'], forma.cleaned_data['age'], forma.cleaned_data['task'], forma.cleaned_data['location'], forma.cleaned_data['prefer_to_chinese'], forma.cleaned_data['majoruse'])
            forma.save(commit=True)
            return index(request)

        else:
            print(forma.errors)

    return render(request, 'questions.html', {'form': forma})
