a, b = map(int, input().split())
def solution(a, b):
    count = 0
    while a<b:
        if b%2 == 0:
            b = int(b/2)
            count += 1
        else:
            if str(b)[-1] == '1':
                b = int(str(b)[:-1])
                count += 1
            else:
                return -1

        if a == b:
            return count+1
    return -1
print(solution(a, b))
