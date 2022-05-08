from django.contrib import admin
from .models import *
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from django.urls import reverse
from django.utils.http import urlencode

# from django.contrib.admin.sites import AdminSite
# AdminSite.index_template = '../templates/admin/index.html'

class LineItemAdmin(admin.StackedInline):
    model = LineItem
    readonly_fields = ["invoice_id", "ledger_account_id"]
    extra = 1


@admin.register(Invoice)
class InvoicesAdmin(admin.ModelAdmin):
    list_display = ["invoice_id", "invoice_number", "invoice_date", "invoice_date_sent", "get_updated_data"]
    search_fields = ["invoice_id", "invoice_number", "invoice_date", "invoice_due_date", "invoice_delivery_period",
                     "invoice_date_sent", ]
    readonly_fields = ["invoice_id", "invoice_number"]
    inlines = [LineItemAdmin]

    def get_updated_data(self, obj):
        url = "http://127.0.0.1:8000/get-updated-data"
        return format_html('<a href="{}" target="_blank">/get-updated-data</a> ', url)

    get_updated_data.short_description = "Use any link below if you need new data from the Invoice api link"
