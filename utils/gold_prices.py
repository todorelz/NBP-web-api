from utils.schemas import GoldPrices
from utils.validators import _validate_date_format, _validate_weekday, _validate_is_future, _validate_top_count
from .consts import BASE_URL_GOLD_PRICES
import requests

def get_gold_price_latest() -> list[dict]:
    response = requests.get(BASE_URL_GOLD_PRICES)
    gold_price_latest = response.json()
    if response.status_code == 200:
        return GoldPrices(gold_price_latest)
    else:
        print("Brak danych")


def get_gold_price_TopCount(top_count: int) -> list[dict]:
    """Funkcja generująca ceny złota dla ostatnich notowań
    Args:
        top_count (int): ilość wybranych ostatnich notowań 
    Returns:
        list[dict]: zwraca listę słowników data, cena dla ostatnich notowań
    """
    _validate_top_count(top_count)
    response = requests.get(f'{BASE_URL_GOLD_PRICES}/last/{top_count}')
    
    if response.status_code != 200:
        return None
    return GoldPrices(response.json())

# Cena złota opublikowana w dniu {date} (albo brak danych)  
def get_gold_price_for_requested_day(date: str) -> list[dict]:
    """Funkcja generująca ceny złota dla wybranej daty
    Args:
        data (str): data w formacie YYYY-MM-DD 
    Returns:
        list[dict]: zwraca listę słowników data, cena dla wybranego dnia
    """
    date_dateformat =_validate_date_format(date)
    _validate_weekday(date_dateformat)
    _validate_is_future(date_dateformat)
    response = requests.get(f'{BASE_URL_GOLD_PRICES}/{date}')
    
    if response.status_code != 200:
        return None
    return GoldPrices(response.json())

# Seria cen złota opublikowanych w zakresie dat od  do  
def get_gold_price_for_requested_days_period(start_date: str, end_date: str) -> list[dict]:
    """Funkcja generująca ceny złota dla wybranego zakresu dat od:do    
    Args:
        start_date (str): data od w formacie YYYY-MM-DD 
        end_date (str): data do w formacie YYYY-MM-DD 
    Returns:
        list[dict]: zwraca listę słowników data, cena dla wybranego przedziału czasowego
    """
    start_date_dateformat, end_date_dateformat  =_validate_date_format(start_date),_validate_date_format(end_date)
    if end_date_dateformat < start_date_dateformat:
        raise Exception(f'data końca przedziału  {end_date} nie może być młodsza niż data poczatku przedziału {start_date}')
    _validate_weekday(start_date_dateformat, end_date_dateformat)
    _validate_is_future(end_date_dateformat)
    response = requests.get(f'{BASE_URL_GOLD_PRICES}/{start_date}/{end_date}')
    
    if response.status_code != 200:
        return None
    return GoldPrices(response.json())