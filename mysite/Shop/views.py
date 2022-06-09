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
from Shop.forms import pcForm




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
        'graphicscard_list': graphicscard_list,
    }
    return HttpResponse(template.render(context, request))

def pcform(request):
    form = pcForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'form':form
    }
    return render(request, 'Shop/forms.html', context)

