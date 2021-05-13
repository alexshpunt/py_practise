from demos.graphs.demo_util import *

import algs.graphs.input_data as graphInput
import algs.graphs.min_span_tree as minSpanningTree

def demo_prims_alg():
    print("Original graph:")
    G = graphInput.DiGraph
    draw_planar_with_weights(G)

    print("Min Spanning Tree (Prim's alg):")
    T = minSpanningTree.prims_min_spanning_tree(G)
    draw_planar_with_weights(T)

def demo_kruskal_alg():
    print("Original graph:")
    G = graphInput.DiGraph
    draw_planar_with_weights(G)

    print("Min Spanning Tree (Kruskal's alg):")
    T = minSpanningTree.kruskal_min_spanning_tree(G)
    draw_planar_with_weights(T)