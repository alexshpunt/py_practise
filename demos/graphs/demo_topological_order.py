from demos.graphs.demo_util import *
from algs.graphs.topological_order import *

import algs.graphs.input_data as graphInput

def demo_topological_order_search():
    print("Original acycle directed graph:")
    G = graphInput.DiAcyclGraph
    draw_planar(G)

    print("Topological order:")
    T = find_topological_order(G)
    draw_planar(T)
    assert( T.edges() == G.edges() )

    print("Original cycled directed graph:")
    G = graphInput.DiCycleGraph
    draw_planar(G)

    print("Topological order can't be found!")
    T = find_topological_order(G)
    draw_planar(T)
    assert( T.edges() != G.edges() )