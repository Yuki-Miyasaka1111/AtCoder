s=input()

for c in s:
    if s.count(c)%2!=0:
        print('No')
        exit()
print('Yes')
        