from django.urls import path
from . import views
from .views import ReportListView

urlpatterns = [
    path('', ReportListView.as_view(), name='report_list'),
]