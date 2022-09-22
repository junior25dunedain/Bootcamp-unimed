import pandas as pd  

dados = pd.read_csv(r'D:\UFCG - ENGENHARIA\Bootcamp_unimed\Primeira analise de dados\datasets\Gapminder.csv',error_bad_lines=False,sep=';')

print(dados.head())

dados.rename(columns={'country':'Pais','continent':'Continente','year':'Ano','lifeExp':'Expectativa de vida','pop':'Pop total','gdpPercap':'PIB'},inplace=True)

print(dados.head(10))

# total de linhas e colunas 
print(dados.shape)

# tipos de dados de cada coluna 
print(dados.dtypes)

# dados estatisticos das colunas numericas desse dataframe
print(dados.describe())

print(dados['Continente'].unique()) 

oceania = dados.loc[dados['Continente'] == 'Oceania']
print(oceania.head()) 

print(dados.groupby('Continente')['Pais'].nunique())

print(dados.groupby('Ano')['Expectativa de vida'].mean())



