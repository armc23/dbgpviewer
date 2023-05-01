from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

def home(request):
    #Check to see if login in 
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        # Atuhenticate
        user = authenticate(request, username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"You have been logged in")
            return redirect('home')
        else:
            messages.success(request,"There was an error loggin in, please try again ")
            return redirect('home')
    else:
       return render(request, 'home.html', {})


#
 #   pass

def logout_user(request):
    logout(request)
    messages.success(request,"You have been Logged Out...")
    return redirect('home')

def register_user(request):
    return render(request,'register.html',{}) 