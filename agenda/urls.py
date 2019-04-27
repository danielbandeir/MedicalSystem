from django.urls import path
from .views import agendar, agendaDay, agend, deletarAgend, deletarAgendDia, editarAgend, editarAgendDia

urlpatterns = [
    path('agendar/', agendar, name='agendar'),
    path('dia/', agendaDay, name="AgendaDia"),
    path('ver/', agend, name="agendaTotal"),
    path('dia/editar/<int:pk>', editarAgendDia, name="editarAgendaDoDia"),
    path('dia/deletar/<int:pk>', deletarAgendDia, name="deletarAgendaDoDia"),
    path('ver/editar/<int:pk>', editarAgend, name="editarAgenda"),
    path('ver/deletar/<int:pk>', deletarAgend, name="deletarAgenda"),
]