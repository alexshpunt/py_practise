import networkx as nx 
import matplotlib.pyplot as plt
import pyalgprac.graphs.algs as graphAlgs
import pyalgprac.graphs.minarb as minArb 
import pyalgprac.graphs.inputdata as graphInput

def make_plot():
    plt.show()
    plt.close()

def draw_planar(G): 
    nx.draw_planar(G, with_labels = True)
    make_plot()

def draw_planar_with_weights(G):
    pos = nx.planar_layout(G)
    weights = nx.get_edge_attributes(G, "weight")
    nx.draw(G, pos, with_labels=True)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=weights)
    make_plot()

def demo_topological_order_search():
    print("Original acycle directed graph:")
    G = graphInput.DiAcyclGraph
    draw_planar(G)

    print("Topological order:")
    T = graphAlgs.find_topological_order(G)
    draw_planar(T)
    assert( T.edges() == G.edges() )

    print("Original cycled directed graph:")
    G = graphInput.DiCycleGraph
    draw_planar(G)

    print("Topological order can't be found!")
    T = graphAlgs.find_topological_order(G)
    draw_planar(T)
    assert( T.edges() != G.edges() )

def demo_prims_alg():
    print("Original graph:")
    G = graphInput.DiGraph
    draw_planar_with_weights(G)

    print("Min Spanning Tree (Prim's alg):")
    T = graphAlgs.MinSpanningTree.prims_min_spanning_tree(G)
    draw_planar_with_weights(T)

def demo_kruskal_alg():
    print("Original graph:")
    G = graphInput.DiGraph
    draw_planar_with_weights(G)

    print("Min Spanning Tree (Kruskal's alg):")
    T = graphAlgs.MinSpanningTree.kruskal_min_spanning_tree(G)
    draw_planar_with_weights(T)

def demo_single_linkage_clustering_naive():
    print("Original graph:")
    G = graphInput.ClusterableGraph
    pos = nx.get_node_attributes(G, "pos")
    nx.draw(G, pos, with_labels = True)
    make_plot()

    print("Clusters:")
    T = graphAlgs.SingleLinkageCluster.naive(G)
    pos = nx.get_node_attributes(T, "pos")
    nx.draw(T, pos, with_labels = True)
    make_plot()

def demo_edmonds_alg():
    G = graphInput.DiCycleGraph
    draw_planar_with_weights(G)
    T = minArb.MinArborescence.edmonds_alg(G)
    draw_planar_with_weights(T)

def demo_dijkstra_search():
    print("Original graph:")
    G = graphInput.DiGraph 
    draw_planar_with_weights(G)

    print("Shortest paths from 1")
    T = graphAlgs.GraphSearch.dijkstra_search(G, 1)
    draw_planar_with_weights(T)

def demo_dfs():
    print("Original graph:")
    G = graphInput.Graph
    draw_planar(G)

    print("(DFS) Spanning tree:")
    T = graphAlgs.GraphSearch.dfs(G, 1)
    draw_planar(T)
    
def demo_bfs():
    print("Original graph:")
    G = graphInput.Graph
    draw_planar(G)

    print("(BFS) Spanning tree:")
    T = graphAlgs.GraphSearch.bfs(G, 1)
    draw_planar(T)
