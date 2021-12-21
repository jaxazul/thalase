# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Blog(models.Model):
    author = models.CharField(max_length=300)
    title = models.CharField(max_length=300)
    content = models.TextField()
    datetime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'blog'


class Complaint(models.Model):
    username = models.CharField(max_length=300)
    title = models.CharField(max_length=300)
    description = models.CharField(max_length=300)
    what_did_you_try = models.CharField(max_length=300)
    date_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'complaint'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class DoctorInfo(models.Model):
    username = models.CharField(primary_key=True, max_length=300)
    mscn_number = models.CharField(max_length=300)
    gender = models.CharField(max_length=300)
    birthday = models.CharField(max_length=300)

    class Meta:
        managed = False
        db_table = 'doctor_info'


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
