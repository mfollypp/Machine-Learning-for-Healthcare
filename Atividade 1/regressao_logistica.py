import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from scipy import stats
import argparse
import statsmodels.api as sm



# Carregar o dataset
heart_csv = r'./heart.csv'
data = pd.read_csv(heart_csv)


# Substituir valores zero por NaN para as colunas selecionadas
cols_with_zeros = ['age', 'cp', 'slope']
data[cols_with_zeros] = data[cols_with_zeros].replace(0, np.nan)


# Resumo das estatísticas descritivas
df = data.describe()
with open('./atividade1_estatisticas_descritivas.md', 'w') as md:
    # Escrever o resumo das estatísticas descritivas no arquivo markdown na linha 5
    md.write(df.to_markdown())
print(df)


# Checa se é necessário gerar as imagens ou não
parser = argparse.ArgumentParser(description='Process some flags.')
parser.add_argument('-g', '--generate-images', action='store_true', help='Generate images')
args = parser.parse_args()
generate_images = args.generate_images


# Iterar sobre as colunas de interesse e verifica se é do tipo numérico
if generate_images:
    for column in ['age', 'chol', 'trestbps', 'thalach']:
        if pd.api.types.is_numeric_dtype(data[column]):

            plt.figure(figsize=(8, 6))
            
            sns.histplot(data=data, x=column, hue='target', multiple='stack', bins=25, palette={1: 'red', 0: 'blue'}, alpha=0.6, edgecolor='black')
            plt.title(f'Histograma de {column}')
            plt.xlabel(column)
            plt.ylabel('Frequência')
            plt.legend(title='Heart Disease', labels=['Positivo', 'Negativo'])
            plt.savefig(f'./images/histograms/histogram_{column}.png')

            sns.boxplot(data=data, x='target', y=column)
            plt.title(f'Boxplot de {column}')
            plt.xlabel('Heart Disease')
            plt.ylabel(column)
            # Clear plt legend from previous plot
            plt.legend([], [], frameon=False)
            plt.savefig(f'./images/boxplots/boxplot_{column}.png')

    # Gráfico de dispersão de todas as variáveis
    sns.pairplot(data, hue='target', palette={0: 'blue', 1: 'red'})
    plt.title('Gráfico de Dispersão de Todas as Variáveis')
    plt.savefig('./images/pairplot.png')


columns = ['age', 'chol', 'thalach']
correlation_results = ''

for i, column in enumerate(columns):
    for column2 in columns[i+1:]:

        # Remover linhas com NaNs nas colunas de interesse
        cleaned_data = data[[column, column2]].dropna()

        # Calcular a correlação de Pearson: 1 = correlação perfeita, -1 = correlação negativa perfeita, 0 = sem correlação
        correlation, p_value = stats.pearsonr(cleaned_data[column], cleaned_data[column2])
        
        # Append dos resultados de correlações
        correlation_results += f'### `{column}` x `{column2}`\n| Coef. Correlacao | P-Valor | \n | --- | --- | \n | {correlation:.4f} | {p_value:.4f} |\n\n'

with open('./atividade1_correlacoes.md', 'w') as md:
    md.write(correlation_results)


# Preparar os dados para o modelo (Com Age e Trestbps: Intercept = 3.96587 / 98.15% de probabilidade)
X = data[['age', 'sex', 'cp', 'chol', 'thalach', 'ca']].dropna()
y = data.loc[X.index, 'target']

# Ajustar o modelo de regressão logística
model = LogisticRegression(max_iter=1000)
model.fit(X, y)

# Resumo dos coeficientes: Valores negativos do intercepto levam a probabilidades baixas e valores positivos a probabilidades altas
coef = pd.DataFrame(model.coef_, columns=X.columns)
coef['Intercept'] = model.intercept_

# Transformar os coeficientes em uma string no formato de uma tabela markdown
coef_md = coef.to_markdown()

# Escrever a tabela markdown em um arquivo
with open('./atividade1_coeficientes.md', 'w') as md:
    md.write(f'### Coeficientes do Modelo:\n{coef_md}')


# Adicionar uma constante para o intercepto
X_const = sm.add_constant(X)

# Ajustar o modelo de regressão logística usando statsmodels
model = sm.Logit(y, X_const)
result = model.fit()


# Obter o AIC: Quanto menor o AIC, melhor o modelo
with open('./atividade1_coeficientes.md', 'a') as md:
    md.write(f'\n\n### AIC do modelo:\n{result.aic}')


# Odds Ratio
odds_ratios = np.exp(result.params)
odds_ratios_df = pd.DataFrame(odds_ratios, columns=['Odds Ratio'])
odds_ratios_md = odds_ratios_df.to_markdown()

# Append the Odds Ratios table to the markdown file
with open('./atividade1_coeficientes.md', 'a') as md:
    md.write(f'\n\n### Odds Ratio:\n{odds_ratios_md}')