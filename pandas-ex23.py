import numpy as np
import pandas as pd

array1 = [1,2,3,4,5,6,7,8]
array2 = [1,3,5,7,9,11,13,15]

ds_array1 = pd.Series(array1)
ds_array2 = pd.Series(array2)

print("Exibindo as séries")
print("Serie 1")
print(ds_array1)

print("\n")
print("Exibindo as séries")
print("Serie 2")
print(ds_array2)

print("\n")
print("Combinando as duas séries")

ds_array = pd.concat([ds_array1,ds_array2],axis=1)

print("\n")
print("Exibindo série concatenada")
print(ds_array)