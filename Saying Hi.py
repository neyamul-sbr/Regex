import re

N = int(input())
regex_pattern = r'^(H|h)(I|i)\s[^Dd]'
for _ in range(N):
    S = input()
    if(re.search(regex_pattern, S)):
        print(S)
