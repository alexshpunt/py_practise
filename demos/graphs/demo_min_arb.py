from demos.graphs.demo_util import *

import algs.graphs.input_data as graphInput
import algs.graphs.min_arb as minArborescence

def demo_edmonds_alg():
    print("Original graph:")
    G = graphInput.DiCycleGraph
    draw_planar_with_weights(G)

    print("Minimal Arborescence")
    T = minArborescence.edmonds_alg(G)
    draw_planar_with_weights(T)