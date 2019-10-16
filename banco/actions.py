def reprova_horas(modeladmin, request, queryset):
    if request.user.is_superuser:
        queryset.update(aprovado=False)


def aprova_horas(modeladmin, request, queryset):
    if request.user.is_superuser:
        queryset.update(aprovado=True)


reprova_horas.short_description = 'Reprovar horas'
aprova_horas.short_description = 'Aprovar horas'
