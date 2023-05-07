from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "sho"
urlpatterns = [
    path('/', views.loginregister, name="shoLoginregister"),
    path('/home/<slug:slug>', views.homeSHO, name="shoHome"),

    path('/login', views.loginSHO, name="shoLogin"),
    path('/logout', views.logoutSHO, name="shoLogout"),

    path('/pending/<slug:slug>', views.pendingFIR, name="pendingFIR"),
    path('/fir/<slug:slug>', views.viewPendingFIR, name="viewPendingFIR"),
    path('/fir/approve/<slug:slug>', views.approvePendingFIR, name="approvePendingFIR"),
    path('/fir/solved/<slug:slug>', views.markSolvedFIR, name="markSolvedFIR"),



    path('/approved/<slug:slug>', views.approvedFIR, name="approvedFIR"),

    path('/searchFIR', views.searchFIR, name="searchFIR"),

    path('/solved/<slug:slug>', views.solvedFIR, name="solvedFIR"),
    

]