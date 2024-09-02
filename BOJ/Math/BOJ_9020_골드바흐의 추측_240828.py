import math

# 1. 에라토스테네스의 체를 사용해 10000까지의 모든 소수를 구합니다.
n = 10000
array = [True for i in range(n + 1)]

for i in range(2, int(math.sqrt(n)) + 1):
    if array[i]:
        for j in range(i * i, n + 1, i):
            array[j] = False

# 모든 소수를 prime_number 리스트에 추가합니다.
prime_number = [i for i in range(2, n + 1) if array[i]]

# 2. 두 소수의 합을 키로 갖고, 합이 되는 두 소수 리스트를 값으로 갖는 딕셔너리 생성
prime_sum_dict = {}

for i in range(len(prime_number)):
    for j in range(i, len(prime_number)):
        p1 = prime_number[i]
        p2 = prime_number[j]
        prime_sum = p1 + p2
        
        if prime_sum % 2 == 0:  # 두 수의 합이 짝수일 때만 수행
            if prime_sum not in prime_sum_dict or abs(p1 - p2) < abs(prime_sum_dict[prime_sum][0] - prime_sum_dict[prime_sum][1]):
                prime_sum_dict[prime_sum] = [p1, p2]

# 결과 출력
N = int(input())
for _ in range(N):
    n = int(input())
    x, y = prime_sum_dict[n]
    print(x, y)