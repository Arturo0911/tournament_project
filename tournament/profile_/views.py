from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from .models import Profile, Cash_per_account
from django.views.decorators.csrf import csrf_exempt

import json


# Create your views here.

def get_profile(request): # GET method

    quantity_data = len(Profile.objects.all())
    json_data_response = []

    for x in range(0, quantity_data):
        
        # Get all objects stored in sqlite

        json_data_response.append({'fullname':Profile.objects.all()[x].full_name , 
        'email_address':Profile.objects.all()[x].email_address , 
        'username':Profile.objects.all()[x].username , 'password':Profile.objects.all()[x].password })
        #print(json_data_response)

    #print(json_data_response)


    
    return HttpResponse(json_data_response)



# To store data into sqlite
@csrf_exempt
def post_profile(request): # POST method

    #return HttpResponse("POST method detected")
    
    if request.method == 'POST':
        json_decoder = request.body.decode('utf-8')
        body = json.loads(json_decoder)
        #print(body)
        

        data_saved = Profile(full_name = body['full_name'],
        email_address= body['email_address'], username = body['username'],
        password = body['password'])

        data_saved.save()



        return HttpResponse("POST method detected")
    else:
        return HttpResponse("There's not any http method")


# To modify and update

@csrf_exempt
def update_profile(request):
    id = request.GET.get('id', '')
    print(id)
    Profile.objects.filter(pk= id).update()
    print(request.body)
    return HttpResponse("To update into sqlite3")
    