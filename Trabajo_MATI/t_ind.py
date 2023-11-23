import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

df = pd.read_csv('lowest_ranked_movies_data.csv')

print(df.head())

import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Cargar el conjunto de datos
movies_df = pd.read_csv("lowest_ranked_movies_data.csv")

# Seleccionar campos relevantes para clustering
selected_fields = ["duration", "rating", "review_count", "year"]

# Filtrar el DataFrame para las columnas seleccionadas

print(movies_df["duration"])
selected_data = movies_df[selected_fields]

print(selected_data)

# Manejar valores nulos (llenar con la media, por ejemplo)
#selected_data = selected_data.fillna(selected_data.mean().astype(int))

# Normalizar los datos para que todas las características tengan la misma escala
scaler = StandardScaler()
normalized_data = scaler.fit_transform(selected_data)

# Aplicar el algoritmo de clustering (K-Means con 5 clusters, por ejemplo)
kmeans = KMeans(n_clusters=5, random_state=42)
movies_df["cluster"] = kmeans.fit_predict(normalized_data)

# Visualización de los clusters
plt.scatter(normalized_data[:, 0], normalized_data[:, 1], c=movies_df["cluster"], cmap="viridis", s=50)
plt.title("Clustering de Películas")
plt.xlabel("Duración Normalizada")
plt.ylabel("Calificación Normalizada")
plt.show()

