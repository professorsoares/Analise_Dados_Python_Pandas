# **Python para análise de dados(Pandas)** - *Fernanda Santos* 3 
#importando a biblioteca pandas
import pandas as pd
# df = pd.read_csv("/content/drive/My Drive/Datasets/Gapminder.csv",error_bad_lines=False, sep=";")
df = pd.read_csv("../datasets/Gapminder.csv",error_bad_lines=False, sep=";")
#Visualizando as 5 primeiras linhas
print(df.head())
df = df.rename(columns={"country":"Pais", "continent": "continente", "year":"Ano", "lifeExp":"Expectativa de vida", "pop":"Pop Total", "gdpPercap": "PIB"})
print(df.head(10))
#Total de linhas e colunas
print("\ndf.shape")
print(df.shape)
print("\ndf.columns")
print(df.columns)
print("\ndf.dtypes")
print(df.dtypes)
df.tail(15)
print("\ndf.describe()")
print(df.describe())

print("df['continente'].unique()")
print(df["continente"].unique())

Oceania = df.loc[df["continente"] == "Oceania"]
Oceania.head()
Oceania["continente"].unique()
df.groupby("continente")["Pais"].nunique()
df.groupby("Ano")["Expectativa de vida"].mean()
df["PIB"].mean()

print('\ndf["PIB"].sum()')
print(df["PIB"].sum())
