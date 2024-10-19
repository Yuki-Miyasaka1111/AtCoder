import sys
import heapq

input = sys.stdin.readline

T = int(input())
results = []

for _ in range(T):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    items = list(zip(A, B))
    items.sort()

    heap = []
    total_Bi = 0
    min_cost = float('inf')

    for Ai, Bi in items:
        heapq.heappush(heap, -Bi)
        total_Bi += Bi

        if len(heap) > K:
            removed_Bi = -heapq.heappop(heap)
            total_Bi -= removed_Bi

        if len(heap) == K:
            cost = Ai * total_Bi
            if cost < min_cost:
                min_cost = cost

    results.append(min_cost)

for res in results:
    print(res)