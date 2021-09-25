from django.urls import path
from .views import index, get_name

urlpatterns = [
    path('', index, name="index"),
    path('name/<str:name>/', get_name, name="getName")
]