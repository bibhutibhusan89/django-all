from django.shortcuts import render

# Create your views here.


from django.template import loader
from django.http import HttpResponse 


def index(request):
    #Call :http://localhost:8000/index/
    template = loader.get_template("index.html")
    name = {"html_name": "Bibhu"}    
    return(HttpResponse(template.render(name)))
