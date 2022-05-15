from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from invoices.utils import get_ledger_accounts, get_customers, get_access_token, create_invoices
from .models import *
from django.contrib import messages
from . import get_invoices


def get_updated_data(request):
    invoice_res = get_invoices.get_or_add_invoices()
    return redirect('admin/invoices/invoice/')
    # return JsonResponse(data={"data": invoice_res}, status=200)


def create_invoice(request):
    if request.method == "POST":
        # print(dict(request.POST))
        status, data = create_invoices(dict(request.POST))
        messages.success(
            request, f"{data}",
        )
        return render(request, '../templates/create_invoice.html')
    return render(request, '../templates/create_invoice.html')


def get_ledger_acc(request):
    request_status, ledger_list = get_ledger_accounts()
    if request_status == 401:
        status_code, token, = get_access_token()
        get_ledger_accounts()
    return JsonResponse(data={"data": ledger_list}, safe=False, status=200)


def get_customer(request):
    request_status, ledger_list = get_customers()
    if request_status == 401:
        status_code, token, = get_access_token()
        get_customers()
    return JsonResponse(data={"data": ledger_list}, safe=False, status=200)

# description
# vat_percentage
# vat
# units
# number_of_units
# amount_per_unit_value
# amount_per_unit_currency
# ledger_account_id

"""
customer_id
invoice_date
net_amounts
send_method
introduction
payment_method


==============
description
vat_percentage
vat
units
number_of_units
amount_per_unit_value
amount_per_unit_currency
ledger_account_id
"""