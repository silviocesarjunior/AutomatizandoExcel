import pandas as pd

#1 - Importando dados
data = pd.read_excel("data/VendaCarros.xlsx")

# print(type(data))

#2-selecionando colunas
df = data[["Fabricante", "ValorVenda", "Ano"]]
print(df)

#3- criando a tabela pivô
pivot_table = df.pivot_table(
    index="Ano",
    columns="Fabricante",
    values="ValorVenda",
    aggfunc="sum"
)
print(pivot_table)

#4-exportando tablea pivô em arquivo excel
pivot_table.to_excel("data/pivot_table.xlsx", "Relatorio")