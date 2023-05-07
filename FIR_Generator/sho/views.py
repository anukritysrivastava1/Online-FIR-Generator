from django.shortcuts import render, redirect, HttpResponse,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from user.models import FIR
from datetime import datetime

# Create your views here.
def loginregister(request):
    return render(request, "sho/loginregistration.html")

def homeSHO(request,slug):
    user = get_object_or_404(User, username = slug)
    station = user.first_name
    pincode = user.last_name
    context = { 'station':station, 'pincode': pincode}
    return render(request, 'sho/landing.html', context)

def loginSHO(request):

    if request.method == "POST":

        email = request.POST['email']
        loginpassword = request.POST['password']
        try:
            UserData = get_object_or_404(User, email = email)
        except:
        
            print('sho')
            messages.error(request, "Invalid Credentials given, Please check and retry again")
            
            return redirect('sho:shoLoginregister') 
        username = UserData.username 
            

        user = authenticate(username = username, password = loginpassword)
        
        if user is None:
            messages.error(request, "Invalid Credentials, Please check and retry again")
            
            return redirect('sho:shoLoginregister')         
        else:
            login(request,user)
            station = user.first_name
            pincode = user.last_name
            
            messages.success(request, "Successfully Logged In")
            context = {'user':username,'email':email, 'station':station, 'pincode': pincode}
            
          
            return render(request,'sho/landing.html', context)
    else:
        return redirect('sho:shoLoginregister')
    
 
def logoutSHO(request):
    logout(request)
    messages.success(request, "Successfully Logout")
    return redirect('/')

def pendingFIR(request,slug):
    pendingFIR = FIR.objects.filter(pincode = slug,status = False, solved = False)
    report = 'Pending'
    context = {'pendingfir':pendingFIR, 'report':report}
    
    return render(request, 'sho/pendingfir.html', context)

def viewPendingFIR(request, slug):
    userfir = get_object_or_404(FIR, sno = int(slug))

    context = {'userfir':userfir}
    return render(request, 'sho/viewfir.html', context)
    
def approvePendingFIR(request, slug):
    userfir = get_object_or_404(FIR, sno = int(slug))
    pincode = userfir.pincode
    userfir.status = True
    userfir.save()
    messages.success(request, "Successfully Approved Pending FIR")
    pendingFIR = FIR.objects.filter(pincode = pincode, status = False)
    context = {'pendingfir':pendingFIR}
    return render(request, 'sho/pendingfir.html', context)

def markSolvedFIR(request, slug):
    userfir = get_object_or_404(FIR, sno = int(slug))
    pincode = userfir.pincode
    userfir.solved = True
    
    userfir.save()
    messages.success(request, "Successfully Mark Solved to Approved FIR")
    pendingFIR = FIR.objects.filter(pincode = pincode, status = True,solved=False)
    context = {'pendingfir':pendingFIR}
    return render(request, 'sho/pendingfir.html', context)


def approvedFIR(request, slug):
    approvedFIR = FIR.objects.filter(pincode = slug,status = True, solved=False)
    report = 'Approved'
    context = {'pendingfir':approvedFIR, 'report':report}
    return render(request, 'sho/pendingfir.html', context)

def searchFIR(request):
    
    return render(request, 'sho/search.html')

def solvedFIR(request, slug):
    solvedFIR = FIR.objects.filter(pincode = slug,solved=True)
    report = 'Solved'
    context = {'pendingfir':solvedFIR, 'report':report}
    return render(request, 'sho/pendingfir.html', context)
    