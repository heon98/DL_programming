from django.shortcuts import render
from django.http import HttpResponse

# create your views here.
def index(request):
    return HttpResponse("Hello, World. You're at the polls index.")

