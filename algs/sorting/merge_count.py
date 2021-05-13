def merge_and_count(A : list, B : list):
    L = list()
    iA, iB = 0,0
    lenA, lenB = len(A), len(B)
    count = 0 
    
    while iA < lenA and iB < lenB: 
        a,b = A[iA], B[iB]
        minElement = min(a,b)
        L.append(minElement)
    
        if minElement is b: 
            count += (len(A) - iA)
            iB += 1
        else: iA += 1

    #As one of the arrays is empty, we can just concatenate them all 
    #in a single line 
    L = L + A[iA:] + B[iB:]

    return count, L

def sort_and_count(L : list):
    if len(L) == 1: 
        return 0, L 

    m = len(L) // 2

    A = L[:m]
    B = L[m:]

    rA, A = sort_and_count(A)
    rB, B = sort_and_count(B)
    r, L = merge_and_count(A,B)

    return rA+rB+r, L

def test_sort_and_count():
    listA = [2, 4, 1, 3, 5]
    r, sorted = sort_and_count( listA )
    print("Original list:", listA, "Inverse count:", r, "Sorted list:", sorted)