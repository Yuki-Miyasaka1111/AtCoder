n=int(input())
k=int(input())
x=int(input())
y=int(input())

ans=0
for i in range(n):
    if i < k:
        ans+=x
    else:
        ans+=y

print(ans)