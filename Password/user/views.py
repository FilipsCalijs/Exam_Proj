
#views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from manPassword.models import Manager

#to create json
from django.contrib.auth.models import User  
from django.http import JsonResponse
import json

@login_required
def home(request):
    managers = Manager.objects.all()
    return render(request, "home.html", {'managers': managers})



def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("user:login")
    else:
        form = SignUpForm()

    return render(request, "registration/signup.html", {"form": form})



def logout(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    print("User has been logged out.")  # Вывод сообщения в консоль
    return redirect("user:login")



def json(request):

    data = list(User.objects.values())
    return JsonResponse(data, safe=False)