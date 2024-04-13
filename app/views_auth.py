from multiprocessing import context
import uuid,requests
from django.conf import settings

import traceback
from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from app.models import * 
# Create your views here.


def loginRouter(request):
    context = {"title": "Login"}
    if request.method == 'POST':

        email = request.POST['email']
        password = request.POST['password']
        required_profile = ProfilesTable.objects.filter(user__email=email)
        if required_profile.exists():
            required_profile = required_profile.first() 
            user = authenticate(username=required_profile.user.username, password=password)
            print("user = ",user)
            print("required_profile.name = ",required_profile.username) 
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                context['error'] = "Invalid Credentials"
                return render(request, 'app/login.html', context)

    print(request.session.get('message'))
    if request.session.get('message'):
        context['message'] = request.session['message']
        del request.session['message']
    return render(request, 'app/login.html', context)


def registerRouter(request):
    context = {"title": "Sign up"} 
    
    if request.method == 'POST':
   
    
        email    = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
         
        account_type = USER_ROLE_FREELANCER_KEYWORD if request.POST['account_type'] == "Freelancer" else USER_ROLE_CLIENT_KEYWORD
        print("Username = ", username)
        print("email = ", email)
        print("password = ", password)
        
        required_profile = ProfilesTable.objects.filter(user__email=email) 
        
        if not required_profile.exists():   
            user = User(username=str(uuid.uuid4()), email=email)
            user.set_password(password)
            user.save()  
            new_profile = ProfilesTable(user=user).save()
         
            new_profile = ProfilesTable.objects.get(user=user)
            new_profile.username = username
            new_profile.password = password 
            new_profile.type = account_type
            new_profile.save()
            # send_email(request)
            domain = request.build_absolute_uri('/')[:-1] 
            email_reset_link = f"{domain}/activateEmail?id={new_profile.id}"
            
            html_content= email_reset_link
            # send_email(subject="Password Reset Link",receiver=email,heading="Reset your Password", html_content=html_content)
            # context['message'] = "Email has been sent successfully."
            
            
            return redirect('login')
        else:
            context['error'] = "User already exists. Try different Email."

    return render(request, 'app/register.html', context)


 

def logoutRouter(request): 
    logout(request)
    return redirect('login')


 





def changePassword(request):
    context = {"title": "Reset Password"}
    password_reset_id = request.GET.get("password_reset_id")
    context['password_reset_id'] = password_reset_id

    if request.method == "POST":
        print(password_reset_id)
        required_profile = ProfilesTable.objects.filter(
            password_reset_id=password_reset_id)
        if required_profile.exists():
            required_profile = required_profile.first()
            required_profile.password_reset_id = ''
            required_profile.save()
            required_user = required_profile.user
            password = request.POST['password']
            user = required_user
            print("New Password = ", password)
            user.set_password(password)
            user.save()
            login(request, user)
            request.session['message'] = "Password Updated Successfully !"
            # return render(request, 'app/login.html',context )
            return redirect("login")

        else:
            context['error'] = "Invalid Password Reset Link"
            return render(request, 'app/changePassword.html', context)

    return render(request, 'app/changePassword.html', context)



 

def sendPasswordResetLink(request):
    if request.method == 'POST':
        context = {"title": "Reset Link"}
        email = request.POST['email']
        required_user = User.objects.filter(email=email)
        if required_user:
            required_user = required_user.first()
            password_reset_id = str(uuid.uuid4())+'-'+str(uuid.uuid4())
            required_profile = ProfilesTable.objects.get(user=required_user)
            required_profile.password_reset_id = password_reset_id
            required_profile.save()
            password_reset_link = request.build_absolute_uri().split("/sendPasswordResetLink")[0]+f'/changePassword?password_reset_id={password_reset_id}'
            print(password_reset_link)
        
            try: 
                html_content= "<h3>Click given link to reset your password</h3> <br>"+ password_reset_link
                # send_email(subject="Password Reset Link",receiver=email,heading="Reset your Password", html_content=html_content)
                context['message'] = "Email has been sent successfully."
            except:
                print(traceback.format_exc())
                context['error'] = "Cannot send email."
                

    return render(request, 'app/sendPasswordResetLink.html')



