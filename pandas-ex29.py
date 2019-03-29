import pandas as pd
import numpy as np

array = {'A' : [1,2,3,4,5], 'B' : [5,4,3,2,1], 'C' : [2,4,6,8,10], 'D' : [1,3,5,7,9]}

array_df = pd.DataFrame(data=array)

print("Exibindo arranjo original")
print(array_df)

filename = 'exercicio29.csv'

print("\n")
print("Salvando dados no arquivo " + filename)
array_df.to_csv(filename,index=False)


