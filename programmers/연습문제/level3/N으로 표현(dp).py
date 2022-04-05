def operation(n1, n2, operator):
    if operator == '+':
        return n1 + n2
    elif n2 != 0 and operator == '/':
        return int(n1 / n2)
    elif operator == '*':
        return n1 * n2
    else:
        return n1 - n2
    
def solution(N, number):
    if N == number:
        return 1
        
    operators = ['+', '/', '*', '-']
    dp = [[] for _ in range(9)]
    dp[0].append(0)
    dp[1].append(N)

    for i in range(2, 9):
        if int(str(N)*i) == number:
            return i
        dp[i].append(int(str(N)*i))
        for j in range(1, i):
            k = i-j
            for n1 in dp[j]:
                for n2 in dp[k]:
                    for op in operators:
                        result = operation(n1, n2, op)
                        if result == number:
                            return i
                        dp[i].append(result)
    return -1