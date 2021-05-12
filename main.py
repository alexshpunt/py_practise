import sys 
import unittest
import demos.graphs.demo as demos
import tests.test_graphalgs as tests 

class EntryPoint: 
    """
usage: main.py <command> 

commands: 
    demo_%TARGET% - Demonstrates an algorithm implemented in the packaged by name %TARGET%
    test - Tests the package 
possible targets: [bfs, dfs, topological_order, dijkstra_search, prims_alg, kruskal_alg]
    """

    @staticmethod
    def show_help(): 
        pass 

    @staticmethod
    def run_tests():
        unittest.main(module="tests.test_graphalgs", verbosity=2)

if __name__ == "__main__":
    arg = sys.argv[1:]
    if arg == ["test"]:
        EntryPoint.run_tests()
    elif arg == ["help"]: 
        print(EntryPoint.__doc__.strip())
    else: 
        demos.demo_edmonds_alg()