from sys import stdin
s = stdin.readline().rstrip()

result = [0,0]
result[int(s[0])] = 1
for i in range(1, len(s)):
    if s[i] != s[i-1]:
        result[int(s[i])] = result[int(s[i])]+1 

print(min(result))