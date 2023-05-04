from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignupForm,LoginForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
import json
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes





def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            print(user.pk)
            current_site = get_current_site(request)
            message = render_to_string('frontend/Email_template.html', {
                'user':user, 'domain':current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
                
            })
            # Sending activation link in terminal
            # user.email_user(subject, message)
            print(account_activation_token.make_token(user))
            mail_subject = 'Activate your account.'
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration.')
            # return render(request, 'acc_active_sent.html')
    else:
        form = SignupForm()
    return render(request, 'frontend/signup.html', {'form': form})


def activate(request,uidb64,token):
     try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
     except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
     if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        print("email verified")
        user.save()
        login(request, user)
        print("higigi")
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
     else:
        return HttpResponse('Activation link is invalid!')

def Login(request):
     if request.method == "POST":
        form = LoginForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            print(username)
            print(password)
            user = authenticate(request, username=username, password=password)
            print(user)
            if user is not None:
                print('hi')
               # messages.success(request, f' welcome {username} !!')
                login(request, user)
                return redirect('home')
        return HttpResponse("error")
    # if a GET (or any other method) we'll create a blank form
     else:
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('home'))
        form = LoginForm()
        return render(request, "frontend/login.html", {"form": form})
def Logout(request):
    logout(request)
    return redirect('login/')
@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def home(request):
    permission_classes=[IsAuthenticated]
    user =request.user
    return render(request,"frontend/homepage.html",{"user":user})