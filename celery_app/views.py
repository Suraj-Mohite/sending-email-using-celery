from celery_app.tasks import Myfunc
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    Myfunc.delay()
    return HttpResponse("Done task")