import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from kneed import KneeLocator

# Carregar o dataset Breast Cancer Wisconsin
from sklearn.datasets import load_breast_cancer
data = load_breast_cancer()


# Criar um DataFrame com as features (não tem missing values conforme consta no archive.ics.uci.edu)
df = pd.DataFrame(data.data, columns=data.feature_names)


# Explorar o dataset
with open('./markdown/atividade3_df_describe.md', 'w') as md:
    md.write(df.describe().to_markdown())


# Escalar os dados (normalização)
scaler = StandardScaler()
scaled_data = scaler.fit_transform(df)


# Explorar os dados escalados
df_scaled = pd.DataFrame(scaled_data, columns=df.columns)
with open('./markdown/atividade3_df_scaled_describe.md', 'w') as md:
    md.write(df_scaled.describe().to_markdown())


# Calcular o número de K (clusters) ideal com o método Elbow usando a soma dos erros quadrados (SSEs) - O melhor número de clusters é onde parece haver um "cotovelo" no gráfico
sse = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, random_state=42)
    kmeans.fit(scaled_data)
    sse.append(kmeans.inertia_)
plt.plot(range(1, 11), sse)
plt.title('Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('SSEs')
plt.savefig('./images/elbow_method.png')


# Definir o número de clusters (K)
for k in [2, 3, 4]:
    # Limpar o plot anterior
    plt.clf()
    plt.cla()

    # Aplicar o KMeans
    kmeans = KMeans(n_clusters=k, random_state=42, max_iter=1000)
    y_predicted = kmeans.fit_predict(df_scaled)

    # Adicionar a coluna Cluster ao DataFrame
    df_scaled['Cluster'] = y_predicted

    # Plotar os scatter plots dos clusters
    for i in range(k):
        cluster_df = df_scaled[df_scaled['Cluster'] == i]
        plt.scatter(cluster_df.iloc[:, 0], cluster_df.iloc[:, 1], label=f'Cluster {i+1}')
    plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c='black', label='Centroids')
    plt.legend()
    plt.title(f'KMeans Clustering with K={k}')
    plt.savefig(f'./images/{k}_clusters.png')
    plt.clf()
    plt.close()

    df_scaled.drop('Cluster', axis=1, inplace=True)


# Aplicar o KMeans
kmeans = KMeans(n_clusters=2, random_state=42, max_iter=1000)
y_predicted = kmeans.fit_predict(df_scaled)

# Adicionar a coluna Cluster ao DataFrame
df_scaled['Cluster'] = y_predicted

# Criando um DataFrame com as componentes principais
pca = PCA(n_components=2)
principal_components = pca.fit_transform(df_scaled)

# Adicionar as componentes principais ao DataFrame
df_pca = pd.DataFrame(data=principal_components, columns=['PC1', 'PC2'])
df_pca['Cluster'] = y_predicted

# Plotar o scatter plot das componentes principais
plt.clf()
plt.cla()
plt.figure(figsize=(10, 10))
sns.scatterplot(x='PC1', y='PC2', hue='Cluster', data=df_pca, palette=['orange', 'green'])
plt.title('PCA of KMeans Clustering')
plt.savefig('./images/pca.png')
plt.clf()
plt.close()