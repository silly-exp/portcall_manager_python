from django.shortcuts import get_object_or_404, render

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from .models import Call, Port, Ship
from .forms import CallForm, HomeForm


def index(request):
    # TODO: lister les ports gérés par l'outil
    # TODO: ajouter au modèle l'indication que le port est géré
    # TODO: masquer toutes les actions tant qu'aucun port n'a été sélectionné.
    if request.method == 'POST':
        form = HomeForm(request.POST)
        if form.is_valid():
            port = get_object_or_404(Port, locode=form.cleaned_data['locode'])
            request.session['port_id'] = port.id 
            return HttpResponseRedirect(reverse('callsmanager:index'))
    else:
        form = HomeForm()
    return render(request, 'callsmanager/index.html', {'form':form})

def call_list(request):
    template = loader.get_template('callsmanager/call_list.html')
    #FIXME: cette façon de faire la requete n'est certainement pas super.
    call_list = Call.objects
    if 'port_id' in request.session.keys():
        call_list = call_list.filter(port_id=request.session['port_id'])
    context = {
        'call_list': call_list.order_by('eta'),
    }
    return HttpResponse(template.render(context, request))

def call_details(request, call_id):
    call = get_object_or_404(Call, pk=call_id)
    return render(request, 'callsmanager/call_details.html', {'call':call})

def call_edit(request, call_id):
    if call_id==0:
        call = Call()
    else:
        call = get_object_or_404(Call, pk=call_id)

    if request.method == 'POST':
        form = CallForm(request.POST)
        if form.is_valid():
            
            call.save()
            return HttpResponseRedirect(reverse('callsmanager:call_details', args={call.id, }))

    else:
        form = CallForm()
    
    return render(request, 'callsmanager/call_form.html', {'call':call, 'form':form})
"""    
    mess = []
    
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

    port.callCount += 1
    call.port = port
    call.ship = ship
    call.num = f"{port.locode}{port.callCount:010d}"
    call.save()
    port.save()
    return HttpResponseRedirect(reverse('callsmanager:call_details', args=(call.id,)))
"""

"""
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
"""