from demos.graphs.demo_util import *

import algs.graphs.input_data as graphInput
import algs.graphs.search as graphSearch


def demo_dijkstra_search():
    print("Original graph:")
    G = graphInput.DiGraph 
    draw_planar_with_weights(G)

    print("Shortest paths from 1")
    T = graphSearch.dijkstra_search(G, 1)
    draw_planar_with_weights(T)

def demo_dfs():
    print("Original graph:")
    G = graphInput.Graph
    draw_planar(G)

    print("(DFS) Spanning tree:")
    T = graphSearch.dfs(G, 1)
    draw_planar(T)
    
def demo_bfs():
    print("Original graph:")
    G = graphInput.Graph
    draw_planar(G)

    print("(BFS) Spanning tree:")
    T = graphSearch.bfs(G, 1)
    draw_planar(T)
