import unittest 
import pyalgprac.graphs.input_data as graphInput
import pyalgprac.graphs.min_arb as minArborescence
import pyalgprac.graphs.search as graphSearch
import pyalgprac.graphs.min_span_tree as minSpanningTree
import pyalgprac.graphs.single_linkage_cluster as singleLinkageCluster
from pyalgprac.graphs.topological_order import *

#TODO: Write better test cases later!
class TestGraphAlgs(unittest.TestCase):
    def test_topological_order_search(self):
        G = graphInput.DiAcyclGraph
        T = find_topological_order(G)
        self.assertTrue( T.edges() == G.edges() )

        G = graphInput.DiCycleGraph
        T = find_topological_order(G)
        self.assertTrue( T.edges() != G.edges() )

    def test_prims_alg(self):
        G = graphInput.DiGraph
        T = minSpanningTree.prims_min_spanning_tree(G)
        self.assertTrue( G.nodes() == T.nodes() )
    
    def test_dijkstra_search(self):
        G = graphInput.DiGraph 
        T = graphSearch.dijkstra_search(G, 1)
        self.assertTrue(G.nodes() == T.nodes())
    
    def test_dfs(self):
        G = graphInput.Graph
        T = graphSearch.dfs(G, 1)
        self.assertTrue(G.nodes() == T.nodes())
        
    def test_bfs(self):
        G = graphInput.Graph
        T = graphSearch.bfs(G, 1)
        self.assertTrue(G.nodes() == T.nodes())

if __name__ == '__main__':
    unittest.main()
