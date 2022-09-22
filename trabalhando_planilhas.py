import pandas as pd  

df1 = pd.read_excel(r'D:\UFCG - ENGENHARIA\Bootcamp_unimed\Primeira analise de dados\datasets\Aracaju.xlsx')
df2 = pd.read_excel(r'D:\UFCG - ENGENHARIA\Bootcamp_unimed\Primeira analise de dados\datasets\Fortaleza.xlsx')
df3 = pd.read_excel(r'D:\UFCG - ENGENHARIA\Bootcamp_unimed\Primeira analise de dados\datasets\Natal.xlsx')
df4 = pd.read_excel(r'D:\UFCG - ENGENHARIA\Bootcamp_unimed\Primeira analise de dados\datasets\Recife.xlsx')
df5 = pd.read_excel(r'D:\UFCG - ENGENHARIA\Bootcamp_unimed\Primeira analise de dados\datasets\Salvador.xlsx')

print(df2.head())

df = pd.concat([df1,df2,df3,df4,df5])

print(df.sample(5))
print(df.dtypes)

df['LojaID'] = df['LojaID'].astype('object')

print(df.isnull().sum())

df['Vendas'].fillna(df['Vendas'].mean(),inplace=True)

df['Receita'] = df['Vendas'].mul(df['Qtde'])

print(df.head())

# retorna a maior receita
print(df['Receita'].max())

# retorna os melhores resultados 
print(df.nlargest(3,'Receita'))

# retorna os piores resulatados 
print(df.nsmallest(3,'Receita'))


# agrupando dados por cidade 
print(df.groupby('Cidade')['Receita'].sum())

# ordenando os dados pela receita 
print(df.sort_values('Receita',ascending=False).head(10))