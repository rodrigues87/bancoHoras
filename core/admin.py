from django.contrib import admin
from .models import BancoHoras


class BancoHorasAdmin(admin.ModelAdmin):
  list_display = ['militar', 'horas_adicionadas', 'horas_usadas', 'descricao']

  search_fields = ['militar']

  list_filter = ('militar',)



admin.site.register(BancoHoras, BancoHorasAdmin)
