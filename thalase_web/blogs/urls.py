from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add, name='add_blog'),
    path('<int:id>/', views.blog, name='blog'),

]