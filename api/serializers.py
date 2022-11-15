from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from users.models import UserProfile, Images


class RegisterUserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = UserProfile
        fields = ['email', 'first_name', 'last_name', 'username', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True},
            'email': {'required': True}
        }

    def create(self, validated_data):
        user = UserProfile(email=self.validated_data['email'],
                           username=self.validated_data['username'], )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        first_name = self.validated_data['first_name']
        last_name = self.validated_data['last_name']
        if password != password2:
            raise serializers.ValidationError({'password do not match'})
        user.set_password(password)
        user.save()
        return user


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        exclude = ('is_verified',)
        extra_kwargs = {
            'license_photo': {'required': False},
            'hospital_name': {'required': False},
            'user_type': {'required': True},
            'contact_number': {'required': True},
            'country': {'required': True},
            'city': {'required': True},
        }

    def validate(self, data):
        data_dict = dict(data)
        data_keys = data.keys()
        account_type = data_dict.get('user_type')
        if account_type == 'Dr' and 'license_photo' not in data_keys:
            raise serializers.ValidationError('License photo required to submit form as Doctor.')
        if account_type == 'Dr' and 'hospital_name' not in data_keys:
            raise serializers.ValidationError('Hospital name required to submit form as Doctor.')

        if account_type == 'Pt' and 'license_photo' in data_keys:
            raise serializers.ValidationError('Patients cannot have liscence photo')
        return data

    def create(self, validated_data):
        return UserProfile(**validated_data)


class GeneralTokenObtainSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super(GeneralTokenObtainSerializer, self).validate(attrs)
        data.update({'user': self.user.username})
        data.update({'id': self.user.id})
        data.update({'user_type': self.user.user_type})
        return data


class XrayImages(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = '__all__'

    def create(self, validated_data):
        image = Images(
            x_ray=self.validated_data['x_ray'],
            doctor=self.validated_data['doctor'],
            patient=self.validated_data['patient'])
        image.save()

        return image

    def validate(self, attrs):
        data = super(XrayImages, self).validate(attrs)
        # data.update({'patient': data.patient.username})
        # data['patient_id'] = data.patient.id
        # data.update({'doctor': data.doctor.username})
        # data['doctor_id']= data.doctor.id
        # data['xray_id']= data.id
        # data['xray_path']: data.x_ray
        return data
