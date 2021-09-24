from django.urls import path
from .views import index, get_name

urlpatterns = [
    path('', index, name="index"),
    path('<str:name>/', get_name, name="getName")
]