from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def supraja(request):
    return HttpResponse('<marquee>HAI HOW ARE YOU</marquee>')
