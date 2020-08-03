from django.shortcuts import HttpResponse, render
import os

# Create your views here.

def codehome(request):

    return render(request, 'codehome/codehome.html')

def notepage(request, category, topic):
    
    context = {
        'category': category,
        'topic': topic,
        'contentURL': 'codehome/code/' + category + '/' + topic + '/' + topic + '.html',
    }

    return render(request, 'codehome/notepage.html', context)