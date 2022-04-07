from urllib import request
from django.shortcuts import render,HttpResponse
from django.http.request import QueryDict
from django.http import HttpResponse
from Blog.models import *
from Blog.forms import *

# Create your views here.
def inicio(request):
    return render(request,'Blog/index.html')

def login(request):
    if request.method == "POST":
        form = loginFormulario(request.POST)
        print(form)
        if form.is_valid():
            data = form.cleaned_data
            usuario = User(username=data["username"],password=data["password"])
            usuario.save()
            return render(request,'Blog/index.html')
    else:
        form = loginFormulario()
        return render (request,'Blog/login.html', {"form":form})
    