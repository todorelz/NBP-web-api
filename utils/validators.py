from .consts import SUPPORTED_CURRENCY_CODES
from typing import Literal
from datetime import date, datetime

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
    
def _validate_date_format(date_str: str) -> date | None: 
    try:
        return datetime.strptime(date_str, "%Y-%m-%d")
    except Exception:
        print(f'{date_str}- data złego formatu')

def _validate_is_future (date: date) -> date | None:
     if datetime.today() > date:
          return date
     else:
          return datetime.today()