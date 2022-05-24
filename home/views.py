from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home/index.html')

def projectOne(request):
    return render(request, 'home/portfolio-item01.html')

def projectTwo(request):
    return render(request, 'home/portfolio-item02.html')

def projectThree(request):
    return render(request, 'home/portfolio-item03.html')

def projectFour(request):
    return render(request, 'home/portfolio-item04.html')

def projectFive(request):
    return render(request, 'home/portfolio-item05.html')

def projectSix(request):
    return render(request, 'home/portfolio-item06.html')