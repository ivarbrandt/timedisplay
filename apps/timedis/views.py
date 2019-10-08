from django.shortcuts import render, HttpResponse
from time import gmtime, strftime

def index(request):
    return HttpResponse("CONNECTED")

def time(request):
    context = {
        "mdy": strftime("%b %d, %Y", gmtime()),
        "time": strftime("%I:%M %p", gmtime())
    }
    return render(request, 'timedis/index.html', context)




# Create your views here.
