from django.shortcuts import render
from django.http import HttpResponse
def create_blog(request):
    return HttpResponse("<h1>Hello! Welcome to home page.</h1>")
