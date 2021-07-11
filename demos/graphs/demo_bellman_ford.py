from demos.graphs.demo_util import *
import algs.graphs.input_data as graphInput
import algs.graphs.bellman_ford_alg as bellman_ford 

def demo_bellman_ford():
    G = graphInput.DiNegGraph
    print("Graph with negative cycles: ")
    draw_planar_with_weights(G)

    t = 't'
    for node in G.nodes():
        if node == t: continue
        s = node
        path, length = bellman_ford.shortest_path(G, s, t)
        print(f"Shortests from s = {s} to t = {t} is {path} with length {length}")
    