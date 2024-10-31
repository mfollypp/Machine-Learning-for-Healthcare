import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar o dataset Breast Cancer Wisconsin
from sklearn.datasets import load_breast_cancer
data = load_breast_cancer()

# Criar um DataFrame com as features
df = pd.DataFrame(data.data, columns=data.feature_names)
df['target'] = data.target

# Verificar se há valores nulos
if df.isnull().sum().sum() != 0:
    print('Found null values in the dataset')

# Explorar o dataset
print(df.describe())

# Escalar os dados (normalização)
scaler = StandardScaler()
df.drop('target', axis=1, inplace=True)
scaled_data = scaler.fit_transform(df)

# Pairplot para visualizar a distribuição dos dados
# df['target'] = data.target
# sns.pairplot(df, diag_kind='kde', hue='target') # preciso ajeitar a quantidade de colunas para visualizar, como tem 30 colunas, ele vai gerar 900 gráficos
# plt.show()

# Calcular o número de K (clusters) ideal com o método Elbow usando a soma dos erros quadrados (SSEs) - O melhor número de clusters é onde parece haver um "cotovelo" no gráfico
sum_of_squared_errors_sum = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, random_state=42)
    kmeans.fit(scaled_data)
    sum_of_squared_errors_sum.append(kmeans.inertia_)
plt.plot(range(1, 11), sum_of_squared_errors_sum)
plt.title('Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('SSEs')
plt.show()

# Definir o número de clusters (K) - Queremos 2 clusters para poder categorizar os tumores em benignos e malignos "ter um tumor ou não"
k = 2

# Aplicar o KMeans
kmeans = KMeans(n_clusters=k, random_state=42)
kmeans.fit(scaled_data)

