"""num을 nonation진법으로 변환하는 메서드"""
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