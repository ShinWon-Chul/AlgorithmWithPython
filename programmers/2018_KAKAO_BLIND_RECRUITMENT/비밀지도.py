def int_to_binary(n, num):
    arr = [ ]
    while True:
        if num == 1:
            arr = [1] + arr
            break
        arr = [num%2] + arr 
        num = int(num/2)
    if len(arr) < n:
        pad = [0] * (n - len(arr))
        arr = pad + arr
    return arr

def solution(n, arr1, arr2):
    new_arr = []
    for i in range(n):
        num = arr1[i] | arr2[i]
        new_arr.append(int_to_binary(n, num))

    for i in range(n):
        new_arr[i] = ''.join(list(map(lambda x: '#' if x == 1 else ' ', new_arr[i])))
    return new_arr