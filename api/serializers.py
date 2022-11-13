from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from users.models import User, UserProfile


class RegisterUserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only = True)
    class Meta:
        model = User
        fields = ['email', 'first_name','last_name', 'username','password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }
    # def validate(self, attrs):
    #     if attrs['password'] != attrs['password2']:
    #         raise serializers.ValidationError(
    #             {"password": "Passwords don\'t match"}
    #         )
    # def save(self):
    #     password = self.validated_data['password']
    #     user = User.objects.create_user(email=self.validated_data['email'],
    #                 username=self.validated_data['username'],)
    #     user.first_name = self.validated_data['first_name']
    #     user.last_name= self.validated_data['last_name'],
    #     user.set_password(password)
    #     user.save()

    def save(self):
        user = User(email=self.validated_data['email'],
                    username=self.validated_data['username'],)
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
        exclude = ('phone_regex', 'is_verified')
        extra_kwargs = {
            'license_photo': {'required': False},
            'hospital_name': {'required': False},
        }

    def validate(self, data):
        data_dict = dict(data)
        data_keys = data.keys()
        account_type = data_dict.get('user_type')
        if account_type == 'Dr' and 'license_photo' not in data_keys:
            raise serializers.ValidationError('License photo required to submit form as Doctor.')
        if account_type == 'Dr' and 'hospital_name' not in data_keys:
            raise serializers.ValidationError('Hospital name required to submit form as Doctor.')
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

