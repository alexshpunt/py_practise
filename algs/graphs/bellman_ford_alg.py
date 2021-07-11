import networkx as nx
import numpy

def shortest_path(G : nx.DiGraph, s, t):
    n = len(G.nodes)
    nodesLst = sorted(list(G.nodes()))
    nodesIndices = {nodesLst[i]:i for i in range(n)} 
    
    inf = float("inf")
    opt = numpy.zeros((n, n))
    for nodeIndex in range(n): opt[nodeIndex, 0] = inf
    opt[nodesIndices[t], 0] = 0 

    predecessor = [None] * (n+1)
    for edgesCount in range(1, n):
        for nodeIndex in range(n):
            edges = G.edges(nodesLst[nodeIndex], data = "weight")
            opt[nodeIndex, edgesCount] = opt[nodeIndex, edgesCount-1]
            for _, w, cost in edges:                 
                wOpt = cost + opt[nodesIndices[w], edgesCount-1]
                if wOpt < opt[nodeIndex,edgesCount]: 
                    opt[nodeIndex,edgesCount] = wOpt
                    predecessor[nodeIndex] = w

    path = [s]
    while path[-1] != t: path.append(predecessor[nodesIndices[path[-1]]])        
    return path, opt[nodesIndices[s], n-1]