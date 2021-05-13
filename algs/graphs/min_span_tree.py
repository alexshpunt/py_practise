import networkx as nx
import heapq
import disjoint_set
import math 

def prims_min_spanning_tree(G : nx.DiGraph):
    Q = list(G.nodes())
    C = {v: math.inf for v in Q}
    prev = {v: None for v in Q}

    while Q:
        u = min(Q, key=lambda x: C[x])
        for v in G[u]:
            vCost = G.edges[u,v]["weight"]
            if vCost < C[v]:
                C[v] = vCost
                prev[v] = u
        Q.remove(u)

    T = nx.DiGraph()
    for v in G.nodes():
        if not prev[v]: continue 
        T.add_edge(prev[v], v, weight = C[v])
    return T

def kruskal_min_spanning_tree(G : nx.DiGraph):
    Q = []
    S = disjoint_set.DisjointSet()
    for e in G.edges():
        u,v = e
        w = G.edges()[u,v]["weight"]
        heapq.heappush(Q, (w, e))

    T = nx.DiGraph()
    while Q:
        w, (u,v) = heapq.heappop(Q)
        if S.connected(u,v): continue
        S.union(u,v)
        T.add_edge(u,v, weight=w)
    return T 