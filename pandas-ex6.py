import numpy as np

array = ['1','2','Python','5','6','Pandas','9','14']

ds_array = pd.Series(array)

print("Serie Pandas")
print(ds_array)

print("Convertendo para série numérica")

ds_array2 = pd.to_numeric(ds_array, errors='coerce')

print("Serie Pandas numérica")
print(ds_array2)