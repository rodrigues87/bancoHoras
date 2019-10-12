
class CounterBase(object):
    title = None
    value = None
    style = None
    icon = None

    def get_title(self, request):
        return self.title
    
    def get_value(self, request):
        return self.value
    
    def get_style(self, request):
        return self.style if self.style else 'primary'
    
    def get_icon(self, request):
        return self.icon if self.icon else 'fa-tasks'


class ModelCounter(CounterBase):
    model = None

    def __init__(self):
        if not self.title:
            self.title = self.model._meta.verbose_name_plural

    def get_value(self, request):
        return self.model.objects.count()
