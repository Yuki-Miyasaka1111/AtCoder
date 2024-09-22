N, A = map(int, input().split())
x = list(map(int, input().split()))

# dp[i][j][k]: i番目までのカードを使ってj枚選び、合計がkになる選び方の数
dp = [[[0] * (N * 50 + 1) for _ in range(N+1)] for _ in range(N+1)]

dp[0][0][0] = 1

for i in range(N): # カードi枚目について
    for j in range(N): # j枚選んだ場合
        for k in range(N * 50 + 1): # 合計kの場合
            if dp[i][j][k] > 0:
                # カードiを選ばない場合
                dp[i+1][j][k] += dp[i][j][k]
                # カードiを選んだ場合
                if k + x[i] <= N * 50: # 合計がN*50を超えない場合
                    dp[i+1][j+1][k+x[i]] += dp[i][j][k]

result = 0
for j in range(1, N+1):
    if j * A <= N * 50:
        result += dp[N][j][j*A]

print(result)