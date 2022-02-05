from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def hallo(reqeust):
    return HttpResponse('Hallo world')
