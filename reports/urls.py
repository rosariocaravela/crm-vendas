from django.urls import path
from . import views

app_name = 'reports'

urlpatterns = [
    path('', views.index, name='index'),
    path('export/clients/excel/', views.export_clients_excel, name='export_clients_excel'),
    path('export/deals/excel/', views.export_deals_excel, name='export_deals_excel'),
    path('export/pdf/', views.export_report_pdf, name='export_report_pdf'),
]
