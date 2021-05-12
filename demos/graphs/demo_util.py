import networkx as nx 
import matplotlib.pyplot as plt

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