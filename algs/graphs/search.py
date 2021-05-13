import networkx as nx
import heapq
import math 

def dijkstra_search(G : nx.DiGraph, source):
    T = nx.DiGraph()

    dist = { source: 0 }
    prev = { source: None }

    Q = []
    for v in G.nodes():
        if v != source: 
            dist[v] = math.inf
            prev[v] = None 
        heapq.heappush(Q, (dist[v], v))

    while Q:
        u = heapq.heappop(Q)[1]
        for v in G[u]: 
            vDist = dist[u] + G.edges[u,v]["weight"]
            if vDist < dist[v]:
                dist[v] = vDist
                prev[v] = u
                heapq.heappush(Q, (vDist, v))

    for v in G.nodes():
        if v == source: continue
        T.add_edge(prev[v], v, weight = dist[v])
    return T 

def dfs(G : nx.Graph, s):
    T = nx.Graph()
    stack = [s]
    while stack:
        u = stack.pop()
        for v in G[u].keys(): 
            if v in T: continue
            T.add_edge(u, v)
            stack.append(v)
    return T

def bfs(G: nx.Graph, s):
    T = nx.Graph()
    L = [[s]] 

    l = 0 
    while L[l]:
        nL = []
        for u in L[l]:
            for v in G[u].keys():
                if v in T: continue
                T.add_edge(u, v)
                nL.append(v)
        L.append(nL)
        l += 1
    return T