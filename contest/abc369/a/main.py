A,B=map(int, input().split())

x = 0
if A == B:
    x = 1
elif abs(B-A) == 1:
    x = 2
elif abs(B-A) == 2:
    x = 3
elif abs(B-A) > 2:
    if abs(B-A) % 2 == 0:
        x = 3
    else:
        x = 2

print (x)