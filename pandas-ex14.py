import pandas as pd
import numpy as np

Info_alunos = {'nome' : ['Aluno1', 'Aluno2', 'Aluno3', 'Aluno4', 'Aluno5', 'Aluno6', 'Aluno7', 'Aluno8', 'Aluno9', 'Aluno10'],
'nota' : [7.5, 8.2, 3.4, np.nan, 8.8, 1.2, np.nan, 4.5, 6.7, 9.4],
'tentativas' : [2,1,3,0,2,1,0,1,3,2],
'aprovado' : ['Sim','Sim','Não','Não','Sim','Não','Não','Não','Sim','Sim']}

labels_alunos = ['a', 'b','c','d','e','f','g','h','i','j']

df_alunos = pd.DataFrame(Info_alunos,index=labels_alunos)

print("\n")
print("Informações básicas")
print(df_alunos.head())

print("\n")
print("Três primeiras linhas")
print(df_alunos.iloc[:3])

print("\n")
print("Colunas nome e nota")
print(df_alunos[['nome','nota']])

print("\n")
print("Colunas nome e nota da terceria até sexta linha")
print(df_alunos[['nome','nota']].iloc[2:6])

print("\n")
print("Número de tentativas maior do que 2")
print(df_alunos[df_alunos['tentativas'] > 2])

total_linhas = len(df_alunos.axes[0])
total_colunas = len(df_alunos.axes[1])

print("\n")
print("Total de linhas = ",total_linhas)
print("Total de colunas = ",total_colunas)

print("\n")
print("Notas NaNs")
print(df_alunos[df_alunos['nota'].isnull()])

print("\n")
print("Notas maiores do que 5 e menores iguais a 10")
print(df_alunos[(df_alunos['nota'] > 5) & (df_alunos['nota'] <= 10)])

print("\n")
print("Número de tentativas menor do que 2 e nota maior do que 6")
print(df_alunos[(df_alunos['nota'] > 6) & (df_alunos['tentativas'] < 2)])

print("\n")
print("Alterando nota do aluno do item d")
df_alunos.loc['d','nota'] = 7.0
print("Dados atualizados")
print(df_alunos)

print("\n")
print("Soma do número de tentativas")
print(df_alunos['tentativas'].sum())

print("\n")
print("Média das notas")
print(df_alunos['nota'].mean())

print("\n")
print("Adicionando aluno 11")
df_alunos.loc['k'] = ['Aluno11', 6.7, 1, 'Sim']
print("Dados atualizados")
print(df_alunos)

print("\n")
print("Removendo o Aluno4")
df_alunos = df_alunos.drop('d')
print("Dados atualizados")
print(df_alunos)

print("\n")
print("Ordenando nomes por ordem decrescente e notas por ordem crescente")
df_alunos.sort_values(by=['nome','nota'], ascending = [False, True])
print(df_alunos)

print("\n")
print("Removendo a coluna tentativas")
df_alunos.pop('tentativas')
print("Dados atualizados")
print(df_alunos)

faltas = [0,3,1,2,2,0,0,4,1,0]
print("\n")
print("Inserindo a coluna faltas")
df_alunos['faltas'] = faltas
print("Dados atualizados")
print(df_alunos)

print("\n")
print("Loop sobre as linhas e colunas")

for index, row in df_alunos.iterrows():
	print(row['nome'], row['nota'], row['faltas'])
	
print("\n")
print("Gerando lista com os nomes das colunas")
lista = df_alunos.columns.values
print(lista)