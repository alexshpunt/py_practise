import networkx as nx
import disjoint_set
import math 

def get_clusters(G : nx.Graph): 
    S = disjoint_set.DisjointSet()
    V = G.nodes()
    for u in V:
        minL = math.inf
        minE = (-1,-1)
        for v in V:
            if u == v: continue
            p0 = V[u]["pos"]
            p1 = V[v]["pos"]
            l = (p1 - p0).length
            if l < minL: 
                minL = l 
                minE = (u,v)
        (u,v) = minE
        S.union(u,v)
    
    T = G.copy()
    for s in list(S.itersets()):
        for u,v in [(u,v) for u in s for v in s]:
            T.add_edge(u,v,)
    return T