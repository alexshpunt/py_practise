import sys 
from sequence_align_helpers import * 
from sequence_align_lin_mem import * 
from sequence_align import * 

def seq_align_div_and_conq(s1, s2):
    def solve(start1, s1, start2, s2, resultPairs : list):
        m, n = len(s1), len(s2)
        if m <= 2 or n <= 2: 
            pairs = [(i+start1, j + start2) for i,j in seq_align(s1,s2)]
            resultPairs.extend(pairs)
            return resultPairs    
                        
        optForward = forward_sequence_align_lin_mem(s1, s2[:n//2])
        optBackward = backward_sequence_align_lin_mem(s1, s2[n//2:])

        pathIndex = -1
        minSum = sys.maxsize
        for i in range(0, len(optForward)):
            f, b = optForward[i, 0], optBackward[i, 0] 
            if f+b <= minSum: 
                minSum = f+ b
                pathIndex = i
        pathNode = (iPathNode, jPathNode) = (start1 + pathIndex, start2 + n // 2)
        resultPairs.append(pathNode)

        solve(start1, s1[:pathIndex], start2, s2[:n//2], resultPairs) 
        solve(iPathNode, s1[pathIndex:], jPathNode, s2[n//2:], resultPairs) 
        return resultPairs 

    return solve(0, s1, 0, s2, [])

def test():
    for s1, s2 in tests: 
        print("----------------------------------------------------------")
        print("Sequence Alignment in Linear Space via Divide and Conquer:")
        print("----------------------------------------------------------")
        pairs = seq_align_div_and_conq(s1, s2)
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