from decimal import Decimal

import requests
import json
from django.conf import settings
from .models import *
from datetime import datetime


def get_customers():
    # todo: get access token
    # loging_url = settings.LOGIN_URL
    # login_res = requests.post(url=loging_url)
    #
    # if login_res.status_code == 200:
    #     login_data = login_res.json()
    #     access_token = login_data['access_token']

    # todo: get list of customers
    token_ins = AccessToken.objects.all().first()
    # if token_ins is not None:
    #     token = token_ins.token
    # else:
    customer_url = settings.CUSTOMER_URL
    headers = {
        "Authorization": "Bearer " + token_ins.token if token_ins is not None else ''
    }
    customer_res = requests.get(url=customer_url, headers=headers)
    if customer_res.status_code == 200:
        # customer_list = [c['id'] for c in customer_res.json()['data']]
        return customer_res.status_code, customer_res.json()['data']
    else:
        return customer_res.status_code, []


def get_ledger_accounts():
    # # todo: get access token
    # loging_url = settings.LOGIN_URL
    # login_res = requests.post(url=loging_url)
    #
    # if login_res.status_code == 200:
    #     login_data = login_res.json()
    #     access_token = login_data['access_token']

    # todo: get list of ledger accounts
    token_ins = AccessToken.objects.all().first()

    ledger_url = settings.LEDGER_ACCOUNT_URL
    headers = {
        "Authorization": "Bearer " + token_ins.token if token_ins is not None else ''
    }
    ledger_res = requests.get(url=ledger_url, headers=headers)
    if ledger_res.status_code == 200:
        # ledger_list = [c['ledger_account_id'] for c in ledger_res.json()['data']]
        return ledger_res.status_code, ledger_res.json()['data']
    else:
        return ledger_res.status_code, []


def get_access_token():
    # todo: get access token
    loging_url = settings.LOGIN_URL
    login_res = requests.post(url=loging_url)

    if login_res.status_code == 200:
        login_data = login_res.json()
        access_token = login_data['access_token']
        token_ins = AccessToken.objects.all().first()
        token_ins.token = access_token
        token_ins.save()
        return login_res.status_code, access_token

    # login_res may 401 Unauthorized
    else:
        return login_res.status_code, ''


def create_invoices(data):
    customer_id = data.get('customer_id')
    invoice_date = data.get('invoice_date')
    net_amounts = data.get('net_amounts')
    send_method = data.get('send_method')  # Possible values: email, self
    introduction = data.get('introduction')
    payment_method = data.get('payment_method')  # Possible values: pay_later, direct_debit, already_paid
    # print(payment_method, introduction, send_method, net_amounts, introduction, customer_id)
    # print(invoice_date[0])

    # todo: items data
    description = data.get('description')
    vat_percentage = data.get('vat_percentage')
    vat = data.get('vat')
    # units = data.get('units')
    number_of_units = data.get('number_of_units')
    amount_per_unit_value = data.get('amount_per_unit_value')
    amount_per_unit_currency = data.get('amount_per_unit_currency')
    ledger_account_id = data.get('ledger_account_id')
    # print(description, vat_percentage, vat, number_of_units, amount_per_unit_value, amount_per_unit_currency,
    #       ledger_account_id, )

    # line_items = []
    # for i in range(len(description)):
    #     temp = {
    #         "description": f"{description[i]}",
    #         "number_of_units": f"{number_of_units[i]}",
    #         "vat_percentage": f"{vat_percentage[i]}",
    #         "amount_per_unit": {
    #             "value": "{:.2f}".format(Decimal(amount_per_unit_value[i])),
    #             "currency": "EUR"
    #         },
    #         "ledger_account_id": f"{ledger_account_id[i]}"
    #     }
    #     line_items.append(temp)

    # body_data = {
    #     "customer_id": f"{customer_id[0]}",
    #     # "invoice_date": "",
    #     "net_amounts": False,  # net_amounts[0],
    #     "send_method": f"{send_method[0]}",
    #     "introduction": f"{introduction[0]}",
    #     "payment_method": f"{payment_method[0]}",
    #     # "line_items": line_items
    # }

    # todo: create invoices

    token_ins = AccessToken.objects.all().first()
    invoice_url = settings.INVOICE_URL
    headers = {
        "Authorization": "Bearer " + token_ins.token if token_ins is not None else '',
        "Content-Type": "application/json"
    }

    data = {
        "customer_id": f"{customer_id[0]}",
        "invoice_date": f"{invoice_date[0]}",
        # "net_amounts": f"",
        "send_method": f"{send_method[0]}",
        "introduction": f"{introduction[0]}",
        "payment_method": f"{payment_method[0]}",
        "line_items": [
            {
                "description": description[i],
                "number_of_units": number_of_units[i],
                "amount_per_unit": {
                    "value": amount_per_unit_value[i],
                    "currency": "EUR"
                },
                # "vat": vat[i],
                "vat_percentage": "21.0",  #
                "ledger_account_id": ledger_account_id[i]
            } for i in range(len(description))
        ],
        "sold_via_platform": "false"
    }
    print(json.loads(json.dumps(data, indent=4)))
    invoice_res = requests.post(url=invoice_url, data=json.dumps(data, indent=4), headers=headers)
    if invoice_res.status_code == 201:
        return invoice_res.status_code, invoice_res.json()
    else:
        return invoice_res.status_code, invoice_res.json()
