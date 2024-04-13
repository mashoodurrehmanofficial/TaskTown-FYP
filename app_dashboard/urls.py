
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import *     
from .views_users import * 
from .views_account import * 
from .views_projects import * 
from .views_search_projects import * 
from .views_payment import * 


urlpatterns = [    
    
    path('', dashboard, name='dashboard'),     
    # Profile     
    path('account', manageAccount, name='manageAccount'),       
    path('addNewExperience', addNewExperience, name='addNewExperience'),       
    path('deleteExperience', deleteExperience, name='deleteExperience'),    
    
       
    path('projects', manageProjects, name='manageProjects'),        
    path('editProject', editProject, name='editProject'),        
    path('addNewProject', editProject, name='addNewProject'),        
    path('viewProject', viewProjectDetails, name='viewProject'),        
    path('viewProjectBids', viewProjectBids, name='viewProjectBids'),        
    path('deleteProject', deleteProject, name='deleteProject'),       
    path('searchProjects', searchProjects, name='searchProjects'),       
    
    path('makePaymentSessionLink', makePaymentSessionLink, name='makePaymentSessionLink'),  
    path('successPayment', successPayment, name='successPayment'),  
         
     
     
         
    
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

