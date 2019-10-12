import random

from django.contrib.auth.models import Group, User
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.apps import apps

from core.models import BancoHoras
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

def usuariosAtivos():
  cadastros = User.objects.count()

  return cadastros


def minhasHoras():
  soma = 0;

  registros = BancoHoras.objects.filter(militar=1)
  for registro in registros:
    soma = soma + registro.horas_adicionadas - registro.horas_usadas

  return soma




class ValiDashboardView(ValiDashboardBase):
    r = lambda: random.randint(0, 100)

    template_name = 'dashboard.html'
    # default count users data
    users = User.objects.count()

    soma = minhasHoras
    """
    # default charts data
    list_charts = [

        {
            # Support Chart types: PolarArea, Pie, Doughnut
            "name": "piechart1",
            "title": "Faltas",
            "chart_type": "Pie",
            "datasets": [

                {
                    "value": 300,
                    "color": '#%02X%02X%02X' % (r(), r(), r()),
                    "label": "Red"
                },
                {
                    "value": 50,
                    "color": '#%02X%02X%02X' % (r(), r(), r()),
                    "label": "Green"
                },
                {
                    "value": 100,
                    "color": '#%02X%02X%02X' % (r(), r(), r()),
                    "label": "Yellow"
                },
            ]
        },
        {
            # Support Chart types: Bar, Line, Radar
            "name": "vendas",
            "title": "Vendas Mensais",
            "chart_type": "Bar",
            "labels": ["2018-03-01", "2018-03-02", "2018-03-03", "2018-03-04", "2018-03-05"],
            "datasets": [
                {
                    "label": "dataset 1",
                    "fillColor": "rgba(220,220,220,0.2)",
                    "strokeColor": "rgba(220,220,220,1)",
                    "pointColor": "rgba(220,220,220,1)",
                    "pointStrokeColor": "#fff",
                    "pointHighlightFill": "#fff",
                    "pointHighlightStroke": "rgba(220,220,220,1)",
                    "data": [65, 59, 80, 81, 80]
                },
                {
                    "label": "dataset 2",
                    "fillColor": "rgba(151,187,205,0.2)",
                    "strokeColor": "rgba(151,187,205,1)",
                    "pointColor": "rgba(151,187,205,1)",
                    "pointStrokeColor": "#fff",
                    "pointHighlightFill": "#fff",
                    "pointHighlightStroke": "rgba(151,187,205,1)",
                    "data": [28, 48, 40, 19, 69]
                }
            ],
        },

    ]
    """
    # default icons data
    list_counters = [
        {"title": "ATIVOS", "value": users, "style": "primary", "icon": "fa-user-circle"},
        {"title": "HORAS", "value": soma, "style": "warning", "icon": "fa-users"},
    ]

