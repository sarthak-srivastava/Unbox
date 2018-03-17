from django.db import models
import datetime

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
Majoruse = (
    ("Calling","Calling"),
    ("Photography","Photography"),
    ("Gaming","Gaming"),
    ("Whatsapp","Whatsapp"),
    ("Movie","Movie"),
    )

class Question_m(models.Model):
    budget = models.CharField(max_length=100, choices=Budget, default='No constraint')
    profession = models.CharField(max_length=100, choices=Profession, default='IT')
    gender = models.CharField(max_length=100, choices=Gender, default='Male')
    age = models.CharField(max_length=100, choices=Age, default='20-30')
    task = models.CharField(max_length=100, choices=Task, default='Camera')

    location = models.CharField(max_length=100, choices=Location, default='Urban')

    prefer_to_chinese = models.CharField(max_length=100, choices=Assertion, default='No')

    class Meta:
      verbose_name_plural = 'Questions'

    def __str__(self):
      return self.item
