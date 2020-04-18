from django.shortcuts import HttpResponse, render
import os

# Create your views here.

def codehome(request):

    return render(request, 'leetcode/codehome.html')

def codepage(request, category, probName):
    
    # read problem description and note from txt
    dirPath = os.path.dirname(os.path.abspath(__file__))
    relPath = 'static/leetcode/src/' + category + '/' + probName + '.txt'
    relPathNote = 'static/leetcode/src/' + category + '/' + probName + 'Note.txt'
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
    
    # default language in cs50 is python, we want to add more language with addition argument
    if category == 'leetcode':
        language = 'cpp'
        addition = ''
    if category == 'cs50':
        language = 'py'
        addition = 'html'

    context = {
        'category': category,
        'language': language,
        'addition': addition,
        'probName': probName,
        'desc1': desc1, 
        'desc2': desc2,
        'begin': begin,
        'examples': examples,
        'notes': notes,
        'cppURL': 'leetcode/code/' + category + '/' + probName + '/cpp.html',
        'pyURL': 'leetcode/code/' + category + '/' + probName + '/py.html',
        'htmlURL': 'leetcode/code/' + category + '/' + probName + '/html.html',
    }

    return render(request, 'leetcode/codepage.html', context)