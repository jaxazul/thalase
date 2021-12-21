from django.shortcuts import render
import django.template


# Create your views here.

def index(request):
    return render(request, 'notifications.html')

def doctors(request):
    return render(request, 'notification-doctor.html')