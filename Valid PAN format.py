import re

N = int(input())

for _ in range(N):
    S = input()
    regex_pattern = r'^[A-Z]{5}\d{4}[A-Z]$'
    if re.search(regex_pattern, S):
        print("YES")
    else:
        print("NO")

