from django.db import models


# Create your models here.
class Doctor(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Patient(models.Model):
    patient_name = models.CharField(max_length=50)
    phone_no = models.CharField(max_length=15)
    kin = models.CharField(max_length=50, null=True)
    kin_phone_no = models.CharField(max_length=15, null=True)
    address = models.TextField()
    SYMPTOMS =models.CharField(max_length=500, null=True)
    bed_num = models.ForeignKey("Bed", on_delete=models.CASCADE)
    prior_sickness = models.TextField()
    dob = models.DateField(null=True)
    doctor = models.ForeignKey("Doctor", on_delete=models.CASCADE, null=True)
    doctors_notes =models.CharField(max_length=50, null=True)
    doctors_visiting_time = models.CharField(null=True, max_length=50, blank=True)
    status = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
        
class Bed(models.Model):
    bed_number = models.CharField(max_length=50)
    occupied = models.BooleanField()
    def __str__(self):
        return self.bed_number


