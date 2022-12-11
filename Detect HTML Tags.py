import re

N = int(input())
l =[]
for _ in range(N):
    S = input()

    kk = re.findall(r'<(\w+)',S)
    for i in kk:
        l.append(i)
a = sorted(set(l))
print(';'.join(a))

