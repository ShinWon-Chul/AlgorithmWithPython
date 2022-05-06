def solution(s):
    arr = []
    for c in s:
        if c == '(':
            arr.append(c)
        else:
            if len(arr) > 0 and arr[-1] == '(':
                arr.pop()
            else:
                arr.append(c)
    
    if len(arr) > 0:
        return False
    else:
        return True