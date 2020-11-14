from django.shortcuts import render
from django.http import HttpResponse

def index(request):
   return  render(request,'index.html')


def about(request):
    return  render(request,'about.html')


def contact(request):
        return  render(request,'contact.html')

    

def login(request):
        return  render(request,'contact.html')

def coach(request):
        return  render(request,'coaching.html')

def time(request):
        return  render(request,'time.html')





