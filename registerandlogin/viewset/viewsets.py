from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.contrib.auth import authenticate
from ..serializer.serializers import RegisterSerializer,LoginSerializer




class RegisterViewset(generics.CreateAPIView):
    queryset=User.objects.all()
    serializer_class=RegisterSerializer
    permission_classes=[AllowAny]
    



class LoginViewset(generics.CreateAPIView):
    serializer_class=LoginSerializer
    permission_classes=[AllowAny]


    def post(self, request):
        username=request.data.get('username')
        password=request.data.get('password')

       

        if not username or not password:
            return Response({'error':'Username or password required'},status=400)
        
        user=authenticate(username=username,password=password)
        
        if user is not None:
            refresh=RefreshToken.for_user(user)
            user_serializer=RegisterSerializer(user) 
            return Response({
                'refresh':str(refresh),
                'access':str(refresh.access_token),
                'user':user_serializer.data,
            })
        return Response({'message':'Invalid credentials'},status=401)

        

