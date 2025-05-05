import sys
input = sys.stdin.readline

N = int(input().strip())
for _ in range(N):
	key = input().strip()
	left_stack = []
	right_stack = []
	for k in key:
		if k == '<':
			if left_stack:
				right_stack.append(left_stack.pop())
		elif k == '>':
			if right_stack:
				left_stack.append(right_stack.pop())
		elif k == '-':
			if left_stack:
				left_stack.pop()
		else:
			left_stack.append(k)

	print(''.join(left_stack + right_stack[::-1]))