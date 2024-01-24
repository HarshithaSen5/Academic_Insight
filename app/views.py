from django.shortcuts import render
from .models import StudentData
from slick_reporting.views import ReportView, Chart
from slick_reporting.fields import ComputationField
from django.db.models import Count
from .forms import CustomFilters

class StudView(ReportView):

    report_model = StudentData
    group_by = "collegename"
    report_title ='Results'
    form_class= CustomFilters

    columns = [
        "collegename",
        ComputationField.create(
            method=Count, field="result", name="result", verbose_name="Total result"
        ),
    ]

    # Charts
    chart_settings = [
        Chart(
            "Total result",
            Chart.BAR,
            data_source=["result"],
            title_source=["collegename"],
        ),
    ]