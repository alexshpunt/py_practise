import matplotlib.pyplot as plt 

class Interval: 
    def __init__(self, s, f, v):
        self.s = s 
        self.f = f 
        self.v = v 

    def __iter__(self):
        return iter((self.s, self.f, self.v))

    def __repr__(self):
        return f"({self.s},{self.f}, v={self.v})"

    def overlaps(self, other):
        if not other: return False
        s0,f0, _ = self 
        s1,f1, _ = other 
        return s0 < f1 and f0 > s1 

class Intervals: 
    def __init__(self, *intervals : list):
        self.data = intervals
        self.M = [None] * len(self.data)
    
    def __iter__(self): 
        return self.data 

    def __len__(self):
        return len(self.data)

    def __repr__(self) -> str:
        return self.data.__repr__()

    def __getitem__(self, i):
        return self.data[i]

    def p(self, i : int):
        interval_i = self.data[i]
        for j in reversed(range(i-1)):
            interval_j = self.data[j]
            if not interval_i.overlaps(interval_j): return j
        return 0 

    def naive_rec_solution(self, i : int):
        if i == 0: return 0 
        return max(self[i].v + self.naive_rec_solution(self.p(i)), self.naive_rec_solution(i-1))

    def mem_rec_solution(self, i : int):
        if i == 0: return 0 
        if self.M[i]: return self.M[i] 

        v = self.data[i].v
        self.M[i] = max(v + self.mem_rec_solution(self.p(i)), self.mem_rec_solution(i-1))
        return self.M[i]

    def iter_solution(self):
        self.M[0] = 0 
        for i in range(len(self.data)):
            if i == 0: continue
            v = intervals[i].v
            self.M[i] = max(v + self.M[self.p(i)], self.M[i-1])
        return self.M[-1]

    def get_solution(self, i : int, l : list = []): 
        if i == 0: return l
        v = self.data[i].v
        if v + self.M[self.p(i)] >= self.M[i-1]:
            l.append(i)
            return self.get_solution(self.p(i), l)
        else: return self.get_solution(i-1,l)
        
intervals = Intervals(
    None, #index 0 
    Interval(0, 4, v = 2),
    Interval(1, 6, v = 4),
    Interval(4, 8, v = 4),
    Interval(2, 10, v = 7),
    Interval(8.5, 11, v = 2),
    Interval(9, 12, v = 1)
)

def show_intervals(intervals : Intervals):
    fig = plt.figure(figsize=(8,8))
    axes = fig.add_axes([0,0,1,1])

    lI = len(intervals)
    print(f"Intervals: {intervals} ({lI})")
    for i in range(lI):
        if not intervals[i]: continue

        s,f,v = intervals[i] 
        points = (s,i), (f,i)
        coords = list(zip(*points))

        axes.scatter(*coords)
        axes.plot(*coords, label = f"v={v}")
        axes.legend()

    plt.show()

print("Original intervals:")
show_intervals(intervals)

lastIntervalIndex = len(intervals)-1

solutionWeight = intervals.iter_solution()
finalSolution = intervals.get_solution(lastIntervalIndex)
solvedIntervals = [intervals[i] for i in range(lastIntervalIndex) if i in finalSolution ]
print(f"Solved intervals (with weight = {solutionWeight}):")
show_intervals(solvedIntervals)


    