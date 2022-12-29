from django.shortcuts import render

# Create your views here.

def user(request):
    d={'name':'chandhu'}
    return render(request,'user.html',d)
