from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.loginregister, name="adminLoginregister"),
    path('/home/<slug:slug>', views.homeAdmin, name="adminHome"),

    path('/login', views.loginAdmin, name="adminLogin"),
    path('/logout', views.logoutAdmin, name="adminLogout"),


]