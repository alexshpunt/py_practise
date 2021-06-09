import numpy
from numpy.core.numeric import extend_all

def seq_align(str1, str2):
    d = 2.0 
    s1, s2 = list(str1), list(str2)
    m, n = len(s1), len(s2)

    def compare(c1, c2):
        if c1 == c2: return 0 
        vowel = "aeiou"
        return 1.0 if (c1 in vowel) == (c2 in vowel) else 3.0

    O = numpy.zeros((m+1, n+1))
    for i in range(m+1): O[i, 0] = i * d 
    for j in range(n+1): O[0, j] = j * d

    for i in range(1, m+1):
        for j in range(1, n+1): 
            a = compare(s1[i-1], s2[j-1])
            O[i,j] = min(a + O[i-1, j-1], d + min(O[i-1, j], O[i, j-1]))
    
    align = [] 

    i, j = m, n
    while i != 0: 
        if i != j: align.append((i,j))
            
        diag = O[i-1, j-1] 
        left = O[i-1, j]
        right = O[i, j-1]

        minD = min(diag, left, right)
        if minD == diag: i,j = i-1, j-1
        elif minD == left: i -= 1 
        else: j -= 1 

    alignLen = max(m, n)
    mid = alignLen // 4
    extension = ['-'] * alignLen
    align1 = list(s1)
    align1.extend(extension)
    align2 = list(s2)
    align2.extend(extension) 

    def shift(arr, i, j):
        if j >= len(arr): return 
        if arr[j] != '-': 
            shift(arr, j, j+1)            
        arr[j] = arr[i]
        arr[i] = '-'

    if len(align1) < len(align2): align1, align2 = align2, align1
    for i,j in align: shift(align2, j-1, i-1)
    
    lastSkip = len(align1)
    while lastSkip > len(align2) and align1[-1] == '-': lastSkip -= 1
    align1 = align1[:lastSkip]

    while True: 
        lastSkip -= 1
        if align1[lastSkip] != align2[lastSkip] or align1[lastSkip] != '-': break;
    align1 = align1[:lastSkip+1]
    align2 = align2[:lastSkip+1]

    print(align)
    print(align1)
    print(align2)
    return O[m, n]

tests = [
    ("mean", "name"),
    ("stop", "stop"),
    ("stop", "stpz"),
    ("stop", "tops"),
    ("ocurrance", "occurrence"),
    ("stop", "post"),
    ("abcde", "abcde"),
    ("abcde", "acbde"),
    ("abcde", "adzbe"),
    ("abcde", "baedx")
]

for s1, s2 in tests: 
    print( (s1, s2), seq_align(s1, s2))
