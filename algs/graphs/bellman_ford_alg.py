import networkx as nx
import numpy

def shortest_path(G : nx.DiGraph, s, t):
    n = len(G.nodes)
    nodesLst = sorted(list(G.nodes()))
    nodesIndices = {nodesLst[i]:i for i in range(n)} 
    
    inf = float("inf")
    opt = [inf] * n
    opt[nodesIndices[t]] = 0.0

    predecessor = [None] * (n+1)
    foundNewMin = False 
    for i in range(1, n):
        for nodeIndex in range(n):
            edges = G.edges(nodesLst[nodeIndex], data = "weight")
            for _, w, cost in edges:                 
                wOpt = cost + opt[nodesIndices[w]]
                foundNewMin = foundNewMin or wOpt < opt[nodeIndex]
                if foundNewMin: 
                    opt[nodeIndex] = wOpt
                    predecessor[nodeIndex] = w
        if not foundNewMin: break 

    path = [s]
    while path[-1] != t: path.append(predecessor[nodesIndices[path[-1]]])        
    return path, opt[nodesIndices[s]]