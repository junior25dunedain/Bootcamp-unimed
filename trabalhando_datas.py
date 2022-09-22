import pandas as pd 
import matplotlib.pyplot as plt 

df1 = pd.read_excel(r'D:\UFCG - ENGENHARIA\Bootcamp_unimed\Primeira analise de dados\datasets\Aracaju.xlsx')
df2 = pd.read_excel(r'D:\UFCG - ENGENHARIA\Bootcamp_unimed\Primeira analise de dados\datasets\Fortaleza.xlsx')
df3 = pd.read_excel(r'D:\UFCG - ENGENHARIA\Bootcamp_unimed\Primeira analise de dados\datasets\Natal.xlsx')
df4 = pd.read_excel(r'D:\UFCG - ENGENHARIA\Bootcamp_unimed\Primeira analise de dados\datasets\Recife.xlsx')
df5 = pd.read_excel(r'D:\UFCG - ENGENHARIA\Bootcamp_unimed\Primeira analise de dados\datasets\Salvador.xlsx')

df = pd.concat([df1,df2,df3,df4,df5])


print(df.dtypes)

df['Receita'] = df['Vendas'].mul(df['Qtde'])

df['Ano_venda'] = df['Data'].dt.year
df['mes_venda'], df['dia_venda'] = (df['Data'].dt.month, df['Data'].dt.day)

df['diferenca_dias'] = df['Data'] - df['Data'].min()

df['trimestre_venda'] = df['Data'].dt.quarter
print(df.sample(5))


vendas_marco_19 = df.loc[(df['Data'].dt.year == 2019) & (df['Data'].dt.month == 3)]

print(vendas_marco_19.sample(5))
print(df['mes_venda'].value_counts())

# visualização grafica
df['LojaID'].value_counts().plot.bar()
plt.show()

df['LojaID'].value_counts(ascending=True).plot.barh()
plt.show()

df.groupby(df['Data'].dt.year)['Receita'].sum().plot.pie()
plt.show()

df['Cidade'].value_counts().plot.bar(title='Total vendas por cidades',color='green')
plt.xlabel('Cidade') 
plt.ylabel('Total vendas') 
plt.show()

plt.style.use('ggplot')
df.groupby(df['mes_venda'])['Qtde'].sum().plot(title='Total de produtos por mês')
plt.xlabel('Mês')
plt.ylabel('Total Produtos vendidos')
plt.legend()
plt.show()

# selecionando as vendas de 2019
df_2019 = df[df['Ano_venda'] == 2019]

# Total de produtos vendidos por mes em 2019 
df_2019.groupby(df_2019['mes_venda'])['Qtde'].sum().plot(marker='o')
plt.xlabel('Mês')
plt.ylabel('Total Produtos vendidos') 
plt.legend() 
plt.show()


# histograma 

plt.hist(df['Qtde'],color='magenta') 
plt.show()

# grafico de dispersão   
plt.scatter(x=df_2019['dia_venda'],y=df_2019['Receita'])
plt.savefig('grafico dispersão.jpg')
plt.show() 

