from django.contrib import admin
from django.urls import path, include
from . import views
app_name = "user"
urlpatterns = [
    path('/', views.loginregister, name="userLoginregister"),
    path('/home', views.home, name="userHome"),

    path('/login', views.loginUser, name="userLogin"),
    path('/logout', views.logoutUser, name="userLogout"),
    path('/register', views.register, name="userRegister"),

    path('/apply', views.apply, name="user-register"),
    path('/applyfir', views.applyFIR, name="userApplyFIR"),

    path('/my/<slug:slug>', views.userDashboard, name="userDashboard"),
    path('/fir/<slug:slug>', views.userFIR, name="userFIR"),


    path('/searchFIR', views.searchFIR, name="searchFIR"),
    path('/cancelFIR', views.cancelFIR, name="cancelFIR"),

    path('/otp', views.verifyotp, name="verifyotp"),





]