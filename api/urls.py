from django.urls import path
from api import views

app_name = 'api'

urlpatterns =[
    path('register', views.registration_view, name='register'),
    path('login', views.LoginView.as_view(), name ='login')
]