from rest_framework import serializers
from django.contrib.auth import get_user_model

from users.models import User


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