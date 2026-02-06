from pydantic import BaseModel, RootModel
from typing import Optional
from datetime import date
from enum import Enum

class CurrencyCode(str, Enum):
    USD = 'USD'
    AUD = 'AUD'
    CAD = 'CAD'
    EUR ='EUR'
    HUF = 'HUF'
    CHF = 'CHF'
    GBP = 'GBP'
    CZK = 'CZK'

class ExchangeRate(BaseModel):
    currency: str 
    code: CurrencyCode
    mid: Optional[float] = None 
    bid: Optional[float] = None 
    ask: Optional[float] = None 

class ExchangeRates(BaseModel):
    table: str
    no: str
    tradingDate: Optional[date] = None
    effectiveDate: date
    rates: list[ExchangeRate]

class GoldPrice(BaseModel):
    data: Optional[date] = date.today()
    cena: float


class GoldPrices(RootModel[list[GoldPrice]]):
    pass