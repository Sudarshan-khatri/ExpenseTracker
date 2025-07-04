from rest_framework import serializers
from django.contrib.auth.models import User




class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['first_name','last_name','username','email','password']

    def create(self,valiadated_data):
        user=User.objects.create_user(
            username=valiadated_data['username'],
            first_name=valiadated_data['first_name'],
            last_name=valiadated_data['last_name'],
            email=valiadated_data['email'],
            password=valiadated_data['password'],
        )
        return user 
    
class LoginSerializer(serializers.Serializer):
    username=serializers.CharField(required=True)
    password=serializers.CharField(required=True)
