from django.shortcuts import render, redirect
from django.contrib import messages
#from django.contrib.auth.models import User  # Assuming you're using the built-in User model
from django.core.exceptions import ValidationError
import re
from myapp.models import User
from myapp.models import Login

def index(request):
    return render(request, 'index.html')

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            login = Login.objects.get(email=email, password=password)  #(user/admin/doctor/nurse/support_staff)
            print(login.user_role)
            if login.user_role == 'admin':
                return redirect('admin_dashboard')
            elif login.user_role == 'user':
                return redirect('home')
            elif login.user_role == 'nurse':
                return redirect('home')
            elif login.user_role == 'support_staff':
                return redirect('home')
            elif login.user_role == 'doctor':
                return redirect('home')
        except Login.DoesNotExist:
            messages.error(request, 'Invalid email or password.')
            return redirect('login')


    return render(request, 'login.html')

# Custom function to validate phone numbers (10 digits)
def validate_phone_number(phone):
    if not re.match(r'^\d{10}$', phone):
        raise ValidationError("Please enter a valid 10-digit phone number.")

def sign_up(request):
    data = User.objects.all()  # Get existing users
    context = {
        'data': data
    }

    if request.method == 'POST':
        full_name = request.POST.get('full-name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')


        # Full name validation
        if not full_name:
            context['full_name_error'] = "Full name is required."
        
        # Email validation
        try:
            # Django's built-in email validation
            User.objects.get(email=email)  # Check if the email already exists
            context['email_error'] = "Email already exists."
        except User.DoesNotExist:
            if not email or '@' not in email:
                context['email_error'] = "Please enter a valid email address."

        # Phone number validation (should be exactly 10 digits)
        try:
            validate_phone_number(phone)
        except ValidationError as e:
            context['phone_error'] = str(e)

        # Password validation (at least 6 characters)
        if len(password) < 6:
            context['password_error'] = "Password must be at least 6 characters long."

        # If there are any validation errors, return the user back to the form
        if context.get('full_name_error') or context.get('email_error') or context.get('phone_error') or context.get('password_error'):
            return render(request, 'sign_up.html', context)

        # If no errors, create the user and save
        user = User(full_name=full_name, phone=phone, email=email, password=password, user_role='user')
        login = Login(email=email, password=password, user_role='user')
        user.save()
        login.save()

        messages.success(request, 'Registration successful! You can now log in.')


    return render(request, 'sign_up.html', context)

def user_profile(request):
    return render(request, 'user_profile.html')

def home(request):
    return render(request, 'home.html')

def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')