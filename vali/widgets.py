from django.contrib.admin.widgets import RelatedFieldWidgetWrapper, FilteredSelectMultiple
from django.forms.widgets import CheckboxSelectMultiple
from django import forms


class ValiDashboardWidget(forms.Widget):
    def render(self, name, value, attrs=None, renderer=None):
        #TODO
        return 'render'


class ValiDateWidget(forms.Widget):
    def render(self, name, value, attrs=None, renderer=None):
        #TODO
        return 'dateinput'


class ValiDateTimeWidget(forms.Widget):
    def render(self, name, value, attrs=None, renderer=None):
        #TODO
        return 'datetimeinput'


# fork FilteredSelectMultiple
class ValiFilteredSelectMultiple(FilteredSelectMultiple):
    """ customize FilteredSelectMultiple, not used for now """

    def get_context(self, name, value, attrs):
        context = super(ValiFilteredSelectMultiple, self).get_context(name, value, attrs)
        context['widget']['attrs']['class'] = 'selectfilter'
        if self.is_stacked:
            context['widget']['attrs']['class'] += 'stacked'
        context['widget']['attrs']['data-field-name'] = self.verbose_name
        context['widget']['attrs']['data-is-stacked'] = int(self.is_stacked)
        return context


class ValiCheckboxSelectMultiple(CheckboxSelectMultiple):
    def get_context(self, name, value, attrs):
        context = super(ValiCheckboxSelectMultiple, self).get_context(name, value, attrs)
        context['widget']['attrs']['class'] = 'vali-multicheckbox list-group'
        return context


class ValiRelatedFieldWidgetWrapper(RelatedFieldWidgetWrapper):
    """ customize ValiRelatedFieldWidgetWrapper, display auth.user.permissions in multiple checkbox """

    def __init__(self, *args, **kwargs):
        super(ValiRelatedFieldWidgetWrapper, self).__init__(*args, **kwargs)
        self.widget = ValiCheckboxSelectMultiple(attrs=self.widget.attrs, choices=self.widget.choices)
