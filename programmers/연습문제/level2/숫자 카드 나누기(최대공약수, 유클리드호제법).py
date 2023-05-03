def GCDofTwoNumbers(a, b):
    while b != 0:
        a, b = b, a%b
    return a

def solution(arrayA, arrayB):
    GCDA, GCDB = arrayA[0], arrayB[0]
    for i in range(len(arrayA)):
        GCDA = GCDofTwoNumbers(GCDA, arrayA[i])
        GCDB = GCDofTwoNumbers(GCDB, arrayB[i])
    resultB = resultA = 0
    
    for i in arrayA:
        if i % GCDB == 0:
            break
    else:
        resultA = GCDB
        
    for i in arrayB:
        if i % GCDA == 0:
            break
    else:
        resultB = GCDA

    return max(resultA, resultB)
