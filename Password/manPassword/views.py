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
    print(managers)
    context = {'managers': managers}  # Define context here
    return render(request, 'passInfo.html', context)


def filter(request):
    category = request.GET.get('category', None)
    sort_order = request.GET.get('sort', None)
    managers = Manager.objects.all()

    # Если указана категория, фильтруем менеджеров по категории
    if category:
        managers = managers.filter(category__icontains=category)

    # Если указано направление сортировки, сортируем менеджеров
    if sort_order == 'asc':
        managers = managers.order_by('category')
    elif sort_order == 'desc':
        managers = managers.order_by('-category')

    context = {'managers': managers}
    return render(request, 'passInfo.html', context)


def jsonPasswords(request):

    data = list(Manager.objects.values())
    return JsonResponse(data, safe=False)


class CreatePassForm(forms.ModelForm):
    class Meta:
        model = Manager
        fields = ['category', 'password', 'description']

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
    if request.method == 'POST':
        form = CreatePassForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('manPassword:showpass')
    else:
        form = CreatePassForm(instance=data)
    return render(request, 'edit_data.html/', {'data': data, 'form': form})
