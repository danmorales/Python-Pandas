import pandas as pd

array1 = [3,7,9,10,13,15,18]
array2 = [2,3,6,8,10,12,14]

ds_array1 = pd.Series(array1)
ds_array2 = pd.Series(array2)

print("Adicionando séries")

ds_sum = ds_array1 + ds_array2

print(ds_sum)

print("Subtraindo séries")

ds_diff = ds_array1 - ds_array2

print(ds_diff)

print("Multiplicando séries")

ds_mult = ds_array1 * ds_array2

print(ds_mult)

print("Dividindo séries")

ds_div = ds_array1 / ds_array2

print(ds_div)