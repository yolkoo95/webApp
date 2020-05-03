from django.shortcuts import HttpResponse, render
import os

# Create your views here.

def codehome(request):

    return render(request, 'codehome/codehome.html')

def codepage(request, category, problemName):
    
    # read problem description and note from txt
    # dirPath = os.path.dirname(os.path.abspath(__file__))
    # relPath = 'static/leetcode/src/' + category + '/' + probName + '.txt'
    # relPathNote = 'static/leetcode/src/' + category + '/' + probName + 'Note.txt'
    # fileURL = os.path.join(dirPath, relPath)
    
    # with open(fileURL, 'r') as f:
    #     lines = (line.rstrip() for line in f)
    #     lines = list((line for line in lines if line))
    #     desc1 = lines.pop(0)
    #     desc2 = lines.pop(0)
    #     begin = lines.pop(0) # example description
    #     examples = lines
    
    # default language in cs50 is python, we want to add more language with addition argument
    if category == 'leetcode':
        language = 'cpp'
        addition = ''
    if category == 'cs50':
        language = 'py'
        addition = 'html'
    if category == 'datastructure':
        language = 'cpp'
        addition = ''

    context = {
        'category': category,
        'language': language,
        'addition': addition,
        'problemName': problemName,
        'problemURL': 'codehome/code/' + category + '/' + problemName + '/' + problemName + '.html',
        'cppURL': 'codehome/code/' + category + '/' + problemName + '/cpp.html',
        'pyURL': 'codehome/code/' + category + '/' + problemName + '/py.html',
        'htmlURL': 'codehome/code/' + category + '/' + problemName + '/html.html',
    }
    # URL indicate where to find source code 

    return render(request, 'codehome/codepage.html', context)