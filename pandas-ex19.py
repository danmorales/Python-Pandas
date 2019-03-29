import pandas as pd

array = {'A' : [1,2,3,4,5,4,3,2,1], 'B' : [5,4,3,2,1,2,3,4,5], 'C' : [2,4,6,8,10,12,14,16,18]}

df_array = pd.DataFrame(data=array)

print("Arranjo original")
print(df_array)

print("\n")
print("Removendo linhas cuja coluna B tenha valores iguais a 3")

df_array_new = df_array[df_array.B != 3]
print("Novo arranjo")
print(df_array_new)
