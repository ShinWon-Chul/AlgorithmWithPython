def solution(elements):
    
    answer = 0
    n = len(elements)
    arr = []
    elements += elements
    for i in range(n):
        for j in range(n):
            arr.append(sum(elements[j:i+j]))
    
    return len(set(arr))