import sys
import copy

input = sys.stdin.readline
string = input().strip()
left_stack = [ s for s in string]
right_stack = []
N = int(input().strip())

for _ in range(N):
	command = input().strip()
	if command == 'L':
		if left_stack:
			right_stack.append(left_stack.pop())
	elif command == 'D':
		if right_stack:
			left_stack.append(right_stack.pop())
	elif command == 'B':
		if left_stack:
			left_stack.pop()
	else:
		c, char = command.split()
		left_stack.append(char)

# print(left_stack)
# print(right_stack)
print(''.join(left_stack + right_stack[::-1]))