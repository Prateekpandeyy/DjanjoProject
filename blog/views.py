from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def shopMainPage(request) :
    return render(request, 'blog/blog.html')
def about(request) :
    return render(request, 'blog/about.html')
def contact(request) :
    return render(request, 'blog/contact.html')
def search(request) :
    return render(request, 'blog/serach.html')
def tracker(request) :
    return render(request, 'blog/tracher.html')
def productview(request) :
    return render(request, 'blog/productview.html')
def checkout(request) :
    return render(request, 'blog/checkout.html')