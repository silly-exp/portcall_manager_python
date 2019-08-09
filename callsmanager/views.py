from django.shortcuts import get_object_or_404, render

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Call, Port, Ship
from django.urls import reverse


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

def call_edit(request, call_id):
    if call_id==0:
        call = Call()
    else:
        call = get_object_or_404(Call, pk=call_id)
    return render(request, 'callsmanager/call_form.html', {'call':call})

def call_create(request):
    mess = []
    call = Call()
    params = request.POST
    #call_control(request.POST)
    if 'locode' not in params or params['locode'] == '':
        mess.append("Pas de LOCODE saisi.")
    else:
        try:
            port = Port.objects.get(locode=params['locode'])
        except Port.DoesNotExist:
            mess.append(f"Pas de port en base pour le locode {params['locode']}")
    
    if 'imo' not in params or params['imo'] == '':
        mess.append("Pas de numéro OMI saisi.")
    else:
        try:
            imo = int(params['imo'])
        except ValueError:
            mess.append(f"Le numéro OMI n'est pas numérique")
        else:
            try:
                ship = Ship.objects.get(imo=imo)
            except Ship.DoesNotExist:
                mess.append(f"Pas de navire en base pour l'OMI {params['imo']}")

    if len(mess) != 0:
        return render(request, 'callsmanager/call_form.html', {'call':call,'error_messages':mess})

    call.port = port
    call.ship = ship
    call.save()
    return HttpResponseRedirect(reverse('callsmanager:call_details', args=(call.id,)))

def call_update(request, call_id):
    mess = []
    call = get_object_or_404(Call, pk=call_id)
    params = request.POST
    #call_control(request.POST)
    if 'locode' not in params or params['locode'] == '':
        mess.append("Pas de LOCODE saisi.")
    else:
        try:
            port = Port.objects.get(locode=params['locode'])
        except Port.DoesNotExist:
            mess.append(f"Pas de port en base pour le locode {params['locode']}")
    
    if 'imo' not in params or params['imo'] == '':
        mess.append("Pas de numéro OMI saisi.")
    else:
        try:
            imo = int(params['imo'])
        except ValueError:
            mess.append(f"Le numéro OMI n'est pas numérique")
        else:
            try:
                ship = Ship.objects.get(imo=imo)
            except Ship.DoesNotExist:
                mess.append(f"Pas de navire en base pour l'OMI {params['imo']}")

    if len(mess) != 0:
        return render(request, 'callsmanager/call_form.html', {'call':call,'error_messages':mess})

    call.port = port
    call.ship = ship
    call.save()
    return HttpResponseRedirect(reverse('callsmanager:call_details', args=(call.id,)))
    