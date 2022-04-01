import math

def solution(n, k):
    arr = []
    num_person = n
    person = [i+1 for i in range(n)]
    
    for _ in range(n):
        nf = math.factorial(num_person-1)
        arr.append(person[int((k-1)/nf)])
        del person[int((k-1)/nf)]
        temp_k = k%nf
        num_person -= 1
        if temp_k == 0:
            k = math.factorial(num_person)
        else:
            k = temp_k

    return arr