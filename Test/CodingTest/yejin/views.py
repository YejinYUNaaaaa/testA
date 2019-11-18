from django.shortcuts import render
from .models import Yejin

def index(request):
    return render(request, 'index.html')

