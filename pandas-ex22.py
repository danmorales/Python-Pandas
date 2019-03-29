import numpy as np
import pandas as pd

array = [1,2,np.nan,4,5,np.nan,np.nan,1,2,2,np.nan,np.nan,4]

df_array = pd.DataFrame(array)

print("Arranjo original")
print(df_array)

print("\n")
print("Determinando a quantidade de NaNs no arranjo")
n_nans = df_array.isnull().values.sum()
print(n_nans)

print("\n")
print("Substituindo os NaNs por 0")
df_array_new = df_array.fillna(0)

print("\n")
print("Arranjo modificado")
print(df_array_new)

print("\n")
print("Média arranjo original ",df_array.mean())

print("\n")
print("Média arranjo modificado ",df_array_new.mean())