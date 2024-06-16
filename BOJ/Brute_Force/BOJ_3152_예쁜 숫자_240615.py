def dfs(node_value):
    global tree_numbers
    global limit
    global p
    if node_value > limit:
        return
    tree_numbers.add(node_value)
    dfs(p * node_value)
    dfs(p * node_value + 1)


def is_pretty_number(n, tree_numbers):
    count = 0
    # 트리의 자식값을 완전 탐색
    for num in tree_numbers:
        if (n - num) in tree_numbers:
            count += 1
        # n을 만들수 있는 노드가 4개이상인 경우
        if count > 3:
            return False
    # n을 만들 수 있는 노드가 2개 뿐인 경우
    if count == 2:
        return True

    # 더해서 n을 만들수 있는 노드가 없는 경우
    else:
        return False

def check_pretty_numbers(numbers):
    # 결과를 저장할 배열
    result = []
    
    # 입력 받은 수중 최대값
    limit = max(numbers)

    # 트리 생성
    dfs(1)
    for n in numbers:

        # 예쁜 숫자인지 판별
        if is_pretty_number(n, tree_numbers):
            result.append('1')
        else:
            result.append('0')
    return result

# 입력
inputs = list(map(int, input().split()))
p = inputs[0]
numbers = inputs[1:]

# 입력 받은 수중 최대값
limit = max(numbers)
tree_numbers = set()

# 실행
result = check_pretty_numbers(numbers)

# 결과 생성
result = ' '.join(result)
print(result)