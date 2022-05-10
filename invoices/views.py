from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import *
import requests
from . import get_invoices


def get_updated_data(request):
    invoice_res = get_invoices.get_or_add_invoices()
    return JsonResponse(data={"data": invoice_res}, status=200)

def create_invoice(request):
    print(request.POST.__dict__)
    return render(request, '../templates/create_invoice.html')



# description
# vat_percentage
# vat
# units
# number_of_units
# amount_per_unit_value
# amount_per_unit_currency
# ledger_account_id