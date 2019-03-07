# from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Person, City, Client
from .serializers import PersonSerializer, ClientCompleteSerializer, \
    CitySerializer, ClientSerializer, PersonSimpleSerializer
from functools import reduce
# Create your views here.


class PersonView(APIView):

    # def get(self, request, person_id):
    #     dummy = Person(person_id=person_id,
    #                    person_name='dummy_name',
    #                    person_birthDate='17-08-1997')
    #     serializer = PersonSerializer(dummy)
    #     return Response(serializer.data)

    def get(self, request):
        person_id = request.GET.get('person_id')

        if person_id is None:
            persons = Person.objects.all()
            serializedPersons = PersonSerializer(persons, many=True)
            return Response(serializedPersons.data, status=200)
        else:
            person = Person.objects.get(person_id=int(person_id))
            serializedPerson = PersonSerializer(person)
            return Response(serializedPerson.data, status=200)

    def post(self, request):
        serializedPerson = PersonSimpleSerializer(data=request.data)
        if serializedPerson.is_valid():
            serializedPerson.save()
            return Response({
                "msg": "Person saved correctly",
                "user": "Wladymir"
            }, status=200)
        else:
            return Response({
                "msg": "Error while saving person",
                "user": "Wladymir",
                "errors": serializedPerson.errors
            }, status=200)


class SumView(APIView):

    def get(self, request):

        first_num = request.GET.get('first_num')
        second_num = request.GET.get('seccond_num')
        user = request.GET.get('user')

        if first_num is not None and second_num \
                is not None and user is not None:

            result = float(first_num)+float(second_num)
            return Response({
                "owner": "Wladymir",
                "result": result,
                "userMsg": "the solicitant was: "+user
            })
        else:
            return Response({
                "status": "one or some parameters where not provided"
            })

    def post(self, request):
        sum_arr = []
        operation = request.data["operation"]
        if operation != "float":
            sum_arr = [float(x) for x in request.data["values"]]
        else:
            sum_arr = request.data["values"]
        result = reduce(lambda acum, current: acum+current, sum_arr)
        return Response({
            "status": "OK",
            "result": result
        })


class ClientView(APIView):

    def get(self, request):
        param = request.GET.get('id')
        if param is None:
            clients = Client.objects.all()
            serializedClients = ClientSerializer(clients, many=True)
            return Response(serializedClients.data, status=200)
        else:
            client = Client.objects.get(client_id=int(param))
            serializedClient = ClientCompleteSerializer(client)
            return Response(serializedClient.data, status=200)

    def post(self, request):
        serializedClient = ClientSerializer(data=request.data)
        if serializedClient.is_valid():
            serializedClient.save()
            return Response({"status": "Client Saved Correctly"}, status=200)
        else:
            return Response({
                "error": True,
                "errors": serializedClient.errors
            })


class CityView(APIView):

    def get(self, request):
        param = request.GET.get('id')
        if param is None:
            cities = City.objects.all()
            serializedCities = CitySerializer(cities, many=True)
            return Response(serializedCities.data, status=200)
        else:
            city = City.objects.get(city_id=int(param))
            serializedCity = CitySerializer(city)
            return Response(serializedCity.data, status=200)

    def post(self, request):
        serializedCity = CitySerializer(data=request.data)
        if serializedCity.is_valid():
            serializedCity.save()
            return Response({"status": "City Saved Correctly"}, status=200)
        else:
            return Response({
                "error": True,
                "errors": serializedCity.errors
            })
