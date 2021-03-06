# from django.conf.urls import url
# from rest_framework.urlpatterns import format_suffix_patterns
from api import views
from django.urls import path

urlpatterns = [
    path('personAPI/person/',
         views.PersonView.as_view()),

    path('calculatorAPI/sum/',
         views.SumView.as_view()),

    path('dbAPI/client/',
         views.ClientView.as_view()),

    path('dbAPI/city/',
         views.CityView.as_view()),
]
