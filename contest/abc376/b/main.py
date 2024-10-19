from collections import deque

def bfs(start, goal, blocked, N):
    if start == goal:
        return 0
    visited = [False] * (N + 1)
    queue = deque()
    queue.append((start, 0))
    visited[start] = True
    while queue:
        node, dist = queue.popleft()
        if node == goal:
            return dist
        next_node = node + 1 if node < N else 1
        prev_node = node - 1 if node > 1 else N
        for neighbor in [next_node, prev_node]:
            if not visited[neighbor] and neighbor != blocked:
                visited[neighbor] = True
                queue.append((neighbor, dist + 1))
    return -1

N, Q = map(int, input().split())
commands = []
for _ in range(Q):
    Hi_Ti = input().split()
    Hi, Ti = Hi_Ti[0], int(Hi_Ti[1])
    commands.append((Hi, Ti))

lpos = 1
rpos = 2
total_moves = 0

for Hi, Ti in commands:
    if Hi == 'L':
        start = lpos
        goal = Ti
        blocked = rpos
        distance = bfs(start, goal, blocked, N)
        total_moves += distance
        lpos = Ti
    else:
        start = rpos
        goal = Ti
        blocked = lpos
        distance = bfs(start, goal, blocked, N)
        total_moves += distance
        rpos = Ti

print(total_moves)