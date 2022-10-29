from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view

from api.serializers import RegisterUserSerializer

@api_view(['POST'])
def registration_view(request):
    serializer = RegisterUserSerializer(data=request.data)
    data ={}

    if serializer.is_valid():
        user = serializer.save()
        data['response']= "successfully registered"
        data['email'] = user.email

    else:
        data = serializer.errors
    return Response(data)
