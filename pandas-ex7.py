import numpy as np

dict_array = {'coluna 1' : [1,2,4,8,16], 'coluna 2' : [1,3,5,7,9], 'coluna 3' : [2,4,6,8,10]}

df_array = pd.DataFrame(data=dict_array)

print("DataFrame original")
print(df_array)

ds_array = df_array.iloc[:,0]

print("Primeira coluna como série")
print(ds_array)
print("Tipo de dado")
print(type(ds_array))