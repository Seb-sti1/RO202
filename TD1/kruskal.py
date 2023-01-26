import numpy as np
import graph
import sys

def main():
    print("Executer krustal pour :")
    print("1) le graphe de l'ex 1")
    print("2) le graphe de gauche de la fig 1")
    print("3) le graphe de droite de la fig 1")

    n = int(input())

    reverse = input("Poids minimum ? (Y/n)") != 'Y'

    if n == 1:
        g = graph_ex1()
    elif n == 2:
        g = graph_fig1_a()
    elif n == 3:
        g = graph_fig1_b()


    # Obtenir un arbre couvrant de poids minimal du graphe
    tree = kruskal(g, reverse)
    
    # S'il existe un tel arbre (i.e., si le graphe est connexe)
    if tree != None:
        
        # L'afficher
        print(tree)
    
    else:
        print("Pas d'arbre couvrant")


def graph_ex1():
    
    # Créer un graphe contenant les sommets a, b, c, d, e, f, g 
    g = graph.Graph(np.array(["a", "b", "c", "d", "e", "f", "g"]))

    # Ajouter les arêtes
    g.addEdge("a", "b",  1.0)
    g.addEdge("a", "c",  3.0)
    g.addEdge("b", "c",  2.0)
    g.addEdge("b", "d",  5.0)
    g.addEdge("b", "e",  7.0)
    g.addEdge("b", "f",  9.0)
    g.addEdge("c", "d",  4.0)
    g.addEdge("d", "e",  6.0)
    g.addEdge("d", "g", 12.0)
    g.addEdge("e", "f",  8.0)
    g.addEdge("e", "g", 11.0)
    g.addEdge("f", "g", 10.0)

    return g
    

def graph_fig1_a():
    
    # Créer un graphe contenant les sommets a, b, c, d, e, f, g, h
    g = graph.Graph(np.array(["a", "b", "c", "d", "e", "f", "g", "h"]))

    # Ajouter les arêtes
    g.addEdge("a", "b",  9.0)
    g.addEdge("a", "f",  6.0)
    g.addEdge("a", "h",  9.0)

    g.addEdge("b", "c",  5.0)
    g.addEdge("b", "d",  5.0)
    g.addEdge("b", "e",  8.0)

    g.addEdge("c", "d",  2.0)
    g.addEdge("c", "g",  5.0)
    
    g.addEdge("d", "h",  7.0)
    g.addEdge("d", "g", 8.0)

    g.addEdge("e", "f",  1.0)
    g.addEdge("e", "g", 3.0)

    g.addEdge("g", "h", 5.0)
    
    return g


def graph_fig1_b():
    
    # Créer un graphe contenant les sommets a, b, c, d, e, f, g, h
    g = graph.Graph(np.array(["a", "b", "c", "d", "e", "f"]))

    # Ajouter les arêtes
    g.addEdge("a", "b",  4.0)
    g.addEdge("a", "c",  3.0)

    g.addEdge("b", "c",  5.0)
    g.addEdge("b", "f",  2.0)

    g.addEdge("c", "f",  5.0)
    g.addEdge("c", "d",  2.0)
    
    g.addEdge("d", "f",  3.0)
    g.addEdge("d", "e", 4.0)

    g.addEdge("e", "f",  3.0)

    return g


# Applique l'algorithme de Kruskal pour trouver un arbre couvrant de poids minimal d'un graphe
# Retourne: Un arbre couvrant de poids minimal du graphe ou None s'il n'en existe pas
def kruskal(g, reverse=False):
    
    # Créer un nouveau graphe contenant les mêmes sommets que g
    tree = graph.Graph(g.nodes)

    # Nombre d'arêtes dans l'arbre
    addedEdges = 0
    
    # Récupérer toutes les arêtes de g
    edges = g.getEdges()
    
    # Trier les arêtes par poids croissant
    edges.sort(reverse=reverse)

    i = 0
    while addedEdges < len(g.nodes) - 1:

        if not tree.createACycle(edges[i]):
            tree.addCopyOfEdge(edges[i])
            addedEdges += 1
        
        i += 1

    return tree


if __name__ == '__main__':
    main()
