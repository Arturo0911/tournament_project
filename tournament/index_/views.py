from django.shortcuts import render, redirect,HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


# import modules insders

from .functions import json_decode



# Create your views here.

def index(request):
    if request.method == 'GET':
        json_data = [
            {
            "nombre": "Arturo Negreiros",
            "description": "This is a test for postman and Django"
            },
            {
            "nombre": "Favio Samanez",
            "description": "This is a test for postman and Django"
            }
        ]
        return HttpResponse(json_data)
    
@csrf_exempt
def _index_post(request):
    
    value_parsed = json_decode.decode_raw_data_post_method(request.body)
    for x in value_parsed:
        print(x,": ", value_parsed[x])


    return HttpResponse("pobando")
    