import numpy as np
import pandas as pd

array = [1,3,4,7,8,10,15]

np_array = np.array(array)

print("Arranjo NumPy")
print(np_array)

print("Convertendo para serie Pandas")

ds_array = pd.Series(np_array)

print("Serie Pandas")
print(ds_array)