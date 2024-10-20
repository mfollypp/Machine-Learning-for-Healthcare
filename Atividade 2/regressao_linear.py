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

# Carregando as tabelas usando pandas
demographic = pd.read_sas(demo)
body_measure = pd.read_sas(bmi)
blood_pressure = pd.read_sas(bp)

# Merge das tabelas utilizando o atributo 'SEQN' como chave
df = pd.merge(demographic[['SEQN', 'RIDAGEYR']], body_measure[['SEQN', 'BMXBMI']], on='SEQN')
df = pd.merge(df, blood_pressure[['SEQN', 'BPXSY1']], on='SEQN')

# Filtrando os dados para incluir apenas indivíduos entre 20 e 60 anos
df = df[(df['RIDAGEYR'] >= 20) & (df['RIDAGEYR'] <= 60)]

# Remover dados faltantes
df = df.dropna(subset=['BMXBMI', 'BPXSY1'])

# Filtrar apenas as colunas de interesse RIDAGEYR, BMXBMI e BPXSY1
df = df[['RIDAGEYR', 'BMXBMI', 'BPXSY1']]

# Análise descritiva dos dados
with open('./markdown/analise_descritiva.md', 'w') as file:
    file.write(df.describe().to_markdown())

# Visualizar a relação entre IMC e PAS
plt.figure(figsize=(8,6))
sns.scatterplot(x='BMXBMI', y='BPXSY1', data=df)
plt.title('Relação entre IMC e Pressão Arterial Sistólica (PAS)')
plt.xlabel('Índice de Massa Corporal (IMC)')
plt.ylabel('Pressão Arterial Sistólica (PAS)')
plt.savefig('./images/scatterplot_BMI_PAS.png')

# Definir as variáveis dependente (X) e independente (y)
X = df[['BMXBMI']]
y = df['BPXSY1']

# Criar e treinar o modelo de regressão linear
model = LinearRegression()
model.fit(X, y)

# Fazer predições
y_pred = model.predict(X)

# Avaliar o modelo
mse = mean_squared_error(y, y_pred)
r2 = r2_score(y, y_pred)
coef = model.coef_[0]

# Salvar os coeficientes do modelo em um arquivo markdown
markdown_content = """
| Métrica                        | Valor   |
|-------------------------------|---------|
| Erro quadrático médio (MSE)   | {:.2f}  |
| Coeficiente da regressão      | {:.2f} |
| Coeficiente de determinação (R²) | {:.2f}  |
""".format(mse, coef, r2)

# Escrever o conteúdo no arquivo markdown
with open('./markdown/coeficientes_modelo.md', 'w', encoding='utf-8') as file:
    file.write(markdown_content)
