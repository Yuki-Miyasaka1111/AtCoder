n, q = map(int, input().split())
s = list(input())
total_abc = 0

# 初期状態のABCの数を数える
for i in range(n - 2):
    if s[i] == 'A' and s[i + 1] == 'B' and s[i + 2] == 'C':
        total_abc += 1

for _ in range(q):
    x, c = input().split()
    x = int(x)

    for i in range(x - 3, x):
        if 0 <= i <= n - 3:
            if s[i] == 'A' and s[i + 1] == 'B' and s[i + 2] == 'C':
                total_abc -= 1

    s[x - 1] = c

    for i in range(x - 3, x):
        if 0 <= i <= n - 3:
            if s[i] == 'A' and s[i + 1] == 'B' and s[i + 2] == 'C':
                total_abc += 1

    print(total_abc)