from .consts import SUPPORTED_CURRENCY_CODES
from typing import Literal
from datetime import date, timedelta, datetime

def _validate_currency_code(code: str) -> None: #_nazwa funkcji - meta funkcja wywoływana tylko przez inną funkcję, nie przez użytkownika bezpośrednio
        if code.upper() not in SUPPORTED_CURRENCY_CODES:
            raise Exception(f'{code} - nieobsługiwana waluta')


def _validate_table(table: Literal['A','C'], allowed_table: list[str]) -> None:
      if table.upper() not in allowed_table:
            raise Exception(f'{table} - nieobsługiwana tabela')
      
def _validate_weekday(*dates: date) -> None:
    for date in dates:
        if date.weekday() in (5,6):
            raise Exception(f'{date} - weekendy nie posiadają kursów')
    
def _validate_date_format(*dates: date) -> date | None: 
    for date in dates:
        try:
            return datetime.strptime(date, "%Y-%m-%d")
        except Exception:
            print(f'{date}- data złego formatu')

def _validate_is_future (date: date) -> date | None:
     if datetime.today() > date:
          return date
     else:
          return datetime.today()

     
def _validate_is_future2 (input_date: str) -> date | None:
     today = datetime.today()
     print(type(input_date),input_date > today)
     if input_date > today:
          input_date
          return today - timedelta(days=1)
     print(input_date)
     return input_date

def _validate_top_count(top_count: int) -> None: 
    if not isinstance(top_count, int):
        raise TypeError("top_count musi być liczbą całkowitą")
    if top_count <= 0:
        raise ValueError("top_count musi być większe od 0")
