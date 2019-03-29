import pandas as pd

array = {'A' : [1,2,3,4], 'B' : ['a','b','c','d'], 'C' : ['aa','bb','cc', 'dd']}

df_array = pd.DataFrame(data=array)

print("Arranjo original")
print(df_array)

ordem = ['C','A','B']

df_array_new = df_array[ordem]

print("\n")
print("Arranjo modificado")
print(df_array_new)