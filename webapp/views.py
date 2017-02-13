from __future__ import unicode_literals
from future.builtins import str
from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import render, redirect

def login(request):
    #return HttpResponse("Hello world")

    return render(request, 'login.html')
