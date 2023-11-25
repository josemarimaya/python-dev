import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from collections import Counter

# Carga el conjunto de datos
movies_df = pd.read_csv('lowest_ranked_movies_data.csv')

# Crea un grafo dirigido
G = nx.Graph()

G2 = nx.Graph()

def define_atrib(datos):
    keys = []
    values = []
    for index, row in datos.iterrows():
        # Campos a analizar
        movie_title = row['name']
        keys.append(movie_title)
        genres = row['genre'].split('|')
        values.append(genres)
        #actors = row['stars'].split('|')
    diccionario = dict(zip(keys, values))
    return diccionario

#print(define_atrib(movies_df))

def grafo_relacion(diccionario):
    grafo = nx.Graph()
    for key in diccionario:
        #print(key)
        # Si no tenemos el nodo lo creeamos
        if not grafo.has_node(key): 
            grafo.add_node(key)
        generos = diccionario[key]
        for key_2 in diccionario:
            #print(key_2)
            if not grafo.has_node(key_2): 
                grafo.add_node(key_2)
            generos_peli2 = diccionario[key_2]
            if key != key_2 : # Si no es lo mismo
                for genero in generos:
                    if genero in generos_peli2:
                        grafo.add_edge(key, key_2,  label='comparten: '+genero) # Añadimos la arista
    
    return grafo

def visualiza(grafo):
    pos = nx.spring_layout(grafo)
    nx.draw(grafo, pos, with_labels=True, font_size=6, node_size=10, node_color='skyblue', font_color='black', font_weight='bold', edge_color='gray', linewidths=0.1)
    plt.show()   

diccionario = define_atrib(movies_df) 
gr = grafo_relacion(diccionario)
visualiza(gr)
#print(list(nx.enumerate_all_cliques(gr)))
print(nx.make_max_clique_graph(gr))

def elimina_sin_relacion(grafo):
    g2 = nx.DiGraph()
    for nodo, grado in grafo.degree:
        if grado == 0:
            g2.add_node(nodo)
    return g2

#gr2 = elimina_sin_relacion(gr)
#visualiza(gr2)

# Calcularemos las comunidades

communities = nx.community.greedy_modularity_communities(gr)

print(enumerate(communities))
# Usamos el algoritmo de greedy coloring

def greedy_color(c, tam_comunidad):
    colors = {}
    for i, comm in enumerate(c):
        if len(comm) > tam_comunidad: # Filtramos por aquellas comunidades que no son un nodo únicamente
            print(f"Comunidad {i + 1}: {list(comm)}")
            for node in comm:
                colors[node] = i
    return colors

color_communities = greedy_color(communities, 1)
#print(color_communities)
comunidades_mayores = greedy_color(communities,2)

def dic_comunidades(c, tam_comunidades):
    comunidades = {}
    for i , comm in enumerate(c):
        if len(comm) > tam_comunidades:
            comunidades[i] = list(comm)
    return comunidades

print(dic_comunidades(communities, 2))

    
def visualiza_barras(cc):
    # Obtiene las comunidades y sus tamaños
    communities = Counter(cc.values())
    print(communities)
    # Muestra una representación en barras
    plt.bar(communities.keys(), communities.values())
    plt.xlabel('Comunidad')
    plt.ylabel('Número de nodos')
    plt.title('Distribución de nodos en comunidades')
    plt.show()

#visualiza_barras(color_communities)

# Agrega nodos y aristas al grafo
for index, row in movies_df.iterrows():
    movie_title = row['name']
    #print(movie_title)
    genres = row['genre'].split('|')
    #print(genres)
    actors = row['stars'].split('|')

    # Agrega nodo de película
    G.add_node(movie_title, node_type='movie')

    # Agrega nodos de género y aristas entre película y género
    for genre in genres:
        G.add_node(genre, node_type='genre')
        G.add_edge(movie_title, genre, relationship='belongs_to_genre')

    # Agrega nodos de actor y aristas entre película y actor
    for actor in actors:
        G.add_node(actor, node_type='actor')
        G.add_edge(movie_title, actor, relationship='has_actor')

# Visualiza el grafo
#pos = nx.spring_layout(G)
#nx.draw(G, pos, with_labels=True, font_size=6, node_size=10, node_color='skyblue', font_color='black', font_weight='bold', edge_color='gray', linewidths=0.1)
#plt.show()

grafo = G

vertices = []
grados = []
for x,y in grafo.degree:
    vertices.append(x)
    grados.append(y)

#print(grafo.degree)
clusters_g = nx.clustering(grafo)
#print("clustering_local", clusters_g)
