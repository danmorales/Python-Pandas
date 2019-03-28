import pandas as pd

array = [1,2,4,5,6,7,8,9,12,14,15,18,19,25,29,35,38,40,45,48,49,50]

array_ds = pd.Series(array)

print("Série original")
print(array_ds)

media_ds = array_ds.mean()
print("Valor médio da série")
print(media_ds)

std_ds = array_ds.std()
print("Desvio padrão da série")
print(std_ds)
