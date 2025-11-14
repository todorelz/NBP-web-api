# 3. ceny złota z ostatnich 30dni https://api.nbp.pl/api/cenyzlota/last/30/?format=json
# narysuj wykres przedstawiający wykres liniowy wartość ceny złota w okresie,
# użyj biblioteki matplotlib

# ZRobić repozytorium
import requests
import matplotlib.pyplot as plt
from pprint import pprint

content = requests.get("https://api.nbp.pl/api/cenyzlota/last/30/?format=json")
gold_datas = content.json()

dates = []
prices = []

for data in gold_datas:
    dates.append(data.get('data'))
    prices.append(data.get('cena'))

plt.plot(dates,prices)
plt.title("Gold prices")
plt.xlabel("dates")
plt.ylabel("price")
plt.Axes.autoscale("dates")
plt.show()
