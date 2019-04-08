import pandas as pd
import numpy as np

def removendo_outliers(valores):
    quantidades = valores.quantile([.25, .75])
    return np.mean(quantidades)

#Dados obtidos em http://worldhappiness.report/

happy = pd.read_csv('Excel/Felicidade.csv', index_col=0)

#Ordenando os dados por ano em ordem crescente e indice de felicidade em ordem decrescente
happy.sort_values(['Year', "Happiness Score"], ascending=[True, False], inplace=True)

#Exibindo as 10 primeiras linhas
print("\n")
print(happy.head(10))

#Exibindo uma visão geral dos dados
print("\n")
print("Este dados tem {0} linhas e {1} colunas".format(happy.shape[0], happy.shape[1]))

#Procurando por NaNs
print("Existem valores NaNs? {}".format(happy.isnull().any().any()))
print("\n")
print(happy.describe())

#categorizando por ano
happy_year = pd.pivot_table(happy, index= 'Year', values= "Happiness Score")
print("\n")
print(happy_year)

#categorizando por região
happy_region = pd.pivot_table(happy, index= 'Region', values= "Happiness Score")
print("\n")
print(happy_region)

#categorizando por ano e região
happy_year_region = pd.pivot_table(happy, index = ['Region', 'Year'], values="Happiness Score")
print("\n")
print(happy_year_region)

#utilizando ano como coluna
happy_column = pd.pivot_table(happy, index= 'Region', columns='Year', values="Happiness Score")
print("\n")
print(happy_column)

#graficando happy_column num gráfico de barras
happy_column.plot(kind= 'barh')
plt.ylabel("Rank de felicidade")
plt.tight_layout()
plt.show()

#manipulando utilizando funções agregadas
happy_agg = pd.pivot_table(happy, index= 'Region', values= "Happiness Score",aggfunc= [np.mean, np.median, min, max, np.std])
print("\n")
print(happy_agg)

#manipulando utilizando funções agregadas e uma função lambda para determinar o número médio de países numa determinada região num dado ano
happy_agg_lambda = pd.pivot_table(happy, index = 'Region', values="Happiness Score",aggfunc= [np.mean, min, max, np.std, lambda x: x.count()/3])
print("\n")
print(happy_agg_lambda)

#removendo outliers
outlier = pd.pivot_table(happy, index = 'Region', values="Happiness Score",aggfunc= [np.mean, removendo_outliers, lambda x: x.count()/3])
print("\n")
print(outlier)

tabela = pd.pivot_table(happy, index = 'Region', values="Happiness Score", aggfunc= [np.mean, removendo_outliers])
tabela_asia = tabela[tabela.index.str.contains('Asia')]
print("\n")
print(tabela_asia)

tabela_europa = tabela[tabela.index.str.contains('Europe')]
print("\n")
print(tabela_europa)

#extraindo valores das colunas região e ano

tabela2 = pd.pivot_table(happy, index = ['Region', 'Year'], values='Happiness Score',aggfunc= [np.mean, removendo_outliers])
tabela_query = tabela2.query('Year == [2015, 2017] and Region == ["Sub-Saharan Africa", "Middle East and Northern Africa"]')
print("\n")
print(tabela_query)

#manipulando dados ausentes, separando em três quantiles
score = pd.qcut(happy["Happiness Score"], 3)
score_table = pd.pivot_table(happy, index= ['Region', score], values= "Happiness Score", aggfunc= 'count')
print("\n")
print(score_table)

score_table_fillna = pd.pivot_table(happy, index= ['Region', score], values= "Happiness Score", aggfunc= 'count', fill_value= 0)
print("\n")
print(score_table_fillna)