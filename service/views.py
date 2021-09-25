from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def serivce(request):
    return render(request, 'service.html', {'page_title':"Our Services"})
