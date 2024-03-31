import pandas as pd

#1 - Importando dados
data = pd.read_excel("data/VendaCarros.xlsx")

print(data)

#2-lista os primeiros registros
print(data.head())

#3-lista os últimos registros
print(data.tail())

#4-contagem de valores por fabricante
print(data["Fabricante"].value_counts())