n,k,x=map(int, input().split())
a=list(map(int, input().split()))

ans = sum(a)
m = sum(ai // x for ai in a)
m = min(m, k)
ans -= m * x
k -= m

a = [ai % x for ai in a]
a.sort(reverse=True)

for i in range(n):
    if k == 0:
        break
    ans -= a[i]
    k -= 1

# 結果を出力
print(ans)