from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("<center><br><h1>Hi, <b>MICHAEL <em>FELIX</em> OKPISA</b></h1><center/>")