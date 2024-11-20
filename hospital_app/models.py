from django.db import models
from django.contrib.auth.hashers import make_password

from django.db import models

class Hospital(models.Model):
    hospital_id = models.AutoField(primary_key=True)
    hospital_name = models.CharField(max_length=100)
    hospital_add = models.CharField(max_length=255)
    hospital_phno = models.CharField(max_length=15, null=True, blank=True)
    hosp_pwd = models.CharField(max_length=128, default=make_password('default_password')) 

    class Meta:
        db_table = 'hospital_app_hospital'

    def __str__(self):
        return self.hospital_name

class Dept(models.Model):
    dept_id = models.AutoField(primary_key=True)
    dept_name = models.CharField(max_length=100)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    def __str__(self):
        return self.dept_name


class Staff(models.Model):
    staff_id = models.AutoField(primary_key=True)
    staff_name = models.CharField(max_length=100)
    staff_phno = models.CharField(max_length=15, null=True, blank=True)
    dept = models.ForeignKey(Dept, on_delete=models.CASCADE)
    staff_pwd = models.CharField(max_length=128, default=make_password('default_password')) 

    class Meta:
        db_table = 'hospital_app_staff'
    def __str__(self):
        return self.staff_name


class Doctor(models.Model):
    dr_id = models.AutoField(primary_key=True)
    dr_name = models.CharField(max_length=100)
    dr_phno = models.CharField(max_length=15, null=True, blank=True)
    dept = models.ForeignKey(Dept, on_delete=models.CASCADE)
    dr_pwd = models.CharField(max_length=128, default=make_password('default_password')) 
    class Meta:
        db_table = 'hospital_app_doctor'

    def __str__(self):
        return self.dr_name

class PatientManager(models.Manager):
    def create_patient(self, name, ph_no, password=None):
        if not name:
            raise ValueError('Patients must have a name')

        if not ph_no:
            raise ValueError('Patients must have a phone number')

        patient = self.model(
            pat_name=name,
            pat_phno=ph_no
        )

        if password:
            patient.pat_pwd = make_password(password)
        else:
            patient.pat_pwd = make_password('default_password')

        patient.save(using=self._db)
        return patient

class Patient(models.Model):
    
    pat_id = models.AutoField(primary_key=True)
    pat_name = models.CharField(max_length=100)
    pat_phno = models.CharField(max_length=15, null=True, blank=True)
    pat_pwd = models.CharField(max_length=128, default=make_password('default_password'))

    objects = PatientManager()

    class Meta:
        db_table = 'hospital_app_patient'

    def __str__(self):
        return self.pat_name

    @property
    def password(self):
        raise AttributeError("Password is not accessible")



class Appointment(models.Model):
    appt_id = models.AutoField(primary_key=True)
    pat = models.ForeignKey(Patient, on_delete=models.CASCADE)
    dr = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()

    class Meta:
        db_table = 'hospital_app_appointment'

    def __str__(self):
        return f"Appointment {self.appt_id} - {self.pat} with {self.dr}"

class Presc(models.Model):
    pres_no = models.AutoField(primary_key=True)
    pat = models.ForeignKey(Patient, on_delete=models.CASCADE)
    med_name = models.CharField(max_length=100)
    date = models.DateField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Prescription {self.pres_no} for {self.pat}"

class Invoice(models.Model):
    invoice_no = models.AutoField(primary_key=True)
    pat = models.ForeignKey(Patient, on_delete=models.CASCADE)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Invoice {self.invoice_no} for {self.pat}"

