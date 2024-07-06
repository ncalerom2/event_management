from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Evento, Inscripcion

admin.site.register(Evento)
admin.site.register(Inscripcion)
