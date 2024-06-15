inputs = list(map(int, input().split()))

def generate_tree_numbers(p, limit):
    """ 주어진 p와 특정 limit 이하의 숫자들만 트리 구조에서 생성 """
    tree_numbers = set()
    def dfs(node_value):
        if node_value > limit:
            return
        tree_numbers.add(node_value)
        dfs(p * node_value)
        dfs(p * node_value + 1)

    dfs(1)
    return tree_numbers

def is_pretty_number(n, tree_numbers):
    count = 0
    for num in tree_numbers:
        if (n - num) in tree_numbers:
            count += 1
        if count > 3:
            return False
    if count == 2:
        return True
    else:
        return False

def check_pretty_numbers(p, numbers):
    result = []
    limit = max(numbers) * 2  # 넉넉한 범위를 설정
    tree_numbers = generate_tree_numbers(p, limit)
    for n in numbers:
        if is_pretty_number(n, tree_numbers):
            result.append('1')
        else:
            result.append('0')
    return result

# 입력
p = inputs[0]
numbers = inputs[1:]

# 예제 실행
result = check_pretty_numbers(p, numbers)
result = ' '.join(result)
print(result)