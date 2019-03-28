import pandas as pd

dict = {'a1' : 1, 'a2' : 5, 'a3' : 20, 'a4' : 50, 'a5' : 80}

print("Dicionario")
print(dict)

dict_series = pd.Series(dict)

print("Dicionario convertido para serie Pandas")

print(dict_series)