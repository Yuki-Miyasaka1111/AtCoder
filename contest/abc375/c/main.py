n = int(input())
a = [list(input().strip()) for _ in range(n)]
ans = [[''] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        d = min(i + 1, j + 1, n - i, n - j)
        ni, nj = i, j

        for _ in range(d % 4):
            ti, tj = nj, n - 1 - ni
            ni, nj = ti, tj

        ans[ni][nj] = a[i][j]

for row in ans:
    print(''.join(row))