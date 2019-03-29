import pandas as pd

array = {'A' : [1,2,3,4,5,4,3,2,1], 'B' : [5,4,3,2,1,2,3,4,5], 'C' : [2,4,6,8,10,12,14,16,18]}

df_array = pd.DataFrame(data=array)

print("Arranjo original")
print(df_array)

print("\n")
print("Exibindo apenas 4 linhas")
pd.set_option('display.max_rows', 5)
print(df_array)

print("\n")
print("Exibindo apenas duas colunas")
pd.set_option('display.max_columns',2)
print(df_array)