
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required
def home(request):
 return render(request, "home.html", {})


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
    messages.success(request, ("You were logged out!"))
    return redirect('home')