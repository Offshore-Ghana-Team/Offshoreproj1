from django.db import models

# Create your models here.
class Person(models.Model):
    First_name = models.CharField(max_length=250)
    Last_name = models.CharField(max_length=250)
    Email = models.EmailField(max_length =250)
    Age = models.IntegerField()
    Income = models.IntegerField()
