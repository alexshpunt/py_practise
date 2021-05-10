import networkx as nx
import heapq
import disjoint_set
import math 
import vectormath as vmath

class MinSpanningTree: 
    @staticmethod
    def prims_min_spanning_tree(G):
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

    @staticmethod
    def kruskal_min_spanning_tree(G):
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



class SingleLinkageCluster: 
    @staticmethod
    def naive(G): 
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

class GraphSearch:
    @staticmethod
    def dijkstra_search(G, source):
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

    @staticmethod
    def dfs(G, s):
        T = nx.Graph()
        stack = [s]
        while stack:
            u = stack.pop()
            for v in G[u].keys(): 
                if v in T: continue
                T.add_edge(u, v)
                stack.append(v)
        return T

    @staticmethod
    def bfs(G, s):
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

def find_topological_order(G):    
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

