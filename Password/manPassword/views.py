from django.shortcuts import render
from .models import Manager
from django.http import JsonResponse
import json

from django.shortcuts import render, redirect


def home(request):
 return render(request, "home.html", {})


def showpass(request):
    managers = Manager.objects.all()
    context = {'managers': managers}  # Define context here
    return render(request, 'passInfo.html', context)



def jsonPasswords(request):

    data = list(Manager.objects.values())
    return JsonResponse(data, safe=False)


from django.shortcuts import render, redirect
from django import forms
from .models import Manager

class CreatePassForm(forms.Form):
    category = forms.CharField(max_length=100, required=False)
    password = forms.CharField(max_length=255)
    description = forms.CharField(widget=forms.Textarea, required=False)

def createPass(request):
    if request.method == 'POST':
        form = CreatePassForm(request.POST)
        if form.is_valid():
            category = form.cleaned_data['category']
            password = form.cleaned_data['password']
            description = form.cleaned_data['description']
            manager = Manager.objects.create(
                user=request.user,
                category=category,
                password=password,
                description=description
            )
            return redirect('user:home') 
    else:
        form = CreatePassForm()
    return render(request, 'createPass.html', {'form': form})
