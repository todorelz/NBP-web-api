from typing import Literal
import requests
from .consts import SUPPORTED_CURRENCY_CODES
from datetime import datetime, date
from .validators import _validate_currency_code,_validate_table, _validate_weekday,_validate_date_format,_validate_is_future

def get_latest_exchange_rate_data(table: Literal["A","B","C"]) -> list[dict] | None:
    _validate_table(table, ['A','B','C'])
    base_url=f'https://api.nbp.pl/api/exchangerates/tables/{table}/'
    response = requests.get(base_url)
    if response.status_code == 200:
        data = response.json()
        return data[-1].get('rates')
    
    
def get_latest_exchanege_rate_single_curency(table: Literal['A','C'], 
                                             code: Literal[SUPPORTED_CURRENCY_CODES]) -> float | None:
    _validate_currency_code(code)
    _validate_table(table,['A','C'])
    response = requests.get(f"https://api.nbp.pl/api/exchangerates/rates/{table}/{code}/")
    if response.status_code == 200:
        return response.json()
    

def get_exchange_rate_for_requested_day(table: Literal['A','C'],
                                       code: Literal[SUPPORTED_CURRENCY_CODES],
                                       date: str)-> dict | None:
    """Funkcja pobierająca ....

    Args:
        table (Literal[&#39;A&#39;,&#39;C&#39;]): podać nazwę ściąganej tabeli
        code (Literal[SUPPORTED_CURRENCY_CODES]): _description_
        date (str): _description_

    Returns:
        dict | None: _description_
    """
    _validate_currency_code(code)
    _validate_table(table,['A','C'])
    date_dateformat = _validate_date_format(date)
    _validate_weekday(date_dateformat)

    response = requests.get(f"https://api.nbp.pl/api/exchangerates/rates/{table}/{code}/{date}/")
    if response.status_code == 200:
        return response.json()
    else:
        print('Brak danych')

#     napisz funkcje:

# 2. do pobrania pojedyńczej waluty z przedziału od:do
def get_exchange_rate_for_requested_days_period(table: Literal['A','C'],
                                       code: Literal[SUPPORTED_CURRENCY_CODES],
                                       start_date: str,
                                       end_date: str)-> list[dict] | None:
    """_summary_

    Args:
        table (Literal[&#39;A&#39;,&#39;C&#39;]): _description_
        code (Literal[SUPPORTED_CURRENCY_CODES]): _description_
        start_date (str): _description_
        end_date (str): _description_

    Raises:
        Exception: _description_

    Returns:
        list[dict] | None: _description_
    """

    _validate_currency_code(code)
    _validate_table(table,['A','C'])
    start_date_dateformat, end_date_dateformat = _validate_date_format(start_date), _validate_date_format(end_date)
    if end_date_dateformat < start_date_dateformat:
        raise Exception(f'data końca przedziału {end_date} nie może być młodsza niż data poczatku przedziału ')
    
    _validate_weekday(start_date_dateformat,end_date_dateformat)
    end_date_dateformat =_validate_is_future(end_date_dateformat)
    
    end_date = datetime.strftime(end_date_dateformat,('%Y-%m-%d'))
    response = requests.get(f'https://api.nbp.pl/api/exchangerates/rates/{table}/{code}/{start_date}/{end_date}/')
    if response.status_code == 200:
        return response.json()
    else:
        print("Brak danych")

# 3. do pobrania całej tabeli walut z danego dnia

# 4. do pobrania całej tabeli walut z przedziału od:do

# całość obsłużyć błędy (walidacja), obsłużyć daty przyszłe i weekendy

# wrócić do zadania z zapisywaniem do plików
# do kazdej funkcji dodać dokstring (""" po enterze za końcu funkcji po ":")
# do zakresów dodać wykresy