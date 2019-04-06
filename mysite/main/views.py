from django.shortcuts import render
import os
# Create your views here.
from django.http import HttpResponse

def homepage(request):
    return render(request = request,
                  template_name='main/header.html')

def find_view(request):
    return render(request = request,
                  template_name='main/find_view.html')

def entities(request):
    return render(request = request,
                  template_name='main/entities.html')


def patterns(request):
    return render(request = request,
                  template_name='main/patterns.html')


def functions(request):
    return render(request = request,
                  template_name='main/functions.html')


def everidata(request):
    return render(request = request,
                  template_name='main/everidata.html')
    
