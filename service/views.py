from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Sessions, User, Vendors, License, Dep, PC
from .tasks import update_db_every_minute


def index(request):
    session = Sessions.objects.all()
    return render(request, "index.html", {"sessions": session})


def create(request):
    update_db_every_minute.delay()
    return HttpResponseRedirect("/")



