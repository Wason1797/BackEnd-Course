from django.db import models

# Create your models here.


class Person(models.Model):
    person_id = models.AutoField(primary_key=True)
    person_name = models.CharField(max_length=50)
    person_birthDate = models.DateField()


class City(models.Model):
    city_id = models.IntegerField(primary_key=True)
    city_name = models.CharField(max_length=20)
    city_zip_code = models.CharField(max_length=10)


class Client(models.Model):
    client_id = models.IntegerField(primary_key=True)
    client_name = models.CharField(max_length=30)
    city_id = models.ForeignKey(City, on_delete=models.PROTECT)
