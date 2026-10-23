import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('dados_linhas.csv')
df['data'] = pd.to_datetime(df['data'])
df = df.sort_values('data')

plt.figure(figsize=(12, 6))
sns.lineplot(data=df, x='data', y='vendas', hue='loja', marker='o')
plt.title('Evolução das Vendas ao Longo do Tempo por Loja')
plt.xlabel('Data')
plt.ylabel('Vendas')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()