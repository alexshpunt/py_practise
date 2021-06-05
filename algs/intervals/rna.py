import networkx as nx
import matplotlib.pyplot as plt

def find_secondary_structure(rna : list):
    def is_complimentary(i,j): 
        s = set([rna[i-1], rna[j-1]])
        return s == set(["A", "U"]) or s == set(["C", "G"])

    M = {}
    pairs = {}
    def OPT(i,j):
        if i > j - 4: return 0
        p = (i,j)
        if p in M.keys(): return M[p]
    
        r = OPT(i,j-1)
        if is_complimentary(i,j): 
            for t in range(i, j): 
                newr = max(r, 1 + OPT(i, t - 1) + OPT(t+1, j-1))
                if newr > r or pairs.get(i) < j:
                    r = newr 
                    pairs[i] = j
        M[p] = r
        return r 
    
    r = OPT(1,len(rna))
    def bykey(item): 
        i,j = item
        return i
    pairs = sorted(pairs.items(), key = bykey)
    return r, pairs[:r]

def rotate(input,d): return input[d:] + input[:d]

rnaList = [
    rotate("ACCGGUAGU", 0),
    rotate("ACAUGAUGGCCAUGU", 0),
    rotate("CAGAUCGGCGAUACGAGCAUAGCAAUGC", 0)
]

for rna in rnaList: 
    n = len(rna)
    print(rna, len(rna))
    r, pairs = find_secondary_structure(rna)
    print(r,pairs)

    G = nx.Graph()
    G.add_nodes_from([(i+1) for i in range(len(rna))])
    for node in G.nodes():
        G.nodes()[node]["pos"] = (node,node * node * node)
    for i in range(1, n): 
        G.add_edge(i, i+1)
    for i,j in pairs: 
        G.add_edge(i,j)
    pos = nx.get_node_attributes(G, "pos")

    labels = dict([(i+1,rna[i]) for i in range(n)])

    plt.figure(figsize=(8, 8))
    plt.axis("off")
    nx.draw(G, labels = labels, with_labels = True, pos = pos)
    plt.show()