from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

from banco.actions import aprova_horas, reprova_horas
from .models import BancoHoras


class FilterUserAdmin(admin.ModelAdmin):
    list_display = ['militar', 'horas_adicionadas', 'horas_usadas', 'descricao', 'aprovado']

    search_fields = ['militar']

    list_filter = ('militar', 'descricao',)

    actions = [reprova_horas, aprova_horas]

    #Determina quais itens serão mostrados na lista
    def get_list_display(self, request):
        if request.user.is_superuser or request.user.groups.filter(name = "supervisor").exists():
            return ['militar', 'horas_adicionadas', 'horas_usadas', 'descricao', 'aprovado']
        else:
            return ['horas_adicionadas', 'horas_usadas', 'descricao', 'aprovado']

    #filtra os resultados do atributo do modelo
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if not request.user.is_superuser or request.user.groups.filter(name = "supervisor").exists():
            if db_field.name == "militar":
                kwargs["queryset"] = User.objects.filter(username=request.user)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    #adidiona um valor default para o atributo
    def get_form(self, request, obj=None, **kwargs):
            form = super(FilterUserAdmin, self).get_form(request, obj, **kwargs)
            #
            if not request.user.is_superuser or request.user.groups.filter(name = "supervisor").exists():
                form.base_fields['militar'].initial = request.user
            return form

    #determina o que será feito ao salvar o objeto
    def save_model(self, request, obj, form, change):
        if obj.aprovado:
            print("entrou")
        if not request.user.is_superuser or request.user.groups.filter(name = "supervisor").exists():
            obj.user = request.user
            obj.save()
        else:
            obj.save()

    def get_queryset(self, request):
        # For Django < 1.6, override queryset instead of get_queryset
        qs = super(FilterUserAdmin, self).get_queryset(request)
        if request.user.is_superuser or request.user.groups.filter(name = "supervisor").exists():
            return qs
        return qs.filter(militar_id=request.user)

    def has_change_permission(self, request, obj=None):
        if not obj:
            # the changelist itself
            return True
        return obj

    def changelist_view(self, request, extra_context=None):
        if not request.user.is_superuser or request.user.groups.filter(name = "supervisor").exists():
            self.list_display = ('horas_adicionadas', 'horas_usadas', 'descricao','aprovado',)
        return super(FilterUserAdmin, self).changelist_view(request, extra_context)

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_staff or request.user.groups.filter(name = "supervisor").exists():
            if request.user.is_superuser:
                return []
            else:
                return ['aprovado']
            # f.name for f in self.model._meta.fields


class MyModelAdmin(FilterUserAdmin):
    pass  # (replace this with anything else you need)


admin.site.register(BancoHoras, MyModelAdmin)
