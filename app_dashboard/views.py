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
    
    
    required_projects = ProjectsTable.objects.filter(created_by=required_profile)
    
    total_projects = len(required_projects)
    total_completed_projects = required_projects.filter(status=PROJECT_STATUS_COMPLETED).count()
    total_open_projects = required_projects.filter(status=PROJECT_STATUS_OPEN).count()
    total_disputed_projects = required_projects.filter(status=PROJECT_STATUS_DISPUTED).count()
    
    context['required_profile'] = required_profile
    context['total_projects'] = total_projects
    context['total_completed_projects'] = total_completed_projects
    context['total_open_projects'] = total_open_projects
    context['total_disputed_projects'] = total_disputed_projects
    
    
    return render(request, 'dashboard/dashboard.html',context)  

