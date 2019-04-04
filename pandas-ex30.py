import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pop_ind = pd.read_csv('CSV/Populacao_Individual.csv')
pop_tot = pd.read_csv('CSV/Populacao_Total.csv')

print("Exibindo informações sobre o arquivo da população individual")
print(pop_ind.info())

print("\n")
print("Exibindo informações sobre o arquivo da população total")
print(pop_tot.info())

print("\n")
print("Exibindo as cinco primeiras linhas do arranjo da população total")
print(pop_tot.head())

print("\n")
print("Exibindo as cinco primeiras linhas do arranjo da população individual")
print(pop_ind.head())

print("\n")
print("Exibindo as cinco últimas linhas do arranjo da população total")
print(pop_tot.tail())

print("\n")
print("Exibindo as cinco últimas linhas do arranjo da população individual")
print(pop_ind.tail())

print("\n")
print("Determinando o número de elementos NaNs do arranjo de população individual")
print(pop_ind[pop_ind.isna()].count())

print("\n")
print("Determinando o número de elementos NaNs do arranjo de população total")
print(pop_ind[pop_tot.isna()].count())

print("\n")
print("Exibindo nomes das colunas da população individual")
print(pop_ind.columns.values)

print("\n")
print("Exibindo nomes das colunas da população total")
print(pop_tot.columns.values)

print("\n")
print("Excluindo países desnecessários")
paises = pop_ind["CountryName"][0:33]        
print(paises)

for i in paises:
	pop_ind = pop_ind[pop_ind["CountryName"] != i]

print("Exibindo os 5 países mais populosos no ano de 2014")
most_pop = pop_ind[pop_ind["Year"] ==2014].sort_values(["Total Population","CountryName"],ascending=False).head(5)
print(most_pop[["CountryName","CountryCode"]])

pop_paises = pop_ind.set_index("CountryCode",drop=True)

pop_china = pop_paises[(pop_paises["Year"] == 1960) | (pop_paises["Year"] == 1970) | (pop_paises["Year"] == 1980) | (pop_paises["Year"] == 1990) | (pop_paises["Year"] == 2000) | (pop_paises["Year"] == 2010)].loc["CHN",["Total Population"]]["Total Population"].values.transpose() /1e6
pop_india = pop_paises[(pop_paises["Year"] == 1960) | (pop_paises["Year"] == 1970) | (pop_paises["Year"] == 1980) | (pop_paises["Year"] == 1990) | (pop_paises["Year"] == 2000) | (pop_paises["Year"] == 2010)].loc["IND",["Total Population"]]["Total Population"].values.transpose() /1e6
pop_usa = pop_paises[(pop_paises["Year"] == 1960) | (pop_paises["Year"] == 1970) | (pop_paises["Year"] == 1980) | (pop_paises["Year"] == 1990) | (pop_paises["Year"] == 2000) | (pop_paises["Year"] == 2010)].loc["USA",["Total Population"]]["Total Population"].values.transpose() /1e6
pop_idn = pop_paises[(pop_paises["Year"] == 1960) | (pop_paises["Year"] == 1970) | (pop_paises["Year"] == 1980) | (pop_paises["Year"] == 1990) | (pop_paises["Year"] == 2000) | (pop_paises["Year"] == 2010)].loc["IDN",["Total Population"]]["Total Population"].values.transpose() /1e6
pop_bra = pop_paises[(pop_paises["Year"] == 1960) | (pop_paises["Year"] == 1970) | (pop_paises["Year"] == 1980) | (pop_paises["Year"] == 1990) | (pop_paises["Year"] == 2000) | (pop_paises["Year"] == 2010)].loc["BRA",["Total Population"]]["Total Population"].values.transpose() /1e6

year = [1960,1970,1980,1990,2000,2010]

dict_most_pop = {"Year" : year, "China" : pop_china, "India" : pop_india, "USA" : pop_usa, "Indonésia" : pop_idn, "Brazil" : pop_bra}
df_paises_most_pop = pd.DataFrame(dict_most_pop)

fig = plt.figure(figsize=(8, 8))
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)

df_paises_most_pop.plot.bar(x='Year',ax=ax1,legend=False)
ax1.set_ylabel("Population (Milions of people)")
ax1.set_title("5 Most Populated Countries")

df_paises_most_pop.plot.barh(x='Year',ax=ax2)
ax2.set_xlabel("Population (Milions of people)")
ax2.set_ylabel("Year")
plt.tight_layout()
plt.show()

print("\n")
print("Exibindo os 5 países menos populosos no ano de 2014")
less_pop = pop_ind[pop_ind["Year"] ==2014].sort_values(["Total Population","CountryName"],ascending=True).head(5)
print(less_pop[["CountryName","CountryCode"]])

