from django.urls import path
from .views import createMedico, buscaMedico, deletarMedic, editarMedi

urlpatterns = [
    path('adicionar/', createMedico, name='criarMedico'),
    path('buscar/', buscaMedico, name='buscarMedico'),
    path('deletar/<int:pk>', deletarMedic, name="deletarMedico"),
    path('editar/<int:pk>', editarMedi, name="editarMedico"),
]