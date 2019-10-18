import random

from django.contrib.auth.models import Group, User
from django.db.models import Q
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.apps import apps

from banco.models import BancoHoras
from cadastro.models import Cadastro
from .counters import CounterBase
from .charts import ChartsBase


class ValiDashboardBase(TemplateView):
    extra_context_data = []
    list_counters = []
    list_charts = []

    def get_list_counters(self):
        list_counters = []
        for counter in self.list_counters:
            if isinstance(counter, CounterBase):
                list_counters.append(
                    {
                        'title': counter.get_title(self.request),
                        'value': counter.get_value(self.request),
                        'style': counter.get_style(self.request),
                        'icon': counter.get_icon(self.request),
                    }
                )
            else:
                list_counters.append(counter)
        return list_counters

    def get_list_charts(self):
        list_charts = []
        for chart in self.list_charts:
            if isinstance(chart, ChartsBase):
                list_charts.append(
                    {
                        'title': chart.get_title(self.request),
                        'name': chart.get_name(self.request),
                        'chart_type': chart.get_chart_type(self.request),
                        'labels': chart.get_labels(self.request),
                        'datasets': chart.get_datasets(self.request),
                    }
                )
            else:
                list_charts.append(chart)
        return list_charts

    def get_extra_context_data(self):
        return self.extra_context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['counters'] = self.get_list_counters()
        context['charts'] = self.get_list_charts()
        return context

    def get_template_names(self):
        return super().get_template_names()

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(ValiDashboardBase, self).dispatch(request, *args, **kwargs)


def verificarHoras(cadastro):
    somaHorasUsuario = 0
    registros = BancoHoras.objects.filter(militar=cadastro)
    for registro in registros:
        somaHorasUsuario = somaHorasUsuario + registro.horas_adicionadas - registro.horas_usadas
    return somaHorasUsuario


class ValiDashboardView(ValiDashboardBase):
    r = lambda: random.randint(0, 100)

    template_name = 'dashboard.html'

    # default count users data

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        list_horasUsuario = []
        usuarios = []

        users = User.objects.all()

        cadastros = Cadastro.objects.filter(user=self.request.user)

        somaHorasUsuario = 0

        for cadastro in cadastros:
            somaHorasUsuario = verificarHoras(cadastro)

        for user in users:
            cadastros = Cadastro.objects.filter(user=user)
            for cadastro in cadastros:
                horasUsuario = verificarHoras(cadastro)
                usuarios.append(user.username)
                list_horasUsuario.append(horasUsuario)

        list_charts = [

            {
                # Support Chart types: Bar, Line, Radar
                "name": "vendas",
                "title": "Banco de horas",
                "chart_type": "Bar",
                "labels": usuarios,
                "datasets": [
                    {
                        "label": "dataset 2",
                        "fillColor": "rgba(151,187,205,0.2)",
                        "strokeColor": "rgba(151,187,205,1)",
                        "pointColor": "rgba(151,187,205,1)",
                        "pointStrokeColor": "#fff",
                        "pointHighlightFill": "#fff",
                        "pointHighlightStroke": "rgba(151,187,205,1)",
                        "data": list_horasUsuario
                    }
                ],
            },

        ]

        list_counters = [
            # {"title": "ATIVOS", "value": users, "style": "primary", "icon": "fa-user-circle"},
            {"title": "MINHAS HORAS", "value": somaHorasUsuario, "style": "danger", "icon": "fa-user-circle"},
        ]

        context['minhas_Horas'] = somaHorasUsuario
        context['counters'] = list_counters
        context['charts'] = list_charts

        return context