pop_tuv = pop_paises[(pop_paises["Year"] == 1960) | (pop_paises["Year"] == 1970) | (pop_paises["Year"] == 1980) | (pop_paises["Year"] == 1990) | (pop_paises["Year"] == 2000) | (pop_paises["Year"] == 2010)].loc["TUV",["Total Population"]]["Total Population"].values.transpose() /1e3
pop_plw = pop_paises[(pop_paises["Year"] == 1960) | (pop_paises["Year"] == 1970) | (pop_paises["Year"] == 1980) | (pop_paises["Year"] == 1990) | (pop_paises["Year"] == 2000) | (pop_paises["Year"] == 2010)].loc["PLW",["Total Population"]]["Total Population"].values.transpose() /1e3
pop_smr = pop_paises[(pop_paises["Year"] == 1960) | (pop_paises["Year"] == 1970) | (pop_paises["Year"] == 1980) | (pop_paises["Year"] == 1990) | (pop_paises["Year"] == 2000) | (pop_paises["Year"] == 2010)].loc["SMR",["Total Population"]]["Total Population"].values.transpose() /1e3
pop_tca = pop_paises[(pop_paises["Year"] == 1960) | (pop_paises["Year"] == 1970) | (pop_paises["Year"] == 1980) | (pop_paises["Year"] == 1990) | (pop_paises["Year"] == 2000) | (pop_paises["Year"] == 2010)].loc["TCA",["Total Population"]]["Total Population"].values.transpose() /1e3
pop_lie = pop_paises[(pop_paises["Year"] == 1960) | (pop_paises["Year"] == 1970) | (pop_paises["Year"] == 1980) | (pop_paises["Year"] == 1990) | (pop_paises["Year"] == 2000) | (pop_paises["Year"] == 2010)].loc["LIE",["Total Population"]]["Total Population"].values.transpose() /1e3

dict_less_pop = {"Year" : year, "Tuvalu" : pop_tuv, "Palau" : pop_plw, "San Marino" : pop_smr, "Turks and Caicos Islands" : pop_tca, "Liechtenstein" : pop_lie}
df_paises_less_pop = pd.DataFrame(dict_less_pop)

fig = plt.figure(figsize=(8, 8))
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)

df_paises_less_pop.plot.bar(x='Year',ax=ax1,legend=False)
ax1.set_ylabel("Population (Thousands of people)")
ax1.set_title("5 Less Populated Countries")

df_paises_less_pop.plot.barh(x='Year',ax=ax2)
ax2.set_xlabel("Population (Thousands of people)")
ax2.set_ylabel("Year")
plt.tight_layout()
plt.show()

print("\n")
print("Computando o percentual da população dos países mais populosos em relação a população mundial")

tot_pop = pop_tot["Total Population"] / 1e6
print("\n")
print("População Percentual dos cinco países mais populosos")

pop_perc_china = df_paises_most_pop["China"].values/ tot_pop * 100
pop_perc_india = df_paises_most_pop["India"].values/ tot_pop * 100
pop_perc_usa = df_paises_most_pop["USA"]/ tot_pop * 100
pop_perc_indonesia = df_paises_most_pop["Indonésia"]/ tot_pop * 100
pop_perc_brazil = df_paises_most_pop["Brazil"]/ tot_pop * 100

dic_pop_perc = {"Year" : year, "China" : pop_perc_china, "India" : pop_perc_india, "USA" : pop_perc_usa, "Indonesia" : pop_perc_indonesia, "Brazil" : pop_perc_brazil}
df_pop_perc = pd.DataFrame(dic_pop_perc)

fig2 = plt.figure(figsize=(8, 8))
ax1 = fig2.add_subplot(211)
ax2 = fig2.add_subplot(212)

df_pop_perc.plot.bar(x='Year',ax=ax1,legend=False)
ax1.set_ylabel("Percentual of World Population")
ax1.set_title("5 Most Populated Countries")

df_pop_perc.plot.barh(x='Year',ax=ax2)
ax2.set_xlabel("Percentual of World Population")
ax2.set_ylabel("Year")
plt.tight_layout()
plt.show()

print("\n")
print("Computando dados da população do Brasil")

pop_brasil_full = pop_paises.loc["BRA"]
pop_brasil_full["Total Population Normalized"] = pop_brasil_full["Total Population"]/1e6

fig3 = plt.figure(figsize=(8, 8))
ax1 = fig3.add_subplot(211)
ax2 = fig3.add_subplot(212)

pop_brasil_full.plot.scatter(x='Year',y='Total Population Normalized',ax=ax1)
ax1.set_xlabel('Year')
ax1.set_ylabel('Population (Milions of people)')
ax1.set_title('Brazilian Population')

pop_brasil_full.plot.scatter(x='Year',y='Urban population (% of total)',ax=ax2)
ax2.set_xlabel('Year')
ax2.set_ylabel('Urban Population (%)')
plt.show()