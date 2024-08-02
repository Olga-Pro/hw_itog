from django.shortcuts import render
from django.views.generic import ListView
from .models import Report


class ReportListView(ListView):
    model = Report
    template_name = 'analytics/report_list.html'