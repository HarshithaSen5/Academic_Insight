from slick_reporting.forms import BaseReportForm
from django import forms
from .models import StudentData
class CustomFilters(BaseReportForm, forms.Form):
    
    clgnamesqrset = StudentData.objects.values_list('collegename', flat=True).distinct().order_by('collegename')
    clgname_choices = [(collegename, collegename) for collegename in clgnamesqrset]
    collegename = forms.ChoiceField(choices=[('', 'All')] + clgname_choices, required=False,label="College Name",widget=forms.Select(attrs={'style': 'width: 300px;'}))

    resultsqrset=StudentData.objects.values_list('result',flat=True).distinct().order_by('result')
    result_choices = [(result, result) for result in resultsqrset]
    result = forms.ChoiceField(choices=[('', 'Select')] + result_choices, required=False,label="Result",widget=forms.Select(attrs={'style': 'width: 300px;'}))

    locqrset=StudentData.objects.values_list('loc',flat=True).distinct().order_by('loc')
    loc_choices = [(loc, loc) for loc in locqrset]
    loc = forms.ChoiceField(choices=[('', 'Select')] + loc_choices, required=False,label="Location",widget=forms.Select(attrs={'style': 'width: 300px;'}))

    def __init__(self, *args, **kwargs):
        super(CustomFilters, self).__init__(*args, **kwargs)

    def get_filters(self):
        filters = {}
        q_filters = []
        if self.cleaned_data["collegename"]:
            filters["collegename"] = self.cleaned_data["collegename"]
        if self.cleaned_data["result"]:
            filters["result"]=self.cleaned_data["result"]
        if self.cleaned_data["loc"]:
            filters["loc"]=self.cleaned_data["loc"]
        

        return q_filters, filters

    def get_start_date(self):
        pass

    def get_end_date(self):
        pass
        