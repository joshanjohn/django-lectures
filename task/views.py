from django import forms
from django.shortcuts import render

# Create your views here.


tasks = ["cook pastha", "clean home", "wask clothes"]

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    priority = forms.IntegerField(label="Priority", min_value=1, max_value=10)

def task(request):
    return render(request, "task/main.html", {
        "tasks": tasks
    })

def add(request):
    if request.method == 'POST':
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            tasks.append(task)

    return render(request, "task/add.html",{
        "form": NewTaskForm()
    })