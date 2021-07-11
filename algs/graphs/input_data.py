import networkx as nx 
import math 
import vectormath as vmath

Graph = nx.Graph()
Graph.add_edges_from(
    [
        (1,2),
        (1,3),

        (2,3),
        (2,4),
        (2,5),

        (3,5),
        (3,7),
        (3,8),

        (4,5),

        (5,6),

        (7,8)
    ]
)

DiAcyclGraph = nx.DiGraph()
DiAcyclGraph.add_edges_from(
    [
        (1,5),
        (1,4),
        (1,7),

        (2,5),
        (2,6),
        (2,3),

        (3,4),
        (3,5),

        (4,5),
        
        (5,6),
        (5,7),

        (6,7)
    ]
)

DiCycleGraph = nx.DiGraph()
DiCycleGraph.add_edges_from(
    [
        (1,2, {"weight": 2}),
        (1,3, {"weight": 10}),
        (1,4, {"weight": 10}),

        (2,3, {"weight": 4}),

        (3,5, {"weight": 2}),
        (3,6, {"weight": 4}),

        (5,4, {"weight": 2}),

        (4,2, {"weight": 1}),
        (4,6, {"weight": 8}),
    ]
)

DiGraph = nx.DiGraph()
DiGraph.add_edges_from(
    [
        (1,2, {"weight": 10}),
        (1,3, {"weight": 20}),
        (1,5, {"weight": 40}),

        (2,4, {"weight": 30}),
        (2,5, {"weight": 11}),

        (3,5, {"weight": 22}),
        (3,6, {"weight": 33}),

        (5,4, {"weight": 12}),
        (5,6, {"weight": 23}),
    ]
)

DiNegGraph = nx.DiGraph()
DiNegGraph.add_edges_from(
    [
        ('a', 'b', {"weight": -4}),
        ('a', 't', {"weight": -3}),
        ('b', 'd', {"weight": -1}),
        ('b', 'e', {"weight": -2}),
        ('c', 'b', {"weight": 8}),
        ('c', 't', {"weight": 3}),
        ('d', 'a', {"weight": 6}),
        ('d', 't', {"weight": 4}),
        ('e', 'c', {"weight": -3}),
        ('e', 't', {"weight": 2}),
    ]
)
#######################################################
def CreateClusterableGraph():
    G = nx.Graph()
    pivots = [
        vmath.Vector2(0,0),
        vmath.Vector2(0,10),
        vmath.Vector2(10,0),
        vmath.Vector2(10,10)
    ]

    i = 1
    for p in pivots:
        for a in range(0, 4):
            x = round(math.cos(math.pi*a * 0.5))
            y = round(math.sin(math.pi*a * 0.5))
            pos = p + vmath.Vector2(x,y)
            G.add_node(i, pos = pos)
            i = i + 1
    return G

ClusterableGraph = CreateClusterableGraph()

#######################################################

Tree = nx.Graph()
Tree.add_edges_from( 
    [
        (1,2),
        (1,5),
        (1,7),

        (2,3),
        (2,4),

        (5,6),

        (7,8),
        (7,9)
    ] 
)