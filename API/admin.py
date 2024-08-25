from django.contrib import admin

# Register your models here.
from .models import USUARIO, PLANTA, HONGO, DIAGNOSTICO, IMAGEN, TRATAMIENTO, HISTORIAL_TRATAMIENTO
admin.site.register(USUARIO)
admin.site.register(PLANTA)
admin.site.register(IMAGEN)
admin.site.register(HONGO)
admin.site.register(DIAGNOSTICO)
admin.site.register(TRATAMIENTO)
admin.site.register(HISTORIAL_TRATAMIENTO)