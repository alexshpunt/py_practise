import networkx as nx
import heapq
import disjoint_set
import math 
import vectormath as vmath

def find_topological_order(G : nx.DiGraph):    
    def count_in_edges(G):
        R = G.reverse()
        edges = {u: 0 for u in G.nodes()}
        for u in G.nodes():
            for v in R[u].keys():
                edges[u] += 1
        return edges

    T = nx.DiGraph()
    inEdges = count_in_edges(G)
    while inEdges:
        u = min(inEdges.keys(), key=lambda k: inEdges[k])
        outEdges = G[u].keys()
        if not outEdges: break

        for v in G[u].keys(): 
            if not v in inEdges: continue
            T.add_edge(u, v)
            inEdges[v] -= 1
        del inEdges[u]

    return T 

