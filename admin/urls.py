from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
path('admins/index/', views.index, name="Aindex"),
path('admins/cip', views.cip, name="cip"),
path('admins/update/<str:pk>', views.update, name="update"),
path('admins/delete/<str:pk>', views.delete, name="delete"),
path('admins/create', views.create, name="Acreate"),
path('admins/logout', views.logout, name="logout"),
path('admins/Acheque', views.Acheque, name="Acheque"),
path('admins/AcC/<str:pk>', views.AcC, name="AcC"),
path('admins/ReC/<str:pk>', views.ReC, name="ReC"),
path('admins/Arec', views.Arec, name="Arec"),
path('admins/deleteR/<str:pk>', views.deleteR, name="deleteR"),
path('/', views.index),


]
