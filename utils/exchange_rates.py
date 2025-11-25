from typing import Literal
import requests
from .consts import SUPPORTED_CURRENCY_CODES, BASE_URL_EXCHANGE_RATES
from datetime import datetime, date
from .validators import _validate_currency_code,_validate_table, _validate_weekday,_validate_date_format,_validate_is_future
from .extractions import get_currency_rates

def get_latest_exchange_rate_data(table: Literal["A","B","C"]) -> list[dict] | None:
    """Funkcja generująca aktualnie obowiązująca tabela kursów

    Args:
        table (Literal[&quot;A&quot;,&quot;B&quot;,&quot;C&quot;]): tabela do wybrania: "A", "B" lub "C"; Tabela A kursów średnich walut obcych,
Tabela B kursów średnich walut obcych, Tabela C kursów kupna i sprzedaży walut obcych

    Returns:
        list[dict] | None: zwraca listę słowników dla każdej waluty
    """
    _validate_table(table, ['A','B','C'])
    base_url=f'{BASE_URL_EXCHANGE_RATES}/tables/{table}/'
    response = requests.get(base_url)
    if response.status_code == 200:
        data = response.json()
        return get_currency_rates(data)
    
    
def get_latest_exchanege_rate_single_curency(table: Literal['A','C'], 
                                             code: Literal[SUPPORTED_CURRENCY_CODES]) -> float | None:
    """Funkcja generująca aktualnie obowiązujący kurs dla wybranej walty

    Args:
        table (Literal[&#39;A&#39;,&#39;C&#39;]): tabela do wybrania: "A", "B" lub "C"; Tabela A kursów średnich walut obcych,
Tabela B kursów średnich walut obcych, Tabela C kursów kupna i sprzedaży walut obcych
        code (Literal[SUPPORTED_CURRENCY_CODES]): trzyliterowy kod waluty

    Returns:
        float | None: zwraca aktualnie obowiązujący kurs dla wybranej walty
    """
    _validate_currency_code(code)
    _validate_table(table,['A','C'])
    response = requests.get(f"{BASE_URL_EXCHANGE_RATES}/rates/{table}/{code}/")
    if response.status_code == 200:
        return response.json()
    

def get_exchange_rate_for_requested_day(table: Literal['A','C'],
                                       code: Literal[SUPPORTED_CURRENCY_CODES],
                                       date: str)-> dict | None:
    """Funkcja generująca kurs dla wybranej walty dla danego dnia
    Args:
        table (Literal[&#39;A&#39;,&#39;C&#39;]): tabela do wybrania: "A", "B" lub "C"; Tabela A kursów średnich walut obcych,
Tabela B kursów średnich walut obcych, Tabela C kursów kupna i sprzedaży walut obcych
        code (Literal[SUPPORTED_CURRENCY_CODES]): trzyliterowy kod waluty
        date (str): data w formacie RRRR-MM-DD (standard ISO 8601), dane dostępne tylko dla dni powszednich

    Returns:
        dict | None: zwraca kurs dla wybranej walty dla danego dnia
    """
    _validate_currency_code(code)
    _validate_table(table,['A','C'])
    date_dateformat = _validate_date_format(date)
    _validate_weekday(date_dateformat)

    response = requests.get(f"{BASE_URL_EXCHANGE_RATES}/rates/{table}/{code}/{date}/")
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
    """Funkcja generująca kurs dla wybranej walty dla wybranego przedziału czasowego

    Args:
        table (Literal[&#39;A&#39;,&#39;C&#39;]): tabela do wybrania: "A", lub "C"; Tabela A kursów średnich walut obcych,
        Tabela C kursów kupna i sprzedaży walut obcych
        code (Literal[SUPPORTED_CURRENCY_CODES]): trzyliterowy kod waluty
        start_date (str): data początkowa wybranego okresu w formacie RRRR-MM-DD (standard ISO 8601), dane dostępne tylko dla dni powszednich
        end_date (str): data końcowa wybranego okresu w formacie RRRR-MM-DD (standard ISO 8601), dane dostępne tylko dla dni powszednich

    Raises:
        Exception: wyjątki podnoszone,gdy parametry zapytania są niezgodne z wymaganym formatem lub, 
        gdy przedział czasowy jest nieprawdiłowo skonstrowany; dane dostępne tylko dla dni powszednich. 
        Start_date musi być wszcześniejszy niż end_date

    Returns:
        list[dict] | None: zwraca kursy dla wybranej walty dla wybranego przedziału czasowego
    """

    _validate_currency_code(code)
    _validate_table(table,['A','C'])
    start_date_dateformat, end_date_dateformat = _validate_date_format(start_date), _validate_date_format(end_date)
    if end_date_dateformat < start_date_dateformat:
        raise Exception(f'data końca przedziału {end_date} nie może być młodsza niż data poczatku przedziału ')
    
    _validate_weekday(start_date_dateformat,end_date_dateformat)
    end_date_dateformat =_validate_is_future(end_date_dateformat)
    
    end_date = datetime.strftime(end_date_dateformat,('%Y-%m-%d'))
    response = requests.get(f'{BASE_URL_EXCHANGE_RATES}/rates/{table}/{code}/{start_date}/{end_date}/')
    if response.status_code == 200:
        return response.json()
    else:
        print("Brak danych")

# 3. do pobrania całej tabeli walut z danego dnia

def get_exchange_rate_for_requested_day(table: Literal["A","B","C"],
                                        date_str: str) -> list[dict] | None:
    """Funkcja generująca kursy walutowe dla wybranego dnia w przeszłości

    Args:
        table (Literal[&quot;A&quot;,&quot;B&quot;,&quot;C&quot;]): tabela do wybrania: "A", lub "C"; Tabela A kursów średnich walut obcych,
        Tabela C kursów kupna i sprzedaży walut obcych
        date_str (str): data w formacie RRRR-MM-DD (standard ISO 8601), dane dostępne tylko dla dni powszednich

    Returns:
        list[dict] | None: zwraca kursy walutowe dla wybranego dnia w przeszłości
    """
    _validate_table(table, ['A','B','C'])
    url=f'{BASE_URL_EXCHANGE_RATES}/tables/{table}/{date_str}/'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return get_currency_rates(data)




# 4. do pobrania całej tabeli walut z przedziału od:do

# całość obsłużyć błędy (walidacja), obsłużyć daty przyszłe i weekendy


# do zakresów dodać wykresy
# pydantic - zobaczyć co to jest :)