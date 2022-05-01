def int_to_nonation(num):
    arr = ''
    while True:
        if num < 2:
            arr = str(num) + arr
            break
        mode = num%2
        arr = str(mode) + arr 
        num = int(num/2)
    return arr

def solution(s):
    answer = [0, 0]
    while s != '1':
        length = len(s)
        s = s.replace('0', '')
        temp_length = len(s)
        s =  int_to_nonation(temp_length)
        answer[0] += 1
        answer[1] += length - temp_length
    return answer