from sequence_align_helpers import * 
from sequence_align_lin_mem import * 
from sequence_align import * 

def seq_align_div_and_conq(s1, s2, P : list):
    m, n = len(s1), len(s2)
    if m <= 2 or n <= 2: 
        pairs, a1, a2, v, O = seq_align(s1,s2) 
        print(s1, s2, a1, a2, pairs, v)
        P.append(pairs)
        return P 
        
    _, Of = forward_sequence_align_lin_mem(s1, s2[:n//2])
    _, Ob = backward_sequence_align_lin_mem(s1, s2[n//2:])
    print(Of)
    print(Ob)

    minSum = 100000
    minQ = -1
    for q in range(0, n+1):
        f = Of[q, 0]
        b = Ob[q, 0]
        if f+b < minSum:
            minSum = f+b 
            minQ = q
            print(f+b, minQ)
    P.append((minQ, n // 2))
    print(P)

    seq_align_div_and_conq(s1[:minQ], s2[:n//2], P) 
    seq_align_div_and_conq(s1[minQ:], s2[n//2:], P) 
    return P

for s1, s2 in tests: 
    P = [] 
    v = seq_align_div_and_conq(s1, s2, P)
    print(P)
