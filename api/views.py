from django.shortcuts import render
from django.conf import settings

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import  IsAuthenticated, AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.oauth2.client import OAuth2Client

from api.serializers import RegisterUserSerializer, UserProfileSerializer, GeneralTokenObtainSerializer


class GoogleLogin(SocialLoginView):
    authentication_classes = [] # disable authentication
    adapter_class = GoogleOAuth2Adapter
    callback_url = "http://localhost:3000"
    client_class = OAuth2Client

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

class LoginView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = GeneralTokenObtainSerializer

@api_view(['POST'])
def profile_view(request):
    pass
