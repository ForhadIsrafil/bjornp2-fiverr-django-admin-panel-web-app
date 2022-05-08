from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import *
import requests
from . import get_invoices


def get_updated_data(request):
    invoice_res = get_invoices.get_or_add_invoices()
    return JsonResponse(data={"data": invoice_res}, status=200)

def create_invoice(request):
    return render(request, '../templates/create_invoice.html')