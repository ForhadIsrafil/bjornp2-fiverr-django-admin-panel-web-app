from django.urls import path
from . import views

app_name = "invoices"
urlpatterns = [
    path('get-updated-data', views.get_updated_data, name='get_updated_data'),
]
