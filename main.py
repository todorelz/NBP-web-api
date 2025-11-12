import requests
from pprint import pprint


#1. dla dziesiejszego dnia weź wszystkie kursy walut w formacie lista tupli, gdzie kod waluty, wartość kursu
# pprint(data)
#2 napisz funkcje do konwersji waluty gdzie argumentym wejściowym jest wartość w zlotówkach a zwracana kwota w odpowiedniej walucie
# niezbędna walidacja, typowanie zmiennych i wartości zwracanej
# obsłóż syatuacje, gdy dana waluta nie istnieje (sprawdź wszystkie kody walut, uwzględnij wielkość liter)

# print(waluta)


content = requests.get("https://api.nbp.pl/api/exchangerates/tables/A/")
data = content.json()
dicts = data[-1].get('rates')

kursy=[]
for dict in dicts:
    rate = (dict.get('code'),dict.get('mid'))
    kursy.append(rate)
pprint(f'Tabela kursów z dnia: {kursy}')

def exch_rate_trans(valuePLN: int|float, waluta: str)->float:
    if not (isinstance(valuePLN,(float,int)) and isinstance(waluta,str)):   
        print(f'Wrong data input')
        return None
    
    for kurs in kursy:
        kurs_short = kurs[0]
        kurs_value=kurs[1]

        if kurs_short==waluta:
            value_waluta = round(valuePLN/kurs[1],2)
            print(f'Przeliczona kwota wynosi: {valuePLN}{kurs_short}')

    return round(valuePLN/kurs[1],2)
print(f' Przeliczona kwota to: {exch_rate_trans(100,'usd')}')



