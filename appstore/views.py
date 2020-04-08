from django.shortcuts import render

# Create your views here.

def appstore(request):

    return render(request, 'appstore/appstore.html')