from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name='index'),


    path('login',views.login,name='login'),
    path('login_form_submission',views.login_form_submission,name='login_form_submission'),

    path('signup',views.signup,name='signup'),
    path('signup_form_submission',views.signup_form_submission,name='signup_form_submission'),

    
    path('contact_form_submission',views.contact_form_submission,name='contact_form_submission'),
]