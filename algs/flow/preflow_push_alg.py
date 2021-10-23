import networkx as nx
from input_data import *

def push_relabel(G : nx.DiGraph, s, t):
    def e(u,v): return Gf.get_edge_data(u,v)
    def cf(u,v): return e(u,v)['capacity'] - e(u,v)['flow']

    excess = {} 
    labels = {} 
    Gf = nx.DiGraph(G)
    nodes = Gf.nodes()
    for u,v in G.edges():
        e(u, v)["flow"] = 0 
        Gf.add_edge(v, u, capacity = 0, flow = 0) 
        excess[u] = excess[v] = 0 
        labels[u] = labels[v]= 0 
    excess[s] = float('inf')
    labels[s] = len(nodes)

    def can_push(u,v): return labels[u] > labels[v] and cf(u,v) > 0
    def push(u,v): 
        d = min(excess[u], cf(u,v))
        e(u,v)['flow'] += d 
        e(v,u)['flow'] -= d 
        excess[u] -= d 
        excess[v] += d 

    def relabel(u):
        adm_arcs = [labels[v] for u,v in Gf.edges(u) if cf(u,v) > 0]
        if excess[u] > 0 and len(adm_arcs) > 0: labels[u] = 1 + min(adm_arcs)

    def residual_nodes(): return [n for n in nodes if excess[n] > 0 and not n in [s,t]]

    #Initial preflow 
    for s,v in Gf.edges(s): push(s,v)

    Ef = residual_nodes() 
    while len(Ef) > 0:
        u = Ef[0] 
        E = [e for e in Gf.edges(u) if can_push(*e)]
        if len(E) > 0: push(*E[0])
        else: relabel(u)
        Ef = residual_nodes() 
    return excess[t]

print(push_relabel(FlowNetwork1, 's', 't'))
print(push_relabel(FlowNetwork2, 'A', 'G'))
print(push_relabel(FlowNetwork3, 's', 't'))
print(push_relabel(FlowNetwork4, 's', 't'))