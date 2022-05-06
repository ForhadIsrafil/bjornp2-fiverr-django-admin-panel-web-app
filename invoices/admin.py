from django.contrib import admin
from .models import *
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from django.urls import reverse
from django.utils.http import urlencode


@admin.register(Invoice)
class InvoicesAdmin(admin.ModelAdmin):
    list_display = ["id", "invoice_number", "invoice_date", "invoice_date_sent", "number_of_units",
                    "amount_per_unit_value", "get_updated_data"]
    search_fields = ["id", "invoice_number", "invoice_date", "invoice_due_date", "invoice_delivery_period",
                     "invoice_date_sent", ]
    readonly_fields = ["invoice_id", "invoice_number", "ledger_account_id"]
    actions = []

    def get_updated_data(self, obj):
        url = "http://127.0.0.1:8000/get-updated-data"
        return format_html('<a href="{}" target="_blank">/get-updated-data</a> ', url)

    get_updated_data.short_description = "Use any link below if you need new data from the Invoice api link"
