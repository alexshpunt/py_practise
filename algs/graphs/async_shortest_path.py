"""
We have a graph, which represents some communication network. 

We would like to find the shortest path in the network. 

We could've used the Dijkstra's algorithm, but we don't have 
information of the whole network, as it's quite dynamic. 

So we want to implement an algorithm, which will use only the local 
information about the neighbors. 

Bellman-Ford algorithm has such a property, so basically a node V
can compute it's value based on the value of a node W, which is it's 
neighbor/adjacent node. 

So for the node V works the next expression: 
OPT[v] = min(Cvw + OPT[w]) for each W neighbor of V. k

We already implemented that in the Bellman-Ford alg improvement, 
so this time we will do an async variant of the same algorithm. 
"""
import networkx as nx
import numpy

def async_shortest_path(G : nx.DiGraph, s, t):
    n = len(G.nodes)
    nodesLst = sorted(list(G.nodes()))
    nodesIndices = {nodesLst[i]:i for i in range(n)} 
    
    inf = float("inf")
    opt = [inf] * n
    opt[nodesIndices[t]] = 0.0
    predecessor = [None] * (n+1)

    activeNodes = set(t)
    while activeNodes: 
        w = activeNodes.pop() 
        wIndex = nodesIndices[w]
        edges = G.in_edges(w, data = "weight")
        for v, _, cost in edges: 
            vIndex = nodesIndices[v]
            vOpt = cost + opt[wIndex]
            if vOpt < opt[vIndex]:
                opt[vIndex] = vOpt
                predecessor[vIndex] = w
                activeNodes.add(v)

    path = [s]
    while path[-1] != t: path.append(predecessor[nodesIndices[path[-1]]])        
    return path, opt[nodesIndices[s]]