import sys
import itertools

sys.setrecursionlimit(1<<25)

input = sys.stdin.readline

n=int(input())
m_g=int(input())
adj_g=[[0]*n for _ in range(n)]
for _ in range(m_g):
    u,v=map(int,input().split())
    u-=1
    v-=1
    adj_g[u][v]=adj_g[v][u]=1

m_h=int(input())
adj_h=[[0]*n for _ in range(n)]
for _ in range(m_h):
    a,b=map(int,input().split())
    a-=1
    b-=1
    adj_h[a][b]=adj_h[b][a]=1

cost=[[0]*n for _ in range(n)]
costs=[]
for i in range(n-1):
    costs.extend(map(int,input().split()))
idx=0
for i in range(n):
    for j in range(i + 1, n):
        cost[i][j] = cost[j][i] = costs[idx]
        idx += 1
            
min_total_cost=float('inf')
for perm in itertools.permutations(range(n)):
    total_cost = 0
    for i in range(n):
        for j in range(i + 1, n):
            edge_G = adj_g[i][j]
            edge_H = adj_h[perm[i]][perm[j]]
            if edge_G != edge_H:
                total_cost += cost[min(perm[i], perm[j])][max(perm[i], perm[j])]
    if total_cost < min_total_cost:
        min_total_cost = total_cost

print(min_total_cost)