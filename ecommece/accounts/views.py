from django.shortcuts import render, redirect
from django.views.generic import CreateView, View, FormView, TemplateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
import uuid
from django.core.exceptions import ValidationError

from .models import CustomUser, Profile
from .forms import UserCreationForm, SignInForm


# Create your views here.

def token_send(request, *args, **kwargs):
    return render(request, "token.html")


class RegistrationView(View):
    def get(self, request, *args, **kwargs):
        form = UserCreationForm()
        return render(request, "register.html", {"form": form})

    def post(self, request, *args, **kwargs):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            email = cleaned_data.get("email")

         
            # If email does not exist, continue with registration process
            f_name = cleaned_data.get("first_name")
            l_name = cleaned_data.get("last_name")
            pwd1 = cleaned_data.get("password1")
            pwd2 = cleaned_data.get("password2")

            # Check if passwords match
            if pwd1 != pwd2:
                messages.error(request, "Passwords do not match.")
                return render(request, "register.html", {"form": form})

            # Create user object and save to database
            user = form.save(commit=False)
            user.email = email
            user.set_password(pwd1)
            user.save()

            # Create profile object and send email with activation link
            auth_token = str(uuid.uuid4())
            profile_obj = Profile.objects.create(user=user, auth_token=auth_token)
            profile_obj.save()
            send_mail_after_registration(email, auth_token)

            # Redirect user to token confirmation page
            return redirect('token')

        # If form is not valid, display error messages
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
            user.backend = 'django.contrib.auth.backends.ModelBackend'  
            login(request, user) 
            messages.success(request, "Your account has been verified and you are now logged in.")
            return redirect('home') 
        else:
            messages.error(request, "Invalid verification token.")
            return redirect('register')
    except Profile.DoesNotExist:
        messages.error(request, "Invalid verification token.")
        return redirect('register')
    except Exception as e:
        messages.error(request, "An error occurred during verification.")
        return redirect('register')



class SignInView(View):
    def get(self, request, *args, **kwargs):
        form = SignInForm()
        return render(request, "login.html", {"form": form})

    def post(self, request, *args, **kwargs):
        form = SignInForm(request.POST)
        if form.is_valid():
            uname = form.cleaned_data.get("email")
            pwd = form.cleaned_data.get("password")
            usr = authenticate(request, email=uname, password=pwd)
            if usr:
                login(request, usr)
                messages.success(request, "Login successfully")
                return redirect('home')
        messages.error(request, "Enter valid Credential")
        return render(request, "login.html", {"form": form})
