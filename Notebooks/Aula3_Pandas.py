# **Python para análise de dados(Pandas)** - *Fernanda Santos* 3 
#importando a biblioteca pandas
import pandas as pd
df = pd.read_csv("/content/drive/My Drive/Datasets/Gapminder.csv",error_bad_lines=False, sep=";")
#Visualizando as 5 primeiras linhas
df.head()
df = df.rename(columns={"country":"Pais", "continent": "continente", "year":"Ano", "lifeExp":"Expectativa de vida", "pop":"Pop Total", "gdpPercap": "PIB"})
df.head(10)
#Total de linhas e colunas
df.shape
df.columns
df.dtypes
df.tail(15)
df.describe()
df["continente"].unique()
Oceania = df.loc[df["continente"] == "Oceania"]
Oceania.head()
Oceania["continente"].unique()
df.groupby("continente")["Pais"].nunique()
df.groupby("Ano")["Expectativa de vida"].mean()
df["PIB"].mean()
df["PIB"].sum()
