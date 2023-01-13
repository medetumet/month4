from django.shortcuts import render
from django.http import  HttpResponse
import datetime

def hello_view(request):
    if request.method == 'GET':
        return HttpResponse("Hello! Its my project")

def date_view(request):
    if request.method == 'GET':
        return HttpResponse (datetime)

def goodby_view(request):
    if request.method == 'GET':
        return HttpResponse("Goodby user!")

