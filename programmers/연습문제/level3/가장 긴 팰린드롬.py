def solution(s):
    max_len = 0
    length = len(s)
    for i in range(length+1):
        for j in range(i):
            string1 = s[j:i]
            string2 = string1[::-1]
            if string2 == string1:
                str_len = i-j
                if str_len > max_len:
                    max_len = str_len
    return max_len