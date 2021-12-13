s = input()
right = []
left = []
rightS = s[:int(len(s)/2)]
leftS = s[int(len(s)/2):]
for i in rightS:
    right.append(int(i))
for i in leftS:
    left.append(int(i))
if sum(right) == sum(left):
    print("LUCKY")
else:
    print("READY")