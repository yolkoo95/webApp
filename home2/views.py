from django.shortcuts import render
import random

# Create your views here.

def homepage(request):
    
    context = {
        'show_intro': True,
        'img_num': random.randint(0, 13),
    }

    return render(request, 'home2/homepage.html', context)