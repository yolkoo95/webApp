from django.shortcuts import render

# Create your views here.

def codehome(request):

    return render(request, 'leetcode/codehome.html')

def leetcode(request):
    
    return render(request, 'leetcode/leetcode.html')

def cs50(request):
    
    return render(request, 'leetcode/leetcode.html')

def datastructure(request):
    
    return render(request, 'leetcode/leetcode.html')

def webapp(request):
    
    return render(request, 'leetcode/leetcode.html')