from django.shortcuts import render
from django.http import HttpResponse
from .lib.checker import regular_expression_checker

# Create your views here.

def checker(request):
    
    context = {

    }

    return render(request, 'checker/checker.html', context)

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

    return render(request, 'checker/checker.html', context)