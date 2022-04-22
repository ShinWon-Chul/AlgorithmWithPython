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

def solution(numbers):
    answer = []
    for num in numbers:
        if num % 2 == 0:
            answer.append(num+1)
        else:
            binary = int_to_binary(num)
            for i, b in enumerate(binary):
                if b == 0:
                    answer.append(num+2**(i-1))
                    break
    return answer