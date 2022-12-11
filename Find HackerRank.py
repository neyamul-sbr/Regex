import re

N = int(input())
regex_pattern1 = r'^(hackerrank)'
regex_pattern2 = r'(hackerrank)$'
for _ in range(N):
    S = input()
    if(re.search(regex_pattern1, S) and re.search(regex_pattern2,S)):
        print(0)
    elif re.search(regex_pattern1,S):
        print(1)
    elif re.search(regex_pattern2,S):
        print(2)
    else:
        print(-1)
