import pandas as pd

array1 = ['A','B','C']
array2 = ['1','2','3','4']
array3 = ['d','e']

serie = pd.Series([array1,array2,array3])

print("Serie original de lista")
print(serie)

print("Convertendo para uma única série")

serie_unique = serie.apply(pd.Series).stack().reset_index(drop=True)

print(serie_unique)