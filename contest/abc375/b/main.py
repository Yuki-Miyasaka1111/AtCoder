import sys
import math

import sys
import math

sys.setrecursionlimit(1 << 25)
input = sys.stdin.readline

N = int(input())
ans = []

for _ in range(N):
    x, y = map(int, input().split())
    ans.append((x, y))

total_cost = 0.0
prev_x, prev_y = 0, 0

for x, y in ans:
    dx = x - prev_x
    dy = y - prev_y
    total_cost += math.hypot(dx, dy)
    prev_x, prev_y = x, y

dx = 0 - prev_x
dy = 0 - prev_y
total_cost += math.hypot(dx, dy)

print("{0:.10f}".format(total_cost))