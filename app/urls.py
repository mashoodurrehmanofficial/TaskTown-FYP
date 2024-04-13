
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import *  
from .views_auth import *   
from .views_ajax import *   
 
urlpatterns = [       
    
    # general
    path('', home, name='home'),     
    path('', home, name='index'),     
    path('products', products, name='products'),     
    path('about', about, name='about'),     
    path('contact', contact, name='contact'),      
      
    path('register/', registerRouter, name='register'),     
    path('login/', loginRouter, name='login'),     
    path('logout/', logoutRouter, name='logout'),
    # path('verifyOtp', verifyOtp, name='verifyOtp'),
    path('changePassword', changePassword, name='changePassword'),     
    path('sendPasswordResetLink/', sendPasswordResetLink, name='sendPasswordResetLink'),     
    
    
    
    # ajax calls 
    path('ajax/setTheme', setTheme, name='setTheme'),
    
    
    # payments
    # path('payment/createCheckoutSession', createCheckoutSession, name='createCheckoutSession'),
    # path('payment/successPayment', successPayment, name='successPayment'),
    # path('createMembershipManagementSession/', createMembershipManagementSession, name='createMembershipManagementSession'),
    # path('cancelMembership/', cancelMembership, name='cancelMembership'),
    # path('cancelMembership', cancelMembership, name='cancelMembership'),
        
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

