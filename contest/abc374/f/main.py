import sys
import threading

def main():
    sys.setrecursionlimit(1 << 25)
    N_K_X = sys.stdin.readline().split()
    while len(N_K_X) < 3:
        N_K_X += sys.stdin.readline().split()
    N, K, X = map(int, N_K_X)
    N = int(N)
    K = int(K)
    X = int(X)
    T_line = []
    while len(T_line) < N:
        T_line += sys.stdin.readline().split()
    T = list(map(int, T_line))
    N = len(T)
    T.sort()

    memo = {}

    from functools import lru_cache

    def dfs(i, last_ship_day):
        if i == N:
            return 0
        key = (i, last_ship_day)
        if key in memo:
            return memo[key]
        res = float('inf')
        max_orders = min(K, N - i)
        for num_orders in range(1, max_orders + 1):
            ship_day = max(T[i], last_ship_day + X)
            total_dissatisfaction = 0
            for k in range(num_orders):
                total_dissatisfaction += ship_day - T[i + k]
            next_last_ship_day = ship_day
            cost = total_dissatisfaction + dfs(i + num_orders, next_last_ship_day)
            res = min(res, cost)
        memo[key] = res
        return res

    result = dfs(0, -X)
    print(result)

threading.Thread(target=main).start()
