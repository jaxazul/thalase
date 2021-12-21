from django.db import models
from django.db import models
from django.contrib.auth.models import User

class EmergencyContacts(models.Model):
    username = models.CharField(primary_key=True, max_length=300)
    emergency_name_1 = models.CharField(max_length=300)
    emergency_phone_1 = models.CharField(max_length=300)
    emergency_email_1 = models.CharField(max_length=300)
    emergency_name_2 = models.CharField(max_length=300)
    emergency_phone_2 = models.CharField(max_length=300)
    emergency_email_2 = models.CharField(max_length=300)
    emergency_name_3 = models.CharField(max_length=300)
    emergency_phone_3 = models.CharField(max_length=300)
    emergency_email_3 = models.CharField(max_length=300)

    class Meta:
        managed = False
        db_table = 'emergency_contacts'




class PatientMedical(models.Model):
    username = models.CharField(primary_key=True, max_length=300)
    birthdate = models.CharField(max_length=250)
    weight = models.CharField(max_length=250)
    height = models.CharField(max_length=250)
    gender = models.CharField(max_length=250)
    blood_type = models.CharField(max_length=250)
    blood_group = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'patient_medical'


class Tips(models.Model):
    tip = models.CharField(max_length=300)
    source = models.CharField(max_length=300)

    class Meta:
        managed = False
        db_table = 'tips'


class DoctorInfo(models.Model):
    username = models.CharField(primary_key=True, max_length=300)
    mscn_number = models.CharField(max_length=300)
    gender = models.CharField(max_length=300)
    birthday = models.CharField(max_length=300)

    class Meta:
        managed = False
        db_table = 'doctor_info'

