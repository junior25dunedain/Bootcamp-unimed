# importando as bibliotecas 
import pandas as pd   
import matplotlib.pyplot as plt 
plt.style.use('seaborn') 

# carregando os dados  
df = pd.read_excel(r'D:\UFCG - ENGENHARIA\Bootcamp_unimed\Primeira analise de dados\datasets\AdventureWorks.xlsx')

# primeiros elementos da base de dados  
print(df.head(10))

# formato do dataframe  
print(df.shape) 

# tipos dos dados de cada coluna
print(df.dtypes) 

# qual o valor da receita total  
print(df['Valor Venda'].sum()) 

# calculando os custos   
df['custo'] = df['Custo Unitário'] * df['Quantidade']
print(df.head())

# qual o custo total
cus_t = df['custo'].sum()
print(f'R$ {cus_t:,.2f}')

# criando a coluna lucro das vendas 
df['Lucro'] = df['Valor Venda'] - df['custo']
print(df.head())

# lucro total    
luc_t = df['Lucro'].sum()
print(f'R$ {luc_t:,.2f}')

# criando coluna com o total de dias para enviar os pedidos 
df['Tempo_envio'] = (df['Data Envio'] - df['Data Venda']).dt.days 

print(df['Tempo_envio'].dtype)

# média de envio dos produtos por marca  
print()
print(df.groupby('Marca')['Tempo_envio'].mean())

# valores missing 
print()
print(df.isnull().sum())

pd.options.display.float_format = '{:20,.2f}'.format

# vamos agrupar por ano e marca 
#print(df.groupby(df['Data Venda'].dt.year,df['Marca'])['Lucro'].sum())

# resetando o index 
lucro_ano = df.groupby([df['Data Venda'].dt.year,'Marca'])['Lucro'].sum().reset_index()
print(lucro_ano)

# qual o total de produtos vendidos? 
print(df.groupby('Produto')['Quantidade'].sum().sort_values(ascending=False)) 

# grafico total de produtos vendidos 
df.groupby('Produto')['Quantidade'].sum().sort_values(ascending=True).plot.barh(title='Total produtos vendidos')
plt.xlabel('Total') 
plt.ylabel('Produto')
plt.show() 

# grafico do lucro por Ano 
df.groupby(df['Data Venda'].dt.year)['Lucro'].sum().plot.bar(title='Lucro x Ano')
plt.xlabel('Ano')
plt.ylabel('Receita')
plt.show() 

# selecionando os dados de  2009 
df_2009 = df[df['Data Venda'].dt.year == 2009]

df_2009.groupby(df_2009['Data Venda'].dt.month)['Lucro'].sum().plot(title='Lucro x Mês')
plt.xlabel('Mês')
plt.ylabel('Lucro') 
plt.show()

df_2009.groupby('Marca')['Lucro'].sum().plot.bar(title='Lucro x Marca')
plt.xlabel('Marca')
plt.ylabel('Lucro') 
plt.xticks(rotation='horizontal')
plt.show()

df_2009.groupby('Classe')['Lucro'].sum().plot.bar(title='Lucro x Classe')
plt.xlabel('Classe')
plt.ylabel('Lucro') 
plt.xticks(rotation='horizontal')
plt.show()

# analise estatistica 
print(df['Tempo_envio'].describe())

# grafico de boxplot
plt.boxplot(df['Tempo_envio'])
plt.show()

# histograma
plt.hist(df['Tempo_envio'])
plt.show()

# tempo maximo e minimo  
print(df['Tempo_envio'].max())
print(df['Tempo_envio'].min())

# identificando o outlier
print(df[df['Tempo_envio'] == 20]) 

df.to_csv('base_dados_novo.csv',index=False)
