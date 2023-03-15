from rest_framework import serializers 
from helloapi.models import User 

class UserSerializer(serializers.ModelSerializer):
    class Meta: 
        model = User 
        fields = ['name', 'email', 'dob']