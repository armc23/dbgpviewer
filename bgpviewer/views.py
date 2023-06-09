from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import SignUpForm,PrefixForm,SitesForm
from .models import Record,Prefix,Site
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

def home(request):
    records = Record.objects.all().order_by('create_at')


    p = Paginator(Record.objects.all(),12)
    page = request.GET.get('page')
    record = p.get_page(page)

    nums = "a" * record.paginator.num_pages

     
    context = {
    'records': records,
    'record':record,
    'nums':nums
 
    }

    #Check to see if login in 
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        # Atuhenticate
        user = authenticate(request, username=username,password=password)
        if user is not None:
            login(request,user)
           # messages.success(request,"You have been logged in")
            return redirect('home')
        else:
            messages.success(request,"There was an error loggin in, please try again ")
            return redirect('home')
    else:
    

       return render(request, 'home.html', context)
# Prefixes

def prefixes(request):
    prefix = Prefix.objects.all()

     
    context = {
    'prefix': prefix
 
    }
 
    return render(request, 'prefixes.html', context)
# Update Prefixes
def update_prefixes(request, prefix_id):
    prefix = Prefix.objects.get(pk=prefix_id)

    form = PrefixForm(request.POST or None, instance=prefix)

    if form.is_valid():
        form.save()
        return redirect('prefixes')
    
    context = {
    'prefix': prefix,
    'form': form
 
    }
 
    return render(request, 'update_prefix.html', context)

# add Prefix
def add_prefix(request):

 
    form = PrefixForm()
    if request.method =="POST":
        form = PrefixForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('prefixes')
    
    context = {
   
    'form': form
 
    }
 
    return render(request, 'add_prefix.html', context)

#Delete Prefix

def delete_prefix(request, prefix_id):
    prefix = Prefix.objects.get(pk=prefix_id)

    if request.method == "POST":
        prefix.delete()
        return redirect('prefixes')
    
    context = {
    'item': prefix,
    
 
    }
 
    return render(request, 'delete_prefix.html', context)

# Sites

def sites(request):
    sites = Site.objects.all()

     
    context = {
    'sites': sites
 
    }
 
    return render(request, 'sites.html', context)

# Update Sites
def update_sites(request, site_id):
    sites = Site.objects.get(pk=site_id)

    form = SitesForm(request.POST or None, instance=sites)

    if form.is_valid():
        form.save()
        return redirect('sites')
    
    context = {
    'sites': sites,
    'form': form
 
    }
 
    return render(request, 'update_site.html', context)

# add Sites
def add_sites(request):

 
    form = SitesForm()
    if request.method =="POST":
        form = SitesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sites')
    
    context = {
   
    'form': form
 
    }
 
    return render(request, 'add_site.html', context)

def delete_sites(request, site_id):
    sites = Site.objects.get(pk=site_id)

    if request.method == "POST":
        sites.delete()
        return redirect('sites')
    
    context = {
    'item': sites,
    
 
    }
 
    return render(request, 'delete.html', context)



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

result_req_per_page = 15

def BootstrapFilterView(request):
    #get all objectss
    records = Record.objects.all().order_by('-create_at')
    

    #get prefixes
    prefix = Prefix.objects.all()
    site = Site.objects.all()

    date_min = request.GET.get('date_min')
    date_max = request.GET.get('date_max')

    query_contains_site = request.GET.get('site')
    query_contains_prefix = request.GET.get('prefix')

    if (query_contains_site and query_contains_site != 'Choose...') and (query_contains_prefix and query_contains_prefix != 'Choose...'):
        records = records.filter(site__icontains=query_contains_site,prefix__icontains=query_contains_prefix)

    if query_contains_site and query_contains_site != 'Choose...':
        records = records.filter(site__icontains=query_contains_site)
       
    elif (query_contains_site and query_contains_site != 'Choose...') and (query_contains_prefix and query_contains_prefix != 'Choose...'):
        records = records.filter(site__icontains=query_contains_site,prefix__icontains=query_contains_prefix)
    
    elif query_contains_prefix and query_contains_prefix != 'Choose...':
        records = records.filter(prefix__icontains=query_contains_prefix)
    
    
    if date_min and date_min != '':
        records =records.filter(create_at__gte=date_min)

    if date_max and date_max!= '':
        records = records.filter(create_at__lte=date_max)

    #print(query_contains_site)
    #print(query_contains_prefix)

    #Pagination

    page = request.GET.get('page',1)
    record_paginator = Paginator(records,result_req_per_page)

    try:
        records = record_paginator.page(page)
    except EmptyPage:
        records = record_paginator.page(record_paginator.num_pages)
    except PageNotAnInteger:
        records =record_paginator.page(result_req_per_page)
    


   

    context = {
        'records': records,
        'prefix': prefix,
        'site': site,
        'page_obj': records,
        'is_paginated':True,
        'paginator': record_paginator
      
        #'query_contains_prefix':query_contains_prefix,
        #'query_contains_site':query_contains_site
    }

    return render(request,"bottstrap_form.html",context)