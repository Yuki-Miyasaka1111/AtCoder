import sys

n_and_rest = sys.stdin.read().split()
n = int(n_and_rest[0])
h = list(map(int, n_and_rest[1:n+1]))

last_greater = [-1] * n
stack = []

for j in range(n):
    while stack and h[stack[-1]] < h[j]:
        stack.pop()
    if stack:
        last_greater[j] = stack[-1]
    else:
        last_greater[j] = -1
    stack.append(j)

diff = [0] * (n + 1)
for j in range(n):
    i_start = last_greater[j] if last_greater[j] != -1 else 0
    i_end = j - 1
    if i_start <= i_end:
        diff[i_start] += 1
        diff[i_end + 1] -= 1

c = [0] * n
current = 0
for i in range(n):
    current += diff[i]
    c[i] = current

print(' '.join(map(str, c)))