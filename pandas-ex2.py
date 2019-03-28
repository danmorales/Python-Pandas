import pandas as pd

array = [1,3,4,7,9,10,12,15]
ds_array = pd.Series(array)

print("Série Pandas e seu tipo")
print(ds_array, "  ",type(ds_array))

print("Convertendo para lista")

list_array = ds_array.tolist()

print("Lista e seu tipo")
print(list_array, " ",type(list_array))