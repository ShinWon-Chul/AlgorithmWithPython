def decision(bracket):
    l = 0
    r = 0
    for i, c in enumerate(bracket):
        if c == '(':
            l += 1
        else:
            r += 1
        if r>l:
            return False
    if l != r:
        return False
    return True

def new_u(u):
    u = u[1:-1]
    new_u = ""
    for c in u:
        if c == '(':
            new_u += ')'
        else:
            new_u += '('
    return new_u

def process(bracket):
    l = 0
    r = 0
    if decision(bracket) or bracket == "":
        return bracket
    else:
        for i, c in enumerate(bracket):
            if c == '(':
                l += 1
            else:
                r += 1
            if l == r:
                u = bracket[:i+1]
                break
        v = bracket[len(u):]
        if decision(u):
            u += process(v)
        else:
            result = '('
            result += process(v)
            result += ')'
            result += new_u(u)
            return result
        return u

def solution(p):
    answer = process(p)
    return answer