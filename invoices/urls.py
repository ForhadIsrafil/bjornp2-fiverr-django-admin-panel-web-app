from django.urls import path
from . import views

app_name = "invoices"
urlpatterns = [
    path('get-updated-data', views.get_updated_data, name='get_updated_data'),
    path('admin/create-invoice', views.create_invoice, name='create_invoice'),
    path('get-ledger', views.get_ledger_acc, name='get_ledger_acc'),
    path('get-customers', views.get_customer, name='get_customer'),
]
