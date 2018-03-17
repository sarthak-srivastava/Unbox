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

    if profession == "IT":
        score[3] = 4
        score[6] = 0
        score[2] = 3
        score[5] = 4
    elif profession == "Engineer":
        score[3] = 3
        score[6] = 3
        score[2] = 0
        score[5] = 4
    elif profession == "Doctor":
        score[3] = 0
        score[6] = 3
        score[2] = 4
        score[5] = 3
    elif profession == "BusinessMan":
        score[3] = 0
        score[6] = 4
        score[2] = 3
        score[5] = 4

    if gender == "male":
        score[3] = 4
        score[4] = score[4]
    elif gender == "female":
        score[3] = score[3]
        score[4] = 4

    if age == "20-30":
        score[5] = 4
        #score[6] =
        score[4] = 4
    elif age == "30-40":
        score[5] = 3
        score[6] = 4
        #score[4] =

    if task == "Battery Life":
        score[6] += 1
        score[4] -= 1
    elif task == "Camera":
        score[6] -= 1
        score[4] += 1

    if location == "Urban":
        score[0] = 4

    elif location == "Rural":
        score[0] = 3

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
    for i in range(3):
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
