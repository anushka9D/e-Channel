from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

# Create your models here. anushka@gmail.com  1234@1234
class Login(models.Model):
    email = models.EmailField(max_length=100, primary_key=True, unique=True) 
    password = models.CharField(max_length=255)
    user_role = models.CharField(max_length=10, choices=[('admin', 'Admin'), ('user', 'User')], default='user')

    def __str__(self):
        return self.email