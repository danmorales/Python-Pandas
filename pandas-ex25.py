import numpy as np
import pandas as pd

tipo = [('Coluna1','int32'), ('Coluna2','int32'), ('Coluna3','int32')]

valores = np.zeros(10, dtype = tipo)

indice = ['Indice'+str(i) for i in range(1,len(valores)+1)]

df_array = pd.DataFrame(valores,index=indice)

print("Exibindo arranjo")
print(df_array)