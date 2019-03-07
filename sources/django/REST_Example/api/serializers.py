from rest_framework import serializers
from .models import Person, Client, City


class PersonSimpleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = ('person_name', 'person_birthDate')


class PersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = ('person_id', 'person_name', 'person_birthDate')


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = ('client_id', 'client_name', 'city_id')


class ClientCompleteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = ('client_id', 'client_name', 'city_id')
        depth = 1


class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = ('city_id', 'city_name', 'city_zip_code')
