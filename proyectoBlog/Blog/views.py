from urllib import request
from django.shortcuts import render,HttpResponse
from django.http.request import QueryDict
from django.http import HttpResponse
from Blog.models import *

# Create your views here.
def inicio(request):
    return render(request,'Blog/inicio.html')