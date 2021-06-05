from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.register, name="reg"),
    path('login/',views.Mlogin, name="login"),
    path('index/login',views.Mlogin, name="Ain"),
    path('account/rib',views.getId, name="rib"),
    path('account/solde',views.getSolde , name="solde"),
    path('account/update',views.update , name="update"),
    path('account/dotationE',views.dotationE , name="dotationE"),
    path('account/aT',views.aT , name="aT"),
    path('account/aE',views.aE , name="aE"),
    path('account/cheque',views.cheque , name="cheque"),
    path('account/c',views.c , name="c"),
    path('account/reclamation',views.reclamation , name="reclamation"),
    path('account/telephonique',views.tele , name="tele"),
    path('account/hT',views.hT , name="hT"),
    path('account/hF',views.hF , name="hF"),
    path('account/facture',views.facture , name="facture"),
    path('account/home',views.home , name="home"),
    path('account/conseille',views.conseille , name="conseille"),

]
