import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('dados_distribuicao.csv')

plt.figure(figsize=(8, 5))
sns.histplot(df['idade'], kde=True, color='blue', bins=15)
plt.title('Distribuição de Idade dos Clientes')
plt.xlabel('Idade')
plt.ylabel('Frequência')
plt.tight_layout()
plt.show()