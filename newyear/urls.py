from django.urls import path
from .views import isitnewyear

urlpatterns = [
    path('', isitnewyear, name="isitnewyear")
]