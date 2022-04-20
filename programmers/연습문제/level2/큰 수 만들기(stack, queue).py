def solution(number, k):
    arr = []    
    for num in number:
        while len(arr) != 0 and arr[-1] < num and k > 0:
            arr.pop()
            k -= 1
        arr.append(num)
            
    result = ''.join(arr)
    if k != 0 :
        result = result[:-k]
        
    return result