import pandas as pd

nomes = ['Andre','Carlos','Luis','Maria','Ana','Jose','Arnaldo','Augusto','Antonio','Daniel','Carol','Carla']

cidade = ['São Paulo','Rio de Janeiro','Port Alegre','Rio de Janeiro','Rio de Janeiro','São Paulo', 'São Paulo','Port Alegre',
		'Rio de Janeiro','São Paulo','São Paulo','São Paulo']
		
array = {'Nome' : nomes, 'Cidade' : cidade}

df_array = pd.DataFrame(data = array)

print("Arranjo")
print(df_array)

habitantes = df_array.groupby(["Cidade"]).size().reset_index(name='Habitantes')

print("\n")
print(habitantes)