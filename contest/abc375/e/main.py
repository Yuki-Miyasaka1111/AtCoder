N = int(input())
A = []
B = []
for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

T = sum(B)

if T % 3 != 0:
    print(-1)
    exit()

max_T = T
INF = float('inf')

dp = [[INF] * (max_T + 1) for _ in range(max_T + 1)]
dp[0][0] = 0

for i in range(N):
    Bi = B[i]
    cost1 = 0 if A[i] == 1 else 1
    cost2 = 0 if A[i] == 2 else 1
    cost3 = 0 if A[i] == 3 else 1
    dp_next = [[INF] * (max_T + 1) for _ in range(max_T + 1)]
    for s1 in range(max_T + 1):
        for s2 in range(max_T + 1):
            if dp[s1][s2] == INF:
                continue
            # チーム1に割り当て
            s1_new = s1 + Bi
            s2_new = s2
            if s1_new <= max_T:
                dp_next[s1_new][s2_new] = min(dp_next[s1_new][s2_new], dp[s1][s2] + cost1)
            # チーム2に割り当て
            s1_new = s1
            s2_new = s2 + Bi
            if s2_new <= max_T:
                dp_next[s1_new][s2_new] = min(dp_next[s1_new][s2_new], dp[s1][s2] + cost2)
            # チーム3に割り当て
            s1_new = s1
            s2_new = s2
            dp_next[s1_new][s2_new] = min(dp_next[s1_new][s2_new], dp[s1][s2] + cost3)
    dp = dp_next

target = T // 3
if dp[target][target] != INF:
    print(int(dp[target][target]))
else:
    print(-1)
