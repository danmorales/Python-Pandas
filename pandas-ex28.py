import pandas as pd
import numpy as np

array = [1,3,4,np.inf,0,1,6,2,np.inf,np.inf,np.inf,0,1,2,1]

array_df = pd.DataFrame(array)

print("Arranjo original")
print(array_df)

print("\n")
print("Removando valores infinitos")
array_df_new = array_df.replace(np.inf, 0)

print("\n")
print("Arranjo modificado")
print(array_df_new)