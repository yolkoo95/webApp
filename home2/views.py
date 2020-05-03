from django.shortcuts import render
from .lib.intro import intro

# Create your views here.

def homepage(request):
    
    context = {
        'show_intro': True,
    }
    
    # merge dict from intro() and context
    context = dict(context, **intro())

    return render(request, 'home2/homepage.html', context)

def terms(request):

    return render(request, 'home2/terms.html')