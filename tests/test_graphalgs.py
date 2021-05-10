import unittest 
import pyalgprac.graphs.algs as graphAlgs
import pyalgprac.graphs.inputdata as graphsInput

#TODO: Write better test cases later!
class TestGraphAlgs(unittest.TestCase):
    def test_topological_order_search(self):
        G = graphsInput.DiAcyclGraph
        T = graphAlgs.find_topological_order(G)
        self.assertTrue( T.edges() == G.edges() )

        G = graphsInput.DiCycleGraph
        T = graphAlgs.find_topological_order(G)
        self.assertTrue( T.edges() != G.edges() )

    def test_prims_alg(self):
        G = graphsInput.DiGraph
        T = graphAlgs.MinSpanningTree.prims_min_spanning_tree(G)
        self.assertTrue( G.nodes() == T.nodes() )
    
    def test_dijkstra_search(self):
        G = graphsInput.DiGraph 
        T = graphAlgs.GraphSearch.dijkstra_search(G, 1)
        self.assertTrue(G.nodes() == T.nodes())
    
    def test_dfs(self):
        G = graphsInput.Graph
        T = graphAlgs.GraphSearch.dfs(G, 1)
        self.assertTrue(G.nodes() == T.nodes())
        
    def test_bfs(self):
        G = graphsInput.Graph
        T = graphAlgs.GraphSearch.bfs(G, 1)
        self.assertTrue(G.nodes() == T.nodes())

if __name__ == '__main__':
    unittest.main()
