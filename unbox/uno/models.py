from django.db import models
import datetime

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

class Question_m(models.Model):
    budget = models.CharField(max_length=100, choices=Budget, default='No constraint')
    profession = models.CharField(max_length=100, choices=Profession, default='IT')
    gender = models.CharField(max_length=100, choices=Gender, default='Male')
    age = models.CharField(max_length=100, choices=Age, default='20-30')
    task = models.CharField(max_length=100, choices=Task, default='Camera')

    location = models.CharField(max_length=100, choices=Location, default='Urban')

    prefer_to_chinese = models.CharField(max_length=100, choices=Assertion, default='No')

    #majoruse = models.CharField(max_length=100, choices=Major_use, default='No')
    size = models.CharField(max_length=100, choices=Assertion, default='No')

    class Meta:
      verbose_name_plural = 'Questions'

    def __str__(self):
      return self.item
