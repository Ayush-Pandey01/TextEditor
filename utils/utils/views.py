# I have created this file - Ayush Pandey

from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'default')
    if djtext == "":
        return render(request, 'alert.html')
    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')

    # Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'",<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        # without punctuation text
        djtext = analyzed

    if fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        # Capitalised text
        djtext = analyzed

    if extraspaceremover == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        # Extraspace Removed text
        djtext = analyzed

    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
    #     New Line removed text
    if newlineremover != "on" and extraspaceremover != "on" and fullcaps != "on" and removepunc != "on":
        # printing the Error msg when no checkbox is ticked
        return render(request, 'alert2.html')
    # rendering the analysed web page
    return render(request, 'analysed.html', params)


def alert(request):
    return render(request, 'alert.html')


def alert2(request):
    return render(request, 'alert2.html')


def about(request):
    return render(request, 'About.html')


def contactus(request):
    return render(request, 'contactus.html')


def Thanks(request):
    feeds = request.POST.get('text', 'default')
    if feeds == "":
        return render(request, 'lastalert.html')
    return render(request, 'Thanks.html')


def lastalert(request):
    return render(request, 'lastalert.html')
