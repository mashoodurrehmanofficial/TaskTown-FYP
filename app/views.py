from django.shortcuts import render,HttpResponse,redirect
from django.views.decorators.csrf import csrf_exempt 
from django.http import JsonResponse
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
import datetime,stripe,traceback
from datetime import timedelta,datetime
from .models import *
from collections import defaultdict
import json,threading 
stripe.api_key  = settings.STRIPE_SECRET_KEY
# Create your views here.
  
  

def home(request):     
    context = {"title": "TaskTown"} 
    return render(request, 'app/home.html' ,context) 
  
   
  
def about(request):     
    context = {"title": "About us"} 
    return render(request, 'app/about.html' ,context) 
  
   
  
def products(request):     
    context = {"title": "Products"} 
    return render(request, 'app/products.html' ,context) 
  
   
  
def contact(request):     
    context = {"title": "Contact us"} 
    if request.method =="POST" :
        data = request.POST
        first_name = data['first_name']
        last_name = data['last_name']
        city = data['city']
        country = data['country']
        company = data['company']
        email = data['email']
        description = data['description']
        ContactUsTable(
            first_name  = first_name,
            last_name   = last_name,
            city        = city,
            country     = country,
            company     = company,
            email       = email,
            description = description,
        ).save()
        
        body = ''
        body += "{:<15} {:<50} <br>".format("First Name:", first_name)
        body += "{:<15} {:<50} <br>".format("Last Name:", last_name)
        body += "{:<15} {:<50} <br>".format("City:", city)
        body += "{:<15} {:<50} <br>".format("Country:", country)
        body += "{:<15} {:<50} <br>".format("Company:", company)
        body += "{:<15} {:<50} <br>".format("Email:", email)
        body += "{:<15} {:<50} <br>".format("Description:", description)
   
        try:
        #     html_content= body
        #     send_email(subject="New Contact Request",receiver=email,heading="New Contact Request", html_content=html_content)
            context['success'] = "Your Request has been submitted successfully. We will contact you soon."
        except:
            print(traceback.format_exc())
            context['error'] = "Cannot send email."
        
        
    return render(request, 'app/contact.html' ,context) 
  
   
   
  
# @login_required(login_url='/login/')
# def profile(request):   
#     context = {"title": "Profile"}
#     user = request.user
#     profile = ProfileTable.objects.get(user=user)
#     if request.method=="POST":
#         password = request.POST['password']
#         email = request.POST['email']
#         user.email = email
#         user.set_password(password)
#         user.save()
#         profile.password = password
#         profile.save()
#         login(request, user) 
        
#     context['message'] = request.session.pop('message', False)
#     context['user'] = user
#     context['profile'] = profile
#     request.session['message'] = False
#     return render(request, 'app/profile.html' ,context) 
 

 