import requests
import json
from django.conf import settings
from .models import *


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
        token_ins, created = AccessToken.objects.get_or_create(token=access_token)
        if created == False:
            token_ins.token = access_token
            token_ins.save()
        return login_res.status_code, access_token

    # login_res may 401 Unauthorized
    else:
        return login_res.status_code, ''
