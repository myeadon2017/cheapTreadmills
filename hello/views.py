from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "index.html")

def ellipticals(request):
    return render(request, "ellipticals.html")

def healthy_snacks(request):
    return render(request, "healthy_snacks.html")

def treadmills(request):
    return render(request, "treadmills.html")

def protien_shakes(request):
    return render(request, "protien_shakes.html")


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
