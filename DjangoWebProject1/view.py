from django.shortcuts import render
from django.http import HttpResponse
from.import view

def index(request):
   return  render(request,'.html')

