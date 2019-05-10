from django.shortcuts import render
from django.http import HttpResponse
from .models import HitCount, MonitoredItem

# Create your views here.
def index(request, pk):
    monitored = MonitoredItem.objects.get(pk=pk)
    h = monitored.hitcount.all()[0]
    #counting the hit
    #todo: use sessions
    h.hits = h.hits + 1
    h.save()
    return HttpResponse(f'{pk} {monitored.hitcount.first()}')
