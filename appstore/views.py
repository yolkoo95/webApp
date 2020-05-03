from django.shortcuts import render
from django.http import HttpResponse
from .lib.checker import regular_expression_checker
from .lib.generator import generator

# Create your views here.

def appstore(request):

    return render(request, 'appstore/appstore.html')

# App - Checker
def checker(request):
    
    context = {

    }

    return render(request, 'appstore/checker/checker.html', context)

def check(request):

    u_input = request.POST['re_input']
    u_samples = request.POST['re_samples']
    
    if (u_input is None) or (u_samples is None):
        return HttpResponse("ValueError: fail to receive data")

    # begin to check
    pattern = u_input
    test_samples = u_samples.splitlines()
    
    results = regular_expression_checker(pattern, test_samples)

    context = {
        'pattern': pattern,
        'results': results,
    }

    return render(request, 'appstore/checker/checker.html', context)

# Graphic - Ticktock
def ticktock(request):

    return render(request, 'appstore/ticktock/ticktock.html')

# Lab - Radar
def radar(request):

    return render(request, 'appstore/radar/radar.html')

# Design - Logindemo
def login(request):

    info = generator()

    context = info

    return render(request, 'appstore/logindemo/login.html', context)

def register(request):

    context = {

    }
    
    return render(request, 'appstore/logindemo/register.html', context)