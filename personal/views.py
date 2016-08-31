from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'personal/Main.html')

def index1(request):
    return render(request,'personal/Taller1_1.html')

def index2(request):
    return render(request,'personal/Taller1_2.html')
