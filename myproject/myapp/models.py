from django.db import models

# Create your models here.
class User(models.Model):
    full_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=10)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    user_role = models.CharField(max_length=100, choices=[('admin', 'Admin'), ('user', 'User'), ('nurse', 'Nurse'), ('support_staff', 'Support_staff'), ('doctor', 'Doctor')], default='user')

    def __str__(self):
        return self.full_name

# Create your models here. anushka@gmail.com  1234@1234  (user/admin/doctor/nurse/support_staff)
class Login(models.Model):
    email = models.EmailField(max_length=100, primary_key=True, unique=True) 
    password = models.CharField(max_length=255)
    user_role = models.CharField(max_length=100, choices=[('admin', 'Admin'), ('user', 'User'), ('nurse', 'Nurse'), ('support_staff', 'Support_staff'), ('doctor', 'Doctor')], default='user')

    def __str__(self):
        return self.email