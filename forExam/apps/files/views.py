from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("На месте")

def download(request):
    return HttpResponse("Страница загрузки файла")