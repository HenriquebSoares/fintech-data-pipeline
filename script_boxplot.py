import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('dados_boxplot.csv')

plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x='departamento', y='salario', palette='Set3')
plt.title('Distribuição de Salários por Departamento')
plt.xlabel('Departamento')
plt.ylabel('Salário')
plt.tight_layout()
plt.show()