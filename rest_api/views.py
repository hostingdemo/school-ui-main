from django.db.models.query import QuerySet
from student.models import Student,AdditionalDetails,Documents,ContactDetails,ParentDetails
from rest_api.Serializers import StudentSerializer,AdditionalDetailsSerializer,DoumentsSerializer,ContactDetailsSerializer,ParentDetailsSerializer
from rest_framework import serializers, viewsets, response
from rest_framework.decorators import action

class StudentViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

class AdditionalDetailsViewSet(viewsets.ModelViewSet):
    queryset=AdditionalDetails.objects.all()
    serializer_class=AdditionalDetailsSerializer

class DocumentsViewSet(viewsets.ModelViewSet):
    queryset=Documents.objects.all()
    serializer_class=DoumentsSerializer

class ContactDetailsViewSet(viewsets.ModelViewSet):
    queryset=Documents.objects.all()
    serializer_class=ContactDetailsSerializer

class ParentDetailsViewSet(viewsets.ModelViewSet):
    queryset=ParentDetails.objects.all()
    serializer_class=ParentDetailsSerializer
