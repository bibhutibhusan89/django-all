from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
import datetime

def hello(request):
    # Call:http://localhost:8000/hello/
    return HttpResponse("<h2> Hello. Welcome to Django!!</h2>")

def index(request):
    #Call:http://localhost:8000/index/
    time = datetime.datetime.now()
    return HttpResponse("<h3>Current Time is: %s</h3>" % time)


from django.views.decorators.http import require_http_methods  

import json

@require_http_methods(['GET'])
def getRequest(request):
    #Call:http://localhost:8000/getR/
    #return HttpResponse('<h1>This is Http GET request.</h1>')
    return HttpResponse(json.dumps({"req_type":"This is Http GET request.", "val":"Success."}))
 
@require_http_methods(['POST'])
def postRequest(request):
    #Call:http://localhost:8000/postR/
    #return HttpResponse('<h1>This is Http POST request.</h1>')
    return HttpResponse(json.dumps({"req_type":"This is Http POST request.", "val":"Success."}))
    