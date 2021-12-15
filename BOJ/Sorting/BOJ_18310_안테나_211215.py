from sys import stdin
n = int(input())
house = list(map(int, stdin.readline().rstrip().split()))
house.sort()
print(house[(n-1)//2])