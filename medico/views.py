from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .form import medicoForm, especializacaoForm
from medico.models import medico, especializacao
from django.contrib.auth.decorators import login_required

@login_required
def createMedico(request):

    form = medicoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('/medico/adicionar/')
    

    return render(request, 'criarMedico.html', {'form': form})

@login_required
def buscaMedico(request):
    nome = request.GET.get('search', None)

    if nome:
        medicos = medico.objects.filter(nome__contains=nome)
    else:
        medicos = medico.objects.all()

    dataBase = {
        'medicos': medicos
    }

    return render(request, 'buscarMedico.html', dataBase)

@login_required
def deletarMedic(request, pk):
    medico.objects.filter(id=pk).delete()

    return HttpResponseRedirect('/medico/buscar/')

@login_required
def editarMedi(request,pk):
    medic = medico.objects.get(id=pk)

    if request.method == "POST":
        form = medicoForm(request.POST, instance=medic)
        print('entroi')
        if form.is_valid():
            form.save()
            print('salvou')
            return redirect("/medico/buscar/")
    else:
        form = medicoForm(instance=medic)


    return render(request, 'editMedic.html', {'form':form})

    
