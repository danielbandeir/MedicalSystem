from django.shortcuts import render
from .form import medicoForm
from .models import medico

def createMedico(request):

    form = medicoForm(request.POST or None)

    if form.is_valid():
        form.save()
    

    return render(request, 'criarMedico.html', {'form': form})
