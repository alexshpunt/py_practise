import matplotlib.pyplot as plt 
import math 
import numpy as np 

#Computes a and b parameters of the line (ax + b)
#which has the minimal error for the each point in the 
#points list 
def compute_line_AB(points : list):
    n = len(points)
    if n == 0: return (0,0)
    sX = sY = sXY = sX2 = 0

    for x,y in points: 
        sXY += x*y
        sX += x 
        sY += y 
        sX2 += x**2
        pass 

    a = (n * sXY - sX*sY) / (n * sX2 - sX ** 2)
    b = (sY - a * sX) / n
    return (a,b)

#Computes an error of all the points to the 
#line defined by (a,b) parameters of (ax+b) function 
def error_L(points : list, lineAB):
    error = 0 
    a,b = lineAB
    for x,y in points: 
        error += (y - a * x - b) ** 2 
    return error 

def solve(points : list):
    cachedResults = {}
    def find_error(i,j):
        if (i,j) in cachedResults.keys(): return cachedResults[i,j]
        p = points[i:j+1]
        e = error_L(p, compute_line_AB(p))
        cachedResults[i,j] = e
        return e

    n = len(points)
    err = {}
    for i,j in [(i,j) for i in range(n) for j in range(i,n)]:
        err[i,j] = find_error(i,j) if i != j else 0 

    #Optimal solution 
    Opt = [10000] * n 
    Opt[0] = 0 
    #The next point of the i segment 
    #of the optimial solution
    Seg = [-1] * n 

    lineCost = max(SAMPLES_ERROR_FACTOR, find_error(0,n-1) / POINTS_NUMBER)
    for i,j in [(i,j) for j in range(0,n) for i in range(0,j)]:
        cost = err[i,j] + lineCost + Opt[i]
        if Opt[j] > cost: Opt[j], Seg[j] = cost, i

    i = n-1
    while i > 0:
        yield i, Seg[i] 
        i = Seg[i]     

#Demo
POINTS_NUMBER = 100
SAMPLES_ERROR_FACTOR = 0.1

def show_points(points, segments):
    fig = plt.figure(figsize=(8,8))
    axes = fig.add_axes([0,0,1,1])

    for x,y in points:
        axes.scatter(x,y)

    for s,f in segments:
        positions = points[s], points[f]
        coords = list(zip(*positions))
        axes.plot(*coords)

    plt.show()

def generate_points(f):
    for x in np.linspace(-2, 2, POINTS_NUMBER):
        def getErr(): return (np.random.ranf() * 2 - 1) * SAMPLES_ERROR_FACTOR
        yield (x + getErr() ,f(x) + getErr())

def show_solution(f): 
    points = list(generate_points(f)) 
    show_points(points, solve(points))

def line(x): return 0.5*x - 0.85
    
def parabolic(x):
    #for this specific sample we want to use only the positive half
    #so we can find a solution of two lines 
    if x < 0: return 0 
    return x**2

def smoothstep(x):
    x = max(0, min(x, 1))
    return x*x*(3-2*x)

def sin(x): return math.sin(x * 4)

examples = [line, 
            parabolic, 
            smoothstep, 
            sin]

for example in examples: 
    show_solution(example)