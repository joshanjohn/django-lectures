from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, "hello/index.html")
    
def get_name(request, name):
    return render(request, "hello/name.html", {
        "name": name.capitalize()
    })