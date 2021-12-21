from django.urls import path

from . import views

urlpatterns = [
   path('', views.index, name='index'),
   path('add', views.add, name='add_complaint'),
   path('<int:id>/', views.complain, name='complain'),

]