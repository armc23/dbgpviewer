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

def is_valid_queryparam(param):
    return param != '' and param is None

def BootstrapFilterView(request):
    records = Record.objects.all()
    prefix = Prefix.objects.all()
    site = Site.objects.all()

    date_min = request.GET.get('date_min')
    date_max = request.GET.get('date_max')


    query_contains_site = request.GET.get('site')
    #uery_contains_site= query_contains_site.strip()
    query_contains_prefix = request.GET.get('prefix')
    #query_contains_prefix = query_contains_prefix.strip()

    print(query_contains_site)
    print(query_contains_prefix)

    if is_valid_queryparam(query_contains_site) and query_contains_site != 'Choose...':
        records = records.filter(site__icontains=query_contains_site)
    
    elif is_valid_queryparam(query_contains_prefix) and query_contains_prefix != 'Choose...':
        records = records.filter(prefix__icontains=query_contains_prefix)

    if is_valid_queryparam(date_min):
        records =records.filter(create_at__gte=date_min)

    if is_valid_queryparam(date_max):
       records = records.filter(create_at__lt=date_max)
    

    context = {
        'records': records,
        'prefix': prefix,
        'site': site
        #'query_contains_prefix':query_contains_prefix,
        #'query_contains_site':query_contains_site
    }

    return render(request,"bottstrap_form.html",context)