from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.index, name="in"),
    path('create/', views.create, name="create"),
    path('logout/', views.logout),

]

