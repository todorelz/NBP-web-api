import requests
from pprint import pprint
content = requests.get("https://api.nbp.pl/api/exchangerates/tables/A/")
data = content.json()
pprint(data)

#1. dla dziesiejszego dnia weź wszystkie kursy walut w formacie lista tupli, gdzie kod waluty, wartość kursu
#2 napisz funkcje do konwersji waluty gdzie argumentym wejściowym jest wartość w zlotówkach a zwracana kwota w odpowiedniej walucie
# niezbędna walidacja, typowanie zmiennych i wartości zwracanej
# obsłóż syatuacje, gdy dana waluta nie istnieje (sprawdź wszystkie kody walut, uwzględnij wielkość liter)
# 3. ceny złota z ostatnich 30dni https://api.nbp.pl/api/cenyzlota/last/30/?format=json
# narysuj wykres przedstawiający wykres liniowy wartość ceny złota w okresie,
# użyj biblioteki matplotlib

# ZRobić repozytorium

