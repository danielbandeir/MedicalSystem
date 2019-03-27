from django.urls import path
from .views import createPaciente,buscarPaciente, deletarPacie, verFicha, editarPacie, addAtendimento

urlpatterns = [
    path('criar/', createPaciente, name='criarPaciente'),
    path('buscar/', buscarPaciente, name="buscarPaciente"),
    path('deletar/<int:pk>', deletarPacie, name="deletarPaciente"),
    path('ver/<int:pk>', verFicha, name="verPaciente"),
    path('editar/<int:pk>', editarPacie, name="editarPaciente"),
    path('adicionar/atendimento/<int:pk>', addAtendimento, name="adicionarAtendimento"),
]