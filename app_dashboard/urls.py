
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import *     
from .views_users import * 
from .views_account import * 
from .views_projects import * 
from .views_search_projects import * 
from .views_payment import * 
from .views_chat import * 


urlpatterns = [    
    
    path('', dashboard, name='dashboard'),     
    # Profile     .html
    path('account', manageAccount, name='manageAccount'),       
    path('viewPublicProfile', viewPublicProfile, name='viewPublicProfile'),       
    path('uploadProfilePicture', uploadProfilePicture, name='uploadProfilePicture'),       
    path('addNewExperience', addNewExperience, name='addNewExperience'),       
    path('deleteExperience', deleteExperience, name='deleteExperience'),    
    
       
    path('projects', manageProjects, name='manageProjects'),        
    path('editProject', editProject, name='editProject'),        
    path('addNewProject', editProject, name='addNewProject'),        
    path('viewProject', viewProjectDetails, name='viewProject'),    
    path('postReview', postReview, name='postReview'),    
        
    path('viewProjectChat', viewProjectChat, name='viewProjectChat'),  
    path('markProjectCompleted', markProjectCompleted, name='markProjectCompleted'),  
    
    path('view_project_chat', view_project_chat, name='view_project_chat'),
    path('view_project_chat/', view_project_chat, name='view_project_chat'),

          
    path('awardProject', awardProject, name='awardProject'),        
    path('withdrawBid', withdrawBid, name='withdrawBid'),        
    
    
    path('viewProjectBids', viewProjectBids, name='viewProjectBids'),        
    path('deleteProject', deleteProject, name='deleteProject'),       
    path('searchProjects', searchProjects, name='searchProjects'),       
    
    path('makePaymentSessionLink', makePaymentSessionLink, name='makePaymentSessionLink'),  
    path('successPayment', successPayment, name='successPayment'),  
         
     
     
         
    
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

