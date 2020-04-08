from django.shortcuts import render

# Create your views here.

def radar(request):

    return render(request, 'radar/radar.html')