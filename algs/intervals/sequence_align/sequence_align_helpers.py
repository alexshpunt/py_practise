def get_alignment(pairs, s1, s2):
    if len(pairs) == 0: return s1, s2

    m, n = len(s1), len(s2)
    c1, c2 = [], []
    ipairs, jpairs = zip(*sorted(pairs))
    i,j = 1,1 
    while i <= m or j <= n: 
        iIsNotGap = j in jpairs or j > n 
        jIsNotGap = i in ipairs or i > m
        if not(iIsNotGap or jIsNotGap): iIsNotGap = jIsNotGap = True 

        c1 += s1[i-1] if iIsNotGap else '-'
        c2 += s2[j-1] if jIsNotGap else '-'

        i += int(iIsNotGap)
        j += int(jIsNotGap)
    return c1, c2

def get_difference(a1, a2):
    factor = 0.0 
    for i in range(len(a1)):
        factor += mismatch_cost(a1[i-1], a2[i-1])
    return factor 

#Function which will return the cost of the mismatch characters 
#If they are identical the cost = 0
#If they are both vowels or consonants then the cost = 1
#Otherwise Cost = 3
def mismatch_cost(ch1, ch2):
    if ch1 == ch2: return 0.0
    if ch1 == '-' or ch2 == '-': return 2.0
    vowel = "aeiou"
    return 1.0 if (ch1 in vowel) == (ch2 in vowel) else 3.0

gapPenalty = 2.0 

tests = [
    ("mean", "name"),
    ("zaco", "azoc"),
    ("stop", "stop"),
    ("stop", "post"),
    ("post", "stop"),
    ("stop", "tops"),
    ("ocurrance", "occurrence"),
    ("occurrence", "ocurrance"),
    ("ab", "abc"),
    ("abc", "ab"),
]