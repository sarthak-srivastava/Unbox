from uno.models import Question_m
from django import forms

Budget = (
    ('5000', '5000'),
    ('10000','10000'),
    ('15000','15000'),
    ('20000','20000'),
    ('40000','40000'),
    ('Flagship','Flagship'),
)

Profession = (
    ('Student','Student'),
    ('Job','Job'),
    ('Business','Buisness'),
    ('Elderly Person','Elderly Person'),
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

Major_use = (
    ('Calling','Calling'),
    ('Photography','Photography'),
    ('Gaming','Gaming'),
    ('Whatsapp','Whatsapp'),
    ('Movie','Movie'),
    )

class Question_f(forms.ModelForm):
    budget = forms.ChoiceField(choices=Budget, help_text="Budget")
    profession = forms.ChoiceField(choices=Profession, help_text="Profession")
    gender = forms.ChoiceField(choices=Gender, help_text="Gender")
    age = forms.ChoiceField(choices=Age, help_text="Age")
    task = forms.ChoiceField(choices=Task, help_text="What is more important to you?")
    majoruse = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=Major_use, help_text="What do you use your tech mostly for?")
    location = forms.ChoiceField(choices=Location, help_text="Place of living")
    size = forms.ChoiceField(choices=Assertion, help_text="Will you prefer small compact phones?")
    prefer_to_chinese = forms.ChoiceField(choices=Assertion, help_text="Will you prefer Chinese brands for better specification")


    class Meta:
        model = Question_m
        fields = ['budget', 'profession', 'gender', 'age', 'task', 'location', 'prefer_to_chinese','majoruse', 'size']
