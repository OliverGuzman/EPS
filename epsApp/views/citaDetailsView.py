from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated

from epsApp.models.cita import Cita
from epsApp.models.paciente import Paciente
from epsApp.serializers.citaSerializer import CitaSerializer

class CitasUserDetail(generics.ListAPIView):
    serializer_class = CitaSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        token = self.request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm = settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token, verify = False)
        
        if valid_data['user_id'] != self.kwargs['pk']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status = status.HTTP_401_UNAUTHORIZED)

        queryset = Cita.objects.filter(idPacientefk_id=self.kwargs['pk'])
        return queryset

class CitasAvailableView(generics.ListAPIView):
    serializer_class = CitaSerializer
    permission_classes = (IsAuthenticated,)
    
    def get_queryset(self):
        queryset= Cita.objects.all()
        token = self.request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm = settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token, verify = False)
        
        if valid_data['user_id'] != self.kwargs['pk']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status = status.HTTP_401_UNAUTHORIZED)  

        queryset2=[]
        for x in queryset:
            if x.citAsignada==False:
                queryset2.append(x)
        return queryset2

class CitaUpdateView(generics.UpdateAPIView):
    serializer_class = CitaSerializer
    permission_classes = (IsAuthenticated,)
    queryset= Cita.objects.all()
    
    def update(self, request, *args, **kwargs):
        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm = settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token, verify = False)
        
        if valid_data['user_id'] != kwargs['ac']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status = status.HTTP_401_UNAUTHORIZED) 

        return super().update(request, *args, **kwargs)