from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('patients_registration/', views.p_regist, name='patient_registration'),
    path('doctor_registration/', views.d_regist, name='doctor_registration'),
    path('staff_registration/', views.s_regist, name='staff_registration'),
    path('hospital_registration/', views.h_regist, name='hospital_registration'),  # Add the name here
    path('hospital_edit/', views.h_edit, name='hospital_edit'),
    path('home_page/', views.home_page, name='home_page'),
    path('add_department/', views.add_dept, name='add_department'),
    path('appointment/', views.appt, name='appointment'),
]
