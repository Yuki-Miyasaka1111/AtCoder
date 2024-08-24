N=int(input())

A=list(map(int, input().split()))

sA = set(A)

for i in range(max(sA)+2):
    if i not in sA:
        print(i)
        break