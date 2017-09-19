from __future__ import unicode_literals

from django.db import models
import datetime

# Create your models here.
class Student(models.Model):
    names = models.CharField(max_length = 100)
    course = models.CharField(max_length = 50)
    description = models.TextField(default='Good teacher')
    registration_date = models.DateField(default=datetime.date.today())
    graduation_date = models.DateField(default = datetime.date.today)
