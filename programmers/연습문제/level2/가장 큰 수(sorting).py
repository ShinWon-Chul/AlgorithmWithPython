def solution(numbers):
    answer = ''
    new_numbers = []
    for num in numbers:
        new_num = str(num)
        length = len(new_num)
        new_num *= 4
        new_numbers.append([new_num[:4], length])
    new_numbers.sort(reverse=True)
    for new_num, length in new_numbers:
        answer += new_num[:length]
    if int(answer) == 0:return '0'
    else: return answer