from django.shortcuts import render, redirect, get_object_or_404
from twilio.rest import Client
import django.template
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
import smtplib

from django.contrib.auth import *
from django.contrib.auth.decorators import login_required
from .models import Tips, PatientMedical, EmergencyContacts, DoctorInfo
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages

import random


# Create your views here.

@login_required(login_url='sign_in')
def index(request):
    n1 = random.randint(1, 10)
    n2 = random.randint(1, 10)

    if n2 == n1:
        n2 = n2 - 2

    tip1 = Tips.objects.get(id=n1)
    tip2 = Tips.objects.get(id=n2)

    return render(request, 'dashboard.html', {'tip1': tip1, 'tip2': tip2})


@login_required(login_url='sign_in')
def dashboard_doctor(request):
    n1 = random.randint(1, 10)
    n2 = random.randint(1, 10)

    if n2 == n1:
        n2 = n2 - 2

    tip1 = Tips.objects.get(id=n1)
    tip2 = Tips.objects.get(id=n2)
    return render(request, 'dashboard_doctor.html', {'tip1': tip1, 'tip2': tip2})


def sign_up(request):
    if request.method == "POST":
        birthdate = request.POST['dob']
        weight = request.POST['weight']
        height = request.POST['height']
        gender = request.POST['gender']
        blood_type = request.POST['blood_type']
        blood_group = request.POST['blood_group']

        emergency_name_1 = request.POST['cname_1']
        emergency_phone_1 = request.POST['cphone_1']
        emergency_email_1 = request.POST['cemail_1']
        emergency_name_2 = request.POST['cname_2']
        emergency_phone_2 = request.POST['cphone_2']
        emergency_email_2 = request.POST['cemail_2']
        emergency_name_3 = request.POST['cname_3']
        emergency_phone_3 = request.POST['cphone_3']
        emergency_email_3 = request.POST['cemail_3']

        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')

            ins = PatientMedical(username=user, birthdate=birthdate, weight=weight,
                                 height=height, gender=gender, blood_type=blood_type,
                                 blood_group=blood_group)
            ins.save()

            ins2 = EmergencyContacts(username=user, emergency_name_1=emergency_name_1,
                                     emergency_phone_1=emergency_phone_1, emergency_email_1=emergency_email_1,
                                     emergency_name_2=emergency_name_2, emergency_phone_2=emergency_phone_2,
                                     emergency_email_2=emergency_email_2,
                                     emergency_name_3=emergency_name_3, emergency_phone_3=emergency_phone_3,
                                     emergency_email_3=emergency_email_3)
            ins2.save()

        return redirect('/sign_in')

    form = CreateUserForm()
    context = {'form': form}
    return render(request, "sign-up.html", context)


def sign_up_doctor(request):
    if request.method == 'POST':
        birthdate = request.POST['dob']
        mscn = request.POST['lics']
        gender = request.POST['gender']
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            ins = DoctorInfo(username=user, mscn_number=mscn, gender=gender, birthday=birthdate)
            ins.save()

            messages.success(request, 'Account was created for' + user)
            return redirect('sign_in')

    form = CreateUserForm()
    context = {'form': form}
    return render(request, "sign-up-doctor.html", context)


def sign_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            # doctor = DoctorInfo.objects.get(username=user)
            # patient = PatientMedical.objects.get(username= user)
            # print(doctor)
            # print(patient)
            try:
                DoctorInfo.objects.get(username=user)
                login(request, user)
                return redirect('/dashboard_doctor')
            except ObjectDoesNotExist:
                login(request, user)
                return redirect('/')

            # if DoctorInfo.objects.get(username=user):
            #     login(request, user)
            #     return redirect('/dashboard_doctor')
            # else:
            #     login(request, user)
            #     return redirect('/')

        else:
            messages.info(request, 'Username or Password is Incorrect')

    context = {}
    return render(request, "sign-in.html", context)


def logoutuser(request):
    logout(request)
    return redirect('/sign_in')


@login_required(login_url='sign_in')
def profile(request):
    user = request.user.username
    user_pro = request.user
    profiles = PatientMedical.objects.get(username=user)
    emergency = EmergencyContacts.objects.get(username=user)

    return render(request, 'profile.html', {"user_pro": user_pro, 'profile': profiles, 'emergency': emergency})


@login_required(login_url='sign_in')
def profile_doctor(request):
    user = request.user.username
    user_pro = request.user
    profiles = DoctorInfo.objects.get(username=user)

    return render(request, 'profile_doctor.html', {"user_pro": user_pro, 'profile': profiles})


@login_required(login_url='sign_in')
def emergency(request):
    user = request.user.username
    emergency = EmergencyContacts.objects.get(username=user)
    email = [emergency.emergency_email_1, emergency.emergency_email_2, emergency.emergency_email_3]
    print(email)

    # sender_email = "olugbilehassan@gmail.com"
    # rec_email = "olugbileabisoye@outlook.com"
    # password = "irtmzjtapmikniae"
    # message = "Hello," + request.user.first_name + " is in distress please reach out now"
    # server = smtplib.SMTP('smtp.gmail.com', 587)
    # server.starttls()
    # server.login(sender_email, password)
    # print("Login success")
    # server.sendmail(sender_email, rec_email, message)
    # print("Email has been sent to ", rec_email)

    for emails in email:
        sender_email = "olugbilehassan@gmail.com"
        rec_email = emails
        password = "irtmzjtapmikniae"
        message = "Hello," + request.user.first_name + " is in distress please reach out now"
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)
        print("Login success")
        server.sendmail(sender_email, rec_email, message)
        print("Email has been sent to ", rec_email)

    phone = [emergency.emergency_phone_1, emergency.emergency_phone_2, emergency.emergency_phone_3]

    print(phone)
    # account_sid = 'AC5413a5a7d7633e1503107db2ba704bfb'
    # auth_token = 'c002d5ab939abb3d45a1c112cc247bb7'
    # client = Client(account_sid, auth_token)
    #
    # message = client.messages.create(
    #     body='hello there, hasssan is in distress',
    #     from_='+19088834650',
    #     to='+2348123205857'
    # )
    # print(message.sid)
    return render(request, "emergency.html", {'emergency': emergency})


@login_required(login_url='sign_in')
def messages(request):
    return render(request, 'messages.html')
