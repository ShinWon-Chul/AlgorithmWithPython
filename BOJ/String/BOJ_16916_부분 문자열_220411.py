import re
import sys

S = sys.stdin.readline().rstrip()
P = sys.stdin.readline().rstrip()

if re.search(P, S):
    print(1)
else:
    print(0)