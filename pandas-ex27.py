import pandas as pd
import numpy as np

Info_alunos = {'nome' : ['Aluno1', 'Aluno2', 'Aluno3', 'Aluno4', 'Aluno5', 'Aluno6', 'Aluno7', 'Aluno8', 'Aluno9', 'Aluno10'],
'nota' : [7.5, 8.2, 3.4, np.nan, 8.8, 1.2, np.nan, 4.5, 6.7, 9.4],
'tentativas' : [2,1,3,0,2,1,0,1,3,2],
'aprovado' : ['Sim','Sim','Não','Não','Sim','Não','Não','Não','Sim','Sim']}

df_alunos = pd.DataFrame(Info_alunos)

print("Arranjo original")
print(df_alunos)

print("Substituindo os NaNs por 0")
df_alunos['nota'] = df_alunos['nota'].fillna(0)

print("\n")
print("Tipo de dados das colunas do arranjo")
tipo = df_alunos.dtypes
print(tipo)

print("\n")
print("Alterando o tipo da coluna nota de float para inteiro")
df_alunos.nota = df_alunos.nota.astype(int)

print("\n")
print("Arranjo modificado")
print(df_alunos)

print("\n")
print("Tipo de dados das colunas do arranjo após alteração")
tipo_new = df_alunos.dtypes
print(tipo_new)