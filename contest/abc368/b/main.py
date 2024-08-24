N=int(input())
A=list(map(int, input().split()))

loop_count = 0
while True:
    A = sorted(A, reverse=True)
    positive_count = sum([1 for a in A if a > 0])
    if positive_count <= 1:
        break
    if A[0] > 0:
        A[0] -= 1
    if A[1] > 0:
        A[1] -= 1
    
    loop_count += 1

print(loop_count)