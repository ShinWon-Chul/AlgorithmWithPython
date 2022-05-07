def int_to_binary(num):
    arr = []
    while True:
        if num < 2:
            arr.append(num)
            break
        mode = num%2
        arr.append(mode) 
        num = int(num/2)
    arr.append(0)
    return arr

def solution(n):
    answer = 0
    bi = int_to_binary(n)
    current_bit = bi[0]
    count = 0
    for i, b in enumerate(bi[1:]):
        next_bit = b
        if current_bit == 1 and next_bit == 0:
            break
        elif current_bit == 1 and next_bit == 1:
            current_bit = next_bit
            count += 1
        else:
            current_bit = next_bit
            
    bi[i+1] = 1
    for j, b in enumerate(bi):
        if j < count:
            answer += 1*2**j
        elif count <= j <= i:
            continue
        else:
            answer += b*2**j
        
    return answer