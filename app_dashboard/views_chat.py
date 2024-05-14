from django.shortcuts import render,HttpResponse,redirect
from django.views.decorators.csrf import csrf_exempt 
from django.http import JsonResponse,request 
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
from datetime import timedelta,datetime
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers import serialize
from django.forms.models import model_to_dict

from collections import defaultdict
import json,threading ,random,string,os,datetime,stripe

from app.models import *

 
    
    
@login_required(login_url='/login/')
def viewProjectChat(request):   
    context = {"title": "Project Chat"} 
    project_id = request.GET.get('id') 
    # required_profile = ProfilesTable.objects.get(id=int(profile_id))
    required_project = ProjectsTable.objects.get(id=int(project_id))
     
    
    
    created_by = model_to_dict(required_project.created_by) 
    freelancer = model_to_dict(required_project.freelancer)
    
    del created_by['skills']
    del created_by['experience']
    del freelancer['skills']
    del freelancer['experience']
    
    context['required_project'] = required_project
    context['required_user'] = request.user
    context['required_user_id'] = request.user.id
    context['employer_profile'] = json.dumps(created_by)
    context['freelancr_profile'] = json.dumps(freelancer )
    # print(payment_intents)
    return render(request, 'dashboard/viewProjectChat.html',context)
    
    
    

def view_project_chat(request):
    context = {"title": "Project Chat"} 
    project_id = request.GET.get('id') 
    # required_profile = ProfilesTable.objects.get(id=int(profile_id))
    required_project = ProjectsTable.objects.get(id=int(project_id))
    
    print()
    
    
    context['required_project'] = required_project
    context['required_user'] = request.user
    context['required_profile'] = ProfilesTable.objects.get(user=request.user)
    return render(request, 'dashboard/chat.html', context)