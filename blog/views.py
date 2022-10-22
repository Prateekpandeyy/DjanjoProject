from django.shortcuts import render
from django.HttpResponse import HttpResponse

# Create your views here.
def shopMainPage (request) :
    return HttpResponse("<h1>Shop </h1>")