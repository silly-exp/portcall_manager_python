#from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader
from .models import Call


def index(request):
    return HttpResponse("Hello, world. You're at the Calls index.")

def call_list(request):
    template = loader.get_template('callsmanager/call_list.html')
    context = {
        'call_list': Call.objects.order_by('eta'),
    }
    return HttpResponse(template.render(context, request))

def call_details(request, call_id):
    call = Call.objects.get(id=call_id)
    output = f"""Détail de l'escale:<br/>
                 {call.num}<br/>
                 {call.port.name}<br/>
                 {call.ship.name}<br/>
                 {call.eta}"""
    return HttpResponse(output)

