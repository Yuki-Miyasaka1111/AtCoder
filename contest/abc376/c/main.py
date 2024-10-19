import sys

sys.setrecursionlimit(1 << 25)
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()

if B[0] < A[0]:
    print(-1)
    sys.exit()

left = 1
right = 2 * 10**9
while left < right:
    mid = (left + right) // 2
    boxes = B + [mid]
    boxes.sort()
    possible = True
    for i in range(N):
        if A[i] > boxes[i]:
            possible = False
            break
    if possible:
        right = mid
    else:
        left = mid + 1

boxes = B + [left]
boxes.sort()
for i in range(N):
    if A[i] > boxes[i]:
        print(-1)
        sys.exit()
print(left)