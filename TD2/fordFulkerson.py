import numpy as np
import graph
import sys

def main():

    # Le poids des arcs de ce graphe correspondent aux capacités
    g = example()

    # Le poids des arcs de ce graphe correspondent au flot
    flow = fordFulkerson(g, "s", "t")

    print(flow)
    
# Fonction créant un graphe sur lequel sera appliqué l'algorithme de Ford-Fulkerson
def example():
        
    g = graph.Graph(np.array(["s", "a", "b", "c", "d", "e", "t"]))

    g.addArc("s", "a", 8)
    g.addArc("s", "c", 4)
    g.addArc("s", "e", 6)
    g.addArc("a", "b", 10)
    g.addArc("a", "d", 4)
    g.addArc("b", "t", 8)
    g.addArc("c", "b", 2)
    g.addArc("c", "d", 1)
    g.addArc("d", "t", 6)
    g.addArc("e", "b", 4)
    g.addArc("e", "t", 2)
    
    return g

# Fonction appliquant l'algorithme de Ford-Fulkerson à un graphe
# Les noms des sommets sources est puits sont fournis en entrée
def fordFulkerson(g, sName, tName):

    """
    Marquage des sommets du graphe:
     - mark[i] est égal à +j si le sommet d'indice i peut être atteint en augmentant le flot sur l'arc ji
     - mark[i] est égal à -j si le sommet d'indice i peut être atteint en diminuant le flot de l'arc ji
     - mark[i] est égal à sys.float_info.max si le sommet n'est pas marqué
    """
    mark = [0] * g.n
    
    # Récupérer l'indice de la source et du puits
    s = g.indexOf(sName)
    t = g.indexOf(tName)
    
    # Créer un nouveau graphe contenant les même sommets que g
    flow = graph.Graph(g.nodes)

    # Récupérer tous les arcs du graphe 
    arcs = g.getArcs()

    while mark[t] != sys.float_info.max:
        mark = [sys.float_info.max] * g.n # Retirer toutes les marques
        mark[s] = 0 # Marquer '+' le sommet s

        new_mark = True

        while new_mark and mark[t] == sys.float_info.max:
            new_mark = False
            
            for arc in arcs:
                # si i marqué, j non marqué, (ij) non saturé
                if mark[arc.id1] != sys.float_info.max \
                    and mark[arc.id2] == sys.float_info.max \
                    and flow.adjacency[arc.id1][arc.id2] < arc.weight:
                    mark[arc.id2] = arc.id1
                    new_mark = True
                
                # si i non marqué, j est marqué, (ij) flux non nul
                if mark[arc.id1] == sys.float_info.max \
                    and mark[arc.id2] != sys.float_info.max \
                    and flow.adjacency[arc.id1][arc.id2] > 0:
                    mark[arc.id1] = -arc.id2
                    new_mark = True

        if mark[t] != sys.float_info.max:
            m = 100_000

            current = t
            while current != s and current != sys.float_info.max:
                new = abs(mark[current])

                if mark[current] >= 0:
                    m = min(m, g.adjacency[new][current] - flow.adjacency[new][current])
                else:
                    m = min(m, flow.adjacency[current][new])

                current = new

            if m == 0:
                break

            current = t
            while current != s and current != sys.float_info.max:
                new = abs(mark[current])
                if mark[current] >= 0:
                    flow.adjacency[new][current] += m
                else:
                    flow.adjacency[current][new] -= m

                current = new
            
    
    return flow
   
if __name__ == '__main__':
    main()
