from django.shortcuts import HttpResponse, render
import os

# Create your views here.

def codehome(request):

    return render(request, 'leetcode/codehome.html')

def codepage(request, category, probName):
    
    # read problem description and note from txt
    dirPath = os.path.dirname(os.path.abspath(__file__))
    relPath = 'static/leetcode/src/leetcode/' + probName + '.txt'
    relPathNote = 'static/leetcode/src/leetcode/' + probName + 'Note.txt'
    fileURL = os.path.join(dirPath, relPath)
    noteURL = os.path.join(dirPath, relPathNote)
    
    with open(fileURL, 'r') as f:
        lines = (line.rstrip() for line in f)
        lines = list((line for line in lines if line))
        desc1 = lines.pop(0)
        desc2 = lines.pop(0)
        begin = lines.pop(0)
        examples = lines
    
    with open(noteURL, 'r') as f:
        lines = (line.rstrip() for line in f)
        notes = list((line for line in lines if line))

    # return (HttpResponse(notes))
    
    context = {
        'category': category,
        'probName': probName,
        'desc1': desc1, 
        'desc2': desc2,
        'begin': begin,
        'examples': examples,
        'notes': notes,
        'cppURL': 'leetcode/code/' + category + '/' + probName + '/cpp.html',
        'pyURL': 'leetcode/code/' + category + '/' + probName + '/py.html',
    }

    return render(request, 'leetcode/codepage.html', context)