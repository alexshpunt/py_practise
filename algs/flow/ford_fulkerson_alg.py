import networkx as nx
from input_data import * 

def get_pairs(path): return [(path[i],path[i+1]) for i in range(0, len(path)-1)]
def construct_path(pred : dict, s, t):
    pred[s] = None 
    path = [] 
    cur = t 
    while cur: 
        path.append(cur)
        cur = pred[cur]
    path.reverse()
    return path

#https://en.wikipedia.org/wiki/Ford%E2%80%93Fulkerson_algorithm
def ford_fulkerson(G : nx.DiGraph, s, t):
    def f(u, v):  return Gf.get_edge_data(u,v)["flow"]
    def c(u, v): return Gf.get_edge_data(u,v)["capacity"] 
    def residual_c(u, v): return c(u,v) - f(u,v) 
    def bottleneck(p): return min([residual_c(*e) for e in p])
    
    def push_flow(u,v, df):
        Gf.get_edge_data(u,v)["flow"] += df 
        if (v,u) in Gf.edges(): Gf.get_edge_data(v,u)["flow"] -= df 

    def find_aug_path(s, t, scale = 1): 
        pred = {} 
        stack = [s] 
        while stack: 
            cur = stack.pop() 
            for u,v in Gf.edges(cur): 
                if residual_c(u,v) < scale or v in pred.keys(): continue 
                stack.append(v)
                pred[v] = u 
        if not t in pred.keys(): return [] 
        return get_pairs(construct_path(pred, s, t))

    Gf = nx.DiGraph(G)
    for u,v in G.edges():
        Gf.get_edge_data(u, v)["flow"] = 0 
        if u != s and v != t: Gf.add_edge(v, u, capacity = 0, flow = 0) 
        
    flow = 0 

    max_s_capacity = max([Gf.get_edge_data(*e)['capacity'] for e in Gf.edges(s)])
    scale = pow(2, math.floor(math.log(max_s_capacity)))
    while scale >= 1: 
        print(scale)    
        while True: 
            path = find_aug_path(s, t, scale)
            if not path: break
            b = bottleneck(path)
            for u,v in path: push_flow(u, v, b)
            flow += b  
        scale /= 2  
    print(flow)

ford_fulkerson(FlowNetwork1, 's', 't')
print("")
ford_fulkerson(FlowNetwork2, 'A', 'G')