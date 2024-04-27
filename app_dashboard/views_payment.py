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

stripe.api_key  = settings.STRIPE_SECRET_KEY


def getDomainName(request):
    domain = request.META['HTTP_HOST']
    domain = domain[:-1] if domain.endswith('/') else domain
    domain = "http://"+domain if 'localhost' in domain else domain
    return domain

@csrf_exempt
def makePaymentSessionLink(request):
    context = {"title":"Project Bids"}
    required_profile = ProfilesTable.objects.get(user=request.user)
 
        


    domain = getDomainName(request)
    # Create a new Checkout Session with the dynamic Price
    if required_profile.stripe_customer_id:
        print("-> Strip Customer Already Exists")
        customer  = stripe.Customer.retrieve(required_profile.stripe_customer_id)
    else:
        print("-> Creating New Strip Customer")
        customer = stripe.Customer.create(
            description=f"{request.user.username} - User ID = {request.user.id}",
        )
    required_profile.stripe_customer_id = customer.id
    required_profile.save()
    
    session = stripe.checkout.Session.create(
        customer=customer,
        payment_method_types=['card'],
        line_items=[
            {
                'price': "price_1P1PI0L7fObk0SODJjC0u8PN",
                'quantity': 1,
            },
        ],
        mode='payment',
        success_url= f"{domain}/dashboard/successPayment?profile_id={required_profile.id}",
        cancel_url= f"{domain}/dashboard/account",
    )

    
    
    return redirect(session.url)

    
    
    
    
@login_required(login_url='/login/')
def successPayment(request):   
    context = {"title": "Membership"} 
    profile_id = request.GET.get('profile_id') 
    required_profile = ProfilesTable.objects.get(id=int(profile_id))
    
    
    stripe_customer_id = required_profile.stripe_customer_id
    
    # List all PaymentIntents associated with the customer
    payment_intents = stripe.PaymentIntent.list(
        customer=stripe_customer_id,
        limit=1  # adjust limit as needed
    )
    amount = payment_intents['data'][0]['amount']
    
    print("amount = ",amount)
    required_profile.balance = required_profile.balance + amount/100
    required_profile.save()
    # print(payment_intents)
    return redirect("manageAccount")
    