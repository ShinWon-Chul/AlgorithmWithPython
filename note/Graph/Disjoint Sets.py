# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        
# 노드의 개수와 간선(union 연산)의 개수 입력 받기
v, e = map(int, input().split())
parent = [0] * (v + 1)# 부모 테이블 초기화

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i
    
# union 연산을 각각 수행
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)
    
# 각 원소가 속한 집합 출력
for i in range(1, v + 1):
    print(f'node {i} in {find_parent(parent, i)}')
    
# 부모 테이블 출력
for i in range(1, v + 1):
    print(f'node {i}s parent is {parent[i]}')

"""
[Input Example]
6 4
1 4
2 3
2 4
5 6

[Output Example]
node 1 in 1
node 2 in 1
node 3 in 1
node 4 in 1
node 5 in 5
node 6 in 5
node 1s parent is 1
node 2s parent is 1
node 3s parent is 1
node 4s parent is 1
node 5s parent is 5
node 6s parent is 5
"""