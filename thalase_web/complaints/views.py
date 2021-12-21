from django.shortcuts import render, redirect, get_object_or_404
import django.template
from django.contrib.auth import *
from django.contrib.auth.decorators import login_required
from .models import Complaint
from django.contrib import messages

# Create your views here.

@login_required(login_url='sign_in')
def index(request):
    user = request.user.username
    complaints = Complaint.objects.filter(username=user).order_by("-date_time")
    for complaint in complaints:
        print (complaint.title)

    return render(request, 'complaints.html', {'complaints':complaints})

def complain(request, id):
    complains = get_object_or_404(Complaint, pk=id)
    return render(request, 'single_complain.html', {'complain': complains})


@login_required(login_url='sign_in')
def add(request):
    if request.method == "POST":
        title = request.POST['title']
        description = request.POST['description']
        what_did_you_try = request.POST['try']

        user = request.user.username
        print(user)

        ins= Complaint(username=user, title=title, description=description, what_did_you_try=what_did_you_try)
        ins.save()
        messages.success(request, 'Complaint successfully logged')

        return redirect('/complaints')


    return render(request, 'add_complaint.html')