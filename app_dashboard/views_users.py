from django.shortcuts import render,HttpResponse,redirect
from django.views.decorators.csrf import csrf_exempt 
from django.http import JsonResponse,request ,FileResponse,HttpResponseNotFound
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required 
from django.db.models import Count
from django.core import serializers
from django.conf import settings
from django.forms.models import model_to_dict
from datetime import timedelta,datetime
from .models import *
from app.models import *
from collections import defaultdict
import json,threading ,random,string,os,stripe

 

def deleteUsers(request): 
    ids = str(request.GET.get("ids")).split(",")
    print("--> ",ids)
    if ids:
        ids = [int(x) for  x in ids]
        required_users = User.objects.filter(id__in=ids)
        required_users.delete()
        print(required_users)
    return JsonResponse({})
