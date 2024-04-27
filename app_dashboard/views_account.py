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
def manageAccount(request):
    context = {"title":"Edit Account"} 
    user:User = request.user
    required_profile = ProfilesTable.objects.get(user=user)
     
    
    if request.method == "POST":
        data = request.POST
        password = data.get('password')
        username = data.get('username') 
        user.set_password(password) 
        
        
        user.save()
        
        required_profile.password = password
        required_profile.username = username
        
        if required_profile.type == USER_ROLE_FREELANCER_KEYWORD:
            skills = [int(x.split("_")[-1]) for x in dict(data).keys() if "skill" in x]
            skills = SkillsTable.objects.filter(id__in=skills) 
            required_profile.skills.clear()
            required_profile.skills.add(*skills)
            
            print(skills)
        
        required_profile.save()
        login(request, user)
        
        
    available_skills = SkillsTable.objects.all()
    context['available_skills'] = available_skills
    
    return render(request, 'dashboard/account.html',context) 



@csrf_exempt
def addNewExperience(request):
    context = {"title":"Edit Account"} 
    user:User = request.user
    required_profile = ProfilesTable.objects.get(user=user)
    
    if request.method == "POST":
        data = request.POST
        title = data.get('title')
        start_date = data.get('start_date') 
        end_date = data.get('end_date')  
        
        
        experience = ExperienceTable(
            title = title, start_date = start_date, end_date = end_date
        )
        experience.save() 
        required_profile.experience.add(experience)
        
        return redirect("manageAccount")
    
    return redirect("manageAccount")

@csrf_exempt
def uploadProfilePicture(request):
    folder_path = settings.MEDIA_ROOT 
    user = request.user
    required_profile = ProfilesTable.objects.get(user=user)
    if request.method == "POST":
        
        if required_profile.image_path:
            image_path = os.path.join(folder_path, required_profile.image_path)    
            if os.path.exists(image_path):
                try:
                    os.remove(image_path)
                except:
                    pass
        
        
        image = request.FILES['image']
        file_name =  str(uuid.uuid4())+".png"
        file_path = os.path.join(folder_path  , file_name)
        
        required_profile.image_path = f"/Media/{file_name}"
        required_profile.save()
        
        with open(file_path, 'wb') as f:
            for chunk in image.chunks():
                f.write(chunk)

    
    return redirect("manageAccount")
        
@csrf_exempt
def deleteExperience(request):
    id = request.GET.get("id")
    experience = ExperienceTable.objects.get(id=int(id))
    experience.delete()
    
    
    return redirect("manageAccount")
        
        