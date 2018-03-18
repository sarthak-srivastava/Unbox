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
    score = [0, 0, 0, 0, 0, 0, 0]
    for i in information:
        if budget == "5000":
            if information[i][0] <= 7000:
                phones[i] = information[i]
        elif budget == "10000":
            if information[i][0] <= 13000 and information[i][0] >= 7000:
                phones[i] = information[i]
        elif budget == "15000":
            if information[i][0] <= 17000 and information[i][0] >= 12000:
                phones[i] = information[i]
        elif budget == "20000":
            if information[i][0] <= 25000 and information[i][0] >= 17000:
                phones[i] = information[i]
        elif budget == "30000":
            if information[i][0] <= 35000 and information[i][0] >= 25000:
                phones[i] = information[i]
        elif budget == "40000":
            if information[i][0] <= 45000 and information[i][0] >= 35000:
                phones[i] = information[i]
        elif budget == "Flagship":
            if gender == "Male":
                phones['GalaxyS9'] = information['GalaxyS9']
            else:
                phones['IphoneX'] = information['IphoneX']
            break

    if profession == "Student":
        score[3] = 3
        score[4] = 3
        score[5] = 4

    elif profession == "Job":
        score[6] = 3
        score[4] = 4
        score[1] = 3

    elif profession == "Business":
        score[6] = 4
        score[2] = 3
        score[1] = 3

    elif profession == "Elderly Person":
        score[3] = 4
        score[6] = 3
        score[2] = 3

    if gender == "Male":
        score[5] = 4
        score[1] = 3
    elif gender == "Female":
        score[2] = 3
        score[4] = 4

    if task == "Battery Life":
        score[6] = 4
    elif task == "Camera":
        score[4] = 4

    if location == "Urban":
        score[0] = 4

    if prefer_to_chinese == "Yes":
        score[0] = 3


    for i in range(7):
        if score[i] < 0:
            score[i] = 0

    top_three = []
    if len(score) <= 3:
        for i in phones:
            top_three.append([i, phones[i][0], calculate(phones[i][1], score) ,phones[i][2], phones[i][3]]);
        top_three.sort(key=lambda x: x[2], reverse=True)
    else:
        for i in phones:
            top_three.append([i, phones[i][0], calculate(phones[i][1], score) ,phones[i][2], phones[i][3]]);
        top_three.sort(key=lambda x: x[2], reverse=True)
        top_three = top_three[:3]
    for i in range(len(top_three)):
        print(top_three[i])

def calculate(a, b):
    s = 0
    for i in range(7):
        s += (a[i] - b[i])**2
    return (1/s)

def index(request):
    context_dict = {'boldmessage': "Unbox"}
    return render(request, 'index.html', context=context_dict)

def question(request):
    forma = Question_f()

    if request.method == 'POST':
        forma = Question_f(request.POST)
        if forma.is_valid():

            print("\nPrinting\n", forma.cleaned_data)
            data_handling(forma.cleaned_data['budget'], forma.cleaned_data['profession'], forma.cleaned_data['gender'], forma.cleaned_data['age'], forma.cleaned_data['task'], forma.cleaned_data['location'], forma.cleaned_data['prefer_to_chinese'], forma.cleaned_data['majoruse'])
            forma.save(commit=True)
            return index(request)

        else:
            print(forma.errors)

    return render(request, 'questions.html', {'form': forma})

def product(request):
    context_dict = {'boldmessage': "Unbox"}
    return render(request, 'product.html', context=context_dict)
