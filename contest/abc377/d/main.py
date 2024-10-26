import sys

data = sys.stdin.read().split()
idx = 0

N = int(data[idx]); idx += 1
M = int(data[idx]); idx += 1

intervals = []
for _ in range(N):
    Li = int(data[idx]); idx += 1
    Ri = int(data[idx]); idx += 1
    intervals.append((Ri, Li))

intervals.sort()

current_max = 0
count = 0
i = 0

for r in range(1, M + 1):
    while i < N and intervals[i][0] <= r:
        current_max = max(current_max, intervals[i][1])
        i += 1
    A_r = current_max
    if A_r < r:
        count += r - A_r

print(count)