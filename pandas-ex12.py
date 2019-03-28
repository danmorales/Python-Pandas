import pandas as pd

array = [1,2,3,5,8,12,15,20,40,50,80,100,150,180,250,280,290,300]

array_ds = pd.Series(array)

print("Série original")
print(array_ds)

print("Subconjunto do item a: valores menores do que 10")

array1 = array_ds[array_ds < 10]
print(array1)

print("Subconjunto do item b: valores maiores do que 50 ")

array2 = array_ds[array_ds > 50]
print(array2)

print("Subconjunto do item c: valores maiores do que 30 e menores do que 250 ")

array3 = array_ds[(array_ds > 30) & (array_ds < 250)]
print(array3)

print("Subconjunto do item d: valores maiores igual a 8 e menores igual a 250 ")

array4 = array_ds[(array_ds >= 8) & (array_ds <= 250)]
print(array4)