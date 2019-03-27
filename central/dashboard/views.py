from django.shortcuts import render
from datetime import date
from django.http import HttpResponseRedirect
from medico.form import medicoForm, especializacaoForm
from medico.models import medico, especializacao
from paciente.models import paciente
from agenda.models import agenda
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    pacientes = paciente.objects.all()
    medicos = medico.objects.all()
    form = especializacaoForm(request.POST or None)
    especialidades = especializacao.objects.all()
    agendaHoje = agenda.objects.filter(data=date.today())

    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/dashboard/')

    database ={
        'form':form,
        'especialidades':especialidades,
        'numeroPacientes':pacientes.count(),
        'numeroMedicos':medicos.count(),
        'numeroAtendimentos':agendaHoje.count(),
    }
    return render(request, "dashboard.html", database)

@login_required
def delEspe(request, pk):
    especializacao.objects.get(id=pk).delete()

    return HttpResponseRedirect('/dashboard/')
