n,c=map(int, input().split())
t=list(map(int, input().split()))
candy=1
last=t[0]

for i in range(1,n):
    if t[i]-last>=c:
        candy+=1
        last=t[i]
print(candy)