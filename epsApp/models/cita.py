from django.db import models
from .paciente import Paciente

class Cita(models.Model):
    idCita = models.AutoField(primary_key = True)
    citFecha = models.DateField()
    citHora = models.TimeField()
    citObservacion = models.CharField('Observación de la Cita', max_length = 256)
    citEspecialidad = models.CharField('Especialidad', max_length = 50)
    idPacientefk = models.ForeignKey(Paciente, related_name = 'cita', on_delete = models.CASCADE, null=True)
    citAsignada = models.BooleanField(default=False)
    