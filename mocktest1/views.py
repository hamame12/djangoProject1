from django.shortcuts import render
from django.shortcuts import HttpResponse, HttpResponseRedirect
from mocktest1.models import *


# Create your views here.

def get_project_list(request):
    aaa = DB_project.objects.filter().all()
    return render(request, 'project_list.html', {"projects": aaa})


def welcome(request):
    return render(request, 'welcome.html')


def del_project(request, pid):
    DB_project.objects.filter(id=pid).delete()
    return HttpResponseRedirect('/project_list/')


def copy_project(request, pid):
    project = DB_project.objects.filter(id=pid).values()
    DB_project.objects.create(name=project.values()[0]['name'], creater=project.values()[0]['creater']).save()
    return HttpResponseRedirect('/project_list/')
1231123