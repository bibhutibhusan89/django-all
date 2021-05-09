from django.shortcuts import render

# Create your views here.


from django.template import loader
from django.http import HttpResponse 
from django.views.decorators.http import require_http_methods

def index(request):
    #Call :http://localhost:8000/index/
    template = loader.get_template("index.html")
    name = {"html_name": "Bibhu"}    
    return(HttpResponse(template.render(name)))

@require_http_methods(["GET"])
def getRequest(request):
    return HttpResponse('<h1>This is Http GET request.</h1>') 
    