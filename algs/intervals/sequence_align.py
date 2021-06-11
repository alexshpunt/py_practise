import numpy

def get_align_pairs(O, i, j):
    while i != 0 and j != 0:
        if i != j: yield i,j

        diag = O[i-1, j-1] 
        left = O[i-1, j]
        right = O[i, j-1]

        minCost = min(diag, left, right)
        if minCost in [diag, left]: i -= 1 
        if minCost in [diag, right]: j -= 1        

def get_alignment(pairs, s1, s2):
    #Helper function which will shift the character by index 'i' 
    #to the 'j' position. If the 'j' position is not '-' (gap)
    #then it will try to move the 'j' character first, basically 
    #pushing it forward
    def shift(arr, i, j):
        if j >= len(arr): return 
        if arr[j] != '-': shift(arr, j, j+1)            
        arr[j], arr[i] = arr[i], '-'

    m, n = len(s1), len(s2)

    extension = ['-'] * max(m,n)
    s1.extend(extension)
    s2.extend(extension) 

    if len(s1) < len(s2): s1, s2 = s2, s1
    for i,j in pairs: shift(s2, j-1, i-1)
    
    lastGapPos = len(s2) - 1
    while s1[lastGapPos] == s2[lastGapPos] and s1[lastGapPos] == '-': lastGapPos -= 1
    return s1[:lastGapPos+1], s2[:lastGapPos+1]

def seq_align(str1, str2):
    #Function which will return the cost of the mismatch characters 
    #If they are identical the cost = 0
    #If they are both vowels or consonants then the cost = 1
    #Otherwise Cost = 3
    def mismatch_cost(ch1, ch2):
        if ch1 == ch2: return 0 
        vowel = "aeiou"
        return 1.0 if (ch1 in vowel) == (ch2 in vowel) else 3.0

    gapPenalty = 2.0 
    s1, s2 = list(str1), list(str2)
    m, n = len(s1), len(s2)

    O = numpy.zeros((m+1, n+1))
    for i in range(m+1): O[i, 0] = i * gapPenalty 
    for j in range(n+1): O[0, j] = j * gapPenalty

    for i in range(1, m+1):
        for j in range(1, n+1): 
            a = mismatch_cost(s1[i-1], s2[j-1])
            O[i,j] = min(a + O[i-1, j-1], gapPenalty + min(O[i-1, j], O[i, j-1]))
    
    pairs = list(get_align_pairs(O, m, n))
    align1, align2 = get_alignment(pairs, s1, s2)

    return pairs, align1, align2, O[m, n]

tests = [
    ("mean", "name"),
    ("stop", "stop"),
    ("zaco", "azoc"),
    ("stop", "tops"),
    ("ocurrance", "occurrence"),
    ("stop", "post"),
    ("abcde", "ab"),
]

for s1, s2 in tests: 
    pairs, align1, align2, difference = seq_align(s1, s2)
    print(f"For the test words {s1,s2} with {difference} difference, there is an alignment:")
    print(f"\t{align1}\n\t{align2}")
    if pairs: 
        print(f"with the next pairs:")
        print(f"\t{pairs}")
    elif difference == 0: print("with zero pairs, as they are the same words\n")
    else: print("with zero pairs, as they are completely different\n")
