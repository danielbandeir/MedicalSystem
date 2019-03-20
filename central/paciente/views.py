from django.shortcuts import render
from .forms import pacienteForm
from .models import paciente


def createPaciente(request):

    if request.method == 'POST':
        form = pacienteForm()

        if form.is_valid():
            form.save()

    return render(request, 'criarPaciente.html', {form : 'form'})
