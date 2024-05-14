from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.


USER_ROLE_FREELANCER_KEYWORD = 'Freelancer'
USER_ROLE_CLIENT_KEYWORD = 'Client'
USER_ROLE_ADMIN_KEYWORD = 'ADMIN'
USER_ROLE_SUPER_ADMIN_KEYWORD = 'SUPER_ADMIN'  
  

AVAILABLE_DISPUTE_STATUSES = [
    "Active","Resolved"
]

PROJECT_STATUS_OPEN = "Open"
PROJECT_STATUS_ACTIVE = "Active"
PROJECT_STATUS_DISPUTED = "Disputed"
PROJECT_STATUS_COMPLETED = "Completed"

AVAILABLE_PROJECT_STATUSES = [
   PROJECT_STATUS_OPEN,
   PROJECT_STATUS_ACTIVE,
   PROJECT_STATUS_DISPUTED,
   PROJECT_STATUS_COMPLETED,
]
AVAILABLE_USER_TYPES = [
    USER_ROLE_FREELANCER_KEYWORD,USER_ROLE_CLIENT_KEYWORD
]


class SkillsTable(models.Model):
    name = models.CharField(max_length=1000,default='')
    rating = models.FloatField(default=0, blank=True)
    def __str__(self) -> str:
        return f'{self.name}'
    
    
class ExperienceTable(models.Model):
    title       = models.CharField(max_length=1000,default='')
    start_date  = models.DateField(blank=True)
    end_date    = models.DateField(blank=True)
    # time = models.DateTimeField(default=datetime.now)

    def __str__(self) -> str:
        return f'{self.title}'
    
    
class ProfilesTable(models.Model):
    __AVAILABLE_USER_TYPES = ( (status,status) for status in AVAILABLE_USER_TYPES ) 
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phone = models.CharField(max_length=100,default='',blank=True)
    balance = models.FloatField(default=0, blank=True)
    
    skills = models.ManyToManyField(SkillsTable,blank=True,related_name='skills')
    experience = models.ManyToManyField(ExperienceTable,blank=True,)
    type =  models.CharField(max_length=1000,default='',choices=__AVAILABLE_USER_TYPES)
    username =  models.CharField(max_length=1000,default='', )
    password =  models.CharField(max_length=1000,default='', )
    stripe_customer_id =  models.CharField(max_length=1000,default='', )
    image_path =  models.CharField(max_length=1000,default='', )
    
    def __str__(self) -> str:
        return f'{self.username}'
    


    
    
class BidsTable(models.Model):
    proposal = models.TextField(default='',blank=True)
    budget  = models.IntegerField(default=0, blank=True)
    created_by = models.ForeignKey(ProfilesTable,on_delete=models.CASCADE,blank=True,null=True,)
    

class MessagesTable(models.Model):
    text = models.TextField(default='',blank=True)
    user = models.ForeignKey(ProfilesTable,on_delete=models.CASCADE)
    time = models.DateTimeField(default=datetime.now)
    
    
class ProjectsTable(models.Model):
    __AVAILABLE_PROJECT_STATUSES = ( (status,status) for status in AVAILABLE_PROJECT_STATUSES )
    title       = models.CharField(max_length=1000,default='')
    description = models.TextField(default='',blank=True)
    status =  models.CharField(max_length=1000,default='',choices=__AVAILABLE_PROJECT_STATUSES)
    start_date  = models.DateField(blank=True)
    end_date    = models.DateField(blank=True)
    budget  = models.IntegerField(default=0, blank=True)
    client_review = models.TextField(default='',blank=True)
    freelancer_review = models.TextField(default='',blank=True)
    freelancer = models.ForeignKey(ProfilesTable,on_delete=models.CASCADE,blank=True,null=True,related_name="freelancer")
    created_by = models.ForeignKey(ProfilesTable,on_delete=models.CASCADE,blank=True,null=True,related_name="created_by")
    bids = models.ManyToManyField(BidsTable,blank=True,related_name="bids")
    skills = models.ManyToManyField(SkillsTable,blank=True,related_name='required_skills')
    messages = models.ManyToManyField(MessagesTable,blank=True)
    
    
class DisputesTable(models.Model):
    __AVAILABLE_DISPUTE_STATUSES = ( (status,status) for status in AVAILABLE_DISPUTE_STATUSES )
    status =  models.CharField(max_length=1000,default='',choices=__AVAILABLE_DISPUTE_STATUSES)
    # messages = models.ManyToManyField(MessagesTable,blank=True)
    
    
     
class ContactUsTable(models.Model): 
    first_name  = models.CharField(max_length=10000, default='',blank=True,null=True)
    last_name   = models.CharField(max_length=10000, default='',blank=True,null=True)
    city        = models.CharField(max_length=10000, default='',blank=True,null=True)
    country     = models.CharField(max_length=10000, default='',blank=True,null=True)
    company     = models.CharField(max_length=10000, default='',blank=True,null=True)
    email       = models.CharField(max_length=10000, default='',blank=True,null=True)
    description = models.CharField(max_length=10000, default='',blank=True,null=True)

    def __str__(self) -> str:
        return f'{self.first_name}'      