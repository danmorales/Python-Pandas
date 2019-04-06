import pandas as pd
import numpy as np

func_junior = pd.read_excel('Excel/Funcionarios.xlsx',sheet_name='funcionarios_junior')
func_junior.set_index('funcinario_id', inplace=True)

func_senior = pd.read_excel('Excel/Funcionarios.xlsx',sheet_name='funcionarios_senior')
func_senior.set_index('funcinario_id', inplace=True)

faturamento = pd.read_excel('Excel/Funcionarios.xlsx',sheet_name='faturamento')

func_concat = pd.concat([func_junior,func_senior])

salario_junior = func_junior["salario"].mean()
salario_senior = func_senior["salario"].mean()
salario_geral = func_concat["salario"].mean()

print("Exibindo os salários médios")
print("Salário médio os funcionários juniors: R${:0,.2f}".format(salario_junior))
print("Salário médio os funcionários seniors: R${:0,.2f}".format(salario_senior))
print("Salário médio de todos os funcionários: R${:0,.2f}".format(salario_geral))

salario_junior_min = func_junior["salario"].min()
salario_senior_min = func_senior["salario"].min()
salario_geral_min = func_concat["salario"].min()

fun_junior_min = func_junior[func_junior["salario"] == salario_junior_min][["primeiro_nome","ultimo_nome","salario"]]
fun_senior_min = func_senior[func_senior["salario"] == salario_senior_min][["primeiro_nome","ultimo_nome","salario"]]
fun_geral_min = func_concat[func_concat["salario"] == salario_geral_min][["primeiro_nome","ultimo_nome","salario"]]

print("\n")
print("Funcionário junior com o menor salário")
print(fun_junior_min)

print("\n")
print("Funcionário senior com o menor salário")
print(fun_senior_min)

print("\n")
print("Funcionário com o menor salário")
print(fun_geral_min)

salario_junior_max = func_junior["salario"].max()
salario_senior_max = func_senior["salario"].max()
salario_geral_max = func_concat["salario"].max()

fun_junior_max = func_junior[func_junior["salario"] == salario_junior_max][["primeiro_nome","ultimo_nome","salario"]]
fun_senior_max = func_senior[func_senior["salario"] == salario_senior_max][["primeiro_nome","ultimo_nome","salario"]]
fun_geral_max = func_concat[func_concat["salario"] == salario_geral_max][["primeiro_nome","ultimo_nome","salario"]]

print("\n")
print("Funcionário junior com o maior salário")
print(fun_junior_max)

print("\n")
print("Funcionário senior com o maior salário")
print(fun_senior_max)

print("\n")
print("Funcionário com o maior salário")
print(fun_geral_max)

func_junior_ordered = func_junior.sort_values("salario")
func_senior_ordered = func_senior.sort_values("salario")
func_geral_ordered = func_concat.sort_values("salario")

print("\n")
print("Ordenando funcionários junior pelo sário")
print(func_junior_ordered)

print("\n")
print("Ordenando funcionários senior pelo sário")
print(func_senior_ordered)

print("\n")
print("Ordenando funcionários pelo sário")
print(func_geral_ordered)

faturamento_min = faturamento["Faturamento"].min()
faturamento_max = faturamento["Faturamento"].max()
faturamento_medio = faturamento["Faturamento"].mean()

ano_min = faturamento["Ano"].min()
ano_max = faturamento["Ano"].max()

print("\n")
print("Faturamento médio entre os anos ",ano_min," e ",ano_max)
print("R${:0,.2f}".format(faturamento_medio))

fat_ano_min = faturamento[faturamento["Faturamento"] == faturamento_min]["Ano"]
fat_ano_max = faturamento[faturamento["Faturamento"] == faturamento_max]["Ano"]

print("\n")
print("Valor mínimo de faturamento e respectivo ano")
print("R${:0,.2f}".format(faturamento_min), " ",fat_ano_min.values)

print("\n")
print("Valor máximo de faturamento e respectivo ano")
print("R${:0,.2f}".format(faturamento_max), " ",fat_ano_max.values)

print("\n")
print("Graficando faturamento em gráficos de barras")

faturamento["faturamento_normalizado"] = faturamento["Faturamento"]/1e6

faturamento.plot.bar(y='faturamento_normalizado',x='Ano',legend=False)
plt.xlabel("Ano")
plt.ylabel("Faturamento (milhões)")
plt.title("Faturamento da empresa")
plt.tight_layout()
plt.show()

savefig('Barplot_Faturamento.png',dpi=100)