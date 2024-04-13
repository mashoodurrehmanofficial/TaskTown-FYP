from django.shortcuts import render,HttpResponse,redirect
from django.views.decorators.csrf import csrf_exempt 
from django.http import JsonResponse,request 
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
from datetime import timedelta,datetime
from app.models import *
from .models import *
from collections import defaultdict 
import json,threading ,random,string,os,stripe
from django.db.models import Q

 


stripe.api_key  = settings.STRIPE_SECRET_KEY 
  
 
def dashboard(request):
    
    context = {"title":"Dashboard"}  
    required_profile = ProfilesTable.objects.get(user=request.user)  
    
    return render(request, 'dashboard/dashboard.html',context)  

