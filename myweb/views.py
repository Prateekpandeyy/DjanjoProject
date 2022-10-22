from django.http import HttpResponse
from django.shortcuts import render
def mainPage(request) :
    return render(request, 'index.html')
def clientPage(request) :
    return render(request, 'client.html')