from rest_framework import serializers
from .models import Person



#AN ABOUTUSER SERIALIZER IS CREATED FOR THE PERSON MODEL 
class AboutUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['First_name','Last_name','Email','Age','Income']