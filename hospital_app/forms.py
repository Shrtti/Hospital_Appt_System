from django import forms
from .models import Patient, Doctor, Staff, Hospital  

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['pat_name', 'pat_phno', 'pat_pwd']  

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['dr_name', 'dr_phno', 'dept','dr_pwd']  

class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ['staff_name', 'staff_phno', 'dept','staff_pwd']  

class HospitalForm(forms.ModelForm):
    class Meta:
        model = Hospital
        fields = ['hospital_name', 'hospital_add', 'hospital_phno', 'hosp_pwd']  

