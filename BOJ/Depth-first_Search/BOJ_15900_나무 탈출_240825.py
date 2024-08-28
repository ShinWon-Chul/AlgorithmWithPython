import sys

N = int(input())  # 트리의 노드 개수를 입력받음

# 각 노드에 연결된 다른 노드들을 저장하기 위한 인접 리스트 초기화
adj = [[] for _ in range(N+1)]

# N-1개의 간선 정보를 입력받아 인접 리스트에 추가
for i in range(N-1):
    n1, n2 = map(int, sys.stdin.readline().rstrip().split())  # 두 노드 n1과 n2를 입력받음
    adj[n1].append(n2)  # n1 노드에 n2 노드 연결
    adj[n2].append(n1)  # n2 노드에 n1 노드 연결

# DFS 탐색을 위한 스택 초기화 (시작 노드는 1번 노드, 거리 l은 0으로 시작)
stack = [[1, 0]]

# 방문 여부를 체크하기 위한 리스트 초기화
chk = [0] * (N+1)
chk[1] = -1  # 1번 노드를 이미 방문한 것으로 표시

# 리프 노드까지의 거리를 저장할 리스트 초기화
ls = []

# 스택이 빌 때까지 DFS 탐색을 수행
while stack:
    cn, l = stack.pop()  # 스택에서 현재 노드와 그 노드까지의 거리를 꺼냄
    chk[cn] = 1  # 현재 노드를 방문했음을 표시

    # 현재 노드가 1번 노드가 아니고, 연결된 노드가 하나뿐이면 리프 노드임
    if cn != 1 and len(adj[cn]) == 1:
        ls.append(l)  # 리프 노드까지의 거리를 ls에 추가
        continue  # 다음 반복으로 넘어감

    # 현재 노드와 연결된 다른 노드들을 스택에 추가
    for nn in adj[cn]:
        if chk[nn] == 0:  # 아직 방문하지 않은 노드만 스택에 추가
            stack.append([nn, l+1])  # 거리 l을 1 증가시켜 스택에 추가

# 리프 노드까지의 거리들의 합을 계산
sum_ls = sum(ls)

# 거리들의 합이 홀수이면 "Yes", 짝수이면 "No" 출력
if sum_ls % 2:
    print('Yes')
else:
    print('No')
