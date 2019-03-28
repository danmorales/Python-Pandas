import pandas as pd

array= ['1','ABC','5','Teste','10','2','6','Python']

ds_array = pd.Series(array)

print("Série original")
print(ds_array)

print("Ordenando valores")

sort_array = ds_array.sort_values()

print(sort_array)

print("Ordenando valores de forma inversa")

inverse_array = ds_array.sort_values(ascending=False)

print(inverse_array)