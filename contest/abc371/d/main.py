import sys

sys.setrecursionlimit(1 << 25)

n = int(sys.stdin.readline())
x = list(map(int, sys.stdin.readline().split()))
p = list(map(int, sys.stdin.readline().split()))

cum_p = [0] * (n + 1)
for i in range(n):
    cum_p[i + 1] = cum_p[i] + p[i]

q = int(sys.stdin.readline())
for _ in range(q):
    l, r = map(int, sys.stdin.readline().split())

    lo = 0
    hi = n
    while lo < hi:
        mid = (lo + hi) // 2
        if x[mid] < l:
            lo = mid + 1
        else:
            hi = mid
    left_index = lo

    lo = 0
    hi = n
    while lo < hi:
        mid = (lo + hi) // 2
        if x[mid] <= r:
            lo = mid + 1
        else:
            hi = mid
    right_index = lo

    total = cum_p[right_index] - cum_p[left_index]
    print(total)
