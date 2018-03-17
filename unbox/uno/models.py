from django.db import models
import datetime

Location = (
    ('goa','Goa'),
    ('mumbai','Mumbai'),
    ('bangalore','Bangalore'),
)

class Question_m(models.Model):
  location = models.CharField(max_length=100, choices=Location,
               default='goa')
  name = models.CharField(max_length=100)
  contact_info = models.CharField(max_length=100)
  item = models.CharField(max_length=100)
  quantity = models.CharField(max_length=100)
  price = models.CharField(max_length=100)
  additional_info = models.CharField(max_length=1000)
  certificates = models.URLField(default='null')


  class Meta:
      verbose_name_plural = 'Questions'

  def __str__(self):
      return self.item
