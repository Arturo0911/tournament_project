from django.shortcuts import render, redirect,HttpResponse
from django.http import JsonResponse

# Create your views here.

def index(request):
    return HttpResponse("<h5>Index page. </h5>")