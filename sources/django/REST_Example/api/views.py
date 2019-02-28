# from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Person
from .serializers import PersonSerializer
from functools import reduce
# Create your views here.


class PersonView(APIView):

    def get(self, request, person_id):
        dummy = Person(person_id=person_id,
                       person_name='dummy_name',
                       person_birthDate='17-08-1997')
        serializer = PersonSerializer(dummy)
        return Response(serializer.data)


class SumView(APIView):

    def get(self, request):
        first_num = request.GET.get('first_num')
        second_num = request.GET.get('seccond_num')
        result = float(first_num)+float(second_num)
        return Response({
            "owner": "Wladymir",
            "result": result
        })

    def post(self, request):
        sum_arr = request.data["values"]
        result = reduce(lambda acum, current: acum+current, sum_arr)
        return Response({
            "status": "OK",
            "result": result
        })
