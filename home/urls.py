from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('', views.index, name='index'),  # Home page
    path('patient-login/', views.patient_login, name='patient_login'),  # Patient login URL
    path('doctor-login/', views.doctor_login, name='doctor_login'),  # Doctor login URL
    path('patient-dashboard/', views.patient_dashboard, name='patient_dashboard'),  # Patient dashboard URL
    path('doctor-dashboard/', views.doctor_dashboard, name='doctor_dashboard'),  # Doctor dashboard URL
    path('signup/', views.signup, name='signup'),
]
