from utils.consts import  SUPPORTED_CURRENCY_CODES

def filter_rates(data: dict) -> dict:
    data['rates'] = [line for line in data.get('rates') if line.get('code') in SUPPORTED_CURRENCY_CODES]
    return data