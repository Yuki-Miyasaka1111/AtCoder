n = int(input())
for i in range(n):
    t, a = map(int, input().split())
    if i == 0:
        T, A = t, a
    else:
        x = max((T + t - 1) // t, (A + a - 1) // a)
        T, A = x * t, x * a
print(T + A)