import math

m=int(input())

a=[]
while m>0:
    a_i = int(math.log(m, 3))
    p = 3**a_i

    a.append(a_i)
    m -= p

n = len(a)

print(n)
a = sorted(a)
print(' '.join(map(str, a)))