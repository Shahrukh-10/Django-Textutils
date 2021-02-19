# Devloper -> Added manually
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request , 'index.html')

def about(request):
    return render(request , 'about.html')

def analyze(request):
    djtext = request.GET.get('text','default')
    removepunc = request.GET.get('removepunc','off')
    fullcaps = request.GET.get('fullcaps','off')
    newlineremover =request.GET.get('newlineremover','off')
    extraspaceremover = request.GET.get('extraspaceremover' , 'off')
    charcount = request.GET.get('charcount','off')
    print(removepunc + ' '+ djtext)

    if removepunc == 'on':
        analyzed =''
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        context = { 
            'analyzedtext':analyzed,
            'purpose':'Remove Punctuation'
        }
        return render(request,'analyze.html',context)

    
    if (fullcaps == 'on'):
        analyzed = ''
        for char in djtext:
            analyzed = analyzed + char.upper()
        context = { 
            'analyzedtext':analyzed,
            'purpose':'Change to upper case'
        }
        return render(request, 'analyze.html',context)



    if(newlineremover == "on"):
        analyzed = ''
        for char in djtext:
            if char != '\n':
                analyzed = analyzed + char
        context = { 
            'analyzedtext':analyzed,
            'purpose':'Removed new line'
        }
        return render(request, 'analyze.html',context)
    

    if (extraspaceremover=='on'):
        analyzed=''
        for index,char in enumerate(djtext):
            if not(djtext[index] == ' ' and djtext[index+1]==' '):
                analyzed = analyzed+char
        context = { 
            'analyzedtext':analyzed,
            'purpose':' Extra Space Remover'
        }
        return render(request, 'analyze.html',context)

    if(charcount == 'on'):
        count=0
        for char in djtext:
            if char != ' ':
                count = count + 1
        context = { 
            'analyzedtext':count,
            'purpose':' Extra Space Remover'
        }
        return render(request, 'analyze.html',context)


    else:
        analyzed = djtext
        context = { 
            'analyzedtext':analyzed,
            'purpose':'No Action'
        }
        return render(request, 'analyze.html',context)


# def removepunc(request):
#     djtext = request.GET.get('text','default')
#     print(djtext)
#     return HttpResponse("Remove punctuation")

# def spaceremover(request):
#     return HttpResponse("Remove space")

# def newlineremover(request):
#     return HttpResponse("Remove newline")

# def charcount(request):
#     return HttpResponse('''Charcount <a href="/" > back </a>''')


# def capfirst(request):
#     return HttpResponse("Capitalize first") 

# def text(request):
#     return HttpResponse('text')