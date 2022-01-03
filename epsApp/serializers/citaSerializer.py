from django.db.models import fields
from epsApp.models.cita import Cita
from rest_framework import serializers

from epsApp.models.paciente import Paciente

class CitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cita
        fields = ['citFecha', 'citHora', 'citObservacion', 'citEspecialidad','idPacientefk','citAsignada']
    
    def to_representation(self, obj):
        queryset=Paciente.objects.all()
        paciente=queryset[0]
        a = str(obj.idPacientefk)
        for x in queryset:
            b=str(x.pacNmDocumento)
            if b == a:
                paciente = x
                break
            
        cita = Cita.objects.get(idCita = obj.idCita)
        return{
                'idCita': cita.idCita,
                'citFecha': cita.citFecha,
                'citHora': cita.citHora,
                'citObservacion': cita.citObservacion,
                'citEspecialidad': cita.citEspecialidad,
                'idPacientefk':paciente.idPaciente,
                'citAsignada':cita.citAsignada,
        }