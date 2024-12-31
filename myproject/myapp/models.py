from django.db import models

# Create your models here. anushka@gmail.com  1234@1234
class Login(models.Model):
    email = models.EmailField(max_length=100, primary_key=True, unique=True) 
    password = models.CharField(max_length=255)
    user_role = models.CharField(max_length=15, choices=[('admin', 'Admin'), ('user', 'User'), ('nurse', 'Nurse'), ('support_staff', 'Support_staff'), ('doctor', 'Doctor')], default='user')

    def __str__(self):
        return self.email


# Create your models here.
class User(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    password = models.CharField(max_length=255)
    appointment_no = models.IntegerField(default=0)

    def __str__(self):
        return self.email

class Admin(models.Model):
    a_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.a_id


class Doctor(models.Model):
    d_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=10)
    birthday = models.DateField(max_length=10)
    specialization = models.CharField(max_length=255)
    consultation_fee = models.DecimalField(max_digits=10, decimal_places=2)
    availability_status = models.BooleanField(default=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    password = models.CharField(max_length=255)
    n_id = models.CharField(max_length=100)

    def __str__(self):
        return self.d_id


class Nurse(models.Model):
    n_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=10)
    birthday = models.DateField(max_length=10)
    address = models.TextField(max_length=400)
    shifts = models.CharField(max_length=255)
    availability_status = models.BooleanField(default=True)
    position = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    password = models.CharField(max_length=255)
    d_id = models.CharField(max_length=100)

    def __str__(self):
        return self.n_id


class SupportStaff(models.Model):
    s_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    birthday = models.DateField(max_length=10)
    availability_status = models.BooleanField(default=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.s_id


class Appointment(models.Model):
    app_id = models.AutoField(primary_key=True)
    patient_name = models.CharField(max_length=255)
    patient_age = models.IntegerField()
    appointment_date = models.DateField(max_length=10)
    clinic_date = models.DateField(max_length=10)
    appointment_status = models.CharField(max_length=100, choices=[('pending', 'Pending'), ('completed', 'Completed')])
    d_id = models.CharField(max_length=100)

    def __str__(self):
        return self.app_id


class contact_us(models.Model):
    c_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.CharField(max_length=1000)

    def __str__(self):
        return self.c_id