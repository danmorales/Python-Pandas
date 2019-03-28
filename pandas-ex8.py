import pandas as pd
import numpy as np

serie = ['2','A','5','B','10','T']

ds_serie = pd.Series(serie)

print("Serie Original")
print(ds_serie)

print("Convertendo a série para um arranjo")

array = np.array(ds_serie.values.tolist())

print(array)