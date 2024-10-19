import sys
from collections import deque

sys.setrecursionlimit(1 << 25)
input = sys.stdin.readline

N, M = map(int, input().strip().split())

graph = [[] for _ in range(N + 1)]
rev_graph = [[] for _ in range(N + 1)]

edges_from_1 = set()
edges_to_1 = set()
self_loop = False

for _ in range(M):
    a, b = map(int, input().strip().split())
    graph[a].append(b)
    rev_graph[b].append(a)
    if a == 1:
        edges_from_1.add(b)
    if b == 1:
        edges_to_1.add(a)
    if a == 1 and b == 1:
        self_loop = True

min_cycle_length = float('inf')

if self_loop:
    min_cycle_length = 1

for u in edges_from_1:
    if u in edges_to_1:
        min_cycle_length = min(min_cycle_length, 2)

dist_from_1 = [-1] * (N + 1)
dist_from_1[1] = 0
queue = deque()
queue.append(1)
while queue:
    u = queue.popleft()
    for v in graph[u]:
        if dist_from_1[v] == -1:
            dist_from_1[v] = dist_from_1[u] + 1
            queue.append(v)

dist_to_1 = [-1] * (N + 1)
dist_to_1[1] = 0
queue = deque()
queue.append(1)
while queue:
    u = queue.popleft()
    for v in rev_graph[u]:
        if dist_to_1[v] == -1:
            dist_to_1[v] = dist_to_1[u] + 1
            queue.append(v)

for u in range(2, N + 1):
    if dist_from_1[u] != -1 and dist_to_1[u] != -1:
        total_length = dist_from_1[u] + dist_to_1[u]
        if total_length < min_cycle_length:
            min_cycle_length = total_length

if min_cycle_length == float('inf'):
    print(-1)
else:
    print(min_cycle_length)
