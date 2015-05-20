from django.db import models
class Institucion(models.Model):
    nombre = models.CharField(max_length=100)
    def __unicode__(self):
        return self.nombre
class Trabajador(models.Model):
    nombres = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    DNI = models.CharField(max_length=8)
    fecha_nacimiento = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30)
    telefono = models.CharField(max_length=30,blank=True)
    celular = models.CharField(max_length=30,blank=True)
    e_mail_personal = models.CharField(max_length=30,blank=True)
    e_mail_llika = models.CharField(max_length=30)
    contacto = models.CharField(max_length=30)
    contacto_telefono=models.CharField(max_length=30)
    def __unicode__(self):
        return self.nombres
    class Meta:
        verbose_name_plural = 'Personal de Llika'
class Cargo(models.Model):
    nombre = models.CharField(max_length=30)
    Trabajador=models.ForeignKey(Trabajador)
    fecha_inicio=models.DateField()
    def __unicode__(self):
        return self.nombre
    class Meta:
        verbose_name_plural = 'Cargo de Personal'
class Institucion(models.Model):
    nombre = models.CharField(max_length=100)
    def __unicode__(self):
        return self.nombre
class InformacionPracticas(models.Model):
    institucion = models.ForeignKey(Institucion)
    fecha_inicio = models.DateField()
    estado = models.BooleanField()
    practicante = models.OneToOneField(Trabajador)
class Proyecto(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=100)
    def __unicode__(self):
        return self.nombre
    class Meta:
        verbose_name_plural = 'Proyectos'
class ControlAsistencia(models.Model):
    trabajador = models.OneToOneField(Trabajador)
    fecha = models.DateField()
    hora_llegada = models.TimeField()
    hora_salida = models.TimeField()
    def __unicode__(self):
        return "Asistencia de "+str(self.trabajador)
    class Meta:
        verbose_name_plural = 'Control Asistencia'
class TareasEncargadas(models.Model):
    proyecto = models.ForeignKey(Proyecto)
    trabajadores = models.ForeignKey(Trabajador)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    def __unicode__(self):
        return self.proyecto.nombre
    class Meta:
        verbose_name_plural = 'Tareas Encargadas'
# empresas
# Clientes
# dominios
# Hosting