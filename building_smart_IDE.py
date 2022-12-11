import re,sys

data = sys.stdin.read()
regex_pattern_comment =r'(^(#|//|/*)|(*/)$)'
s=data.split('\n')
print(s)
for i in s:
    if(re.search(regex_pattern_comment,i)):
        continue
    else:
        if(re.search(r'import\sjava', i)):
            print("Java")
            break
        elif(re.search(r'int\smain',i)):
            print('C')
            break
        else:
            print('Pyhton')
            break
