
class ChartsBase(object):
    chart_type = None
    name = None
    title = None
    labels = None
    datasets = None

    def get_chart_type(self, request):
        return self.chart_type

    def get_name(self, request):
        return self.name

    def get_title(self, request):
        return self.title

    def get_labels(self, request):
        return self.labels

    def get_datasets(self, request):
        return self.datasets


class ModelCharts(ChartsBase):
    model = None

    def __init__(self):
        if not self.title:
            self.title = self.model._meta.verbose_name + 'Data'

        if not self.chart_type:
            self.chart_type = 'Bar'

        if not self.name:
            self.name = self.chart_type + 'chart'
