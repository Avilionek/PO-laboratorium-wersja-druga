from cgitb import html
from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from django.shortcuts import render
from .models import PC
from .models import HardDrive
from .models import Design
from .models import GraphicsCard

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic



def harddrive(request):
    harddrive_list = HardDrive.objects.all
    template = loader.get_template('Shop/harddrive.html')
    context = {
        'harddrive_list': harddrive_list,
    }
    return HttpResponse(template.render(context, request))

def pc(request):
    pc_list = PC.objects.all
    template = loader.get_template('Shop/pc.html')
    context = {
        'pc_list': pc_list,
    }
    return HttpResponse(template.render(context, request))

def design(request):
    design_list = Design.objects.all
    template = loader.get_template('Shop/design.html')
    context = {
        'design_list': design_list,
    }
    return HttpResponse(template.render(context, request))


def graphicscard(request):
    graphicscard_list = GraphicsCard.objects.all
    template = loader.get_template('Shop/graphicscard.html')
    context = {
        'design_list': graphicscard_list,
    }
    return HttpResponse(template.render(context, request))

