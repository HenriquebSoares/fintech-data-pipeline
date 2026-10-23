import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('dados_regressao.csv')

plt.figure(figsize=(8, 5))
sns.regplot(
    data=df,
    x='renda_mensal',
    y='gasto_mensal',
    color='purple',
    scatter_kws={'alpha': 0.6},
)
plt.title('Regressão Linear: Gasto Mensal vs Renda Mensal')
plt.xlabel('Renda Mensal')
plt.ylabel('Gasto Mensal')
plt.tight_layout()
plt.show()