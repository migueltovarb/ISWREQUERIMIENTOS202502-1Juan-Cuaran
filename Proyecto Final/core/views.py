from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Users
# Create your views here.
#HTML

def index (request):
    return HttpResponse("<h1>Index</h1>")

def hello (request, username):
    return HttpResponse("<h1>Hello %s</h1>"  %username)

def about (request):
    return HttpResponse("about")

def get_users (request):
    users = Users.objects.all() 
    return JsonResponse(users)