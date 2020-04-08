from django.shortcuts import render
from .lib.generator  import generator
# Create your views here.

def login(request):

    info = generator()

    context = info

    return render(request, 'logindemo/login.html', context)

def register(request):

    context = {

    }
    
    return render(request, 'logindemo/register.html', context)