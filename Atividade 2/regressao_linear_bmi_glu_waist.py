import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score # Parameter 'squared' is deprecated


# URLs das tabelas
# demo = 'https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/DEMO_I.XPT'
# bmi = 'https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/BMX_I.XPT'
# bp = 'https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/BPX_I.XPT'
# glu = 'https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/GLU_I.XPT'

# Paths das tabelas
demo = './XPTs/DEMO_I.XPT'
bmi = './XPTs/BMX_I.XPT'
bp = './XPTs/BPX_I.XPT'
glu = './XPTs/GLU_I.XPT'

# Carregando as tabelas usando pandas
demographic = pd.read_sas(demo)
body_measure = pd.read_sas(bmi)
blood_pressure = pd.read_sas(bp)
glucose = pd.read_sas(glu)

# Merge das tabelas utilizando o atributo 'SEQN' como chave
df = pd.merge(demographic[['SEQN', 'RIDAGEYR']], body_measure[['SEQN', 'BMXBMI', 'BMXWAIST']], on='SEQN')
df = pd.merge(df, blood_pressure[['SEQN', 'BPXSY1']], on='SEQN')
df = pd.merge(df, glucose[['SEQN', 'LBXGLU']], on='SEQN')

# Filtrando os dados para incluir apenas indivíduos entre 20 e 60 anos
df = df[(df['RIDAGEYR'] >= 20) & (df['RIDAGEYR'] <= 60)]

# Remover dados faltantes
df = df.dropna(subset=['BMXBMI', 'BPXSY1', 'LBXGLU', 'BMXWAIST'])

# Filtrar apenas as colunas de interesse RIDAGEYR, BMXBMI e BPXSY1
df = df[['RIDAGEYR', 'BMXBMI', 'BPXSY1', 'LBXGLU', 'BMXWAIST']]

# Análise descritiva dos dados
with open('./markdown/analise_descritiva_bmi_glu_waist.md', 'w') as file:
    file.write(df.describe().to_markdown())

# Visualizar a relação entre IMC e PAS
plt.figure(figsize=(8,6))
sns.scatterplot(x='BMXBMI', y='LBXGLU', data=df)
plt.title('Relação entre IMC e Glicose')
plt.xlabel('Índice de Massa Corporal (IMC)')
plt.ylabel('Glicose Sanguínea')
plt.savefig('./images/scatterplot_BMI_GLU.png')

plt.figure(figsize=(8,6))
sns.scatterplot(x='BMXBMI', y='BMXWAIST', data=df)
plt.title('Relação entre IMC e Circunferência da Cintura')
plt.xlabel('Índice de Massa Corporal (IMC)')
plt.ylabel('Circunferência da Cintura')
plt.savefig('./images/scatterplot_BMI_WAIST.png')

# Definir as variáveis dependente (X) e independente (y)
columns = ['LBXGLU', 'BMXWAIST']
markdown_content = ""

for column in columns:
    X = df[['BMXBMI']]
    y = df[column]

    # Criar e treinar o modelo de regressão linear
    model = LinearRegression()
    model.fit(X, y)

    # Fazer predições
    y_pred = model.predict(X)

    # Avaliar o modelo
    mse = mean_squared_error(y, y_pred)
    r2 = r2_score(y, y_pred)
    coef = model.coef_[0]

    # Adicionar os coeficientes do modelo ao conteúdo markdown
    markdown_content += """
### BMXBMI x {}
| Métrica                        | Valor   |
|-------------------------------|---------|
| Erro quadrático médio (MSE)   | {:.2f}  |
| Coeficiente da regressão      | {:.2f} |
| Coeficiente de determinação (R²) | {:.2f}  |
    """.format(column, mse, coef, r2)

# Escrever o conteúdo no arquivo markdown
with open('./markdown/coeficientes_modelo_bmi_glu_waist.md', 'w', encoding='utf-8') as file:
    file.write(markdown_content)

# Verificar qual a estimativa de BMXWAIST para um IMC específico
imc = 25
waist_pred = model.predict([[imc]])[0]
print(f"Para um IMC de {imc}, a circunferência da cintura estimada é {waist_pred:.2f} cm.")