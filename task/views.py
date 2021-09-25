from django.shortcuts import render

# Create your views here.

tasks = ["cook pastha", "clean home", "wask clothes"]

def task(request):
    return render(request, "task/main.html", {
        "tasks": tasks
    })