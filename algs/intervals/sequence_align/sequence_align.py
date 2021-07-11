import numpy
from numpy.core.arrayprint import BoolFormat
from sequence_align_helpers import *

def get_align_pairs(O, i, j):
    while i != 1 and j != 1:
        diag = O[i-1, j-1] 
        down, left = O[i-1, j], O[i, j-1]

        minCost = min(diag, down, left)
        if minCost in [diag, down]: i -= 1
        if minCost in [diag, left]: j -= 1

        if i != j: yield i,j        

def seq_align(s1, s2):
    s1, s2 = list(s1), list(s2)
    m, n = len(s1), len(s2)

    O = numpy.zeros((m+1, n+1))
    for i in range(m+1): O[i, 0] = i * gapPenalty 
    for j in range(n+1): O[0, j] = j * gapPenalty

    for i in range(1, m+1):
        for j in range(1, n+1): 
            a = mismatch_cost(s1[i-1], s2[j-1])
            O[i,j] = min(a + O[i-1, j-1], gapPenalty + O[i-1, j], gapPenalty + O[i, j-1])

    return list(get_align_pairs(O, m, n))

def back_seq_align(s1, s2):
    s1, s2 = list(s1), list(s2)
    m, n = len(s1), len(s2)

    O = numpy.zeros((m+1, n+1))
    for i in range(m+1): O[m, i] = (m-i) * gapPenalty 
    for j in range(n+1): O[j, n] = (n-j) * gapPenalty

    for i in reversed(range(m)):
        for j in reversed(range(n)): 
            a = mismatch_cost(s1[i], s2[j])
            O[i,j] = min(a + O[i+1, j+1], gapPenalty + min(O[i+1, j], O[i, j+1]))
    
    return list(get_align_pairs(O, m, n))

def test():
    for s1, s2 in tests: 
        print("----------------------------------------------------------")
        print("Sequence Alignment:")
        print("----------------------------------------------------------")
        pairs = seq_align(s1, s2)
        align1, align2 = get_alignment(pairs, s1, s2)
        difference = get_difference(align1, align2)
        print(f"For the test words {s1,s2} with {difference} difference, there is an alignment:")
        print(f"\t{align1}\n\t{align2}")
        if pairs: 
            print(f"with the next pairs:")
            print(f"\t{pairs}")
        elif difference == 0: print("with zero pairs, as they are the same words\n")
        else: print("with zero pairs, so either they are completely different",
                    "or one word is a substring of another\n")
test()