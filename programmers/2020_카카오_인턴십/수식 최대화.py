import itertools

def calculate(num1, num2, operator):
    if operator == '*':
        return str(int(num1) * int(num2))
    elif operator == '+':
        return str(int(num1) + int(num2))
    else:
        return str(int(num1) - int(num2))

def operation(exp, ops):
    tmp = ""
    arr = []
    for e in exp:
        if e.isdigit():
            tmp += e
        else:
            arr.append(tmp)
            arr.append(e)
            tmp = ""
    arr.append(tmp)

    for o in ops:
        stack = []
        while arr:
            a = arr.pop(0)
            if a == o :
                stack.append(calculate(stack.pop(), arr.pop(0), o))
            else:
                stack.append(a)

        arr = stack
    return arr

def solution(expression):
    operators = ['-', '+', '*']
    operators = list(itertools.permutations(operators))
    result = []
    for ops in operators:
        result += operation(expression, ops)
    result = map(lambda x : abs(int(x)), result)
    return max(result)
    