from django.shortcuts import render
from rest_framework.views import APIView 
from rest_framework.response import Response 
from .models import User
from .serializer import UserSerializer

import json
from django.http import JsonResponse

# Create your views here.
class HelloWorld(APIView): 
    def get(self, request): 
        print('Hello World!') 
        return Response({'message': 'Hello World!'}) 
    
class UserAPIView(APIView): 
    
    def get(self, request): 
        Users = User.objects.all() 
        serialzer = UserSerializer(Users, many=True) 
        return JsonResponse(serialzer.data, safe=False) 
    
    def get(self, request, *args, **kwargs): 
        pk = kwargs.get('pk', None) 
        try: 
            user = User.objects.get(pk=pk) 
            serilizer = UserSerializer(user, many=False) 
            return JsonResponse(serilizer.data, safe=False) 
        except:
            print('User not found') 
            return Response({'message': 'User not found'}, status=404) 
    
    def post(self, request): 
        body_unicode = request.body.decode('utf-8') 
        body = json.loads(body_unicode) 
        
        name = body.get('name', None) 
        email = body.get('email', None) 
        dob = body.get('dob', None) 
        
        user = User.objects.create(name=name, email=email, dob=dob)
        serializer = UserSerializer(user, many=False) 
        print('User created',serializer.data ) 
        return JsonResponse({ "message":"User created", "data": serializer.data })
    
    def put(self, request, *args, **kwargs): 
        pk = kwargs.get('pk', None) 
        body_unicode = request.body.decode('utf-8') 
        body = json.loads(body_unicode) 
        
        try: 
            user = User.objects.get(pk=pk) 
        except:
            print('User does not exist') 
            return Response({'message': 'User does not exist'}) 
        
        try: 
            user.name = body.get('name', None) 
            user.email = body.get('email', None) 
            user.dob = body.get('dob', None) 
            user.save() 
            return JsonResponse({'message': 'Updated User!'}) 
        except:
            return Response({'message': 'error in updating user data'}) 
        
    def delete(self, request, *args, **kwargs): 
        pk = kwargs.get('pk', None) 
        
        try: 
            user = User.objects.get(pk=pk) 
        except:
            return Response({'message': 'User not found'}) 
        
        User.delete(user)
        print('Updated User', user) 
        return JsonResponse({'message': 'Deleted User!'}) 