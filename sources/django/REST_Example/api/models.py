from django.db import models

# Create your models here.


class Person(models.Model):
    person_id = models.IntegerField()
    person_name = models.CharField(max_length=50)
    person_birthDate = models.DateField()
