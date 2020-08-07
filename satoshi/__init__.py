# -*- coding: utf-8 -*-

# - > satoshi -
# * Quan.digital *

# author: canokaue
# date: 01/02/2020
# kaue.cano@quan.digital

# Minimalistic implementation of a satoshi to fiat
# converter package. Simple yet useful.

import requests
import os

CRYPTOCOMPARE_ENDPOINT = "https://min-api.cryptocompare.com/data/price?fsym=%s&tsyms=%s"
COINDESK_ENDPOINT = 'http://api.coindesk.com/v2/bpi/currentprice.json'
# easily expandable...

BTC_FRACTION = float(10**-8) # A satoshi is one hundred millionth (0.00000001) of 1₿

def to_fiat(satoshis=1, fiat='USD'):
    '''Get BTC quote from cryptocompare.com then convert to
        satoshi in order to get fiat price.'''
    quote_url = CRYPTOCOMPARE_ENDPOINT % ('BTC',fiat.upper())
    response = requests.get(quote_url)
    btc_value = response.json().get(fiat.upper())
    fiat_value = float(satoshis * BTC_FRACTION) * float(btc_value)
    return '{:.2f}'.format(fiat_value)

def print_art():
    '''Read ASCII art from bitcoin_art.txt and print directly'''
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'bitcoin_art.txt'), 'r') as f:
        for line in f.read().split('\n'):print(line)