
from django.contrib.auth.models import User
from django.conf import settings
from django.shortcuts import redirect, render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render, HttpResponse, get_object_or_404, HttpResponseRedirect
from django.http import HttpResponse, HttpResponsePermanentRedirect
from django.utils.deprecation import MiddlewareMixin
from django.urls import reverse
from django.utils import timezone
from .models import *


def context_processor(request):
    context = {}
    path = request.path 
    sidebar_menu = [
        {"path": ["/dashboard/"], "text":"Dashboard", "icon": "home", } ,
        {"path": ["/dashboard/searchProjects"], "text":"Search", "icon": "search", } ,
        {"path": ["/dashboard/projects"], "text":"Projects", "icon": "layers", } ,
        # {"path": ["/dashboard/Chat"], "text":"Chat", "icon": "message-circle", } ,
        {"path": ["/dashboard/account"], "text":"Account", "icon": "user", } ,
        {"path": ["/logout"], "text":"Logout", "icon": "log-out", } ,
 ] 

        
         
    for i, x in enumerate(sidebar_menu):
        sidebar_menu[i]['active'] = any([x for x in sidebar_menu[i]['path'] if x== path])

    
    context['sidebar_menu'] = sidebar_menu
    url = request.build_absolute_uri() 
    if [x for x in ["login", 'register', 'sendPasswordResetLink', "password_reset_id"] if x.lower() in url.lower()]:
        context['hide_navbar'] = True
    else:
        context['hide_navbar'] = False
    
    user = request.user
    if user.is_authenticated:
        required_profile = ProfilesTable.objects.get(user=user)
        context['profile'] = required_profile 
            
        
         
    context['USER_ROLE_FREELANCER_KEYWORD'] = USER_ROLE_FREELANCER_KEYWORD
    context['PROJECT_STATUS_OPEN'] = PROJECT_STATUS_OPEN
    context['PROJECT_STATUS_ACTIVE'] = PROJECT_STATUS_ACTIVE
    context['USER_ROLE_CLIENT_KEYWORD'] = USER_ROLE_CLIENT_KEYWORD 


    context['user'] = user
    context['is_dark_theme'] = request.session.pop('is_dark_theme', False) 
    request.session['is_dark_theme'] = context['is_dark_theme']
        
    print("user = ", request.user) 
    return context


 
 

