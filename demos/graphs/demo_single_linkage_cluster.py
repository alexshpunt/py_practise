from demos.graphs.demo_util import *

import pyalgprac.graphs.input_data as graphInput
import pyalgprac.graphs.single_linkage_cluster as singleLinkageCluster

def demo_single_linkage_clustering_naive():
    print("Original graph:")
    G = graphInput.ClusterableGraph
    pos = nx.get_node_attributes(G, "pos")
    nx.draw(G, pos, with_labels = True)
    make_plot()

    print("Clusters:")
    T = singleLinkageCluster.get_clusters(G)
    pos = nx.get_node_attributes(T, "pos")
    nx.draw(T, pos, with_labels = True)
    make_plot()
