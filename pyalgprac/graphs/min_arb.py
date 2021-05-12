import networkx as nx

#https://en.wikipedia.org/wiki/Edmonds'_algorithm
def edmonds_alg(in_G : nx.DiGraph): 
    G = in_G.copy()
    nodes = G.nodes
    edges = G.edges 
    def getWeight(e): return edges[e]["weight"]
    def getWeightUV(u,v): return getWeight((u,v))

    #We need to substract from all the in-edges the weight 
    #of the in-edge with the minimum weight amongh them'
    #The edges with the 0 cost after the process are the parts
    #of our min arborescence  
    for u in nodes:
        inEdges = G.in_edges(u)
        if not inEdges: continue

        minE = min(inEdges, key=getWeight)
        minW = getWeight(minE)

        for e in inEdges: edges[e]["weight"] -= minW

    #If there is no cycle we are done, we can just return the result
    try: 
        cycle = nx.find_cycle(G)
    except:
        return G     

    #Otherwise there is a cycle and we need to get that 
    C = nx.DiGraph()
    for u,v in cycle: C.add_edge(u, v, weight=getWeightUV(u,v))

    #To solve the task we need to compress the cycle into a super node
    CycleIndex = G.number_of_nodes() + 1
    G_minus_C = G.copy()

    #To do this, we need to find out all the in and out edges comint from/to the cycle
    edgesWithCycle = {}
    for u,v in edges: 
        #if they are either not in the cycle, or both nodes are in the cycle
        #we need to skip them, because it doesn't matter for the algorithm 
        if (u in C) == (v in C): continue 

        edge = (CycleIndex, v)
        if not u in C: edge = (u,CycleIndex)

        #If there are parallel edges, we want to keep only the one with the minimum cost 
        w = getWeightUV(u, v)
        if not edge in G_minus_C.edges or G_minus_C.edges[edge]["weight"] > w: 
            edgesWithCycle[edge] = (u,v)
            u,v = edge
            G_minus_C.add_edge(u,v, weight=w)

    #Then just remove the cycle from the graph, as it's now replaced with the super node
    for u in C.nodes():  G_minus_C.remove_node(u)

    #This solution has a reccursive nature, so we just need to process the graph 
    #until there is no cycle and we can return the arborescence
    G_minus_C = edmonds_alg(G_minus_C)

    #Then we need to reconstruct the super node's structure it had before the compression
    G_minus_C.add_edges_from(C.edges(data = True))
    
    for key,value in edgesWithCycle.items():
        u,v = value
        G_minus_C.add_edge(u,v, weight = getWeightUV(u, v))

        #We need to break the cycle, by removing the edge that was causing that 
        ku, kv = key
        if kv != CycleIndex: continue
        inEdges = [ (in_u,in_v) for in_u,in_v in G_minus_C.in_edges(v) if in_u != u or in_v != v]
        G_minus_C.remove_edges_from(inEdges)

    G_minus_C.remove_node(CycleIndex)

    return G_minus_C