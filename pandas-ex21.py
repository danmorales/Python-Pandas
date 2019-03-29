import pandas as pd

array = {'A' : [1,2,3,4,5,4,3,2,1], 'B' : [5,4,3,2,1,2,3,4,5], 'C' : [2,4,6,8,10,12,14,16,18]}

df_array = pd.DataFrame(data=array)

print("Arranjo original")
print(df_array)

print("\n")
print("Exibindo linha com id=3")
id = 3
resultado = df_array.iloc[[id]]
print(resultado)