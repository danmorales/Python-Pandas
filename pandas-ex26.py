import pandas as pd

array = {'Coluna1' : [1,2,3,4,5], 'Coluna2' : [2,4,6,8,10], 'Coluna3' : [1,3,5,7,9]}

array_df = pd.DataFrame(array)

print("Arranjo original")
print(array_df)

print("\n")
print("Verificando se existe Coluna4")

if 'Coluna4' in array_df.columns:
	print("Coluna4 está presente")
else:
	print("Coluna4 não está presente")
	
print("\n")
print("Verificando se existe Coluna1")

if 'Coluna1' in array_df.columns:
	print("Coluna1 está presente")
else:
	print("Coluna1 não está presente")