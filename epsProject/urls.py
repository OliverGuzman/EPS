"""epsProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from epsApp import views

urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('paciente/', views.PacienteCreateView.as_view()),
    path('paciente/<int:pk>/', views.PacienteDetailView.as_view()),
    path('cita/<int:pk>/', views.CitasUserDetail.as_view()),
    path('citasDisponible/<int:pk>/',views.CitasAvailableView.as_view()),
    path('agendarCita/<int:ac>/<int:pk>/',views.CitaUpdateView.as_view())

]