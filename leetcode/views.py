from django.shortcuts import HttpResponse, render
import os

# Create your views here.

def codehome(request):

    return render(request, 'leetcode/codehome.html')

def codepage(request, category, probName):
    
    # read problem description from txt
    dirPath = os.path.dirname(os.path.abspath(__file__))
    relPath = 'static/leetcode/src/leetcode/3Sum.txt'
    fileURL = os.path.join(dirPath, relPath)
    
    with open(fileURL, 'r') as f:
        lines = (line.rstrip() for line in f)
        lines = list((line for line in lines if line))
        desc1 = lines.pop(0)
        desc2 = lines.pop(0)
        begin = lines.pop(0)
        examples = lines

    # return (HttpResponse(examples))
 
    context = {
        'category': category,
        'probName': probName,
        'desc1': desc1,
        'desc2': desc2,
        'begin': begin,
        'examples': examples,
        'cppURL': 'leetcode/code/' + category + '/' + probName + '/cpp.html',
        'pyURL': 'leetcode/code/' + category + '/' + probName + '/py.html',
    }

    return render(request, 'leetcode/codepage.html', context)