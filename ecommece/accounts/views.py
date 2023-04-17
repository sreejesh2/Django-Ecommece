from django.shortcuts import render, redirect
from django.views.generic import CreateView, View, FormView,TemplateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
import uuid

from .models import CustomUser, Profile
from .forms import UserCreationForm,SignInForm


# Create your views here.

def token_send(request,*args, **kwargs):
    return render(request,"token.html")



class RegistrationView(View):
    def get(self, request, *args, **kwargs):
        form = UserCreationForm()
        return render(request, "register.html", {"form": form})

    def post(self, request, *args, **kwargs):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            user = form.save()
            auth_token = str(uuid.uuid4())
            profile_obj = Profile.objects.create(user=user, auth_token=auth_token)
            profile_obj.save()
            send_mail_after_registration(email, auth_token)
            return redirect('token')
        return render(request, "register.html", {"form": form})

def send_mail_after_registration(email, token):
    subject = "Your Account needs to be Verified"
    message = f"Hi! Please paste the link to verify your account: http://127.0.0.1:8000/verify/{token}"
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list)

def verify(request, auth_token):
    try:
        profile_obj = Profile.objects.filter(auth_token=auth_token).first()
        if profile_obj:
            profile_obj.is_verified = True
            profile_obj.save()
            user = profile_obj.user
            user.is_active = True
            user.save()
            login(request, user)  # Log in the user
            messages.success(request, "Your account has been verified and you are now logged in.")
            return redirect('home')  # Redirect to home page after login
        else:
            messages.error(request, "Please enter a valid email.")
            return redirect('register')
    except Exception as e:
        print(e)


class IndexView(TemplateView):
    template_name="home.html"

class SignInView(View):
    def get(self,request,*args, **kwargs):
        form=SignInForm()
        return render(request,"login.html",{"form":form})
    
    def post(self,request,*args, **kwargs):
        form=SignInForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            usr=authenticate(request,username=uname,password=pwd)
            if usr:
                login(request,usr)
                messages.success(request,"Login successfully")
                return redirect('home')
        messages.error(request,"Enter valid Credential")    
        return render(request,"login.html",{"form":form})    
            

