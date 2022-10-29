from django.urls import path
from api.views import registration_view

app_name = 'api'

urlpatterns =[
    path('register', registration_view, name='register')
]