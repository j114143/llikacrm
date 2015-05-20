from django import forms
from models import Proyecto,Trabajador,Institucion,InformacionPracticas,ControlAsistencia,TareasEncargadas,Cargo
class ProyectoForm(forms.ModelForm):
	class Meta:
		model = Proyecto
		fields = ('nombre','descripcion')

class TrabajadorForm(forms.ModelForm):
	class Meta:
		model = Trabajador
		fields = ('nombres','apellidos','dni','fecha_nacimiento','direccion','telefono','celular','e_mail_personal','e_mail_llika','contacto','contacto_telefono',)
class InstitucionForm(forms.ModelForm):
    class Meta:
        model = Institucion
        fields = ('nombre',)

class PracticasForm(forms.ModelForm):
    class Meta:
        model = InformacionPracticas
        fields = ('institucion','fecha_inicio','estado','practicante',)

class AsistenciaForm(forms.ModelForm):
    class Meta:
        model = ControlAsistencia
        fields = ('trabajador','fecha','hora_llegada','hora_salida',)

class TareasForm(forms.ModelForm):
    class Meta:
        model = TareasEncargadas
        fields = ('proyecto','trabajadores','fecha_inicio','fecha_fin',)
class CargoForm(forms.ModelForm):
    class Meta:
        model = Cargo
        fields = ('nombre','trabajador','fecha_inicio',)