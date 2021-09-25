from django.shortcuts import render
from datetime import date

# Create your views here.


def isitnewyear(request): 
    today = str( date.today())
    if  today[5:10]== '01-01':
        return render(request, 'isitnewyear/newyear.html', {"boolean": "YES"})        
    else:
        return render(request, 'isitnewyear/newyear.html', {"boolean": "NO"})        
