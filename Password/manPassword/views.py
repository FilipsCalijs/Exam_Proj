from django.shortcuts import render
from .models import Manager
from django.shortcuts import redirect, get_object_or_404
from django.http import JsonResponse
import json
from django.shortcuts import render, redirect
from django import forms



def home(request):
 return render(request, "home.html", {})


def showpass(request):
    managers = Manager.objects.all()
    context = {'managers': managers}  # Define context here
    return render(request, 'passInfo.html', context)



def jsonPasswords(request):

    data = list(Manager.objects.values())
    return JsonResponse(data, safe=False)



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




def delete(request, id):
    dele = get_object_or_404(Manager, pk=id)
    dele.delete()
    return redirect('user:home')


def edit_data(request, data_id):
    data = get_object_or_404(Manager, pk=data_id)
    form = CreatePassForm(request.POST or None)
    return render(request, 'edit_data.html/', {'data': data, 'form': form})