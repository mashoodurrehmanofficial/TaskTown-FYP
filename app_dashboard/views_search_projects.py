from django.shortcuts import render,HttpResponse,redirect
from django.views.decorators.csrf import csrf_exempt 
from django.http import JsonResponse,request 
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
from datetime import timedelta,datetime
from .models import *
from django.views.decorators.csrf import csrf_exempt

from collections import defaultdict
import json,threading ,random,string,os,datetime,stripe

from app.models import *



@csrf_exempt
def searchProjects(request):
    context = {"title":"Search"} 
    user:User = request.user
    required_profile = ProfilesTable.objects.get(user=user)
    
     
    available_projects = ProjectsTable.objects.filter(
        created_by=required_profile,status=PROJECT_STATUS_OPEN
    ) 
        
       
    json_available_projects = []
    for i,project in enumerate(list(available_projects)):
        json_available_projects.append({
            "id": project.id,
            "title": project.title,
            "start_date": str(project.start_date),
            "end_date": str(project.end_date),
            "budget": project.budget,
            "description": project.description,
            # "freelancer_profile_username": project.freelancer.username if project else "",
            # "freelancer_profile_id": project.freelancer.id,
            "total_bids": int(project.bids.all().count()),
        }) 
    context['available_projects'] = available_projects
    context['json_available_projects'] = json.dumps(json_available_projects)
    context['available_project_statuses'] = AVAILABLE_PROJECT_STATUSES
    
    return render(request, 'dashboard/searchProjects.html',context) 
 