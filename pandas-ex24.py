import numpy as np
import pandas as pd

array = ['5/11/2019','12/25/2015','1/31/2008','10/12/2018']

ds_array = pd.Series(array)
print("Arranjo original")
print(ds_array)

print("\n")
print("Convertendo para o formato dia/hora")
date = pd.to_datetime(ds_array)
df_date = pd.DataFrame(date)

print("Arranjo convertido")
print(df_date)