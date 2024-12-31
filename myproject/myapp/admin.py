from django.contrib import admin
from .models import Login
from .models import User
from .models import Admin
from .models import Doctor
from .models import Appointment
from .models import Nurse
from .models import SupportStaff


admin.site.register(Login)
admin.site.register(User)
admin.site.register(Admin)
admin.site.register(Doctor)
admin.site.register(Appointment)
admin.site.register(Nurse)
admin.site.register(SupportStaff)
# Register your models here.

