from django.shortcuts import render
from .models import Manager

def showpass(request):
    managers = Manager.objects.all()
    context = {'managers': managers}  # Define context here
    return render(request, 'passInfo.html', context)


# НЕ ЗАБУДЬ ЗАВТРА (ТЕ СЕГОДНЯ) ЗАПУШИТ