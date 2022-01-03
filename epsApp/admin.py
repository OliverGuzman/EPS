from django.contrib import admin
from .models.paciente import Paciente
from .models.cita import Cita

admin.site.register(Paciente)
admin.site.register(Cita)

# Register your models here.
