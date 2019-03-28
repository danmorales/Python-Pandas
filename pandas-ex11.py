import pandas as pd

array = ['10','30','ABC','50','Python','Teste']

ds_array = pd.Series(array)

print("Série Original")
print(ds_array)

new = pd.Series(['20','25'])

new_ds_array = ds_array.append(new)

print("Série nova")
print(new_ds_array)