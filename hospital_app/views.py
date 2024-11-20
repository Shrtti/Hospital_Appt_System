from django.shortcuts import render, redirect
from .forms import PatientForm, DoctorForm, StaffForm, HospitalForm  
from .models import Patient, Doctor, Staff, Hospital
from django.contrib.auth.hashers import make_password


def home(request):
    return render(request, 'hospital_app/index.html')

def home_page(request):
    return render(request, 'hospital_app/home_page.html')

def p_regist(request):
    if request.method == 'POST':
        name = request.POST.get('pat_name')
        print(f"Name: {name}") 
        ph_no = request.POST.get('pat_phno')
        print(f"Phone Number: {ph_no}")
        passw = request.POST.get('pat_pwd')
        print(f"Password: {passw}")  
        
        data=Patient.objects.create_patient(name, ph_no, passw)
        data.save()
        return redirect('home_page')
    
    return render(request, 'hospital_app/Patient_regist.html')

def d_regist(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid(): 
            doctor = form.save(commit=False)  
            doctor.password = make_password(form.cleaned_data['password'])  
            doctor.save()
              
            return redirect('hospital_app/home_page')
    else:
        form = DoctorForm()  
    return render(request, 'hospital_app/doctor_regist.html', {'form': form})

def s_regist(request):
    if request.method == 'POST':
        form = StaffForm(request.POST)
        if form.is_valid(): 
            staff = form.save(commit=False)  
            staff.password = make_password(form.cleaned_data['password'])  
            staff.save()
              
            return redirect('hospital_app/home_page')
    else:
        form = DoctorForm()  
    return render(request, 'hospital_app/staff_regist.html', {'form': form})

def h_regist(request):
    if request.method == 'POST':
        name = request.POST.get('h_name')
        ph_no = request.POST.get('h_phno')
        add = request.POST.get('h_add')
        passw = request.POST.get('h_pwd')
          
        
        data=Hospital.objects.create_hospital(name, ph_no, add, passw)
        data.save()
        return redirect('hospital_edit')
    
    return render(request, 'hospital_app/Patient_regist.html')

def h_edit(request):
    return render(request, 'hospital_app/hospital_edit.html')

def add_dept(request):
    return render(request, 'hospital_app/add_dept.html')

def appt(request):
    return render(request, 'hospital_app/appointment.html')


