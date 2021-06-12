import networkx as nx
import matplotlib.pyplot as plt
import numpy
import math
from numpy.core.fromnumeric import sort 

def find_secondary_structure(rna : list):
    def is_complimentary(i,j): 
        s = set([rna[i-1], rna[j-1]])
        return s == set(["A", "U"]) or s == set(["C", "G"])

    n = len(rna) + 1
    M = numpy.zeros((n,n))
    pairs = []

    for t in range(5, n-1):
        for i in range(1, n - t): 
            j = i + t
            if is_complimentary(i,j): 
                M[i,j] = max(M[i,j-1], 1 + M[i, t-1] + M[t+1, j-1])
                pairs.append((i,j))
            else: 
                M[i,j] = M[i,j-1]

    def sort_by_len(item): 
        i,j = item
        return max(i,j) - min(i,j)
    pairs.sort(key = sort_by_len, reverse = True)

    resultPairs = []
    limI,limJ = 0,n
    for i,j in pairs:
        if i <= limI or j >= limJ: continue 
        resultPairs.append((i,j))
        limI, limJ = i, j

    print(M[1:n//2, n//2:])
    return round(M[1, n-1]), resultPairs

def rotate(input,d): return input[d:] + input[:d]

rnaList = [
    rotate("ACCGGUAGU", 0),
    rotate("ACAUGAUGGCCAUGU", 0),
    rotate("UCGUAACGAUACGAGCAUAGCGGCUA", 0)
]

for rna in rnaList: 
    n = len(rna)
    print(f"Input RNA string {rna} of length {len(rna)}")
    pairsCount, resultPairs = find_secondary_structure(rna)
    print(f"Has secondary structure of {pairsCount} pairs: ")
    print(f"\t{resultPairs} (len {len(resultPairs)})\n")

    G = nx.Graph()
    G.add_nodes_from([(i+1) for i in range(len(rna))])
    for node in G.nodes():
        G.nodes()[node]["pos"] = (node,node * node * node)
    for i in range(1, n): 
        G.add_edge(i, i+1)
    for i,j in resultPairs: 
        G.add_edge(i,j)
    pos = nx.get_node_attributes(G, "pos")

    labels = dict([(i+1,rna[i]) for i in range(n)])

    plt.figure(figsize=(8, 8))
    plt.axis("off")
    nx.draw(G, labels = labels, with_labels = True, pos = pos)
    plt.show()