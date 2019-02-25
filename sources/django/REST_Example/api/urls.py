# from django.conf.urls import url
# from rest_framework.urlpatterns import format_suffix_patterns
from api import views
from django.urls import path

urlpatterns = [
    path('personAPI/getDummyObj/<int:person_id>',
         views.PersonView.as_view()),

    path('calculatorAPI/sum/<str:first_num>&<str:second_num>',
         views.SumView.as_view()),

]
