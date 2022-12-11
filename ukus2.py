import re

N = int(input())
para = ''
for _ in range(N):
    para += input() + ' '

T = int (input())

for _ in range(T):
    uk = input()
    us = re.sub('our', 'or', uk)
    kk = re.findall(rf'\b({uk}|{us})\b', para)
    print(len(kk))