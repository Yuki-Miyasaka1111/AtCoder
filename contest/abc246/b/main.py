import math

A,B=map(int, input().split())

C=math.sqrt(A*A + B*B)

X = A / C
Y = B / C

print(f"{X:.12f} {Y:.12f}")