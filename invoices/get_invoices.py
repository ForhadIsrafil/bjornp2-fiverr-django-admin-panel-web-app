import requests
import json
from django.conf import settings

from .models import *


def get_or_add_invoices():
    # # todo: get access token
    # loging_url = settings.LOGIN_URL
    # login_res = requests.post(url=loging_url)
    #
    # if login_res.status_code == 200:
    #     login_data = login_res.json()
    #     access_token = login_data['access_token']
    #     # print(access_token)
    token_ins = AccessToken.objects.all().first()
    # todo: get list of invoices
    invoice_url = settings.INVOICE_URL
    headers = {
        "Authorization": "Bearer " + token_ins.token if token_ins is not None else ''
    }
    invoice_res = requests.get(url=invoice_url, headers=headers)
    if invoice_res.status_code == 200:
        for invoice in invoice_res.json()['data']:
            invoice_id = invoice['id']
            invoice_number = invoice['invoice_number']
            invoice_date = invoice['invoice_date']
            invoice_due_date = invoice['invoice_due_date']
            invoice_delivery_period = invoice['invoice_delivery_period']
            invoice_date_sent = invoice['invoice_date_sent']

            payment_method = invoice['payment_method']

            # todo: line_items start
            line_items = invoice.get('line_items')
            # print("line item: ", line_items.__len__())
            if line_items.__len__() != 0:
                # send data to the model for save them
                if Invoice.objects.filter(invoice_id=invoice_id).exists():
                    pass
                else:
                    invoice_ins = Invoice(invoice_id=invoice_id, invoice_number=invoice_number,
                                          invoice_date=invoice_date, invoice_due_date=invoice_due_date,
                                          invoice_delivery_period=invoice_delivery_period,
                                          invoice_date_sent=invoice_date_sent, payment_method=payment_method)
                    invoice_ins.save()

                    for item in line_items:
                        description = line_items[0]['description']
                        vat_percentage = line_items[0]['vat_percentage']
                        vat = line_items[0]['vat']
                        units = line_items[0]['units']
                        number_of_units = line_items[0]['number_of_units']

                        amount_per_unit_value = line_items[0]['amount_per_unit']['value']
                        amount_per_unit_currency = line_items[0]['amount_per_unit']['currency']

                        ledger_account_id = line_items[0]['ledger_account_id']
                        line_item_ins = LineItem(invoice=invoice_ins, description=description,
                                                 vat_percentage=vat_percentage, vat=vat, units=units,
                                                 number_of_units=number_of_units,
                                                 amount_per_unit_value=amount_per_unit_value,
                                                 amount_per_unit_currency=amount_per_unit_currency,
                                                 ledger_account_id=ledger_account_id, )
                        line_item_ins.save()


            # todo: line_items start end
            else:
                if Invoice.objects.filter(invoice_id=invoice_id).exists():
                    pass
                else:
                    invoice_ins = Invoice(invoice_id=invoice_id, invoice_number=invoice_number,
                                          invoice_date=invoice_date, invoice_due_date=invoice_due_date,
                                          invoice_delivery_period=invoice_delivery_period,
                                          invoice_date_sent=invoice_date_sent, payment_method=payment_method)
                    invoice_ins.save()

        return True, invoice_res.status_code, "Reload Your Invoice Admin Panel Now."
    else:
        return False, invoice_res.status_code
