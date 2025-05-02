#O(N)또는 O(Log)시간대로 끝내야함
# 라인스와핑을 사용하면 O(N)에 끝낼 수 있음

# 먼저 입력을 받겠습니다.
import math

N, L= list(map(int, input().split()))
data = []
for i in range(N):
	data.append(list(map(int, input().split())))

data.sort()

answer = 0
start, end = 0, 0 #현재까지의 널빤지의 거리를 초기화 해주겠습니다.
for i in range(N):
	s, e = data[i]
	if i == 0: # 첫번째 물웅덩이를 덮어주겠습니다.
		l = e-s # 첫 번째 물웅덩이의 길이
		# print('l', l)
		answer += math.ceil(l/L) # 널빤지의 갯수
		# print('answer1', answer)
		# 마지막 널빤지의 처음과 끝 길이
		start = s
		end = s + L * answer - 1
		continue
	if end >= s:
		if end >= e:
			continue
		else:
			l = e-end-1 # 덮히지 않은 물웅덩이 길이를 구해줍니다.
			# print('e', e)
			# print('end', end)
			# print('s', s)
			# print('l:', l)
			answer += math.ceil(l/L) # 널빤지의 갯수
			# 마지막 널빤지의 처음과 끝 길이
			# 마지막 널빤지의 끝 길이 업데이트
			end += L * math.ceil(l/L)
			# print('answer2', answer)
	else:
		l = e-s # 물웅덩이의 길이
		answer += math.ceil(l/L) # 널빤지의 갯수
		start = s
		end = s + L * math.ceil(l/L) - 1
		# print('answer3', answer)

# 마지막 널빤지의 갯수를 더해줍니다.

print(answer)		


# 1 6
# 8 12
#13 17
# 상수 조건
# O(2N)
# 초기 하나 놓기

# 마지막 널빤지 끝 길이보다 물울덩이 시작이 안에 있나?
	# 마지막 널빤지 끝 길이보다 물웅덩이 끝이 안에 있나?
		#continue
	# 끝이 바깥에 있다면 
		# 널빤지 += 1
		# 끝길이 업데이트

# else:
	# 널빤지 새로 시작
	# 널빤지. += 1
	# 널빤지 시작 끝 길이 업데이트

