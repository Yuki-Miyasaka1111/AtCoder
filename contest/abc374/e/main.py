import sys
import math

input_data = sys.stdin.read().split()
idx = 0
N = int(input_data[idx]); idx += 1
X = int(input_data[idx]); idx += 1
machines = []
for _ in range(N):
    Ai = int(input_data[idx]); idx += 1
    Pi = int(input_data[idx]); idx += 1
    Bi = int(input_data[idx]); idx += 1
    Qi = int(input_data[idx]); idx += 1
    machines.append((Ai, Pi, Bi, Qi))

def compute_cost(W, A, P, B, Q, T):
    processed_by_T = B * T
    if processed_by_T >= W:
        S = 0
    else:
        S = (W - processed_by_T + A - 1) // A
    return P * S + Q * T

def min_cost_for_process(W, A, P, B, Q):
    if W <= 0:
        return 0
    min_cost = math.inf
    T_limit = min((W + B - 1) // B, 10**6)
    for T in range(0, T_limit + 1):
        S = (W - B * T + A - 1) // A if W - B * T > 0 else 0
        cost = P * S + Q * T
        if cost < min_cost:
            min_cost = cost
    return min_cost

W_max_candidates = []
for (A, P, B, Q) in machines:
    max_S = X // P
    max_T = X // Q
    W_i_max = A * max_S + B * max_T
    W_max_candidates.append(W_i_max)
W_max = min(W_max_candidates + [2 * 10**9])
low = 0
high = W_max
answer = 0

while low <= high:
    mid = (low + high) // 2
    total_cost = 0
    for A, P, B, Q in machines:
        cost = min_cost_for_process(mid, A, P, B, Q)
        total_cost += cost
        if total_cost > X:
            break
    if total_cost <= X:
        answer = mid
        low = mid + 1
    else:
        high = mid - 1

print(answer)
