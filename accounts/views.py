from django.shortcuts import render, redirect, HttpResponse
from .forms import RegistrationForm
import uuid
from django.core.mail import send_mail
from  django.contrib.sites.shortcuts import get_current_site
from .models import CustomUser
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def register_view(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_email_verified = False
            token = str(uuid.uuid4())
            user.email_verification_token = token
            user.save()

            subject = "Email verification"
            current_site =  get_current_site(request)
            activation_link = f"http://{current_site}/accounts/verify-email/{token}/"
            message = f"Click the link to activate your account: {activation_link}"
            send_mail(subject, message, "info@booksmith.com", [user.email,])
            return redirect("accounts:login")

    else:
        form = RegistrationForm()
        return render(request, "accounts/register.html", {"form": form})


def verify_email_view(request, token):
    try:
        user =  CustomUser.objects.get(email_verification_token=token)
        if user:
            user.is_email_verified = True
            user.email_verification_token = None
            user.save()
            return redirect("accounts:login")
        else:
            return HttpResponse("Token is invalid or expierd!")
    except:
        return HttpResponse("User not found!")


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user.is_email_verified:
                login(request, user)
                return redirect("booksmith:home")
            else:
                return HttpResponse("Email not verified!")

    else:
        form = AuthenticationForm()
        return render(request, "accounts/login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("accounts:login")