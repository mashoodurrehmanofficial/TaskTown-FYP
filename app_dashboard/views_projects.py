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
def manageProjects(request):
    context = {"title":"Projects"} 
    user:User = request.user
    required_profile = ProfilesTable.objects.get(user=user)
    
    if required_profile.type == USER_ROLE_FREELANCER_KEYWORD:
        available_projects = ProjectsTable.objects.filter(freelancer=required_profile)
    else:
        available_projects = ProjectsTable.objects.filter(created_by=required_profile)
        
       
    json_available_projects = []
    for i,project in enumerate(list(available_projects)):
        json_available_projects.append({
            "id": project.id,
            "title": project.title,
            "start_date": str(project.start_date),
            "end_date": str(project.end_date),
            "budget": project.budget,
            # "freelancer_profile_username": project.freelancer.username if project else "",
            # "freelancer_profile_id": project.freelancer.id,
            "total_bids": int(project.bids.all().count()),
        }) 
    context['available_projects'] = available_projects
    context['json_available_projects'] = json.dumps(json_available_projects)
    context['available_project_statuses'] = AVAILABLE_PROJECT_STATUSES
    
    return render(request, 'dashboard/manageProjects.html',context) 


@csrf_exempt
def editProject(request):
    context = {"title":"Add New Project"} 
    user:User = request.user
    required_profile = ProfilesTable.objects.get(user=user)
    
    project_id = request.GET.get('id')
    if str(project_id).isnumeric():
        required_project = ProjectsTable.objects.get(id=int(project_id))
    else:
        required_project = ProjectsTable()
        
    available_skills = SkillsTable.objects.all()
    context['available_skills'] = available_skills
    
    if request.method == "POST":
        data = request.POST 
        title = data['title']
        description = data['description']
        budget = data['budget']
        start_date = data['start_date']
        end_date = data['end_date']
        
        required_project.title = title
        required_project.description = description
        required_project.budget = budget
        required_project.start_date = start_date
        required_project.end_date = end_date
        required_project.created_by = required_profile
        required_project.status = PROJECT_STATUS_OPEN
        
        
        required_project.save()
        skills = [int(x.split("_")[-1]) for x in dict(data).keys() if "skill" in x]
        skills = SkillsTable.objects.filter(id__in=skills) 
        required_project.skills.clear()
        required_project.skills.add(*skills)
        
        print(skills)
        
        
        
        return redirect("manageProjects")
    
    context['required_project'] = required_project
    return render(request, 'dashboard/editProject.html',context) 
    


@csrf_exempt
def viewProjectDetails(request):
    context = {"title":"Project Details"}
    id = request.GET.get("id")
    required_project = ProjectsTable.objects.get(id=int(id))
    required_freelancer = ProfilesTable.objects.get(user=request.user)
    required_profile = ProfilesTable.objects.get(user=request.user)
    required_bid = required_project.bids.filter(created_by=required_freelancer)
    
    if required_bid:
        context['required_bid'] = required_bid.first()
     
    if request.method == "POST":
        data = request.POST
        
        proposal = data['proposal']
        budget  = data['budget']
        
        
        if required_bid.exists():
            required_bid = required_bid.first()
        else:
            required_bid = BidsTable()
            required_bid.save()
            required_project.bids.add(required_bid)
            
        required_bid.proposal = proposal
        required_bid.budget = budget
        required_bid.created_by = required_freelancer
        
        required_bid.save()
        context['required_bid'] = required_bid
        
        return redirect(f'/dashboard/viewProjectBids?id={required_project.id}')
        
        
     
    context['required_project'] = required_project
    context['allow_bid_submittion'] = required_project.created_by != required_profile
    
    
    return render(request, 'dashboard/viewProjectDetails.html',context)  
        

@csrf_exempt
def withdrawBid(request):
    context = {"title":"Project Bids"}
    project_id = request.GET.get("project_id")
    required_project = ProjectsTable.objects.get(id=int(project_id))
    required_freelancer = ProfilesTable.objects.get(user=request.user)
    required_bid = required_project.bids.filter(created_by=required_freelancer) 
    required_bid.delete() 
    
    return redirect(f'/dashboard/viewProjectBids?id={project_id}') 


@csrf_exempt
def awardProject(request): 
    context = {"title":"Project Bids"}
    project_id = request.GET.get("project_id")
    freelancer_id = request.GET.get("freelancer_id")
    required_project = ProjectsTable.objects.get(id=int(project_id))
    required_freelancer = ProfilesTable.objects.get(id=int(freelancer_id))
    
    required_project.freelancer = required_freelancer
    required_project.status = PROJECT_STATUS_ACTIVE
    required_project.save()
    return redirect(f'/dashboard/viewProjectBids?id={project_id}') 



@csrf_exempt
def viewProjectBids(request):
    context = {"title":"Project Bids"}
    id = request.GET.get("id")
    required_project = ProjectsTable.objects.get(id=int(id))
     
    context['required_project'] = required_project
    
    required_freelancer = ProfilesTable.objects.get(user=request.user)
    context["bid_submitted"] = required_project.bids.filter(created_by=required_freelancer).exists()
    
    required_profile = ProfilesTable.objects.get(user=request.user)
    
    context['allow_award'] = required_project.created_by.id ==  required_profile.id
    
    print(context)
    
    return render(request, 'dashboard/viewProjectBids.html',context)  




        

@csrf_exempt
def deleteProject(request):
    id = request.GET.get("id")
    project = ProjectsTable.objects.get(id=int(id))
    project.delete()
    
    
    return redirect("manageProjects")
        
        