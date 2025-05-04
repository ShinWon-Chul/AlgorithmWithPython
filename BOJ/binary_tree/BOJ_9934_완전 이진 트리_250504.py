import sys
sys.setrecursionlimit(10000)

K = int(input())
nums = list(map(int, input().split()))
tree = [[] for _ in range(K)]  # 각 레벨별 노드를 저장할 리스트

def build_tree(arr, level):
	# 재귀 함수의 종료조건을 구현 하겠습니다.
	if not arr:
		return
	mid = len(arr) // 2
	tree[level].append(str(arr[mid]))
	build_tree(arr[:mid], level+1)
	build_tree(arr[mid+1:], level+1)

build_tree(nums, 0)
for k in range(K):
	print(' '.join(tree[k]))