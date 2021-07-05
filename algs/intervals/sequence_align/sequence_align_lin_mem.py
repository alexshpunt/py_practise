import numpy 
from sequence_align_helpers import * 

def forward_sequence_align_lin_mem(s1, s2): 
    print(s1, s2)
    m,n = len(s1), len(s2)
    O = numpy.zeros((m+1, 2))
    for i in range(1, m+1): O[i,0] = i * gapPenalty 

    for j in range(1, n+1):
        O[0,1] = j * gapPenalty 
        for i in range(1, m+1):
            a = mismatch_cost(s1[i-1], s2[j-1])
            O[i, 1] = min(a + O[i-1, 0], gapPenalty + min(O[i-1, 1], O[i, 0]))
        for i in range(m+1): O[i,0] = O[i,1]
        
    return O[m, 1], O

def backward_sequence_align_lin_mem(s1, s2): 
    print(f"backward {s1, s2}")
    m,n = len(s1), len(s2)

    O = numpy.zeros((max(m,n)+1, 2))
    for i in reversed(range(0, m+1)): O[i,1] = (m-i) * gapPenalty 

    for j in reversed(range(0, n)):
        O[m,0] = (n-j) * gapPenalty 
        for i in reversed(range(0, m)):
            a = mismatch_cost(s1[i], s2[j])
            O[i, 0] = min(a + O[i+1, 1], gapPenalty + min(O[i+1, 0], O[i, 1]))
        for i in range(m+1): O[i,1] = O[i,0]
    return O[0, 1], O

def test():
    for s1, s2 in tests: 
        print("Forward:")
        f, O = forward_sequence_align_lin_mem(s1,s2)
        print("\nBackward:")
        b, O = backward_sequence_align_lin_mem(s1,s2)
        print(s1, s2)
        print(f"forward: {f} backward {b}")
        print(f == b)
        print()