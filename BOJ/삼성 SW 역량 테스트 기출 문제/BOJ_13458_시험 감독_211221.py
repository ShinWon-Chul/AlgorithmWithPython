from sys import stdin
n = int(input())
a = list(map(int, stdin.readline().rstrip().split()))
b, c = map(int, input().split()) #총감독, 부감독이 감독할 수 있는 응시자 수

result = 0
for i in a:
    #총감독은 반드시 한명 있어야 함
    full = 1
    #총감독 혼자서 모든 응시자를 감독할 수 있는경우
    if i-b < 0:
        result += full
        
    #부감독이 감독해야 할 응시자수
    else:
        parts = (i-b)//c
        if (i-b) %c != 0:
            #나머지가 있다면 한명이 더 필요함
            part = 1
        else:
            part = 0
        result = result + full + parts + part
print(result)