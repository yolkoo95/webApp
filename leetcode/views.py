from django.shortcuts import render

# Create your views here.

def leetcode(request):
    
    return render(request, 'leetcode/leetcode.html')