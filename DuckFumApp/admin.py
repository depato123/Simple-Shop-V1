from django.contrib import admin
from .models import MiModelo

@admin.register(MiModelo)
class MiModeloAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha_creacion')