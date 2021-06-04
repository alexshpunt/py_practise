import numpy

class Task: 
    def __init__(self, i, w):
        self.i = i
        self.w = w 
    
    def __iter__(self):
        yield self.i
        yield self.w

def subset_sum(tasks : list, W):
    n = len(tasks)
    O = numpy.zeros((n+1, W+1))
    for i, wi in tasks:
        for w in range(W+1): 
            if w < wi: O[i, w] = O[i-1, w]
            else: O[i, w] = max(O[i-1, w], wi + O[i-1, w-wi])
    return O[n][W]

tasks = [
    Task(1, 2),
    Task(2, 2),
    Task(3, 3)
]
print(subset_sum(tasks, 6))