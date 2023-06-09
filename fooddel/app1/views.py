from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate , logout , login as loginUser
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import *
from d import recommend1
import pymongo


@login_required(login_url="LoginPage")
def HomePage(request):
   if request.method == 'POST':
       search=request.POST.get('search')
       result=recommend1(search)
       
       
       context = {'result': result}
       return render(request, 'search.html' , context)
       
       
       
   return render(request, 'home.html')
def Signup(request):
    
    if request.method == 'POST':
        uname=request.POST.get('Name')
        email=request.POST.get("mail")
        dob=request.POST.get("dob")
        pass1=request.POST.get('password')
        pass2=request.POST.get('confirm_p')
       
        if pass1!=pass2:
            return HttpResponse("p1 not equla to p2")
        else:
           my_user=User.objects.create_user(uname,email,pass1) 
           my_user.save()
           new_input=userInfo(usernames=uname,emmails=email,dob=dob)
           new_input.save()
           
           return redirect('LoginPage')
        
    
    return render(request, 'login.html')

def login(request):

       
    if request.method == 'POST':
         username = request.POST.get('uname') 
         password = request.POST.get('pass') 

         user = authenticate(request , username = username, password = password) 

         if user is not None:
            loginUser(request,user) 
            return redirect('HomePage') 
         else:
            return HttpResponse("User info Incorrect")
        
       
      
    return render(request, 'login.html')
   
def logoutPage(request):
    logout(request)
    
    return redirect('LoginPage')

def ksburger(request):
    
    
    
    return render(request,'ksbakers.html')

def search(request):
    return render(request, 'search.html')

def profile(request):
    cuser = request.user
  
    info_list=User.objects.all()
    i=cuser.id
    em=cuser.email
    name=cuser.username
    
    context={'name':name,'email':em,'id':i}
    return render(request, 'profile.html',context)


def order(request):
    if request.method =='POST':
        Hname=request.POST.get('hotel_name')
        DineIn_or_not=request.POST.get("dining_preference")
        Cuisine = request.POST.get('cuisine[]')
        Address=request.POST.get('address')
        order = Order(name=Hname , type = DineIn_or_not , cusine=Cuisine,address=Address)
        order.save()
    
    
    return render(request, 'order.html')




