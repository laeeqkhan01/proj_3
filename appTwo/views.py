from django.shortcuts import render
from django.http      import HttpResponse

# Create your views here.

def pageTwo(request):
  return render(request, 'appTwo/t1.html')

def jqrydemo(request):
  return render(request, 'appTwo/t2.html')
