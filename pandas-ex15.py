import pandas as pd

array = {'A' : [1,2,3,4], 'B' : ['a','b','c','d'], 'C' : ['aa','bb','cc', 'dd']}

df_array = pd.DataFrame(data=array)

print("Exibindo arranjo")
print(df_array)

colunas = ['Coluna 1','Coluna 2', 'Coluna 3']

df_array.columns = colunas

print("\n")
print("Exibindo arranjo atualizado")
print(df_array)