from django.urls import path
from api import views

app_name = 'api'

urlpatterns =[
    path('register/', views.registration_view, name='register'),
    path('login/', views.LoginView.as_view(), name ='login'),
    path('user_profile/<int:pk>', views.UserProfileView.as_view(), name='profile'),
    path('doctor_view/', views.XrayDoctor.as_view(), name='doctor_dashboard'),
    path('patient_view/', views.XrayPatient.as_view(), name='patient_dashboard'),
    # path('detail_view/<int:pk>', views.XrayDetail.as_view(), name='view_detail'),

]