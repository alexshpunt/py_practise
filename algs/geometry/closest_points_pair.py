import matplotlib.pyplot as plt 
import numpy as np
import math
import cProfile

NUMBER_OF_POINTS = 1000

def find_closest_points(P : list):
    def d(p0,p1): return math.dist(p0,p1)

    def rec(Px, Py):
        if len(Px) <= 3: 
            pairs = [(p0,p1) for p0 in Px for p1 in Px if p0 != p1]
            return min(pairs, key = lambda p: d(*p))

        mid = len(Px) // 2
        Qx, Qy = Px[:mid], Py[:mid]
        Rx, Ry = Px[mid:], Py[mid:]
        
        q0,q1 = rec(Qx, Qy)
        r0,r1 = rec(Rx, Ry)
        minD = min(d(q0,q1), d(r0,r1))

        L = Qx[-1]
        Sy = [p for p in Py]
        lSy = len(Sy)

        foundP = None 
        for i in range(lSy):
            s0 = Sy[i]
            for j in range(i+1, min(i+16, lSy)):
                s1 = Sy[j]
                dS = d(s0,s1) 
                if dS < minD: 
                    foundP = (s0,s1)
                    minD = dS

        if foundP: return foundP
        if d(q0,q1) < d(r0,r1): return (q0,q1)
        return (r0,r1)

    Px = sorted(P, key = lambda p: p[0])
    Py = sorted(P, key = lambda p: p[1])
    return rec(Px, Py)

def brute_force_find_closest_point(P : list):
    allPairs = [(p0,p1) for p0 in P for p1 in P if p0 != p1]
    return min(allPairs, key = lambda pair: math.dist(pair[0], pair[1]))

def generate_points():
    x = np.random.randn(NUMBER_OF_POINTS)
    y = np.random.randn(NUMBER_OF_POINTS)
    return x,y

def points_array(x,y): return list(zip(x,y))
def coords_array(p): return list(zip(*p))


def show_module():
    def show_plot(searchFunc):
        fig = plt.figure(figsize=(8,8))
        axes = fig.add_axes([0,0,1,1])

        x,y = generate_points()
        axes.scatter(x,y)

        points = points_array(x,y)
        closestPoints = searchFunc(points)
        x,y = coords_array(closestPoints)

        axes.plot(x,y)
        plt.show()

    testCase = 2
    print("Brute force alg result:")
    np.random.seed(testCase)    
    show_plot(brute_force_find_closest_point)

    print("Optimized alg result:")
    np.random.seed(testCase)    
    show_plot(find_closest_points)

def validate_module():
    def sanity_check(i):
        np.random.seed(i)    
        points = points_array(*generate_points())
        bfResult = brute_force_find_closest_point(points)
        opResult = find_closest_points(points)
        outResult = math.dist(*bfResult) == math.dist(*opResult)
        if not outResult: print (f"The test case #{i} has an error!")
        return outResult

    sanityCheckResults = [sanity_check(i) for i in range(100)]
    successRate = sanityCheckResults.count(True) / len(sanityCheckResults)
    print(f"SuccessRate {successRate*100}%")

def benchmark_module(number_of_tests):
    def test_brute_force(i):
        np.random.seed(i)    
        points = points_array(*generate_points())
        brute_force_find_closest_point(points)
        
    def test_search(i):
        np.random.seed(i)
        points = points_array(*generate_points())
        find_closest_points(points)
        
    cProfile.run(f"[test_brute_force(i) for i in range({number_of_tests})]")
    cProfile.run(f"[test_search(i) for i in range({number_of_tests})]")

# show_module()
# validate_module()
# benchmark_module(100)