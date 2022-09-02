from cgitb import reset
from re import template
from turtle import ycor
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from .models import Child, Child2, Child3
from django.urls import reverse
# Create your views here.

def index(request):
    # return HttpResponse("Hello Child1.")
    # template = loader.get_template("myPage.html")
    # myChild = Child.objects.all().values()
    # output = ""
    # for i in myChild:
    #     output += i["firstName"]
    mychild = Child.objects.all().values()
    template = loader.get_template("index.html")
    context = {
        'mychild' : mychild
    }
    return HttpResponse(template.render(context, request))

def home(request):
    mychild = Child2.objects.all().values()
    template = loader.get_template("newindex.html")
    context = {
        'mychild' : mychild
    }
    return HttpResponse(template.render(context, request))

def cricket(request):
    mychild = Child3.objects.all().values()
    template = loader.get_template("cricket.html")
    context = {
        'mychild' : mychild
    }
    return HttpResponse(template.render(context, request))

def add(request):
    template = loader.get_template("add.html")
    return HttpResponse(template.render({}, request))

def cricketadd(request):
    template = loader.get_template("cricketadd.html")
    return HttpResponse(template.render({}, request))

def addrecord(request):
    first = request.POST['first']
    last = request.POST['last']
    email = request.POST['email']
    child = Child(firstName = first,lastName =  last,email =  email)
    child.save()
    return HttpResponseRedirect(reverse('index'))

def cricketaddrecord(request):
    first = request.POST['first']
    last = request.POST['last']
    team = request.POST['team']
    role = request.POST['role']
    child = Child3(firstName = first,lastName =  last,cricketTeam =  team, role = role)
    child.save()
    return HttpResponseRedirect(reverse('cricket'))

def delete(request, id):
    mychild = Child.objects.get(id=id)
    mychild.delete()
    return HttpResponseRedirect(reverse('index'))

def cricketdelete(request, id):
    mychild = Child3.objects.get(id=id)
    mychild.delete()
    return HttpResponseRedirect(reverse('cricket'))

def update(request, id):
    mychild = Child2.objects.get(id=id)
    template = loader.get_template("update.html")
    context = {
        'mychild' : mychild
    }
    return HttpResponse(template.render(context, request))

def updaterecord(request, id):
    first = request.POST['first']
    last = request.POST['last']
    email = request.POST['email']
    mychild = Child.objects.get(id=id)
    mychild.firstName = first
    mychild.lastName = last
    mychild.email = email
    mychild.save()
    return HttpResponseRedirect(reverse('index'))

def cricketupdate(request, id):
    mychild = Child3.objects.get(id=id)
    template = loader.get_template("cricketupdate.html")
    context = {
        'mychild' : mychild
    }
    return HttpResponse(template.render(context, request))

def cricketupdaterecord(request, id):
    first = request.POST['first']
    last = request.POST['last']
    team = request.POST['team']
    role = request.POST['role']
    # print(team )
    mychild = Child3.objects.get(id=id)
    mychild.firstName = first
    mychild.lastName = last
    mychild.cricketTeam = team
    mychild.role = role
    mychild.save()
    return HttpResponseRedirect(reverse('cricket'))