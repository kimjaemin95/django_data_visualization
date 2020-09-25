from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password




# Create your views here.
def line(request):
    '''
    http://127.0.0.1:8000/graph/line/
    '''
    return render(request, 'home.html')
