import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from scipy import stats

# Carregar o dataset
heart_csv = r'./heart.csv'
data = pd.read_csv(heart_csv)

# Mostrar as primeiras linhas do dataset
# print(data.head())

# Substituir valores zero por NaN para as colunas selecionadas
cols_with_zeros = ['age', 'cp', 'slope']
data[cols_with_zeros] = data[cols_with_zeros].replace(0, np.nan)

# Resumo das estatísticas descritivas
# print(data.describe())

# Iterar sobre as colunas de interesse e verifica se é do tipo numérico
# for column in ['age', 'chol', 'trestbps', 'thalach']:
#     if pd.api.types.is_numeric_dtype(data[column]):

#         plt.figure(figsize=(8, 6))
        
        # sns.histplot(data=data, x=column, hue='target', multiple='stack', bins=25, palette={0: 'blue', 1: 'red'}, alpha=0.6, edgecolor='black')
        # plt.title(f'Histograma de {column}')
        # plt.xlabel(column)
        # plt.ylabel('Frequência')
        # plt.legend(title='Heart Disease', labels=['Negativo', 'Positivo'])
        # plt.show()

        # sns.boxplot(data=data, x='target', y=column)
        # plt.title(f'Boxplot de {column}')
        # plt.xlabel('Heart Disease')
        # plt.ylabel(column)
        # plt.show()

        # Grafico de dispersão de trestbps e thalach
        # sns.scatterplot(data=data, x='trestbps', y='thalach', hue='target', palette={0: 'blue', 1: 'red'})
        # plt.title('Gráfico de Dispersão de trestbps e thalach')
        # plt.xlabel('trestbps')
        # plt.ylabel('thalach')
        # plt.show()

# Gráfico de dispersão de todas as variáveis
# sns.pairplot(data, hue='target', palette={0: 'blue', 1: 'red'})
# plt.title('Gráfico de Dispersão de Todas as Variáveis')
# plt.show()




# Preparar os dados para o modelo
X = data[['age', 'trestbps']].dropna() # Com Age e Trestbps: Intercept = 3.96587 / 98.15% de probabilidade
y = data.loc[X.index, 'target']

# Ajustar o modelo de regressão logística
model = LogisticRegression()
model.fit(X, y)

# Resumo dos coeficientes
coef = pd.DataFrame(model.coef_, columns=X.columns)
coef['Intercept'] = model.intercept_ # Valores negativos do intercepto levam a probabilidades baixas e valores positivos a probabilidades altas
print(coef)

# Odds Ratio
odds_ratios = np.exp(model.coef_[0])
print('Odds Ratios:')
for feature, ratio in zip(X.columns, odds_ratios):
    print(f'{feature}: {ratio:.4f}')

# Remover linhas com NaNs nas colunas de interesse
cleaned_data = data[['age', 'trestbps']].dropna()

# Calcular a correlação de Pearson: 1 = correlação perfeita, -1 = correlação negativa perfeita, 0 = sem correlação
correlation, p_value = stats.pearsonr(cleaned_data['age'], cleaned_data['trestbps'])
print(f'Coeficiente de Correlação: {correlation:.4f}, p-valor: {p_value:.4f}')