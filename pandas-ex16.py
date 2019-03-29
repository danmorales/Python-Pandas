import numpy as np
import pandas as pd

array = {'A' : [1,2,3,4,5,2,10,3,4,2,11], 'B' : [11,12,13,14,15,10,9,11,12,14,20]}

df_array = pd.DataFrame(data=array)

print("Arranjo original")
print(df_array)

print("\n")
print("Exibindo linhas em que a coluna A tenha valor igual a 2")

data = df_array.loc[df_array['A'] == 2]
print(data)