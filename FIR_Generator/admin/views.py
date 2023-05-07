from django.shortcuts import render, redirect, HttpResponse,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from user.models import FIR
from datetime import datetime
# Create your views here.
def loginregister(request):
    return render(request, "admin/loginregistration.html")

def homeAdmin(request,slug):
    user = get_object_or_404(User, username = slug)
    station = user.first_name
    pincode = user.last_name
    context = { 'station':station, 'pincode': pincode}
    return render(request, 'sho/landing.html', context)

def loginAdmin(request):

    if request.method == "POST":

        email = request.POST['email']
        loginpassword = request.POST['password']
       
        UserData = get_object_or_404(User, email = email)
        
        if UserData is None:
            messages.error(request, "Invalid Credentials, Please check and retry again")
            
            return render('admin:adminLoginregister') 
        username = UserData.username 
            

        user = authenticate(username = username, password = loginpassword)
        
        if user is None:
            messages.error(request, "Invalid Credentials, Please check and retry again")
            
            return redirect('admin:adminLoginregister')         
        else:
            login(request,user)
            station = user.first_name
            pincode = user.last_name
            
            messages.success(request, "Successfully Logged In")
            context = {'user':username,'email':email, 'station':station, 'pincode': pincode}
            
          
            return render(request,'admin/landing.html', context)
    else:
        return redirect('admin:adminLoginregister')
 