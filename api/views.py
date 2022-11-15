from django.shortcuts import render
from django.conf import settings


from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import  IsAuthenticated, AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView

# from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
# from rest_auth.registration.views import SocialLoginView
# from allauth.socialaccount.providers.oauth2.client import OAuth2Client

<<<<<<< HEAD
from api.serializers import RegisterUserSerializer, UserProfileSerializer
=======
from api.serializers import RegisterUserSerializer, UserProfileSerializer, GeneralTokenObtainSerializer, XrayImages
from users.models import  UserProfile, Images
from api.permissions import DoctorPermission, PatientPermission

# class GoogleLogin(SocialLoginView):
#     authentication_classes = [] # disable authentication
#     adapter_class = GoogleOAuth2Adapter
#     callback_url = "http://localhost:3000"
#     client_class = OAuth2Client
>>>>>>> 9074060ab346af9be6dca56762f7741b3491eb54

@api_view(['POST'])
def registration_view(request):
    serializer = RegisterUserSerializer(data=request.data)
    data ={}

    if serializer.is_valid():
        user = serializer.save()
        data['response']= "successfully registered"
        data['email'] = user.email
        data['username'] = user.username

    else:
        data = serializer.errors
    return Response(data)

<<<<<<< HEAD

@api_view(['POST'])
def profile_view(request):
    pass
=======
class LoginView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = GeneralTokenObtainSerializer

class UserProfileView(generics.UpdateAPIView):
    queryset = UserProfile.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = UserProfileSerializer



class XrayPatient(APIView):

    permission_classes = (IsAuthenticated, PatientPermission,)
    def get(self, request, format=None):
        images = Images.objects.filter(patient=request.user.id)
        serializer = XrayImages(images, many=True)
        return Response(serializer.data)


class XrayDoctor(APIView):

    permission_classes = (IsAuthenticated, DoctorPermission,)
    def get(self, request, format=None):
        images = Images.objects.filter(doctor=request.user.id)
        serializer = XrayImages(images, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = XrayImages(data=request.data)
        data={}
        if serializer.is_valid():
            image = serializer.save()
            data['response'] = "Successfully submitted image"
            data['patient_name'] = image.patient.username
            data['patient_id'] = image.patient.id
            data['doctor_name'] = image.doctor.username
            data['doctor_id'] = image.doctor.id
            data['xray_path'] = image.x_ray.path
            data['xray_id'] = image.id
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class XrayDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    permission_classes = (IsAuthenticated)
    def get_object(self, pk):
        try:
            return Images.objects.get(pk=pk)
        except Images.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        image = self.get_object(pk)
        if request.user.id == image.patient.id or request.user.id == image.doctor.id:
            serializer = XrayImages(image)
            return Response(serializer.data)


    def delete(self, request, pk, format=None):
        if request.user.user_type == 'Dr' and request.user.is_verified == True:
            image = self.get_object(pk)
            image.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response("Cannot Delete by Patient or unverified Doctor")
>>>>>>> 9074060ab346af9be6dca56762f7741b3491eb54
