from uno.models import Question_m
from django import forms

Budget = (
    ('Less than 5000','Less than 5000'),
    ('Less than 10000','Less than 10000'),
    ('Less than 20000','Less than 20000'),
    ('Less than 50000','Less than 50000'),
    ('No constraint','No constraint'),
)

Profession = (
    ('IT','IT'),
    ('Engineer','Engineer'),
    ('Doctor','Doctor'),
    ('BusinessMan','BuisnessMan'),
)

Gender = (
    ('Male', 'Male'),
    ('Female', 'Female'),
)

Age = (
    ('10-20', '10-20'),
    ('20-30', '20-30'),
    ('30-40', '30-40'),
    ('40+', '40+'),
)

Task = (
    ('Battery Life', 'Battery Life'),
    ('Camera', 'Camera'),
)

Location = (
    ('Urban','Urban'),
    ('Rural','Rural'),
)

Assertion = (
    ('Yes','Yes'),
    ('No','No'),
)

class Question_f(forms.ModelForm):
    budget = forms.ChoiceField(choices=Budget, help_text="Budget")
    profession = forms.ChoiceField(choices=Profession, help_text="Profession")
    gender = forms.ChoiceField(choices=Gender, help_text="Gender")
    age = forms.ChoiceField(choices=Age, help_text="Age")
    task = forms.ChoiceField(choices=Task, help_text="What is more important to you?")

    location = forms.ChoiceField(choices=Location, help_text="Place of living")

    prefer_to_chinese = forms.ChoiceField(choices=Assertion, help_text="Will you prefer Chinese brands for better specification")


    class Meta:
        model = Question_m
        fields = ['budget', 'profession', 'gender', 'age', 'task', 'location','location', 'prefer_to_chinese']
