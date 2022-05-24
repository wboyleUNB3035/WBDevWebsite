from django.shortcuts import render

# Create your views here.

def athletics(request):
    return render(request, 'athletics/athletics.html')