def dfs(result, digits):
    global max_num
    global min_num
    global signs

    
    # 부등호를 만족하는지 검사
    for i in range(len(result)-1):
        if signs[i] == '<':
            if int(result[i]) > int(result[i+1]):
                return
        else:
            if int(result[i]) < int(result[i+1]):
                return

    # 부등호를 전부 만족한다면
    else:
        # k+1개 만큼 숫자를 고름
        if len(result) == k+1:
            if result > max_num:
                max_num = result
            if result < min_num:
                min_num = result

            return

    for i in range(10):
        if str(i) in digits:
            result += str(i) 
            new_digits = digits.replace(str(i), '')
            dfs(result, new_digits)
            result = result.replace(str(i), '')

# 입력 받기
k = int(input())
signs = input().strip().split()
digits = '0123456789'

max_num = ''
min_num = '9876543210'

# 결과 계산
dfs('', digits)

# 출력
print(max_num)
print(min_num)
