import requests
import json
from django.conf import settings
from .models import *


def get_customers():
    # todo: get access token
    loging_url = settings.LOGIN_URL
    login_res = requests.post(url=loging_url)

    if login_res.status_code == 200:
        login_data = login_res.json()
        access_token = login_data['access_token']

        # todo: get list of customers
        customer_url = settings.INVOICE_URL
        headers = {
            "Authorization": "Bearer " + access_token
        }
        customer_res = requests.get(url=customer_url, headers=headers)
        if customer_res.status_code == 200:
            customer_list = [c['id'] for c in customer_res.json()['data']]


def get_ledger_accounts():
    # todo: get access token
    loging_url = settings.LOGIN_URL
    login_res = requests.post(url=loging_url)

    if login_res.status_code == 200:
        login_data = login_res.json()
        access_token = login_data['access_token']

        # todo: get list of ledger accounts
        ledger_url = settings.LEDGER_ACCOUNT_URL
        headers = {
            "Authorization": "Bearer " + access_token
        }
        ledger_res = requests.get(url=ledger_url, headers=headers)
        if ledger_res.status_code == 200:
            ledger_list = [c['ledger_account_id'] for c in ledger_res.json()['data']]
            return ledger_list
        else:
            return []
