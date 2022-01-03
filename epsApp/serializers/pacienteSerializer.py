from django.db.models import fields
from rest_framework import serializers
from epsApp.models.paciente import Paciente
from epsApp.models.cita import Cita
from epsApp.serializers.citaSerializer import CitaSerializer

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = ['idPaciente', 'pacNmDocumento', 'password', 'pacNombres', 'pacApellidos', 'pacFechaNacimiento', 
            'pacTipoDocumento', 'pacDireccion', 'pacTelefono', 'pacEmail', 'pacGenero', 'pacEstado']

    def create(self, validated_data):
        pacienteInstance = Paciente.objects.create(**validated_data)
        return pacienteInstance

    def to_representation(self, obj):
        paciente = Paciente.objects.get(idPaciente = obj.idPaciente)
        return{
                'idPaciente': paciente.idPaciente,
                'pacNmDocumento': paciente.pacNmDocumento,
                'pacNombres': paciente.pacNombres,
                'pacApellidos': paciente.pacApellidos,
                'pacFechaNacimiento': paciente.pacFechaNacimiento,
                'pacTipoDocumento': paciente.pacTipoDocumento,
                'pacDireccion': paciente.pacDireccion,
                'pacTelefono': paciente.pacTelefono,
                'pacEmail': paciente.pacEmail,
                'pacGenero': paciente.pacGenero,
                'pacEstado': paciente.pacEstado,
                
}