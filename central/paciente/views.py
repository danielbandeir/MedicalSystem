from django.shortcuts import render
from .forms import pacienteForm
from .models import paciente


def createPaciente(request):
        
    form = pacienteForm(request.POST or None)

    if form.is_valid():
        form.save()

    return render(request, 'criarPaciente.html', {'form' : form})
