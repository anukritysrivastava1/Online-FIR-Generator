from django.shortcuts import render, redirect, HttpResponse,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from user.models import FIR
from datetime import datetime
# Create your views here.


def loginregister(request):
    return render(request, "controller/loginregistration.html")

def homeController(request,):
    return render(request, 'controller/landing.html')

def loginController(request):

    if request.method == "POST":

        email = request.POST['email']
        loginpassword = request.POST['password']
       
        UserData = get_object_or_404(User, email = email)
        
        if UserData is None:
            messages.error(request, "Invalid Credentials, Please check and retry again")
            
            return render('controller:controllerLoginregister') 
        username = UserData.username 
            

        user = authenticate(username = username, password = loginpassword)
        
        if user is None:
            messages.error(request, "Invalid Credentials, Please check and retry again")
            
            return redirect('controller:controllerLoginregister')         
        else:
            login(request,user)
            print('admin')
           
            
            messages.success(request, "Successfully Logged In")
            context = {'user':username,'email':email, }
            
          
            return render(request,'controller/landing.html', context)
    else:
        return redirect('controller:controllerLoginregister')
 

def logoutController(request):
    logout(request)
    messages.success(request, "Successfully Logout")
    return redirect('/')


def searchFIR(request):
    return render(request, 'controller/search.html')


def manageSHO(request):
    users = User.objects.exclude(last_name__exact='').exclude(last_name__isnull=True)
    context ={'user':users}

    for i in users:
        print(i.last_name)
    return render(request, 'controller/managesho.html', context)

def viewSHOdetails(request, slug):
    sho = get_object_or_404(User, username = slug )
    context = {'sho':sho}
    return render(request, 'controller/viewsho.html', context)


def createSHO(request):
    return render(request, 'controller/createsho.html')
    
def editSHO(request):
    if request.method == "POST":
        oldusername = request.POST['oldusername']
        sho = get_object_or_404(User, username = oldusername)

        email = request.POST['email']
        psw = request.POST['psw']
        username = request.POST['username']
        paddress = request.POST['paddress']
        ppin = request.POST['ppin']

        if email:
            sho.email = email
        if psw:
            sho.password = psw
        if username :
            sho.username = username
        if paddress:
            sho.first_name = paddress
        if ppin :
            sho.last_name = ppin

        sho.save()
        messages.success(request, 'Selected SHO Details Modified Successfully')
        return redirect('controller:manageSHOaccount')

        

def deleteSHO(request,slug):
    sho = User.objects.get(username=slug)
    sho.delete()
    messages.success(request, f' SHO Account of {slug} deleted Successfully')
    return redirect('controller:manageSHOaccount')


def newSHO(request):

    if request.method == "POST":

        email = request.POST['email']
        psw = request.POST['psw']
        pswrepeat = request.POST['psw-repeat']
        if psw != pswrepeat:
            messages.error(request,"Your Password didn't match")
            return redirect('controller:newSHOaccount')
        username = request.POST['username']
        paddress = request.POST['paddress']
        ppin = request.POST['ppin']

        newsho = User.objects.create_user(username=username,email=email,password=psw, first_name = paddress, last_name = ppin )
        newsho.save()
        messages.success(request,"New SHO account has been created Successfully")

        return render(request,'controller/createsho.html')
       

    return redirect('controller:newSHOaccount')
    