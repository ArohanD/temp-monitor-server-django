from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .sys_monitor import getTemps

def index(request):
    return JsonResponse(getTemps().Name, safe=False)
