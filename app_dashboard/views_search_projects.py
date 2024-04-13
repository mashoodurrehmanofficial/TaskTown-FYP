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
    
    # context = {**context, **dict(request.GET)}
    
    query_title = request.GET.get('query_title')
    query_min_budget = request.GET.get('query_min_budget')
    query_max_budget = request.GET.get('query_max_budget')
    query_skills = request.GET.getlist('query_skills')
    
    
    
    min_budget = int(query_min_budget) if query_min_budget else 0
    max_budget = int(query_max_budget) if query_max_budget else 999999999999999999
    query_title = query_title if query_title else ''
    
    
    context['query_title'] = query_title
    context['query_min_budget'] = query_min_budget
    context['query_max_budget'] = query_max_budget
    context['query_skills'] = query_skills
    
    print(query_skills)
     
    available_projects = ProjectsTable.objects.filter(
        title__contains=query_title, created_by=required_profile,status=PROJECT_STATUS_OPEN, budget__gte=min_budget, budget__lte=max_budget, 
    ) 
    
    if query_skills: 
        available_projects = available_projects.filter(skills__name__in=query_skills)
        
        
       
       
    required_freelancer = ProfilesTable.objects.get(user=request.user)
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
            "skills": project.skills,
            "total_bids": int(project.bids.all().count()),
            "bid_submitted": project.bids.filter(created_by=required_freelancer).exists(),
        }) 
        
    available_projects = json_available_projects
    context['available_projects'] = available_projects
    # context['json_available_projects'] = json.dumps(json_available_projects)
    context['available_project_statuses'] = AVAILABLE_PROJECT_STATUSES
    available_skills = SkillsTable.objects.all()
    context['available_skills'] = available_skills  
    
    return render(request, 'dashboard/searchProjects.html',context) 
 