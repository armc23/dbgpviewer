from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import SignUpForm
from .models import Record,Prefix,Site

def home(request):
    records = Record.objects.all().order_by('create_at')

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
       

       return render(request, 'home.html', {'records':records})


#
 #   pass

def logout_user(request):
    logout(request)
    messages.success(request,"You have been Logged Out...")
    return redirect('home')

def register_user(request):
    if request.method =='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            #Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request,user)
            messages.success(request,"You have successfuly registered a new User")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request,'register.html',{'form':form}) 
    return render(request, 'register.html', {'form':form})

def BootstrapFilterView(request):
    records = Record.objects.all()
    prefix = Prefix.objects.all()
    site = Site.objects.all()


    query_contains_site = request.GET.get('site')
    query_contains_prefix = request.GET.get('prefix')

    if query_contains_site != '' and query_contains_site is not None:
        records = records.filter(site=query_contains_site)
    
    elif query_contains_prefix != '' and query_contains_prefix is not None:
        records = records.filter(prefix=query_contains_prefix)   

    context = {
        'records': records,
        'prefix': prefix,
        'site': site
    }

    return render(request,"bottstrap_form.html",context)