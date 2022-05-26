def solution(s):
    answer = ''
    s = ' ' + s
    n = len(s)
    for i in range(1, n):
        if not s[i].isdigit() and s[i-1] == ' ':
            answer += s[i].upper()
        else:
            answer += s[i].lower()
    return answer