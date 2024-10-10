# 풀이 1
# n = int(input()) 
# binary_number = bin(n)[2:] 
# count = binary_number.count('1') 

# print(count)

# 풀이 2
n = int(input())
count = 0

while n > 0:
    count += n & 1  # n의 마지막 비트가 1이면 count 증가
    n >>= 1  # n을 오른쪽으로 1 비트 이동

print(count)