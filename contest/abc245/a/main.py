A, B, C, D=map(int, input().split())

A = A * 60 * 60
B = B * 60
C = C * 60 * 60
D = D * 60

tk = A + B
ao = C + D + 1

if tk > ao:
    print("Aoki")
elif tk < ao:
    print("Takahashi")