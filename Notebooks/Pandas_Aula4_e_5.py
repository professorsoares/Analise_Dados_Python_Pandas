#**Trabalhando com Planilhas do Excel**  4 e 5
#Importando a biblioteca
import pandas as pd
#Leitura dos arquivos
df1 = pd.read_excel("Aracaju.xlsx")
df2 = pd.read_excel("Fortaleza.xlsx")
df3 = pd.read_excel("Natal.xlsx")
df4 = pd.read_excel("Recife.xlsx")
df5 = pd.read_excel("Salvador.xlsx")
df5.head()
#juntando todos os arquivos
df = pd.concat([df1,df2,df3,df4,df5])
#Exibindo as 5 primeiras linhas
df.head()
#Exibindo as 5 últimas linhas
df.tail()
df.sample(5)
#Verificando o tipo de dado de cada coluna
df.dtypes
#Alterando o tipo de dado da coluna LojaID
df["LojaID"] = df["LojaID"].astype("object")
df.dtypes
df.head()
**Tratando valores faltantes**
#Consultando linhas com valores faltantes
df.isnull().sum()
#Substituindo os valores nulos pela média
df["Vendas"].fillna(df["Vendas"].mean(), inplace=True)
df["Vendas"].mean()
df.isnull().sum()
df.sample(15)
#Substituindo os valores nulos por zero
df["Vendas"].fillna(0, inplace=True)
#Apagando as linhas com valores nulos
df.dropna(inplace=True)
#Apagando as linhas com valores nulos com base apenas em 1 coluna
df.dropna(subset=["Vendas"], inplace=True)
#Removendo linhas que estejam com valores faltantes em todas as colunas
df.dropna(how="all", inplace=True)
**Criando colunas novas**
#Criando a coluna de receita
df["Receita"] = df["Vendas"].mul(df["Qtde"])
df.head()
df["Receita/Vendas"] = df["Receita"] / df["Vendas"] 
df.head()
#Retornando a maior receita
df["Receita"].max()
#Retornando a menor receita
df["Receita"].min()
#nlargest
df.nlargest(3, "Receita")
#nsamllest
df.nsmallest(3, "Receita")
#Agrupamento por cidade
df.groupby("Cidade")["Receita"].sum()
#Ordenando o conjunto de dados
df.sort_values("Receita", ascending=False).head(10)
#**Trabalhando com datas**
#Trasnformando a coluna de data em tipo inteiro
df["Data"] = df["Data"].astype("int64")
#Verificando o tipo de dado de cada coluna
df.dtypes
#Transformando coluna de data em data
df["Data"] = pd.to_datetime(df["Data"])
df.dtypes
#Agrupamento por ano
df.groupby(df["Data"].dt.year)["Receita"].sum()
#Criando uma nova coluna com o ano
df["Ano_Venda"] = df["Data"].dt.year
df.sample(5)
#Extraindo o mês e o dia
df["mes_venda"], df["dia_venda"] = (df["Data"].dt.month, df["Data"].dt.day)
df.sample(5)
#Retornando a data mais antiga
df["Data"].min()
#Calculando a diferença de dias
df["diferenca_dias"] = df["Data"] - df["Data"].min()
df.sample(5)
#Criando a coluna de trimestre
df["trimestre_venda"] = df["Data"].dt.quarter
df.sample(5)
#Filtrando as vendas de 2019 do mês de março
vendas_marco_19 = df.loc[(df["Data"].dt.year == 2019) & (df["Data"].dt.month == 3)]
vendas_marco_19.sample(20)
