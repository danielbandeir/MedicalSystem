from django.shortcuts import render, redirect
from .forms import agendaForm
from .models import agenda
from datetime import date
from django.contrib.auth.decorators import login_required


@login_required
def agendar(request):
    form = agendaForm(request.POST or None)

    if form.is_valid():
        form.save()

    return render(request, "agendar.html", {'form':form})

@login_required
def agendaDay(request):
    nome = request.GET.get('search', None)

    if nome:
        agendaDia = agenda.objects.filter(nomePaciente__Nome__contains=nome, data=date.today())
    else:
        agendaDia = agenda.objects.filter(data=date.today())


    database={
        'agenda':agendaDia
    }

    return render(request, 'agendaDia.html', database)


@login_required
def agend(request):
    nome = request.GET.get('search', None)

    if nome:
        agendaTotal = agenda.objects.filter(nomePaciente__Nome__contains=nome)
    else:
        agendaTotal = agenda.objects.filter()


    database={
        'agenda':agendaTotal
    }

    return render(request, 'agenda.html', database)

@login_required
def deletarAgendDia(request, pk):
    agenda.objects.filter(id=pk).delete()

    return redirect('/agenda/dia/')

@login_required
def editarAgendDia(request,pk):
    agend = agenda.objects.get(id=pk)

    if request.method == "POST":
        form = agendaForm(request.POST, instance=agend)
        if form.is_valid():
            form.save()
            return redirect('/agenda/dia/')
    else:
        form = agendaForm(instance=agend)


    return render(request, 'editAgendaDia.html', {'form':form})


@login_required
def deletarAgend(request, pk):
    agenda.objects.filter(id=pk).delete()

    return redirect('/agenda/ver/')

@login_required
def editarAgend(request,pk):
    agend = agenda.objects.get(id=pk)
    
    type(agend.data)
        

    print(agend.data)

    if request.method == "POST":
        form = agendaForm(request.POST, instance=agend)
        if form.is_valid():
            form.save()
            return redirect('/agenda/ver/')
    else:
        form = agendaForm(instance=agend)


    return render(request, 'editarAgenda.html', {'form':form})


    
