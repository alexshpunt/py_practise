import numpy

class Item: 
    def __init__(self, i, w, v):
        self.i = i
        self.w = w 
        self.v = v
    
    def __iter__(self):
        yield self.i
        yield self.w
        yield self.v 

def subset_sum(items : list, W):
    n = len(items)
    O = numpy.zeros((n+1, W+1))
    for i, wi, v in items:
        for w in range(W+1): 
            if w < wi: O[i, w] = O[i-1, w]
            else: O[i, w] = max(O[i-1, w], v + O[i-1, w-wi])
    return O[n][W]

tasks = [
    Item(1, 3, 4),
    Item(2, 4, 2),
    Item(3, 2, 1)
]
print(subset_sum(tasks, 6))