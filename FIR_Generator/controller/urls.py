from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "controller"
urlpatterns = [
    path('', views.loginregister, name="controllerLoginregister"),
    path('/home', views.homeController, name="controllerHome"),

    path('/login', views.loginController, name="controllerLogin"),
    path('/logout', views.logoutController, name="controllerLogout"),


    path('/searchFIR', views.searchFIR, name="searchFIR"),
    path('/manageSHO', views.manageSHO, name="manageSHOaccount"),
    path('/viewSHO/<slug:slug>', views.viewSHOdetails, name="viewSHOdetails"),
    path('/createsho', views.createSHO, name="newSHOaccount"),
    path('/editSHO', views.editSHO, name="editSHOaccount"),
    path('/newsho', views.newSHO, name="newsho"),
    path('/deleteSHOaccount/<slug:slug>', views.deleteSHO, name="deleteSHOaccount"),

]