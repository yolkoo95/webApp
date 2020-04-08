from django.shortcuts import render

# Create your views here.

def ticktock(request):

    return render(request, 'ticktock/ticktock.html')