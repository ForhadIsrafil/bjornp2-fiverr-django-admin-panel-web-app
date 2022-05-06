from django.db import models


class Invoice(models.Model):
    invoice_id = models.UUIDField(unique=True, null=True, blank=True)
    invoice_number = models.CharField(max_length=255, null=True, blank=True)
    invoice_date = models.DateField(null=True, blank=True)
    invoice_due_date = models.DateField(null=True, blank=True)
    invoice_delivery_period = models.DateField(null=True, blank=True)
    invoice_date_sent = models.DateField(null=True, blank=True)

    description = models.TextField(null=True, blank=True)
    vat_percentage = models.FloatField(null=True, blank=True)
    vat = models.PositiveIntegerField(null=True, blank=True)
    units = models.FloatField(null=True, blank=True)
    number_of_units = models.FloatField(null=True, blank=True)
    amount_per_unit_value = models.FloatField(null=True, blank=True)
    amount_per_unit_currency = models.CharField(max_length=4, null=True, blank=True)
    ledger_account_id = models.UUIDField(max_length=255, null=True, blank=True)
    payment_method = models.CharField(max_length=50, null=True, blank=True)
