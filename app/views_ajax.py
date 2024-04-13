from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *
from itertools import groupby
from operator import itemgetter 
import datetime
import json


def setTheme(request):
    context = {}
    is_dark_theme = request.GET.get("is_dark_theme") == 'true'
    request.session['is_dark_theme'] = is_dark_theme 
    print("is_dark_theme = ", is_dark_theme) 
    return JsonResponse(context)


