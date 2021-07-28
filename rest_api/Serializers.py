from django.contrib.auth import models
from student.models import Student,Documents,ParentDetails,ContactDetails,AdditionalDetails
from rest_framework import serializers

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'

class ContactDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=ContactDetails
        fields='__all__'

class ParentDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=ParentDetails
        fields='__all__'

class AdditionalDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=AdditionalDetails
        fields='__all__'

class DoumentsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Documents
        fields='__all__'

