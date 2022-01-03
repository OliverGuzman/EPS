from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password

class PacienteManager(BaseUserManager):
    def create_user(self, username, password = None):
        if not username:
            raise ValueError('Usuario no existe')
        user = self.model(username = username)
        user.set_password(password)
        user.save(using = self._db)
        return user

    def create_superuser(self, username, password):
        user= self.create_user(
            username = username,
            password = password,
        )
        user.is_admin = True
        user.save(using = self._db)
        return user

class Paciente(AbstractBaseUser, PermissionsMixin):
    idPaciente = models.BigAutoField(primary_key = True)
    pacNmDocumento = models.CharField('Número Documento', max_length = 11, unique = True)
    password = models.CharField('Contraseña', max_length = 128)
    pacNombres = models.CharField('Nombres Paciente', max_length = 45)
    pacApellidos = models.CharField('Apellidos Paciente', max_length=45)
    pacFechaNacimiento = models.DateField()
    pacTipoDocumento = models.CharField('Tipo Documento', max_length = 20)
    pacDireccion = models.CharField('Dirección', max_length = 60)
    pacTelefono = models.CharField('Número Teléfono', max_length = 11)
    pacEmail= models.EmailField('Email', max_length = 45)
    pacGenero = models.CharField('Género', max_length = 9)
    pacEstado = models.BooleanField()

    def save(self,**kwargs):
        some_salt='mMUj0dRIK6vgtdIYepkIxN'
        self.password = make_password(self.password, some_salt)
        super().save(**kwargs)
    
    objects= PacienteManager()
    USERNAME_FIELD = "pacNmDocumento"