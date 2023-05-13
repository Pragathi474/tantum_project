from django.http import request
from django.shortcuts import render,HttpResponse
from . models import *
from django.contrib import messages

from django.conf import settings
from django.core.mail import send_mail
import random



def index(request):
    return render(request,'index.html')
def signup(request):
    return render(request,'signup.html')

def signup_form_submission(request):
    if request.method=="POST":
        if signup_table.objects.filter(username=request.POST.get('username'),
                                        email=request.POST.get('email'),
                                        password=request.POST.get('password'),
                                        confirm_password=request.POST.get('confirm_password')):
            messages.error(request,'username/password taken already',extra_tags='already')
            return render(request,'signup.html')
        else:
          
            reg=signup_table(username=request.POST.get('username'),
                                email=request.POST.get('email'),
                                password=request.POST.get('password'),
                                confirm_password=request.POST.get('confirm_password'))
            reg.save()

            #api code
           
            try:
                otp_number=random.randint(000000,999999)
                print(f"your otp number is :",otp_number)
                
                email=request.POST.get('email')

                print(f"user email is {email}")
                subject = 'Welcome to TANTUM'
                   
                message = f'Hi {email}, Thank you! for signing in TANTUM PROJECTS. Your tantumid is: {otp_number}.\nYou can check out our projects with detailed description.'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [email, ]
                send_mail( subject, message, email_from, recipient_list )
                print("mail sent successfuly")
        
                return render(request,'login.html')
            except:
                print("********sorry email is not sending please type proper email id")
                return render(request,'login.html')
        
    else:
        return render(request,'signup.html')
def login(request):
    return render(request,'login.html')

def login_form_submission(request):
    if request.method=="POST":
        if signup_table.objects.filter(username=request.POST.get('username'),
                                         password=request.POST.get('password')):
            #logger_data=signup_table.objects.get(username=request.POST.get('username'),
                                                   # password=request.POST.get('password')) 
            #view_data=customer_table.objects.all() 
            #return render(request,'index.html',{'logger_data':logger_data,'view_data':view_data})
            return render(request,'project.html')
        else:
            
            messages.error(request,'Invalid username/password',extra_tags='already')
            return render(request,'login.html')

def contact_form_submission(request):
    ex1=contact_table(name=request.POST.get('name'),
                     email=request.POST.get('email'),
                     subject=request.POST.get('subject'),
                     message=request.POST.get('message'))
    ex1.save()
    return HttpResponse(ex1)
