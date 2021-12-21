from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('sign_up_doctors/', views.sign_up_doctor, name='sign_up_doctor'),
    path('sign_in/', views.sign_in, name='sign_in'),
    path('log_out/', views.logoutuser, name='log_out'),
    path('profile/', views.profile, name= 'profile'),
    path('emergency/', views.emergency, name= 'emergency'),
    path('dashboard_doctor/', views.dashboard_doctor, name='dashboard_doctor'),
    path('profile_doctor/', views.profile_doctor, name='profile_doctor'),
    path('messages/', views.messages, name = 'message')


]