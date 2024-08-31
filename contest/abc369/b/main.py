N = int(input())
lp = -1
rp = -1
x = 0

for i in range(N):
    A, S = input().split()
    A = int(A)

    if S == "L":
        if lp == -1:
            lp = A
        else:
            x += abs(A - lp)
            lp = A
    elif S == "R":
        if rp == -1:
            rp = A
        else:
            x += abs(A - rp)
            rp = A
    

print(x)
