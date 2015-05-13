from django.contrib import admin
from .models import Trabajador, Proyecto, ControlAsistencia, TareasEncargadas,Institucion, InformacionPracticas
class TrabajadorAdmin(admin.ModelAdmin):
    list_display = ('nombres','apellidos','telefono','correo',)
class ProyectoAdmin(admin.ModelAdmin):
    list_display = ('nombre','descripcion',)
    search_fields  = ('nombre',)
class ControlAdmin(admin.ModelAdmin):
    list_display=('trabajador','fecha','hora_llegada','hora_salida',)
class TareasAdmin(admin.ModelAdmin):
    list_display=('proyecto','trabajadores','fecha_inicio',
'fecha_fin',)
# Register your models here.
admin.site.register(Trabajador,TrabajadorAdmin)
admin.site.register(Proyecto,ProyectoAdmin)
admin.site.register(ControlAsistencia,ControlAdmin)
admin.site.register(TareasEncargadas,TareasAdmin)
admin.site.register(Institucion)
admin.site.register(InformacionPracticas)