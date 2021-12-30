def int_to_nonation(num, nonation):
    d_ = {10 : 'A', 11 : 'B', 12 : 'C', 13 : 'D', 14 : 'E', 15 : 'F'}
    arr = ''
    while True:
        if num < nonation:
            if num > 9:
                num = d_[num]
                arr = num + arr
                break
            else:
                arr = str(num) + arr
                break
        mode = num%nonation
        if mode > 9:
            mode = d_[mode]
            arr = mode + arr 
        else:
            arr = str(mode) + arr 
        num = int(num/nonation)
    return arr

def solution(n, t, m, p):
    order = 1 # 순서
    num = 0 # 변환할 수
    count = 0 #출력한 수
    result = []

    while True:
        converted_num = int_to_nonation(num, n)
        for c in converted_num:
            times = order%m
            if times == 0:
                times = m
            if times == p:
                result.append(c)
                order += 1
                count +=1
                if count == t:
                    break
            else:
                order += 1
        if count == t:
            break
        num += 1
    answer = ''.join(result)
    
    return answer