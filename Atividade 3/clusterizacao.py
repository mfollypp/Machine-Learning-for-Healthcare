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
# sum_of_squared_errors_sum = []
# for i in range(1, 11):
#     kmeans = KMeans(n_clusters=i, random_state=42)
#     kmeans.fit(scaled_data)
#     sum_of_squared_errors_sum.append(kmeans.inertia_)
# plt.plot(range(1, 11), sum_of_squared_errors_sum)
# plt.title('Elbow Method')
# plt.xlabel('Number of clusters')
# plt.ylabel('SSEs')
# plt.show()

# Definir o número de clusters (K) - Queremos 2 clusters para poder categorizar os tumores em benignos e malignos "ter um tumor ou não"
k = 2

# Aplicar o KMeans
kmeans = KMeans(n_clusters=k, random_state=42)
kmeans.fit(scaled_data)

pca = PCA(n_components=2)
principal_components = pca.fit_transform(scaled_data)
df_pca = pd.DataFrame(data=principal_components, columns=['PC1', 'PC2'])

df_pca['Cluster'] = kmeans.labels_

# Visualizar os clusters
plt.figure(figsize=(10, 6))
sns.scatterplot(x='PC1', y='PC2', data=df_pca, hue='Cluster') # , hue='Cluster' if you have cluster labels
plt.title('PCA Cluster Plot')
# Adicione os nomes das colunas originais escolhidas como principal component
plt.xlabel(f'PC1 - {round(pca.explained_variance_ratio_[0] * 100, 2)}%')
plt.ylabel(f'PC2 - {round(pca.explained_variance_ratio_[1] * 100, 2)}%')
plt.show()

# Visualizar os clusters
# cluster1_df = df[df['Cluster'] == 0]
# cluster2_df = df[df['Cluster'] == 1]
# plt.scatter(cluster1_df.iloc[:, 0], cluster1_df.iloc[:, 1], c='red', label='Cluster 1')
# plt.scatter(cluster2_df.iloc[:, 0], cluster2_df.iloc[:, 1], c='blue', label='Cluster 2')
# plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c='black', label='Centroids')
# plt.legend()
# plt.show()