import sys

input = sys.stdin.read
data = input().split()
idx = 0

N = int(data[idx]); idx += 1
K = int(data[idx]); idx += 1

P = [int(x)-1 for x in data[idx:idx+N]]
idx += N

visited = [False]*N

final_P = [0]*N

for i in range(N):
    if not visited[i]:
        cycle = []
        current = i
        while not visited[current]:
            visited[current] = True
            cycle.append(current)
            current = P[current]
        C = len(cycle)
        if C ==0:
            continue
        shift = pow(2, K, C)
        for idx_in_cycle, elem in enumerate(cycle):
            new_idx = (idx_in_cycle + shift) % C
            final_P[elem] = cycle[new_idx]

print(' '.join(str(x+1) for x in final_P))
