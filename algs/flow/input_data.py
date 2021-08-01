import networkx as nx 
import math 
import vectormath as vmath

FlowNetwork1 = nx.DiGraph()
FlowNetwork1.add_edges_from(
    [
        ('s','u', {"capacity": 20}),
        ('s','v', {"capacity": 10}),
        ('u','v', {"capacity": 30}),
        ('u','t', {"capacity": 10}),
        ('v','t', {"capacity": 20}),
    ]
)

FlowNetwork2 = nx.DiGraph()
FlowNetwork2.add_edges_from(
    [
        ('A','B', {"capacity": 3}),
        ('A','D', {"capacity": 3}),
        ('B','C', {"capacity": 4}),
        ('C','A', {"capacity": 3}),
        ('C','D', {"capacity": 1}),
        ('C','E', {"capacity": 2}),
        ('D','E', {"capacity": 2}),
        ('D','F', {"capacity": 6}),
        ('E','B', {"capacity": 1}),
        ('E','G', {"capacity": 1}),
        ('F','G', {"capacity": 9}),
    ]
)