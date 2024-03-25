from django.shortcuts import render
from myapp.models import Contact,Profile
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout

def index(request):
    return render(request,'index.html')

def contact_us(request):
    context={}
    if request.method == "POST":
        name = request.POST.get("name")
        em = request.POST.get("email")
        sub = request.POST.get("subject")
        msz = request.POST.get("message")

        obj = Contact(name=name, email=em , subject=sub , message=msz)
        obj.save()
        context['message']=f"Dear {name},Thanks for your time!!"

    return render(request,'contact.html',context)


def about(request):
    return render(request, 'about.html')

def team_view(request):
    return render(request, 'team.html') 

def all_dishes_view(request):
    return render(request, 'all_dishes.html') 

def login(request):
    return render(request, 'register.html') 

def register(request):
    context={}
    if request.method=="POST": 
        #fetch data from html form
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('pass')
        contact = request.POST.get('number')
        check = User.objects.filter(username=email)
        if len(check)==0:
            #save data to both table
            usr = User.objects.create_user(email,email,password)
            usr.first_name = name
            usr.save()     

            profile = Profile(user=usr,contact_number = contact)
            profile.save()
            context['status'] = f"User '{name}' Registered Successfully!!"
        else:
            context['error'] = f"A User with this email already exist...!!"
    return render(request, 'register.html',context)





def check_user_exist(request):
    email = request.GET.get('usern')
    check = User.objects.filter(usernaem=email)
    if len(check)==0:
        return JsonResponse({'status':0,'message':'Not Exist'})
    else:
        return JsonResponse({'status':1,'message':'Exists'})
    

def signin(request):
    context ={}
    if request.method=="POST":
        emai = request.POST.get('email')
        passw = request.POST.get('password')

        check_user = authenticate(username=emai, password=passw)
        if check_user:
            login(request,check_user)
            context.update({'message':'Login success!','class':'alert-success'})
            pass
        else:
            context.update({'message':'Invalid Login Details!','class':'alert-danger'})
    return render(request,'login.html',context)    