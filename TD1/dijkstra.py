import graph
import sys

def main():
    print("Executer Dijkstra pour :")
    print("1) le graphe de l'ex 2")
    print("2) le graphe de gauche de la fig 2")
    print("3) le graphe de droite de la fig 2")

    n = int(input())

    if n == 1:
        g, origin = graph_ex2()
    elif n == 2:
        g, origin = graph_fig2_a()
    elif n == 3:
        g, origin = graph_fig2_b()

    # Applique l'algorithme de Dijkstra pour obtenir une arborescence
    tree = dijkstra(g, origin)
    print(tree)


def graph_ex2():
    cities = []
    cities.append("Paris")
    cities.append("Hambourg")
    cities.append("Londres")
    cities.append("Amsterdam")
    cities.append("Edimbourg")
    cities.append("Berlin")
    cities.append("Stockholm")
    cities.append("Rana")
    cities.append("Oslo")

    g = graph.Graph(cities)
    
    g.addArc("Paris", "Hambourg", 7)
    g.addArc("Paris",  "Londres", 4)
    g.addArc("Paris",  "Amsterdam", 3)
    g.addArc("Hambourg",  "Stockholm", 1)
    g.addArc("Hambourg",  "Berlin", 1)
    g.addArc("Londres",  "Edimbourg", 2)
    g.addArc("Amsterdam",  "Hambourg", 2)
    g.addArc("Amsterdam",  "Oslo", 8)
    g.addArc("Stockholm",  "Oslo", 2)
    g.addArc("Stockholm",  "Rana", 5)
    g.addArc("Berlin",  "Amsterdam", 2)
    g.addArc("Berlin",  "Stockholm", 1)
    g.addArc("Berlin",  "Oslo", 3)
    g.addArc("Edimbourg",  "Oslo", 7)
    g.addArc("Edimbourg",  "Amsterdam", 3)
    g.addArc("Edimbourg",  "Rana", 6)
    g.addArc("Oslo",  "Rana", 2)

    return g, "Paris"

def graph_fig2_a():
    nodes = []
    nodes.append("a")
    nodes.append("b")
    nodes.append("c")
    nodes.append("d")
    nodes.append("e")
    nodes.append("f")
    nodes.append("g")
    nodes.append("r")

    g = graph.Graph(nodes)
    
    g.addArc("r", "a", 5)
    g.addArc("r",  "b", 4)
    g.addArc("a", "c", 3)
    g.addArc("b",  "a", 5)
    g.addArc("b",  "c", 3)
    g.addArc("b",  "c", 9)
    g.addArc("c",  "d", 2)
    g.addArc("c",  "f", 6)
    g.addArc("c",  "g", 8)
    g.addArc("d",  "a", 8)
    g.addArc("d",  "e", 2)
    g.addArc("e",  "c", 4)
    g.addArc("g",  "f", 5)

    return g, "r"


def graph_fig2_b():
    cities = []
    cities.append("A")
    cities.append("B")
    cities.append("C")
    cities.append("D")
    cities.append("E")
    cities.append("F")
    cities.append("G")
    cities.append("r")

    g = graph.Graph(cities)
    
    g.addArc("r", "A", 2)
    g.addArc("r",  "G", 3)
    g.addArc("A",  "B", 3)
    g.addArc("A",  "F", 1)
    g.addArc("B",  "C", 2)
    g.addArc("D",  "C", 2)
    g.addArc("E",  "D", 3)
    g.addArc("E",  "F", 2)
    g.addArc("F",  "D", 4)
    g.addArc("F",  "G", 3)
    g.addArc("G",  "E", 2)

    return g, "r"
    


def argmin(L, v2):
    cand = None

    for i in range(len(L)):
        if i not in v2 and (cand == None or L[cand] > L[i]):
            cand = i
    
    return cand


def dijkstra(g, origin):	
    # Get the index of the origin 
    r = g.indexOf(origin)

    # Next node considered 
    pivot = r

    # Liste qui contiendra les sommets ayant été considérés comme pivot
    v2 = []
    v2.append(r)

    pred = [0] * g.n

    # Les distances entre r et les autres sommets sont initialement infinies
    pi = [sys.float_info.max] * g.n
    pi[r] = 0

    for j in range(1, g.n):
        for y in [e.id2 for e in g.getArcs() if e.id1 == pivot]:
            if pi[pivot] + g.adjacency[pivot][y] < pi[y]:
                pi[y] = pi[pivot] + g.adjacency[pivot][y]
                pred[y] = pivot

        pivot = argmin(pi, v2)
        v2.append(pivot)

    final = graph.Graph(g.nodes)

    for i in range(len(pi)):
        if g.adjacency[pred[i]][i] < sys.float_info.max:
            final.addArc(g.nodes[pred[i]], g.nodes[i], g.adjacency[pred[i]][i])

    return final

   
if __name__ == '__main__':
    main()
