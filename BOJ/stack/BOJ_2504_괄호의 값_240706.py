bracket = input()
stack = []

def calculate_bracket(bracket):
    global stack
    tmp=1
    result = 0

    for i in range(len(bracket)):
        b = bracket[i]
        if b  == '(':
            stack.append(b)
            tmp *= 2

        elif b == '[':
            stack.append(b)
            tmp *= 3

        elif b == ')':
            if not stack or stack[-1] != '(':
                result = 0
                break
            else:
                if bracket[i-1] == '(':
                    result += tmp
            stack.pop()
            tmp //= 2

        # ]    
        else:
            if not stack or stack[-1] != '[':
                result = 0
                break
            else:
                if bracket[i-1] == '[':
                    result += tmp
                stack.pop()
                tmp //= 3
                
    return result

result = calculate_bracket(bracket)
if stack:
    print(0)
else:
    print(result)
