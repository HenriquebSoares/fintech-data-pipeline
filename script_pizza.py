import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('dados_pizza.csv')

plt.figure(figsize=(8, 8))
plt.pie(
    df['faturamento'],
    labels=df['canal_venda'],
    autopct='%1.1f%%',
    startangle=140,
    colors=sns.color_palette('pastel'),
)
plt.title('Faturamento por Canal de Venda')
plt.tight_layout()
plt.show()