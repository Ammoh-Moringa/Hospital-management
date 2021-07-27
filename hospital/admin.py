from hospital.models import Bed, Doctor, Patient
from django.contrib import admin

# Register your models here.
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Bed)
