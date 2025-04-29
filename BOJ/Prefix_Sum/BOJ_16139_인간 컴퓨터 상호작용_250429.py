text = input()
q = int(input())

chars = set(text)
prefix_dict = {}

for c in chars:
	arr = []
	# 먼저 캐릭터 비교를 수행하겠습니다.
	for t in text:
		if c == t:
			arr.append(1)
		else:
			arr.append(0)
	# 그다음 arr에 대해서 prefix_sum을 구하겠습니다.
	prefix_sum = [0]
	summary = 0
	for i in arr:
		summary += i
		prefix_sum.append(summary)
	# 그다음 딕셔너리에 해당 prefix sum을 맵핑 시키겠습니다.
	prefix_dict[c] = prefix_sum

# 쿼리 수만큼 순회 하겠습니다.
for _ in range(q):
	alr = input().split()
	a = alr[0]
	l = int(alr[1])
	r = int(alr[2])
	if a not in prefix_dict:
		print(0)
	else:
		char_prefix_sum_arr = prefix_dict[a]
		char_sum = char_prefix_sum_arr[r+1] - char_prefix_sum_arr[l]
		print(char_sum)

