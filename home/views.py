from django.shortcuts import render

# Create your views here.

def home(request):

    context = {

    }

    return render(request, 'home/homepage.html', context)

def terms(request):

    context = {

    }

    return render(request, 'home/terms.html', context)