from django.shortcuts import render, redirect, HttpResponse,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import FIR
from datetime import datetime
# Create your views here.

def home(request):
    return render(request,'user/landing.html')

def loginregister(request):
    
    return render(request, "user/loginregistration.html")

def loginUser(request):

    if request.method == "POST":

        email = request.POST['email']
        loginpassword = request.POST['password']
        try:
            UserData = get_object_or_404(User, email = email)
        except:
        
            
            messages.error(request, "Invalid Credentials given, Please check and retry again")
            
            return redirect('user:userLoginregister') 
        username = UserData.username 
            

        user = authenticate(username = username, password = loginpassword)
        
        if user is None:
            messages.error(request, "Invalid Credentials, Please check and retry again")
            
            return redirect('user:userLoginregister')         
        else:
            login(request,user)
            station = user.first_name
            pincode = user.last_name
            
            messages.success(request, "Successfully Logged In")
            context = {'user':username,'email':email, 'station':station, 'pincode': pincode}
            
          
            return render(request,'user/landing.html', context)
    else:
        return redirect('user:userLoginregister')
    
def logoutUser(request):
    logout(request)
    messages.success(request, "Successfully Logout")
    return redirect('/')

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        

        # check for errorneous input
        if len(username)>10:

            if username.isdigit():
                messages.error(request, "Your username must contain atleast 1 character")

            messages.error(request, "Your username must be less than 10 characters")
            return redirect('user:userLoginregister')
        
        
        # Creating User
        else:
            myuser = User.objects.create_user(username = username, email = email, password=password)
            myuser.save()
            messages.success(request,"Your account has been created Successfully")
            user = authenticate(username = username, password = password)
            login(request,user)

            return render(request,'user/landing.html')
    

def apply(request):
    return render(request, 'user/apply.html')

def applyFIR(request):

    if request.method == "POST":
        username = request.POST.get('username')
        UserData = get_object_or_404(User, username = username)
        useremail = UserData.email
        fullName = request.POST.get('application[name]')
        email = request.POST.get('application[email]')
        mobNo = request.POST.get('application[mobile]')
        aadhar = request.POST.get('application[aadhar]')
        address = request.POST.get('application[address]')
        district = request.POST.get('application[district]')
        state = request.POST.get('application[state]')
        pinCode = request.POST.get('application[pin]')
        toc = request.POST.get('application[type]')
        incidentDateTime = request.POST.get('application[date]')
        
        detailsOfIncident = request.POST.get('application[details]')
        suspect = request.POST.get('application[suspect]')
        witness = request.POST.get('application[witness]')

        context = {'username':username,'useremail':useremail, 'email':email,'fullName':fullName, 'mobNo':mobNo, 'aadhar':aadhar,
                   'address':address,'district':district, 'state':state, 'pinCode':pinCode, 'toc':toc, 'incidentDateTime':incidentDateTime,
                   'detailsOfIncident':detailsOfIncident,'suspect':suspect,'witness':witness }
        return render(request,'user/otp.html',context)
        return

        
        
        fir = FIR(username=username, useremail = useremail, victimemail = email, victimfullname = fullName,
                  mobno = mobNo, aadharno = aadhar,address = address, district = district, state = state,
                  pincode = pinCode, typeofcrime = toc, incidentdatetime = incidentDateTime,
                  detailsofincident = detailsOfIncident, suspect = suspect, witness = witness)
        
        fir.save()
        messages.success(request, "Your FIR has been generated successfully")
        
    else:
        messages.error(request, "Error occured , please check and try again")
        return render(request, 'user/apply.html')

def verifyotp(request):
    if request.method == "POST":
        username = request.POST.get('username')
        useremail = request.POST.get('useremail')
        
       
        fullName = request.POST.get('fullName')
        email = request.POST.get('email')
        mobNo = request.POST.get('mobNo')
        aadhar = request.POST.get('aadhar')
        address = request.POST.get('address')
        district = request.POST.get('district')
        state = request.POST.get('state')
        pinCode = request.POST.get('pinCode')
        toc = request.POST.get('toc')
        incidentDateTime = request.POST.get('incidentDateTime')
        print(incidentDateTime)
        incidentDateTime = datetime.strptime(str(incidentDateTime), '%Y-%m-%dT%H:%M')
        print(incidentDateTime)
        detailsOfIncident = request.POST.get('detailsOfIncident')
        suspect = request.POST.get('suspect')
        witness = request.POST.get('witness')
        otp = request.POST.get('otp')

        context = {'username':username,'useremail':useremail, 'email':email,'fullName':fullName, 'mobNo':mobNo, 'aadhar':aadhar,
                'address':address,'district':district, 'state':state, 'pinCode':pinCode, 'toc':toc, 'incidentDateTime':incidentDateTime,
                'detailsOfIncident':detailsOfIncident,'suspect':suspect,'witness':witness }
        if otp != "12345678":
            messages.error(request, "You Entered Wrong OTP, Please check and try again")
            return render(request,'user/otp.html',context)
       
        fir = FIR(username=username, useremail = useremail, victimemail = email, victimfullname = fullName,
                  mobno = mobNo, aadharno = aadhar,address = address, district = district, state = state,
                  pincode = pinCode, typeofcrime = toc, incidentdatetime = incidentDateTime,
                  detailsofincident = detailsOfIncident, suspect = suspect, witness = witness)
        fir.save()

        messages.success(request, "Your FIR has been generated successfully")
        return render(request, 'user/success.html')


def userDashboard(request,slug):
    
    userfir = FIR.objects.filter(username=slug)
    len = 1
    for i in userfir:
        len += 1
    row = (len//4)+2
    height = row*60
    print(height)
   
    context = {'userfir':userfir, 'style':height}
    return render(request, 'user/my.html', context)
    
    
def userFIR(request,slug):

    userfir = get_object_or_404(FIR, sno = int(slug))

    context = {'userfir':userfir}
    return render(request, 'user/viewfir.html', context)


def searchFIR(request):
        
    if request.method == "POST":
        username = request.POST.get('username')
        from_date = request.POST.get('date[from]')
        to_date = request.POST.get('date[to]')
        selected_values = request.POST.get('status')
        print(selected_values)
        start_date = datetime.strptime(str(from_date), '%Y-%m-%d')
        end_date = datetime.strptime(str(to_date), '%Y-%m-%d')
        records = FIR.objects.filter(incidentdatetime__range=(start_date, end_date), username = username)
        if 'pending' in selected_values:
            records = FIR.objects.filter(incidentdatetime__range=(start_date, end_date), username = username, status = False )
        elif 'approved' in selected_values:
            records = FIR.objects.filter(incidentdatetime__range=(start_date, end_date), username = username, status = True )
        elif 'solved' in selected_values:
            records = FIR.objects.filter(incidentdatetime__range=(start_date, end_date), username = username, solved = True )
        else:
            records = FIR.objects.filter(incidentdatetime__range=(start_date, end_date), username = username, )
            
        messages.success(request, f"Showing {selected_values} results from {from_date} to {to_date}")
        context = {'userfir': records}
        return render(request, 'user/search.html', context)
    
    return render(request, 'user/search.html')


def cancelFIR(request):
    return render(request, 'user/cancel.html')
        